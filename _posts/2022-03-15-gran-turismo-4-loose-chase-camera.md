---
layout: post
title: "Gran Turismo 4 Loose Chase Camera"
excerpt: "Much awaited Gran Turismo 3-like camera for Gran Turismo 4 and Tourist Trophy."
thumbnail: "assets/img/posts/gt4-gt3-cam/gt3-cam-banner.jpg"
feature-img: "assets/img/posts/gt4-gt3-cam/gt3-cam-banner.jpg"
image: "assets/img/posts/gt4-gt3-cam/gt3-cam-banner-full.jpg"
twitter: {card: "summary_large_image"}
game-series: ["gran-turismo-4", "tourist-trophy"]
date: 2022-03-15 20:10:00 +0100
tags: [Releases]
---

*TL;DR - if you are not interested in an overview of those cheat codes,
scroll down to the [**Download**](#download) section for download links.*

***

Those who played Gran Turismo 4 are probably familiar with the issue at hand, but in case you didn't -- one of the changes
introduced in Gran Turismo 4 is a new chase camera. The previous games had a chase camera that would swing gently to the sides
in corners; while Gran Turismo 4 technically does the same, the camera is much "stiffer" and stays centered even when taking
corners at a very high speed.

As you may have guessed already, many people disliked the change, and sadly we never got an in-game option to customize
the camera (it took until GT Sport for this to become an option) -- until now.

Interestingly, Polyphony made that change **very** late in development -- GT4 First Preview, one of the demos released well after GT4 Prologue
still has a GT3-like chase camera!

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I never before compared an &quot;old&quot; Gran Turismo chase camera with the &quot;new&quot; one introduced in GT4, so I wasn&#39;t sure how big of a deal it is. Now comparing GT4 and GT4 First Preview (still using &quot;old&quot; chase camera), the difference is indeed major. Interesting! <a href="https://t.co/l4GgPLel6f">pic.twitter.com/l4GgPLel6f</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1449783924654235651?ref_src=twsrc%5Etfw">October 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

In the past, there have been attempts at bringing a GT3-style camera back to GT4, but none of them replicated the behaviour exactly.
With my approach, I investigated the **exact** differences between GT4 First Preview and the final GT4. For what I need,
I assumed that GT4 FP's camera is exactly how a GT3-style camera would have behaved in GT4 had it not been changed last minute:
* The chase camera works as if on a spring and it has two hardcoded parameters.
* "Max angle" value determines how far the camera can lean before the spring effect stops it. Final GT4 sets this value to `15.0`, GT4FP sets it to `10.0`.
* "Damper" value determines how fast the camera self-centers. Final GT4 sets this value to `120.0`, GT4FP sets it to `30.0` -- making the spring effect 4 times stronger in the final game!

With a cheat code modifying just those two values, GT4 First Preview's camera is back in the final GT4 (and Tourist Trophy)!

<div align="center" class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/5kk63H3nYsQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

But what if you wanted to customize the camera further? Since the cheat code I created is intended to be as user-friendly as possible,
adjusting parameters is trivial. For example, here I made the camera even stiffer than the default ("damper" set to `360.0`), thus emulating the GT5/GT6 chase camera:

<div style="width:100%;height:0px;position:relative;padding-bottom:56.250%;"><iframe src="https://streamable.com/e/p5wz8z" frameborder="0" width="100%" height="100%" allowfullscreen style="width:100%;height:100%;position:absolute;left:0px;top:0px;overflow:hidden;"></iframe></div>

# Far chase camera

Aside from the camera stiffness, GT4 Prologue and GT4 First Preview have one more difference -- instead of the hood/roof camera, they have a second chase camera, located farther and higher from the car:

<p align="center">
<img src="{% link assets/img/posts/console-codes-2/gt4p-units.jpg %}">
</p>

The final GT4 does not remove this camera entirely; instead, it is available as one of the replay cameras.
With another cheat code, I managed to **add** this camera back to the in-race selection as a new, fourth selectable camera:

<p align="center">
<img src="{% link assets/img/posts/gt4-gt3-cam/gt4-far-chase-cam.jpg %}">
</p>

# Download

All listed cheats can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/gt/gran-turismo-4.md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download cheat codes for Gran Turismo 4</a> \\
<a href="{% link _games/gt/tourist-trophy.md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download cheat codes for Tourist Trophy</a>