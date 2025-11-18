---
layout: post
title: "A technical dive into JDM: Japanese Drift Master"
date: 2025-05-23 16:50:00 +0200
excerpt: Does it deliver? First impressions, benchmarks, optimized settings, Steam Deck compatibility. And some bonus Unreal Engine 5 bugs.
game-series: "japanese-drift-master"
image: "assets/img/games/bg/japanese-drift-master.jpg"
thumbnail: "assets/img/games/bg/japanese-drift-master.jpg"
feature-img: "assets/img/games/bg/japanese-drift-master-alt.jpg"
twitter: {card: "summary_large_image"}
tags: [Reviews]
---

* TOC
{:toc}

# Introduction

There is a new kid on the block -- 2025 seems to be a year of independent racing games set in Japan,
and now, nearly two years after the first public demo, **JDM: Japanese Drift Master** released on {% include elements/time.html date="2025-05-21" text="May 21st" %}:

<div class="center-blocks">
<iframe src="https://store.steampowered.com/widget/1153410/" frameborder="0" width="646" height="190"></iframe>
</div>

My [Tokyo Xtreme Racer analysis]({% post_url 2025-01-21-tokyo-xtreme-racer-2025-review %}) from a few months ago was received well,
and so a few days ago I was given a review key for JDM, so I could look into it and share my thoughts. With both games revolving around
the Japanese car culture, and both running on **Unreal Engine 5.4**, comparisons are to be expected.

I spent the past several days playing the game, tinkering with settings, reporting bugs, running benchmarks,
and simply cruising around. In this review, I'm focusing on the technical experience, scalability, options, and performance.
Are you interested in this game but are on the fence due to your PC specs? Do you have doubts about some of its technical aspects?
Or maybe you want to see how it progressed from the 2023 demo? My findings may help you make a decision.

# What is Japanese Drift Master about anyway?

{:.sidenote}
If you'd rather jump to reading the technical overview of the game right away, go ahead and skip to [The technicalities](#the-technicalities).

If you're not following this particular sub-genre of racing games closely, you may not have heard of Japanese Drift Master earlier.
JDM is an open-world, story-driven racing game set in Guntama, a fictional mountainous region of Japan that focuses but doesn't limit itself to drifting.
Sounds familiar? Parallels to media like [Initial D](https://en.wikipedia.org/wiki/Initial_D){:target="_blank"} aren't a coincidence --
the game tells its story through manga comics, drawing clear inspirations from this cult Japanese manga.

Right from the get-go, the game puts you in a drift spec Nissan Silvia S15, and from the very first moment, it's clear that the focus is on drifting.
After a brief intro limiting the player to a predefined course, we are thrown into the open world and given the chance to buy and tune their car.
From there, the game opens up and the player may either concentrate on going through the races or just forget it and cruise on the winding Japanese roads.

{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_hD930Ez5ox.jpg" thumbnail="auto" %}

Before now, the game first had a proof-of-concept demo released back in mid-2023, followed by a prologue approximately a year later, in mid-2024.
They both were generally well received, although they pale in comparison to the current state of the game -- those older previews,
especially the first demo, had a bit of a "default Unreal game" feel to them, but now it's all gone. It's immediately noticeable that a lot of work
was put into making the game look and play like a fully featured product. This is further emphasized by the fact the two preview versions
ran on **Unreal Engine 4**, while the final game runs on **Unreal Engine 5** -- if you feel like the following screenshots look a generation apart,
that's because they are.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_RfPrRQlo36.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_JdlGpXOPIA.jpg" thumbnail="auto" %}
<figcaption markdown="span">The first demo looked nice already, but was... very dark, for some reason.</figcaption>
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_i2WGdQlH9z.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_pd5rsHZMIT.jpg" thumbnail="auto" %}
<figcaption markdown="span">"Rise of the Scorpion" looked closer to the final game, but that's still not it. Showed a lot of ghosting too.</figcaption>
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250515234214_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_5TfSeFjPSK.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_Tgac5oCmW8.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_TqDBkSzZkb.jpg" thumbnail="auto" %}
<figcaption markdown="span">The full release looks great even if you cannot "afford" to enable ray-tracing.</figcaption>
</figure>

When I wasn't gathering data for the review, I *loved* my time with JDM. I played through two of the five chapters available to reviewers,
during which I raced in numerous drift and grip events, and explored the map quite a bit. With JDM's starter selection of 27 cars
(to be expanded later), 7 radio stations, and tons of visual and mechanical tuning options, this might just be my favorite racing game of 2025 so far.
It hits all the notes that made Test Drive Unlimited great, albeit without supercars -- the cars I got to drive feel uniquely mine,
and I had to earn the right to get them. Or, true to TDU's spirit, I could just take any car for a test drive and trash it around those
narrow, twisty roads.

{% include figures/video.html link="https://i.imgur.com/JvuNXIo.mp4" attributes="controls"
    caption="I know it's not exclusive to that one franchise, but when I see a game that lets me roll the windows down and listen to the engine sounds,
            I think \"Test Drive Unlimited\"." %}

Full disclosure -- at the moment, this feature (rolling down windows) doesn't work correctly as the action is not bound to the keyboard.
I reported this to the developers.

# The technicalities

Japanese Drift Master is cool, but does it work well? I'll try to answer that based on my expertise and the data I gathered
while playing the pre-release versions **1.0.17.1** and **1.0.21.1**, as well as a release build **1.1.40.1**.
The game updated ahead of its launch, but most of my observations still apply to the current public build.

## Game engine and system requirements

The final version of JDM runs on **Unreal Engine 5.4**, which is the same UE version as Tokyo Xtreme Racer. Unlike that game, my rig partially falls under
the minimum requirements -- they list an **Intel Core i5-9400F** and an **NVIDIA GeForce GTX 1660**,
while I still use an **Intel Core i9-12900K** with my **NVIDIA GeForce GTX 1070**.
On the CPU front I am set, sitting well above even the recommended specs, but this GPU is pushing it -- as the GeForce GTX 16 series
is a slightly downgraded 20 series, a 10 series card is under the minimum requirements.

Thankfully, my experience wasn't all that miserable. In this case, I opted to go for the highest details I could get reasonably stable 60 FPS on,
which the game was hitting most of the time, but not always. For this review, my settings of choice are:

* 1080p with TSR Quality.
* Frame generation Off (obviously).
* Mirrors Off.
* Motion Blur On.
* Anti-Aliasing, Shadows, and Global Illumination on Medium (Lumen Global Illumination disabled).
* Textures on Ultra (although I might need to reduce that, given I have 8GB VRAM).
* All the other options are on High.

For Shadows, I additionally tweaked my settings with a script, but I'll elaborate on that later in a separate subsection.
The script changes I made in the pre-release version are now mostly reflected in the current public build, so ironically enough,
they made my pre-release screenshots look more like the build you'll be playing.

All screenshots in this post are taken at these detail settings unless stated otherwise.

{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_clhqK335VG.jpg" thumbnail="auto" %}

Starting with some negatives:
* Unfortunately, JDM does exhibit shader stutter, and as of the time of writing this review, the game does not precompile shaders on the first boot.
  This might change later, but during my testing, I had to put up with the stutter -- it wasn't unbearable, but it certainly was noticeable,
  and it soured the experience. Unreal Engine's worst contribution to the gaming landscape handicaps yet another game.
* Anti-aliasing is forced and necessary for the game's art style to look right. Forcing AA off from the console makes the game look grainy.
* Although upscaling is optional, it's enabled by default. Keep this in mind when configuring the game's settings.
* **As of the time of writing this review (at the game version 1.1.40.1), the game has trouble remembering some graphics options and resets them every launch,
  even though they appear to be set correctly in the settings. Right now, this is known to affect the Mirrors option. This bug has been reported and acknowledged by the developers.**
  Should I be notified that this bug is fixed, I will edit this point accordingly.

## In-game graphics options

On the surface, Japanese Drift Master has a standard set of UE5 graphical options and upscalers:

{% include figures/image.html link="/assets/img/posts/jdm-review/screens/jdm-graphics-options.png" thumbnail="auto" %}

* Even though most options conform to the standard scalability groups from Unreal, they are not used at all and instead, all options tweak
  the specific detail variables directly from the code. This means that many INI tweaks will simply not work, as changes done from code take precedence over the project settings.
* Unfortunately, the benchmark is simply a simulation running on an empty screen and not a live demo.

### Graphics presets

JDM comes with a set of 5 presets: **Low**, **Medium**, **High**, **High Plus**, and **Ultra**.
From my observations, High Plus is close to default UE5's High preset, while High slightly scales back compared to the default,
for example by deactivating Lumen. Presets are independent of the resolution scaling, so for my comparisons, I settled on the highest available
resolution scaling option in the review build, **TSR Quality**.

The presets look as follows. Click on the images to open them full screen:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250520193555_1.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250520193726_1.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250520193746_1.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250520193832_1.jpg" thumbnail="auto" caption="High Plus" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250520193854_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250517141130_1.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250517141149_1.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250517141207_1.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250517141234_1.jpg" thumbnail="auto" caption="High Plus" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250517141251_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

* On **Low**, shadows and reflections are basic and low resolution, props have an extremely low draw distance,
  and any lights outside of the ambient lighting practically do not exist. The game still looks acceptable, but it's clearly missing "something".
  It's also way too dark at night.
* On **Medium**, screen-space Global Illumination activates, giving the day environment a slightly darker, more planted look. Shadows and props are rendered further away,
  and at night, some dim light sources appear. More props are placed on the map. In the current build, the volumetric fog is also enabled
  (in the review build I took those screenshots from, it enabled on High instead).
* On **High**, lights are fully featured, volumetric clouds are enabled,
  draw distance is significantly increased (notice the trees on the far away mountain), and shadows are higher resolution, have more cascades (so they draw at a farther distance),
  and show more self-shadowing (like on the rearview mirror in the day scene). Even more props appear.
* On **High Plus**, Lumen Global Illumination and Lumen Reflections kick in, giving the scene a better-lit, more realistic look. Draw distance of small props is further increased.
* **Ultra** introduces a flare effect and further increases the GI quality. The day scene looks slightly darker as it should according to the weather, and the night scene gains
  a more pronounced bloom effect from the light sources. Shadows seem to be softer and blend with the ambiance better. Self-reflections are also introduced.


### Resolution upscaling options

JDM comes with a standard selection of up-to-date upscalers:
* DLSS4
* TSR
* XeSS 2.0.1

Curiously, DLSS is selectable even on hardware that isn't supposed to support it -- in this case, Unreal falls back to TSR.

All upscalers share the same set of presets:
* Native/Ultra (100% resolution scale)
* Quality (66%)
* Balanced (58%)
* Performance (55%)
* Ultra-Performance (50%)

The review build I tested lacked the Native scaling option, so all my testing was done on TSR Quality.
Native was added just before the public launch -- it's way too much for my GTX 1070,
but players using more modern GPUs might be up for it.

### Individual options and the effects of Lumen

I won't be comparing every single graphics option in the game, as this time there are too many of them, so I encourage you to experiment
if you need to reclaim some performance from your game. That said, there are a few outliers I would like to cover.

* **Detail Quality** and **Environment Quality** options alter the complexity of the scene by adding more foliage and props,
  as you could notice on the preset comparisons above.
  These two options require restarting the game to take effect, but they have a huge impact on the GPU load,
  so if you're looking for performance, don't hesitate to experiment with those options.

* **Effects** improve the shading of props and foliage and enable volumetric clouds on High and above.
  I only observed a very minor visual difference otherwise, yet the performance hit is noticeable, so if you don't care about volumetric clouds
  too much, you can get some performance out of this option.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_HMvp2J2zOn.jpg" thumbnail="auto" caption="Low" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_VKv5L8nfp1.jpg" thumbnail="auto" caption="High" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_G91ltEvIMp.jpg" thumbnail="auto" caption="Ultra" %}
  </figure>

* **Shadows** increase the resolution of shadows, the number of cascades, and their draw distance. On High Plus and Ultra, more props cast shadows too
  (such as the signage). On Medium and above, volumetric fog is added. This option also affects lighting in a weird way, which I consider a bug.
  I elaborate on this more at the very end of this review, in [Unreal Engine bugs, in my game?](#unreal-engine-bugs-in-my-game)
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_CFjwTI2f9O.jpg" thumbnail="auto" caption="Low" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_tHX6MWrEKC.jpg" thumbnail="auto" caption="Medium" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_IuBXCYTnxD.jpg" thumbnail="auto" caption="High" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_Vxrt1c0Scg.jpg" thumbnail="auto" caption="High Plus/Ultra" %}
  </figure>

* **Global Illumination** controls the lighting of the entire scene. At Medium, Screen-Space GI enables, although I struggled to see any improvement
  on the scenes I used for testing -- perhaps other scenes show more improvements on higher details. At High Plus, Lumen Global Illumination enables,
  giving the entire scene RTGI. It's probably the single most impactful option in the game, both in terms of performance, and visual improvement.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_6eZYTDqZWI.jpg" thumbnail="auto" caption="Low/Medium/High" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_TXueTfgMXE.jpg" thumbnail="auto" caption="High Plus/Ultra" %}
  </figure>
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_j96PKvCuJy.jpg" thumbnail="auto" caption="Low/Medium/High" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_oqLmpjb09k.jpg" thumbnail="auto" caption="High Plus/Ultra" %}
  </figure>

* **Reflections** are relatively self-explanatory. On Low/Medium/High, screen-space reflections of progressively better quality are used,
  while on High Plus and Ultra, Lumen reflections kick in.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_XTCo7qTePu.jpg" thumbnail="auto" caption="Low/Medium" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_7uxG3tHooc.jpg" thumbnail="auto" caption="High" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_JUPOCn8Flv.jpg" thumbnail="auto" caption="High Plus" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_gszQxAqGiT.jpg" thumbnail="auto" caption="Ultra" %}
  </figure>

  Lumen Reflections requires Lumen Global Illumination to be active. If screen-space GI is used, reflections are screen-space even on Ultra.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_scAhjf2r4V.jpg" thumbnail="auto" caption="High GI" %}
  {% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_nIJrah0EsV.jpg" thumbnail="auto" caption="Ultra GI" %}
  </figure>

***

Regarding the usage of Lumen, I'm satisfied with JDM's direction -- ray-traced Global Illumination improves the game's visuals drastically,
but they've also been obviously crafted with screen-space effects in mind. Lower details look *worse*, but they don't look *bad or incomplete*.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250515101206_1.jpg" thumbnail="auto" caption="Global Illumination, Reflections - High, Shadows - Medium" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/20250515101223_1.jpg" thumbnail="auto" caption="Global Illumination, Reflections, Shadows - High Plus" %}
</figure>

Naturally, ray-traced effects require considerable horsepower and even powerful GPUs might struggle to maintain high frame rates at higher resolutions,
which is why many modern Unreal Engine 5 games (including this one) enable resolution scaling by default.
It's up to you to decide if you wish to deal with this in return for more natural lighting and reflections.

# Benchmarks

Is benchmarking the game on a GPU under the minimum requirements a sensible idea? Probably not, but I believe it can still help -- because realistically speaking,
those values can be treated as an absolute baseline showing that the game will perform *at least this well* on supported hardware.
I suspect the relative performance between presets might be similar on more powerful hardware too.

I ran all the benchmarks on a pre-release version **1.0.17.1**, running at 1920x1080 with TSR Quality -- as of the time of writing this review,
the public version **1.1.40.1** has performance figures within the margin of error compared to my earlier samples.
In all those benchmarks, I started the game around noon, in the first garage the player gains access to,
then I turned right and continued driving along the road for the entire duration of that 30-second benchmark.
{% include figures/image.html thumbnail="/assets/img/posts/jdm-review/benchmark-1.webp" style="natural" %}

As with Tokyo Xtreme Racer, I also benchmarked the two highest detail presets with Global Illumination set to High, to disable Lumen.
Whether you need performance or simply don't want your GPU to heat up too much, it's an option worth exploring.
{% include figures/image.html thumbnail="/assets/img/posts/jdm-review/benchmark-2.webp" style="natural" %}

Personally, I consider those results satisfactory. Considering those benchmarks are done on a 2016 GPU that is under the minimum requirements,
the fact the game is evidently playable on Medium details is a pleasant surprise. With lower-spec PCs I imagine some CPU bottlenecks may start appearing,
but due to the obvious imbalance of my home setup, I am not able to pinpoint those effectively.

# Steam Deck

I also tested the game on my LCD Steam Deck for some time. The experience isn't ideal, but it works. I tried the game on **Medium** details with TSR Balanced,
but the Deck cannot sustain a stable 30 FPS at these details, even if at first glance it seems that it can. On **Low** with TSR Balanced, the framerate oscillates between
30 and 40 FPS, so locking the game to 30 FPS is reasonable.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-1-medium.jpg" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-2-medium.jpg" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-3-medium.jpg" %}
<figcaption>At first glance, the game runs fine on Medium, but frame drops show up very quickly.</figcaption>
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-1-low.jpg" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-2-low.jpg" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/deck-3-low.jpg" %}
<figcaption>On Low details, the experience is much smoother. Add a 30 FPS limiter and you should be fine.</figcaption>
</figure>

The good:
* On the Deck screen, even the lowest details with TSR Balanced look acceptable.
* The game doesn't slow down under 60 FPS, so locking to 30 or 40 FPS is perfectly fine.
* The game autosaves frequently, so it's good for short sessions.
* The developers have promised future performance optimizations for the Deck and a Steam Deck preset. At the time of writing this review, this preset doesn't yet exist.

The bad:
* The battery drains incredibly fast -- on a Deck LCD, you're likely looking at under 1 hour of playtime.
* At one point, my Deck ran out of VRAM, and the game locked up the entire console, putting it at one frame per half a minute. At that point,
  I was playing on Medium textures, so I strongly recommend sticking to Low textures.
* There are a few UI bugs on 16:10 displays. I have reported them directly to the developers, so they are aware of those issues.
* The game misdetects Deck's resolution as 800x1280, and an attempt to change it breaks the resolution permanently for that session.

Overall, do I think it's a good experience on Deck? Definitely not if you plan to play on the go due to the extreme battery drain, but if you play at home or docked,
you can have some fun. It's not an optimal way to play JDM, though.

# Unreal Engine bugs, in my game?

Can my blog post be complete without highlighting obscure bugs? Of course not 🙃

While tailoring the settings to my liking I noticed that my game was annoyingly dark. I narrowed it down to the Shadows Detail setting -- on High,
the game is properly bright, but that setting is too much for my GPU. On Medium, I have good performance, but everything is dark.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_Pz9IvN2Bso.jpg" thumbnail="auto" caption="Medium Shadows" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_qJPAqLOzOQ.jpg" thumbnail="auto" caption="High Shadows" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_XEW6gAzGgz.jpg" thumbnail="auto" caption="Medium Shadows" %}
{% include figures/image.html link="/assets/img/posts/jdm-review/screens/JDM-Win64-Shipping_vYYebVt3Jv.jpg" thumbnail="auto" caption="High Shadows" %}
</figure>

Lowering Shadows details lowers their draw distance, and so lights draw at a lower distance too -- this makes sense. However, they clearly shouldn't
be dimmer even at a close range! For this, I could leverage the fact that JDM uses Unreal Engine 5, and dive into the code directly.

The light draw distance is controlled by a `r.LightMaxDrawDistanceScale` cvar. Medium Shadows set this value to `0.5`, while High and above leave it at
the default `1.0`. This value is then used to calculate the final brightness of the light source in `GetLightFadeFactor` (comments added by me)

```cpp
float GetLightFadeFactor(const FSceneView& View, const FLightSceneProxy* Proxy)
{
  FSphere Bounds = Proxy->GetBoundingSphere();

  const float DistanceSquared = (Bounds.Center - View.ViewMatrices.GetViewOrigin()).SizeSquared();
  extern float GMinScreenRadiusForLights;
  float SizeFade = FMath::Square(FMath::Min(0.0002f, GMinScreenRadiusForLights / Bounds.W) * View.LODDistanceFactor) * DistanceSquared;
  SizeFade = FMath::Clamp(6.0f - 6.0f * SizeFade, 0.0f, 1.0f);

  extern float GLightMaxDrawDistanceScale; // r.LightMaxDrawDistanceScale
  float MaxDist = Proxy->GetMaxDrawDistance() * GLightMaxDrawDistanceScale; // Max distance is decreased
  float Range = Proxy->GetFadeRange(); // Fade range is not
  float DistanceFade = MaxDist ? (MaxDist - FMath::Sqrt(DistanceSquared)) / Range : 1.0f; // Does this make sense??
  DistanceFade = FMath::Clamp(DistanceFade, 0.0f, 1.0f);
  return SizeFade * DistanceFade;
}
```

Do you see something wrong? `FadeRange` and `MaxDist` are both configurable per-light, yet only one of them is decreased as details decrease.
As `FadeRange` indicates the area where the light should start fading down to zero intensity, this creates a noticeable problem -- in an extreme case,
where an artist sets `FadeRange` and `MaxDist` to equal values as they want the light to fade from 100% to 0% smoothly throughout its entire draw distance,
this will cap the light at 50% intensity! I believe this is exactly what's happening in JDM.

Funny enough, in Unreal Engine 5.5, Epic noticed this issue, and then... left it as-is to preserve "legacy behavior".
```cpp
// NOTE: Feels like we should scale fade range by GLightMaxDrawDistanceScale as well, but would change legacy behavior
float Range = Proxy->GetFadeRange();
```
Clearly, they haven't thought of a case like this, where the "legacy behavior" is undesirable and visually broken.

As usual, the fix is trivial - simply scale `Range` by `GLightMaxDrawDistanceScale`, and the bug should be resolved!
**I reported this issue to JDM devs and it has been acknowledged, and might potentially be fixed in the future.**
I might also report this issue to Epic directly and showcase that their insistence on preserving the wrong behavior hurts games that don't expect it.

# What's next for JDM?

The developers of Japanese Drift Master have published a roadmap for the next 9 months, promising more cars, features, and bug fixes.
I enjoy the game in its current iteration a lot already, but there are a few technical things I'd like to see addressed:
1. Resolution scaling should be exposed as a slider, not only presets. This is what Tokyo Xtreme Racer does, and everyone is happy.
2. A lot of folks, myself included, end up accidentally running out of VRAM when ramping up the settings too high. A VRAM usage indicator in the menus would be nice.
3. With some tweaks, JDM could be a great Deck-ready game. I hope the promised performance updates deliver on that.

Personally, I'm glad to see a brand new contender in the racing games scene that is ambitious and (mostly) delivers on the promise, and on top of everything,
it comes from my home country 🙃 Happy drifting!
