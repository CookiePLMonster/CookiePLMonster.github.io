---
layout: post
title: "New modifications for Gran Turismo 2"
excerpt: "A pack of new and remade cheat codes to make the game look better than ever."
thumbnail: "assets/img/posts/gt2-cheats/gt2-banner.jpg"
feature-img: "assets/img/posts/gt2-cheats/gt2-banner.jpg"
image: "assets/img/posts/gt2-cheats/gt2-banner.jpg"
twitter: {card: "summary_large_image"}
game-series: "gran-turismo-2"
date: 2021-09-06 18:00:00 +0200
tags: [Releases]
juxtapose: true
---

*TL;DR #1 - if you are not interested in an overview of my new Gran Turismo 2 cheat codes,
scroll down to the [**Download**](#download) section for download links.*

*TL;DR #2 - if you are currently using **any** of my Gran Turismo 2 cheats, please redownload them.
Every single GT2 cheat published on my website has been updated.*

***

If you're following me on Twitter, you might have noticed that for the past few weeks I've been [revisiting my currently released Gran Turismo 2 codes](https://twitter.com/__silent_/status/1428127640372846595?s=20).
The initial plan was to only update the widescreen fix, but as usual, I dug deeper in the game and the result of it is a total of **six new cheats** and two revised cheats.
Needless to say, let me briefly showcase every new and revised cheat.

**DISCLAIMER:** Every cheat I showcase here has been developed with [DuckStation](https://github.com/stenzek/duckstation/) in mind. Since DuckStation's cheat system implements more codes than a regular GameShark
cheat device, I cannot guarantee these cheats work correctly with any other emulator. In the case of Gran Turismo 2, using these extended codes was essential for getting the cheats to work without side effects,
so I cannot provide versions not using them.
Additionally, when making these cheats I found several bugs in DuckStation. If you encounter **any** issues while using them, please make sure your DuckStation is up to date on the **preview** channel.

# New cheats

## Widescreen fix 2.0
While I was hosting a widescreen fix for Gran Turismo 2, originally made by **HugoPocked**, for a while, I recently picked it up again because I wanted to perfect it further.
The current cheat worked fine in race and in most menus, but also came with shortcomings -- some menus and the rear view mirror were visibly squashed, and with the way the cheat was done
fixing it was impossible.

I decided to pick it up again using HugoPocked's cheat as the starting point, and tracked down the exact source of data determining the viewport dimensions.
The result of my research is a widescreen cheat that is much longer than the previous one (from 7 to 70 lines!), but also patches the actual viewport data for different screens
instead of modifying it per-code context. This is how my new cheat compares to the old one in those few previously imperfect cases:

<div class="media-container small">
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/loading-before.jpg" left-label="Old"
            right="/assets/img/posts/gt2-cheats/loading-after.jpg" right-label="New" %}
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/race-before.jpg" left-label="Old"
            right="/assets/img/posts/gt2-cheats/race-after.jpg" right-label="New" %}
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/gtmode-before.jpg" left-label="Old"
            right="/assets/img/posts/gt2-cheats/gtmode-after.jpg" right-label="New" %}
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/postrace-before.jpg" left-label="Old"
            right="/assets/img/posts/gt2-cheats/postrace-after.jpg" right-label="New" %}
</div>

This is not the only benefit of a new cheat -- since it now operates on the screen sizes, it's possible to trivially calculate proper values for any aspect ratio.
Because of this, I now ship **16:9** and **21:9** variations of the cheat on my blog, but I have also published a Python script I used to generate these cheats.
With this script, you may generate a widescreen code for all supported game versions (every version except for NTSC-U 1.0) for any aspect ratio you wish to use. For example, 64:9:
{% include figures/image.html link="/assets/img/posts/gt2-cheats/wide-showcase.jpg" %}

## Full detail AI cars + 8MB RAM cheat
By default, Gran Turismo and Gran Turismo 2 both use very aggressive LODs for AI cars. The player's car is locked to the highest LOD level, while AI cars cycle between
three LDO models depending on distance from the camera.
When playing the game on the native resolution it's nearly impossible to notice, but of course with upscaling LODs become much more obvious and jarring.

To counter this, I created a cheat forcing all cars on the track to use the highest LOD level, previously reserved for the player. As a result, the game looks far better than originally!
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/lod-start-before.jpg" left-label="Stock"
                right="/assets/img/posts/gt2-cheats/lod-start-after.jpg" right-label="Full detail" %}
{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/lod-race-before.jpg" left-label="Stock"
                right="/assets/img/posts/gt2-cheats/lod-race-after.jpg" right-label="Full detail" %}

However, this comes at a price -- with the cheat activated, the amount of geometry visible on screen at once is so high, the game runs out of space in its polygon buffers
and starts skipping geometry!
{% include figures/image.html link="/assets/img/posts/gt2-cheats/missing-geometry.jpg" caption="Something is missing." %}

I fixed this with another cheat, doubling the size of the game's polygon buffers. Since a stock PS1 doesn't have enough RAM for this, this cheat code utilizes
extra RAM from dev PS1 units instead (dev PS1 units have 8MB RAM instead of 2MB RAM). Therefore, a **8MB RAM** cheat must be used together with
a `Enable 8MB RAM (Dev Console)` option in DuckStation. It can be enabled from Game Properties individually for each game:
{% include figures/image.html link="/assets/img/posts/gt2-cheats/duckstation-devram.jpg" style="natural" %}

**NOTE:** Earlier versions of DuckStation had a bug in the PGXP implementation where moving the polygon buffers to the 8MB RAM region caused artifacts.
If the geometry looks wobbly while using these cheats with PGXP or it looks like it's falling apart, please update DuckStation.

## HUD & rear view mirror toggle
By default, it is impossible to completely hide the UI in GT2 during races or replays. Additionally, the rear view mirror only shows in the bumper camera
and it cannot be down in chase cameras. This cheat allows to toggle the rear view mirror by tapping `L3` (cycling between "always on", "default" and "always off")
and toggle the entire HUD by holding `L3`. Combined with a Pause and Frame Step features of PS1 emulators (including DuckStation), this can essentially act as
a cheap version of Photo Mode 😉

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/gt2-cheats/hud-1.jpg" %}
{% include figures/image.html link="/assets/img/posts/gt2-cheats/hud-2.jpg" %}
</div>

## Replay cameras in race
By default, Gran Turismo 2 has 3 camera modes in race, but 9 modes in replays, with the cinematic camera being a separate, 10th mode.
This cheat makes all replay cameras accessible in race, and allows to switch the cinematic camera by holding `R1`.

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/gt2-cheats/cameras-1.jpg" %}
{% include figures/image.html link="/assets/img/posts/gt2-cheats/cameras-2.jpg" %}
</div>

## Slightly increased draw distance
Fair warning -- this cheat doesn't do wonders. The game's draw distance is determined by the track data itself, and so it's impossible
to increase it arbitrarily. However, Gran Turismo 2 has a slightly higher draw distance in replays than it does in races.
With this cheat, I enabled the replay draw distance in races. Curiously, one of the things it "fixes" is a notorious hole in the ground
at the start of Midfield!

{% include figures/juxtapose.html left="/assets/img/posts/gt2-cheats/draw-distance-before.jpg" left-label="Stock"
                right="/assets/img/posts/gt2-cheats/draw-distance-after.jpg" right-label="Higher draw distance" %}

Similarly to the **Full detail AI cars** cheat, this cheat might benefit from an expanded polygon buffer space. Consider using this cheat
together with a **8MB RAM** cheat and dev console memory enabled for the game (instructions above).

# Revised cheats

**NOTE:** These revised cheats act only as bugfixes, no new features have been introduced. Please update regardless, as only recently I realized that
because of the way Gran Turismo 2 handles loading code overlays, my old methods of patching were unsafe and could result in random issues.
Now I figured out how to patch this game safely, and updated the following cheats:

## 60 FPS
What I previously ruled out as "unexplainable issues" when working on the 60 FPS cheat, I was now able to confirm to be caused by an old,
careless method of patching. I have updated the cheat to be safer now, and as a positive side effect it also became simpler.

I also added NTSC-J variations of the cheat.

## Metric system
This cheat was in fact broken, and I only missed an obvious crash because I never tested it with interpreters.
I've now updated this cheat to be safer and merged Arcade and Simulation cheat into a single cheat.

# Download

All listed cheats can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/gt/gran-turismo-2.md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download cheat codes for Gran Turismo 2</a>

# What's next?

This batch of cheats might not be the last. I've been working on combining Arcade and Simulation discs, with promising results:

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">OK, maybe combining Gran Turismo 2 discs can be viable after all... <a href="https://t.co/gdzDnQtsDt">pic.twitter.com/gdzDnQtsDt</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1431682023270268928?ref_src=twsrc%5Etfw">August 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

I also attempted to give AI cars their own engine sounds, but this causes the emulated console... to run out of audio RAM! Unlike normal RAM, it's impossible to expand it so that
improvement will probably not be realized anytime soon, if ever.
