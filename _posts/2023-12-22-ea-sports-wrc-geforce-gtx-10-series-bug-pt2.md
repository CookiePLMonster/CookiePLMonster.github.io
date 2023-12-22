---
layout: post
title: "Fan research vs official fix -- EA Sports WRC decal rendering on GeForce GTX 10 series cards"
excerpt: "SilentPatch vs the official v1.4.0 update."
thumbnail: "assets/img/posts/ea-wrc-2/rd-banner.jpg"
feature-img: "assets/img/posts/ea-wrc-2/rd-banner.jpg"
image: "assets/img/posts/ea-wrc-2/rd-square.jpg"
game-series: "ea-sports-wrc"
date: 2023-12-22 21:30:00 +0100
tags: Articles
---

* TOC
{:toc}

*[HLSL]: High-level Shader Language
*[SRV]: Shader-resource View

This article is a follow-up to [Fixing EA Sports WRC decal rendering on GeForce GTX 10 series cards]({% post_url 2023-11-22-ea-sports-wrc-geforce-gtx-10-series-bug %}).

# Introduction

On {{ "2023-12-14" | date: page.date-format }}, Codemasters released [the v1.4.0 update](http://x.ea.com/78991) for EA Sports WRC.
Among countless fixes, two items align with the fixes previously published in SilentPatch:

> * Fixed an issue where Fanatec and location event plates would appear stretched when using NVIDIA GTX 10 series GPUs.
> * Fixed an issue where framerate would drop to below 10 fps when using the Livery Editor on NVIDIA 10 series GPUs.

This was somewhat expected, since by the time I released SilentPatch last month, I've had the opportunity to get in touch with Codemasters
and share my findings in as much detail as possible. I was later informed that the issue was fixed internally and was given an OK to publish
SilentPatch as a stop-gap solution for the affected users. My efforts have also been highlighted on the official EA Sports WRC Discord 🙂
In the end, everyone won.

With this out of the way (and with SilentPatch officially deprecated), I was curious about the approach used for the official fix.
In this short article, I'll dissect the official fix and compare it with mine.

# The official fix

Let's start with a recap. When I figured out the root cause of the original bug, I outlined two possible approaches that could be taken here:

> 1. Make the SRV typeless by defining the stride explicitly and setting the format to `DXGI_FORMAT_UNKNOWN`. This approach does not require modifying the shaders.
> 2. Modify the shader the same way I did, replacing `StructuredBuffer<uint>` with `Buffer<float2>`. This way the shader handles the existing input buffer layout correctly,
>    regardless of the GPU vendor/generation, and a current way of accessing the buffers is used.

In my fix, I went for the second approach, because replacing shaders is a much easier task than tracking down specific resource creation.
However, I was under the impression that the official fix would adopt the other approach, as that would've fixed all similar broken cases.
Surprisingly, I was wrong -- with the v1.4.0 update, the buffer definitions remain unchanged:
{% include figures/image.html link="/assets/img/posts/ea-wrc-2/input-buffers.jpg" style="natural" caption="Notice that the resources still have a defined format and are not `UNKNOWN`." %}

Instead, automatic variable names from RenderDoc immediately show that Codemasters changed the shaders themselves -- in v1.3.0, the automatically generated name
of the first bound resource was `structuredbuffer0`, in v1.4.0 it's `texture0`, indicating that the way the resource is accessed by the shader has changed!

Indeed, looking at the shader assembly of the fixed shader, it now looks identical to the shader from SilentPatch -- which means my suggested solution of changing
the shader inputs was used as-is:

```hlsl
   imad r0.x, v1.x, cb0[1].x, cb0[1].y
   ld_indexable(buffer)(float,float,float,float) r0.xy, r0.xxxx, t0.xyzw
   mov o3.xy, r0.xyxx
```

Is this the best solution? I can't say this with absolute certainty of course, but I am somewhat surprised at the approach taken.
However, the other solution (making the buffers typeless) may have introduced problems with other shaders, so perhaps the current solution
was thought of as the safest.

However, I have a few more points to raise about this fix. It technically is complete, but it could have been done better, as I believe the current solution
is not complete, and DirectX specification is still violated by those shaders:

1. `texture1` is of type `R8G8B8A8_SNORM`, but the shader accesses it through `Buffer<float4>`. If my knowledge of HLSL is correct,
   the sampler used here should have been `Buffer<snorm float4>`.
2. `structuredbuffer2` and `structuredbuffer3` still use `StructuredBuffer<>` samplers, despite those buffers not being typeless.
   In an ideal case, they should also have been changed to use `Buffer<>`. **This is most likely a violation of the DirectX spec.**
3. `texture0` is of type `R16G16_FLOAT`, therefore the shader could have leveraged GPU's support for 16-bit floating point values if the resource was sampled as `min16float2`.
   This type combines compatibility with specialization -- as it leverages native support for half-floats on supported hardware, and falls back to full floating point values otherwise.

# Other fixes in the v1.4.0 update

The changelog of this update is massive, but I'd like to highlight two other things:

1. Aside from the aforementioned changes, the Livery Editor performance is now improved on all PC configurations.
  Before this update, the editor was slow for everyone since the game was re-rendering all decals to an 8192x8192 render target **every frame**.
  In v1.4.0, this is only done when the decals are added/removed/moved/scaled.
2. This update introduced the Central European Rally, a new location in the Czech Republic.
  Unfortunately, this has [introduced a critical issue with the existing Career Mode saves](https://x.ea.com/79082), making saves from further WRC seasons unusable.
  This is a gameplay issue that in a game of this scope is effectively un-fixable from the outside, and the fix addressing it is scheduled only for mid-January -- so
  it's a bummer 😔
