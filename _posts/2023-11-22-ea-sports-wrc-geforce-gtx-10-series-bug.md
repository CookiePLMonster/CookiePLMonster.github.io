---
layout: post
title: "Fixing EA Sports WRC decal rendering on GeForce GTX 10 series cards"
excerpt: "Pascal cards exposing broken shaders."
thumbnail: "assets/img/posts/ea-wrc/mini-banner.jpg"
feature-img: "assets/img/posts/ea-wrc/mini-banner.jpg"
image: "assets/img/posts/ea-wrc/mini-banner.jpg"
game-series: "ea-sports-wrc"
date: 2023-11-22 19:20:00 +0100
twitter: {card: "summary_large_image"}
tags: [Articles, Releases]
juxtapose: true
---

_TL;DR - if you are not interested in a technical dive into the graphical glitch fixed by SilentPatch, scroll down to the [**Download**](#download)
section for a download link._

***

* TOC
{:toc}

*[HLSL]: High-level Shader Language
*[SRV]: Shader-resource View

For the follow-up article, see
[Fan research vs official fix -- EA Sports WRC decal rendering on GeForce GTX 10 series cards]({% post_url 2023-12-22-ea-sports-wrc-geforce-gtx-10-series-bug-pt2 %}).

# Introduction

Ever since the newest WRC game from Codemasters and EA was released on {{ "2023-11-03" | date: page.date-format }}, I've had *a lot* of fun playing it.
Although my GTX 1070 is close to its end of life, I managed to find a good compromise between performance and quality somewhere in the middle ground
between Medium and High graphical details, and I'm able to play the game comfortably.

{: #broken-screenshots}
Throughout my playthrough, I'd also post a few screenshots on social media, such as those -- you'll see later why I bring it up.
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/20231103172210_1.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/20231103172210_1.jpg" %}
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/20231105172831_1.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/20231105172831_1.jpg" %}
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/20231110211229_1.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/20231110211229_1.jpg" %}
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/F-rc13EWAAAANmf.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/F-rc13EWAAAANmf.jpg" %}
<figcaption markdown="span">You may already be able to spot what's wrong with those screenshots, but at the time I completely missed all the clues.</figcaption>
</figure>

I had already overheard the news about some people being unable to use the Livery Editor, but I didn't put too much thought into it until I tried to use it myself.
I tried to put a decal on my car, but without much success:
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/F-rMUNjXEAAEWiN.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/F-rMUNjXEAAEWiN.jpg"
                            caption="Two questions come to mind: where is my decal, and why is the game running at 8 FPS?" %}

I shared this screen on Discord in hopes of finding someone else with the same issue, and one person pointed out that other than the decal, I am missing something
else -- **the driver number and the driver/co-driver names are completely missing from the side window!** Sure enough, all cars were broken for me in one way or another,
but I think Vauxhall Nova takes the crown with just how gloriously unusable it had become:
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/broken-nova.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/broken-nova.jpg" %}

Indeed, it seems that I hit the very Livery Editor bug I was warned about. [A thread in EA Answers HQ](https://answers.ea.com/t5/Bug-Reports/Stretched-car-decals/td-p/13146747)
has entire pages of people reporting this bug, with one interesting point -- **everyone** disclosing their PC specs in that thread is playing the game on GTX 9xx or 10xx series!
It would seem that no other GPU vendor and/or generation except for those is affected. While Maxwell (9xx series) cards are not officially supported by the game, Pascal (10xx series)
are, as the game's minimum system requirements list the GTX 1060. Additionally, this issue is partially mentioned in the current version
of the [Known Issues](https://answers.ea.com/t5/General-Discussion/EA-SPORTS-WRC-Release-Notes/m-p/13145127/thread-id/559) page, although it's more widespread than the thread says:
> On GTX 1060 GPU the Fanatec and Flag Decals on vehicles have stretching glitch

Now [scroll up](#broken-screenshots). See all these weird "scratches" and lines on these cars and rear windshields? Only then did I realize that the broken Livery Editor
and these are actually related -- the artifacts on rear windshields are the flags and driver numbers, while "scratches" on cars are most likely the rally-specific/Fanatec decals!

Me being me, I didn't want to just continue playing the game in this state -- it was time to set up [RenderDoc](https://renderdoc.org/).

# Investigation and debugging

For this investigation, I took a frame capture of the aforementioned Nova. These decals are rendered only once and not every frame, so capturing the exact frame required
a few attempts. I then remoted to another PC with RTX 3070 and opened the same capture on it. Usually, RenderDoc captures are not guaranteed to work across different PCs
with different graphics cards, especially with low-level APIs like D3D12 used by WRC, but in this case, a capture from the GTX 1070 PC played back on the RTX 3070 PC just fine
(the opposite crashes the D3D12 device, though). Not only that, but on that PC the very same capture also... did not display the bug!
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/screens/thumb/nova-1070.jpg" left-label="GTX 1070"
                right="/assets/img/posts/ea-wrc/screens/thumb/nova-3070.jpg" right-label="RTX 3070" %}

Cases like this are always interesting and reminiscent of my [Far Cry investigation]({% post_url 2018-07-07-farcry-d3d9-bug %}). RenderDoc captures the record of every single D3D command
issued by the game in the frame, together with the input data; then, previewing events in the capture involves replaying the saved sequence of events up to the point of the selected event.
In other words, if two PCs show different results on the same capture, the bug is not the matter of the game setting things up differently between hardware,
but rather **the hardware itself interpreting the given commands and data in a diverging way!**

RenderDoc's Mesh Viewer provides another clue -- apparently, these draws take the car's body mesh as input, and it obviously looks the same across different hardware...
{% include figures/image.html link="/assets/img/posts/ea-wrc/input-mesh.jpg" style="natural" %}

...but the outputs look... let's just say, *drastically* different.
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/output-mesh-1070.jpg" left-label="GTX 1070"
                right="/assets/img/posts/ea-wrc/output-mesh-3070.jpg" right-label="RTX 3070"
                caption="Oh no." %}{:style="max-width: 551px"}

The above comparison concerns the body decals, but it's the same for nameplates on windows. This is how they render:
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/output-decal-1070.png" left-label="GTX 1070"
                right="/assets/img/posts/ea-wrc/output-decal-3070.png" right-label="RTX 3070" %}{:style="max-width: 512px"}

Or presented in a different view, highlighting one of the draw calls in pink:
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/output-decal-draw-1070.jpg" left-label="GTX 1070"
                right="/assets/img/posts/ea-wrc/output-decal-draw-3070.jpg" right-label="RTX 3070" %}{:style="max-width: 512px"}

I initially feared that this could be a low-level D3D12 issue (missing synchronization, etc.), but the issue persisted when running the game in a D3D11 mode
through a `-dx11` command line argument. With this in mind, the first obvious culprit is a vertex shader, especially since they are shared between backends.
RenderDoc gives an option to preview the shader assembly, and the vertex shader used for these decals is not too long:

```hlsl
vs_5_0
      dcl_globalFlags refactoringAllowed
      dcl_constantbuffer cb0[2], immediateIndexed
      dcl_resource_structured t0, 4
      dcl_resource_buffer (float,float,float,float) t1
      dcl_resource_structured t2, 16
      dcl_resource_structured t3, 4
      dcl_input v0.xyz
      dcl_input_sgv v1.x, vertexid
      dcl_output_siv o0.xyzw, position
      dcl_output o1.xyz
      dcl_output o2.xyz
      dcl_output o3.xy
      dcl_temps 4
   0: imad r0.x, v1.x, cb0[1].x, cb0[1].y
   1: ld_structured_indexable(structured_buffer, stride=4)(mixed,mixed,mixed,mixed) r0.x, r0.x, l(0), t0.xxxx
   2: ushr r0.y, r0.x, l(16)
   3: f16tof32 r1.xy, r0.xyxx
   4: frc r0.xy, r1.xyxx
   5: mov o3.xy, r1.xyxx
   6: mad r0.xy, r0.xyxx, l(2.0000, 2.0000, 0.0000, 0.0000), l(-1.0000, -1.0000, 0.0000, 0.0000)
   7: mov o0.y, -r0.y
   8: mov o0.x, r0.x
   9: mov o0.zw, l(0.0000, 0.0000, 0.0000, 1.0000)
  10: ld_structured_indexable(structured_buffer, stride=4)(mixed,mixed,mixed,mixed) r0.x, v1.x, l(0), t3.xxxx
  11: and r0.x, r0.x, l(0x0000ffff)
  12: imul null, r0.y, r0.x, l(3)
  13: imad r0.xz, r0.xxxx, l(3, 0, 3, 0), l(1, 0, 2, 0)
  14: ld_structured_indexable(structured_buffer, stride=16)(mixed,mixed,mixed,mixed) r1.xyzw, r0.y, l(0), t2.xyzw
  15: mov r2.xyz, v0.xyzx
  16: mov r2.w, l(1.0000)
  17: dp4 o1.x, r1.xyzw, r2.xyzw
  18: ld_structured_indexable(structured_buffer, stride=16)(mixed,mixed,mixed,mixed) r3.xyzw, r0.x, l(0), t2.xyzw
  19: ld_structured_indexable(structured_buffer, stride=16)(mixed,mixed,mixed,mixed) r0.xyzw, r0.z, l(0), t2.xyzw
  20: dp4 o1.y, r3.xyzw, r2.xyzw
  21: dp4 o1.z, r0.xyzw, r2.xyzw
  22: imad r0.w, v1.x, cb0[1].z, l(1)
  23: ld_indexable(buffer)(float,float,float,float) r2.xyz, r0.wwww, t1.xyzw
  24: dp3 o2.x, r1.xyzx, r2.xyzx
  25: dp3 o2.y, r3.xyzx, r2.xyzx
  26: dp3 o2.z, r0.xyzx, r2.xyzx
  27: ret
```

Nothing seems obviously wrong here, and any attempts at debugging this shader in RenderDoc failed since the shader interpreter did not manifest this issue
when stepping through the shader assembly (or in other words, the output positions matched the expected result, not the "broken" result from Pascal cards).
However, RenderDoc also gives an option of replacing shaders on runtime, so I could debug this issue by editing the shader in-capture.
Unfortunately, re-assembling shaders is not possible in newer APIs (used to be possible back in D3D8/D3D9 days), so to be able to do that,
I had to reimplement the entire shader in HLSL. I rewrote it exactly in the way I understood the above shader assembly, and the result was surprising -- the bug was gone:
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/nova-3070.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/nova-3070.jpg"
            caption="Yes, it's technically the exact same screenshot as above -- but since it's a render of the very same RenderDoc capture, they look 1:1 identical." %}

I initially thought I rewrote the shader 1:1 to the original, so I started investigating the differences. The only two different components were the output position and `TEXCOORD2`,
and the shader derives both from the same input. Therefore, I could isolate the changes down to only the writes to `o3`.
In my shader, I declared the `t0` sampler as `StructuredBuffer<half2>`, as that's what I thought the original shader did. However, this results in the generated code looking slightly different:
<figure class="media-container small">
<figure markdown="1" class="fig-entry" style="text-align: left">
```hlsl
   imad r0.x, v1.x, cb0[1].x, cb0[1].y
   ld_structured_indexable(structured_buffer, stride=4)(mixed,mixed,mixed,mixed) r0.x, r0.x, l(0), t0.xxxx
   ushr r0.y, r0.x, l(16)
   f16tof32 r1.xy, r0.xyxx
   mov o3.xy, r1.xyxx
```
<figcaption markdown="span">The original shader samples the buffer with a stride of 4, and unpacks 16-bit floats from the sampled value.</figcaption>
</figure>
<figure markdown="1" class="fig-entry" style="text-align: left">
```hlsl
   imad r0.x, v1.x, cb0[1].x, cb0[1].y
   ld_structured_indexable(structured_buffer, stride=8)(mixed,mixed,mixed,mixed) r0.xy, r0.x, l(0), t0.xyxx
   mov o3.xy, r0.xyxx
```
<figcaption markdown="span">My custom shader samples the buffer with a stride of 8, and uses these values directly.</figcaption>
</figure>
</figure>

It's reasonable to assume that this difference is responsible for my accidental bug fix, but I couldn't confirm it until I figured out **why**
is the generated code different. I initially thought it was maybe because the original shader was compiled with support for 16-bit floats and mine wasn't,
but then my colleague and I casually chatted about this issue with pointed out that for Unreal Engine games, it's common to declare their input buffers with
type `uint` and manually extract the half-floats, like so:
```hlsl
uint uvSample = t0[n];
float2 uv = f16tof32(uint2(uvSample, uvSample >> 16));
```

What is the result of mirroring this approach in the affected shader? This time, the generated shader assembly is line-to-line identical to the original shader, stride of 4 bytes included.
And when it comes to rendering, well...
{% include figures/image.html link="/assets/img/posts/ea-wrc/screens/nova-1070.jpg" thumbnail="/assets/img/posts/ea-wrc/screens/thumb/nova-1070.jpg"
            caption="The same disclaimer as above applies." %}

Just to be clear -- what the original shader is doing is not always wrong, but in the case of the **current setup** it is, and I don't know why it works on the other
GPU vendors and architectures. Maybe it's worked around via a driver-level hack that is not enabled for the Nvidia 9xx and 10xx series.

What is the setup that makes sampling the buffer as `uint` not work? RenderDoc presents it as a set of four typed buffers:
{% include figures/image.html link="/assets/img/posts/ea-wrc/input-buffers.jpg" style="natural" %}

There are two problems with this approach:
1. When accessing the buffers via `StructuredBuffer`, it is assumed that the buffer is laid out in an arbitrary structure with a predefined stride.
   It is explained nicely by János Turánszki in their [Dynamic vertex formats post](https://wickedengine.net/2023/11/16/dynamic-vertex-formats/),
   but the main clue is provided [by MSDN](https://learn.microsoft.com/windows/win32/direct3dhlsl/sm5-object-structuredbuffer):
   > The SRV format bound to this resource needs to be created with the `DXGI_FORMAT_UNKNOWN` format.

   This is clearly not the case with the above setup, as RenderDoc reports the format of the first bound buffer as `R16G16_FLOAT`.
   However, even though this mistake is technically a spec violation, it's **not** causing rendering issues on my end -- `StructuredBuffer<half2>`
   and `StructuredBuffer<float2>` both work "fine", even though they are incorrect.
2. Another much worse mistake is the buffer format itself. Because the SRV of the first buffer has a predefined `FLOAT` type, sampling it as `uint` is forbidden
   and **this** is what causes the rendering glitches on my GPU! With typed buffers, it doesn't matter that the data is technically the same if it is to be
   read as bytes directly -- SRV format and sampler type **must** match, with no exceptions. The fact it works elsewhere is either due to sheer luck, or an existing driver-level hack.

With this in mind, it is clear that there are two possible fixes for this:
1. Make the SRV typeless by defining the stride explicitly and setting the format to `DXGI_FORMAT_UNKNOWN`. This approach does not require modifying the shaders.
2. Modify the shader the same way I did, replacing `StructuredBuffer<uint>` with `Buffer<float2>`. This way the shader handles the existing input buffer layout correctly,
   regardless of the GPU vendor/generation, and a current way of accessing the buffers is used.

Are any other shaders broken in the same way? At least one more shader is -- in the Livery Editor, the user has an option of painting the roof/bonnet/mirror/spoiler in different
colors to the rest of the body. On the below comparison, all these parts should be orange, but due to an identical bug in the paint shader this doesn't work on the 10 series:
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/screens/thumb/F-v8RUQXIAABxkz.jpg" left-label="GTX 1070"
                right="/assets/img/posts/ea-wrc/screens/thumb/F-v8R5fXUAA_DgA.jpg" right-label="RTX 3070"
                caption="The liveries used here are **not** identical, so this is only about the colored parts." %}

# Putting the fix into the game

OK, but now what? I have a theoretical fix for this issue ready, but it's all isolated to RenderDoc captures. Having technically solved this issue,
I wanted to put it in my game to have a stop-gap solution for this bug until it's been officially fixed.

It then struck me I already released a very similar modification 3.5 years ago
-- [Gold Filter Restoration for Deus Ex: Human Revolution Director's Cut]({% post_url 2020-04-26-dxhr-dc-gold-filter %}) largely relies on replacing shaders on runtime,
much like what I would need to do here. It's only done for D3D11, but that is not an issue, since I can run the game using this API via a command line argument.
Unreal's D3D11 implementation might be a little bit less performant than D3D12, but that's fine for the time being -- I prefer to trade a bit of performance for
correct visuals.

Gold Filter Restoration seems like an ideal base for this fix -- it acts as a D3D11 wrapper, no different from [ReShade](https://reshade.me/).
No code is hooked in the game, so if WRC uses an anti-cheat, it's extremely unlikely to become upset at this.

In practice, this approach is easy to code and reliable. A wrapper around `ID3D11Device` lets me intercept the vertex shader creation,
so the two broken shaders can just be replaced with my custom implementations, and the game is none the wiser:

```cpp
HRESULT STDMETHODCALLTYPE D3D11Device::CreateVertexShader(const void* pShaderBytecode, SIZE_T BytecodeLength,
                                ID3D11ClassLinkage* pClassLinkage, ID3D11VertexShader** ppVertexShader)
{
  if (BytecodeLength >= 4 + 16)
  {
    static constexpr std::array<uint32_t, 4> decalShader = { 0x428ffe45, 0x1c518347, 0xb48bed82, 0x25dc2319 };
    static constexpr std::array<uint32_t, 4> paintShader = { 0xfae61074, 0xefbc29b0, 0xa9ec5152, 0x837d0756 };

    const uint32_t* hash = reinterpret_cast<const uint32_t*>(reinterpret_cast<const uint8_t*>(pShaderBytecode) + 4);
    if (std::equal(decalShader.begin(), decalShader.end(), hash))
    {
      return m_orig->CreateVertexShader(FIXED_DECAL_SHADER, sizeof(FIXED_DECAL_SHADER), pClassLinkage, ppVertexShader);
    }
    else if (std::equal(paintShader.begin(), paintShader.end(), hash))
    {
      return m_orig->CreateVertexShader(FIXED_PAINT_SHADER, sizeof(FIXED_PAINT_SHADER), pClassLinkage, ppVertexShader);
    }
  }
  return m_orig->CreateVertexShader(pShaderBytecode, BytecodeLength, pClassLinkage, ppVertexShader);
}
```

With this one single change, liveries are working in-game as they should 🙂 Additionally, the aforementioned horrible performance of the Livery Editor
is resolved -- on my GTX 1070, resulting in an uplift of 5 FPS &rarr; 55 FPS while editing decals!
{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/screens/thumb/20231119194714_1.jpg" left-label="GTX 1070 (Default)"
                right="/assets/img/posts/ea-wrc/screens/thumb/20231119194407_1.jpg" right-label="GTX 1070 (SilentPatch)" %}

One more thing -- the fix is technically ready as-is, but I wanted to make extra sure it cannot cause any conflicts if this issue gets fixed officially in the future.
If the devs fix this bug by modifying the shaders, their hashes will change, and they will not be intercepted with my replacements.
However, if they opt to fix the SRVs instead, it could result in a conflict.

To avoid this, I "gated off" this SilentPatch. If the user attempts to run it on a game build that is newer than what is public at the time of writing this post,
they'll be greeted with a warning message instructing the user to remove my fix and remove the command line argument:
{% include figures/image.html link="/assets/img/posts/ea-wrc/patched-warning.jpg" style="natural" %}

If the next official patch doesn't address the issue, I will update my fix against that future patch. It may be annoying for the end user, but it's the only way
to be completely sure no unintended side effects occur.

# Download

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/ea-sports-wrc.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for EA Sports WRC</a>

After downloading, you set up the patch with the following:
1. Extract the archive to the game directory, so the `d3d11.dll` file resides next to the `WRC.exe` file.
2. On Steam/EA App, add `-dx11` to the game's launch arguments.

Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).

***

For those interested,
the full source code of the mod has been published on GitHub, so it can be freely used as a reference:
<a href="https://github.com/CookiePLMonster/SilentPatchEAWRC" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
