---
layout: post
title: A technical dive into the new Tokyo Xtreme Racer
date: 2025-01-21 10:30:00 +0100
excerpt: Looking into the game ahead of the Early Access launch with my first impressions, benchmarks, and Steam Deck compatibility.
game-series: ["tokyo-xtreme-racer-2025"]
image: "assets/img/games/bg/tokyo-xtreme-racer-2025.jpg"
thumbnail: "assets/img/games/bg/tokyo-xtreme-racer-2025.jpg"
feature-img: "assets/img/games/bg/tokyo-xtreme-racer-2025-alt.jpg"
twitter: {card: "summary_large_image"}
tags: [Articles]
---

* TOC
{:toc}

# Introduction

It's been 18 years since the last release of a [Tokyo Xtreme Racer](https://en.wikipedia.org/wiki/Tokyo_Xtreme_Racer){:target="_blank"}
game outside of the two not-so-well-received mobile installments. This is about to change, as Genki is releasing a new TXR game
in Steam Early Access on January 23rd:

<div class="center-blocks">
<iframe src="https://store.steampowered.com/widget/2634950/" frameborder="0" width="646" height="190"></iframe>
</div>

A few days ago, I received a review key for the game and was given a free hand to play and inspect it however I wish;
[a press kit](https://x.com/Tokyo_Xtreme/status/1873759324541255952){:target="_blank"} was also sent to me (thanks, folks!), but as of the time of publishing this review,
it's stuck in transit 😬.
I spent some time playing the game (and trying to break it, of course), and I ran a few benchmarks to determine how well my PC could handle
the game in this state. Needless to say -- I am more than satisfied with how well the game treated me.

If you are interested in a more gameplay-focused review, you might want to check
[Adam's review of the game on The Drive](https://www.thedrive.com/news/tokyo-xtreme-racer-early-access-review){:target="_blank"} before continuing with my post.
In my review, I'm taking a different approach: I will focus on the technical experience, scalability, options, and performance.
I'm no Digital Foundry, but my findings should still help players pick the optimal settings to play the game smoothly on their PCs.
Believe me -- this game is extraordinarily scalable, much more than I initially expected.

# The game

{:.sidenote}
If you'd rather jump to reading the technical overview of the game right away, go ahead and skip to [The technicalities](#the-technicalities).

Let's get back to the basics. What *is* Tokyo Xtreme Racer anyway? Perhaps you know this series under a different name, as throughout the years,
different publishers gave it many, **many** different titles:
* **Tokyo Xtreme Racer** is the US title, most widely used out of all.
* **Shutokō Battle** is the original Japanese title.
* **Tokyo Highway Battle** is the name given to a 1996 PS1 game published internationally.
* **Tokyo Highway Challenge** is the name given to the two Dreamcast games published in Europe.
* **Street Supremacy** is the name given to a 2005 PSP game published internationally.
* **Import Tuner Challenge** is the name given to a 2006 X360 game published internationally.
* Like a cherry on top, the two **Tokyo Xtreme Racer: Drift** games are technically **not** part of the Shutokō Battle series.
  Instead, they belong to a spin-off series, called **Kaidō Battle**.[^kaido-battle-confusion]

[^kaido-battle-confusion]: You don't want to know how confusing the international names of games in this spin-off are.

Not confusing at all, right? Thankfully, this upcoming release is free of this mess:
it's simply called **Shutokō Battle** in Japan and **Tokyo Xtreme Racer** everywhere else. Phew.

Fret not, though, as moving forward things are not this complicated. In fact, the core gameplay loop in all TXR games
is simplistic: you cruise at night around the highways located (for the most part) in Tokyo, flash your headlights at the rival cars
to challenge them to a race, then overtake them and stay in front for long enough to win.
If you've ever seen any of the "highway battle"-esque mods for games like Assetto Corsa, Tokyo Xtreme Racer is the series that inspired them all.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_8GDaPci446.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_WCwP2tKd6c.jpg" thumbnail="auto" %}
<figcaption markdown="span">Challenged a rival and then stayed in front of them for long enough? Congrats, you win!</figcaption>
</figure>

My personal experience with TXR isn't too broad: I only started playing these games recently and only got up to the first PS2 game, TXR Zero,
so I wouldn't be able to tell you yet how well the newer games (especially ITC) play.
Regardless, the 2025 Tokyo Xtreme Racer delivers much of the same qualities as the classic games: you start with a bunch of money and a few cars
to choose from, you defeat a few easy rivals, upgrade your car (and eventually get a new one), and make your way to defeating new teams
with progressively faster drivers.

{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_EgN7xJ2wxK.jpg" thumbnail="auto"
        caption="New to the series is the ability to challenge and race traffic cars. If you fancy steamrolling a truck, now you can." %}

The core of the game is exactly as simple as it sounds, but it's presented in a way that doesn't get old and makes you want to race more.
I started my playthrough in a tiny Suzuki Swift that defeated the first few teams of rivals on the famous
[C1 Route](https://en.wikipedia.org/wiki/Inner_Circular_Route) without much trouble, before unlocking the Shinkanjo, Wangan, and Yokohane routes.
As the game is in Early Access, it's not yet content complete: it currently features 50 cars, and about half of the game's planned rivals,
at the moment sitting at around 200. Much like in the older games, each rival has their backstory you get to learn as you defeat them -- the game
is light on a concrete "story", but those rival backstories are the one thing tying the lore of the series together.

{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_ZV2KfDV8p3.jpg" thumbnail="auto" %}

What makes this game (and the series in general) tick is the *vibe*. Much like NFS Underground is remembered for its immaculate representation
of the tuner culture, Tokyo Xtreme Racer immerses you in the environment of the infamous Japanese highway racers. You find yourself looking
for the best way to tune your car for each segment of the highway, make it look and drive well, and constantly wondering what car you'll
be challenging on your route next.

Or, if you want to just cruise on the Wangan and soak in the energy of a wide, mostly-empty highway at night,
you can -- in the 2025 Tokyo Xtreme Racer this is made even easier by the addition of a toggleable autopilot. It's a bit of a missed opportunity
that the game doesn't currently feature a Photo Mode or any sort of customizable camera, as it could go very well with the automatic cruising.
But hey, we are still in Early Access: other than the other half of the game, those are the exact kinds of things that perhaps can make their way
into the game during this period.

{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_P2FLCLorMY.jpg" thumbnail="auto" %}

# The technicalities

Enough on the gameplay itself, as I don't intend this to be a review of how the game plays: I wish to focus on how the game **works**.
The main point of this review is to detail my experience with the game in its current state. The version I tested is the **0.10.0 Early Access Version**.
It has also been updated during the weekend as I was writing this review, but all benchmarks were done on the most up-to-date version.
The build I am testing may or may not be the same as the launch build once the game releases on the 23rd.

## Game engine and my experience on an underpowered GPU

The 2025 Tokyo Xtreme Racer is built on **Unreal Engine 5.4**, which has initially been met with a lot of skepticism; for a good reason,
considering that numerous recently released games using Unreal Engine 5 are plagued with stutter and subpar performance even on the top end GPUs.
I had my own reasons to worry -- the game's minimum system requirements list an **Intel Core i7-7700** and an **NVIDIA GeForce GTX 1050Ti**.
On the CPU front, I was more than ready with my **Intel Core i9-12900K**, but not so much on the GPU front with my **NVIDIA GeForce GTX 1070**.
A few Unreal Engine 5 games I tried ran terribly, so I was ready to be miserable. I also remembered
[my adventures with EA Sports WRC showing artifacts on my GPU]({% post_url 2023-11-22-ea-sports-wrc-geforce-gtx-10-series-bug %}),
even though the GeForce 10 series was within the minimum system requirements.

Considering the minimum requirements state they target Low graphics options at 1080p, I expected to be confined to a mix of Low
and Medium settings. Instead, I am running the game at a stable 60 frames per second at:
* Native 1080p (no upscaling)
* FXAA
* Global Illumination on Medium (which disables Lumen Global Illumination)
* Textures on Ultra
* All the other options on High

All screenshots posted above were also taken at these detail settings, so albeit not maxed out, they still look great.

{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/2634950_20250118235221_1.jpg" thumbnail="auto"
    caption="This screenshot was taken with supersampling, but other than that, it's at the exact detail settings I play the game at." %}

Needless to say, when I [shared that news online](https://x.com/__silent_/status/1880227794690666740){:target="_blank"},
people were positively surprised and the perception of the engine of choice shifted immediately.
Turns out, not every UE5 game has to run poorly on older graphics cards.
Not only that, but I did not observe practically any shader compilation stutter or traversal stutter!

This news also benefits those with more modern cards -- after all, if a GTX 1070 from 2016 can run the game comfortably on High
details, anything newer can likely max the game out without much trouble.

## In-game graphics options

Tokyo Xtreme Racer comes with a fairly standard set of Graphics Settings that conform to the default Unreal's scalability options.
A few additional options are present though:
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/Tokyo_Xtreme_Racer_graphics.png" thumbnail="auto" %}

In this section, I will provide a comparison between all available presets, and elaborate (with examples) on the graphical settings
that make the most difference. Some of the options seem to make no difference, so it's good to isolate the meaningful ones!

For now, I will be only showcasing the visual differences. For benchmarks, scroll down.

### Anti-Aliasing and Upscaling

Most notably, Anti-Aliasing options are not like a typical UE5 game: you can select between **None**, **FXAA**, **TSR**, and (on supported hardware)
**DLSS**. There is no forced TAA, and upscaling options are independent of Anti-Aliasing, which means the game can have a perfectly sharp and stable image!
Unfortunately, the upscaling options cannot go above 100%, only below -- so supersampling is not possible without the config file changes.
DLSS can be used as both an upscaler and an anti-aliasing solution: setting the AA mode to DLSS, and keeping the Upscaling Quality at Native will effectively
give you DLAA.

### Graphics Quality presets

The game comes with a standard set of 4 presets: **Low**, **Medium**, **High**, and **Ultra**. They act as a good baseline for further configuring
the game to your liking, with one nasty caveat -- while these options do not affect Anti-Aliasing, they **do** affect Upscaling, setting the scales to **50%**,
**58%**, **67%**, and **100%** respectively! This makes for a pretty poor representation of how the options truly look, so in my comparison below,
and later in the post, **I will always stick to using FXAA and 100% resolution scaling.** This way, the screenshots and benchmarks will be consistent
and more representative of how the options affect the game.

The presets look as follows. Click on the images to open them full screen:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_ygJuaTWJlN.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_j3hqqeCSC3.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_xDSSGrLl3b.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_MG8p6c74l9.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_CSmWJUNcAh.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_21MctOOEsc.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_Mr6aHc5v15.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_29H0MD0YMV.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_gV7tWAI3QE.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_vNd7TLDLCR.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_II1nPwLKls.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_CeYMx8TdPq.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

* On the **Low** preset shadows, reflections, and post-processing practically do not exist. The game doesn't look bad, but something is definitely missing.
* On the **Medium** preset dynamic shadows, reflections, and a subtle vignette effect appear. The draw distance is also visibly boosted.
* **High** preset introduces Lumen Global Illumination and Lumen Reflections, giving more light to the entire scene, and replacing sharp screen-space reflections
  on cars and in the tunnels with software ray-traced reflections that account for the material roughness. Shadows are also even higher resolution.
  Bloom is now applied to distant light sources like lamposts and building windows.
* **Ultra** preset further bumps up the draw distance and shadow resolution, and introduces self-reflections: you can see that on the first comparison,
  the third brake light reflects in the rear windshield.

### Individual options and recommended settings

For each option, I'll explain what it does (if I managed to figure it out), and my recommendation on the setting to use.
Of course, your mileage may vary depending on your PC specs.

* **Draw Distance** -- self-explanatory, higher settings make further objects draw on-screen. Option I recommend: **As high as you can**.

* **Post Processing** -- higher settings enable a vignette filter and bloom on the light sources. However, I did not see any differences past High, visual or performance.
  Option I recommend: **High**.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_IE6sLKU9A6.jpg" thumbnail="auto" caption="Low" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_W2P3NtS4hv.jpg" thumbnail="auto" caption="Medium" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_H6Ly2eZKhU.jpg" thumbnail="auto" caption="High/Ultra" %}
  </figure>
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_b3nt1sNDUp.jpg" thumbnail="auto" caption="Low" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_VG8U9Bxqxu.jpg" thumbnail="auto" caption="Medium" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_bGghgf9rG0.jpg" thumbnail="auto" caption="High/Ultra" %}
  </figure>

* **Shadows** -- at Low, only static shadows exist. At higher settings, shadow resolution is bumped up, and seems like more light sources cast shadows too.
  Ultra shadows appear to be very heavy, although they look the best. Option I recommend: **High, or Ultra if you can handle it**.
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_QHoSDGPXVd.jpg" thumbnail="auto" caption="Low" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_tryxUs4ZuV.jpg" thumbnail="auto" caption="Medium" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_UtLcmUamKL.jpg" thumbnail="auto" caption="High" %}
  {% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_u39lfaIVSP.jpg" thumbnail="auto" caption="Ultra" %}
  </figure>

* **Global Illumination** and **Reflections** -- at Low/Medium, these options use screen-space effects. At High/Ultra, Lumen ray-tracing features enable,
  impacting the look of the entire scene at the cost of performance. These two options are closely related to each other and also the ones my non-RTX card could not handle
  right. I'll be elaborating on Lumen separately in the next section. Option I recommend: **High or Ultra if want Lumen, otherwise Medium GI and High Reflections**.

* **Effects** -- this option appears to change the way the sky looks, perhaps switching between a pre-rendered image and volumetric clouds. However, the change is
  so subtle I struggled to see any difference. Option I recommend: **High if you want peace of mind, Low if you're looking for performance**.

* **Shading** -- this option, undocumented even in Unreal docs, appears to change the used shader quality. I couldn't spot any difference between the options,
  visual, or performance. Option I recommend: **Any**.

* **Texture** -- makes the game load higher resolution versions of textures, and enables progressively higher Anisotropic Filtering. Option I recommend:
  **You will probably be fine with Ultra**, even on Steam Deck I use that without issues.

### More about Lumen

The **Global Illumination** and **Reflections** options appeared to be a source of confusion, but thankfully, they actually follow the default behavior
of Unreal Engine 5:
* Lumen Global Illumination toggles at **Global Illumination High**.
* **Reflections** use screen-space reflections at **Low/Medium** and Lumen (ray-traced) Reflections at **High/Ultra**. However, Lumen Reflections require Lumen GI,
  so they are enabled **only** if Global Illumination is also set to **High/Ultra**.

To clarify -- Lumen is the Unreal's implementation of ray tracing. Unsurprisingly, it is also the main performance hit in the game:
for example, I run the game just fine with Global Illumination Medium and Reflections High, because then Lumen is inactive.
This effect is done purely in software (in compute shaders), that's why it works on my non-RTX GPU and is just very demanding.
As far as I can tell, there is **no** hardware ray tracing in the game.

Is ray tracing worth the performance hit in this game? The effects seem to be negligible in open spaces, but quite noticeable in tunnels and on car reflections.
Lumen GI makes the light bounce off all surfaces and contribute to how nearby objects are lit, which is most noticeable when two cars are close together
and under a strong source of light. With Lumen Reflections on top, screen-space reflections are disabled and replaced with ray-traced reflections,
so even off-screen objects can contribute to the final look. Material roughness is also accounted for, so reflections like the ones in the tunnels are no longer crystal clear;
instead, they are realistically fuzzy and scattered.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_5nWf56DDce.jpg" thumbnail="auto" caption="No Lumen" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_xjw2HQPkxe.jpg" thumbnail="auto" caption="Lumen GI" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_4XEGdZtsZl.jpg" thumbnail="auto" caption="Lumen GI + Reflections" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_Kw7j24wrDy.jpg" thumbnail="auto" caption="No Lumen" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_yRiolJljVD.jpg" thumbnail="auto" caption="Lumen GI" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_UcuJyBdDto.jpg" thumbnail="auto" caption="Lumen GI + Reflections" %}
</figure>

In some cases, possible minor oversights surface when playing without Lumen. For example, the road in this tunnel is correctly lit when not using Lumen GI, but the walls are not:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_rWFRBua9nN.jpg" thumbnail="auto" caption="No Lumen" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_QLxFYKV0Nr.jpg" thumbnail="auto" caption="Lumen GI + Reflections" %}
</figure>

# How well does the game run? Benchmarks

I said earlier that my GeForce GTX 1070 handles the game more than fine at native 1080p, but how is that reflected in metrics? I benchmarked the four graphical presets
(at 100% Scaling, as I mentioned at the beginning of the previous section) in a 45-second long drive around the C1 Inner Loop, starting outside and heading through multiple tunnels.

The results show the game is quite scalable, as was said earlier:
{% include figures/image.html thumbnail="/assets/img/posts/txr2025-review/benchmark-1.webp" style="natural" %}

Low and Medium are obviously playable and they fare great, High and Ultra are both noticeably slower.
However, since both these presets include Lumen, I ran two more tests, where I kept the preset as-is,
but turned the **Global Illumination** down to Medium in order to disable Lumen GI and Reflections:
{% include figures/image.html thumbnail="/assets/img/posts/txr2025-review/benchmark-2.webp" style="natural" %}

IMO these results are great and show exactly why I considered the game playable on High details.
Ultra is still quite slow on this machine (yet still faster than High with Lumen), but as noted in the detailed options breakdown,
it's mostly due to Ultra Shadows being demanding. Obviously, on PCs with newer and beefier GPUs,
Lumen will not drop the performance down to unplayable framerates, but the performance hit will be measurable regardless of the GPU.

Out of sheer curiosity, I also attempted to run the game on an older PC I have access to, with **Intel Core i7-6700K** (one generation under the minimum requirements)
and **NVIDIA GeForce GTX 550Ti** (half a decade under the minimum requirements), and...
[**it works!** I would not call it playable, but it's hard to expect that from a 2011 GPU](https://x.com/__silent_/status/1881343596395418100){:target="_blank"}.
Although 60 FPS is achievable on the lowest details and with upscaling, cars exhibit graphical artifacts, and Unreal warns the user about outdated drivers on every launch
(since NVIDIA stopped supporting Fermi cards in 2018).


# Steam Deck experience

Like numerous other people who got the game early, I also took the opportunity to test TXR on my Steam Deck.
Looking at the above benchmark, it shouldn't be a surprise that the game works fine!
On the lowest details, the game runs without any issues whatsoever and never dips under 60 frames per second.
It has enough headroom to accommodate a few options (like Global Illumination, Draw Distance, and Textures)
to be bumped up to Medium, too.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/20250120232934_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/20250120232123_1.jpg" thumbnail="auto" %}
</figure>

The good:
* On the lowest details, Deck has no issue keeping stable 60 FPS.
* 1280x800 is supported out of the box, so there are no black bars on the top and bottom of the screen.
* The game handles touch and gamepad input just fine, although, at the time of writing this review, no official presets were present yet.
  However, manually selecting a gamepad preset worked well.
* Native Steam Deck prompts are present!

The bad:
* The biggest issue of them all -- **at the moment, the game slows down when it's running at under 60 FPS**.
  This makes the 40Hz mode on the Deck unusable but also means that those with lower-end PCs do not have the option to target 30 FPS.
* The UI is a bit small for the Deck, although it's still readable if you squint.
* Unsurprisingly, the game drains the battery pretty fast.

Overall, would I recommend getting the game to play on Deck? **Yes!** The game already runs very well on this device, and it can only get better over time.
In fact, its performance on Deck already got better between the time I first tried it last week, and now, as the latest pre-release patch noticeably improved
the game's performance.

# What's next for TXR?

Once TXR launches on Steam on the 23rd, it's expected to stay in Early Access for four months. During this time, we may expect to see the second half of
the game completed, and more cars added. The console ports were not ruled out, but their existence depends on how well the game will be received on PC.

As for my personal wishlist? I would love to see an option to import custom decals in the Livery Editor. The selection of decals is already quite wide
(and it will likely expand later in the EA phase), but, given my modding spirit, I already could not help but take advantage of the fact
it's an UE5 game:

{% include figures/image.html link="/assets/img/posts/txr2025-review/screens/TokyoXtremeRacer-Win64-Shipping_geJxq5AQoC.jpg" thumbnail="auto"
     caption="COOOOKIE" %}

For now, I'll continue racing! I'll keep my fingers crossed for this game's success, as it delivers exactly what you would expect from a Tokyo Xtreme Racer game.
It's old school at heart, and in the age of enormous live-service games, it's a great thing.

***
