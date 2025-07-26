---
layout: post
title: Modding Gran Turismo 2000 beyond boundaries
date: 2025-07-26 18:50:00 +0200
excerpt: Car select? Check. Widescreen? Check. Modern controls? Check.
game-series: "gran-turismo-2000"
image: "assets/img/posts/gt2000-cheats/gt2000-banner.jpg"
thumbnail: "assets/img/posts/gt2000-cheats/gt2000-banner.jpg"
feature-img: "assets/img/posts/gt2000-cheats/gt2000-banner.jpg"
twitter: {card: "summary_large_image"}
tags: Releases
---

<aside class="sidenote" markdown="1">
TL;DR: If you are not interested in an overview of my new Gran Turismo 2000 cheat codes,
**go to the [Download](#download) section for download links.**
</aside>

***

* TOC
{:toc}

{% assign pad-cross="**X**{:style='color:rgb(124, 178, 232);font-family:monospace, monospace'}" %}
{% assign pad-triangle="**△**{:style='color:rgb(64, 226, 160);font-family:monospace, monospace'}" %}
{% assign pad-circle="**O**{:style='color:rgb(255, 102, 102);font-family:monospace, monospace'}" %}
{% assign pad-square="**☐**{:style='color:rgb(255, 105, 248);font-family:monospace, monospace'}" %}

*[RTTI]: Run-Time Type Information

# Introduction

Over the past few weeks, I've been researching **Gran Turismo 2000**.
If that rings no bells for you, that's okay -- before Gran Turismo,
Polyphony Digital's initial idea was to launch a new, smaller Gran Turismo game for the PS2 before the end of 2000. However,
as the release slipped into 2001, it eventually became **Gran Turismo 2000: A-Spec**, then **Gran Turismo 3: A-Spec**. We do, however,
have a single build of GT2000 publicly available -- a small, 2-minute-long demo given away during a PlayStation Festival in early 2000.

You might ask, what makes this limited demo so interesting, other than the name? While it's true that this game eventually
formed what we know as Gran Turismo 3, it's also essentially a different game. Gran Turismo 2 and Gran Turismo 2000 were developed
side by side for most of 1999. At first GT2000, was likely supposed to be "GT2 on the PS2" (just like Gran Turismo HD was initially thought to be "GT4 on the PS3").
This is evident in the festival demo's visuals, sounds, and code: distant car LODs use GT2 models as-is, and big chunks of the game's code (like physics)
strongly hint at being ported straight from the PS1!

This is further backed by pre-release interviews with Kazunori Yamauchi himself:
> **Originally conceived as nothing more than a fancy-shmancy update of Gran Turismo 2 with pretty graphics,** this is now a fully fledged sequel.
> "My original plan for this title was to be released close to the PS2 launch, when it would feature 50 different cars and four racing tracks,"
> project leader and producer Kazunori Yamauchi tells us. "It would have been positioned as a digest or demo version of the GT series for the PS2.
> That's why it was titled as GT2000 and not the formal name, GT3."
{:cite="https://archive.org/details/official-u.-s.-playstation-magazine-issue-40-january-2001/page/120/mode/2up"}

<cite>Official U.S. PlayStation Magazine</cite> Issue 40, January 2001[^opm-gt2000]

[^opm-gt2000]: Read online: <https://archive.org/details/official-u.-s.-playstation-magazine-issue-40-january-2001/page/120/mode/2up>{:target="_blank"}

This is why I dove into the GT2000 demo despite its extremely limited content. Unless more prototype builds show up online in the future, this is our only chance
to peek at what Gran Turismo 2 on the PlayStation 2 would be like. Documenting this demo and understanding how it works provides us with a unique opportunity
to see Gran Turismo in a very scaled-down, intermediate state of development.

# The main goals

When I dove into this demo, I wanted to see how far it could be pushed content-wise. By default, the experience it offers is extremely limited -- the player gets to race
around Seattle Circuit against 5 AI cars for 120 seconds, driving a Mitsubishi Lancer Evo V, and they can only choose the Lancer's color and the handling model,
much like in Arcade Mode in the PS1 GTs. The "race" itself is also extremely barebones: it doesn't count laps or split times, and the race cannot
be finished; instead, the game automatically switches to a replay after the time limit expires.

The tracks are immediately a lost cause: while some earlier public previews of GT2000
[showed Special Stage Route 5](https://www.youtube.com/watch?v=hWCTj_i-JBI&t=70s){:target="_blank"}, the festival build doesn't feature any usable leftovers;
the only `highway` files that are left behind are in the formats this build doesn't care about.

The situation with cars is a little better, since the AI opponents drive different cars with their distinct sounds and characteristics.
**Xenn765** has also looked into GT2000 a long time ago and [created ARMax codes allowing the player to take control of the AI cars](https://www.gtplanet.net/forum/threads/xenns-cheat-device-codes-includes-demo-codes.187354/){:target="_blank"},
so the player can "swap seats" with AI and drive their cars. What I wanted to know was -- could these findings be used to create a "complete" car selection,
where the player sees a different car in the main menu and *starts* the race in it?

This curiosity sent me down a rabbit hole that resulted in a collection of cheats I'm sharing here with you today.

# Published mods

## Car Select

The existing car select cheat proves those cars are drivable, but I wanted to break down how to switch the player's car without affecting AI.
I discovered that this build, unlike the final GT3, still uses GT2's parts data, down to the vehicle identifiers and code using fixed-point values,
like a PS1 game would, proving that this code is likely identical to GT2!

Matching the vehicle identifiers to their names from Gran Turismo 2, the six cars available in this build are:
* `m2g6n` -- **Mitsubishi Lancer Evolution VI GSR '99**; oddly enough, the actual car available is a **Lancer Evolution V GSR '98**, but using Evo VI's parts data.
* `t291n` -- **Toyota Altezza RS200 '98**
* `s2lgn` -- **Subaru Legacy B4 RSK '98**
* `a28sn` -- **Mazda RX-7 Type RS '98**
* `n24vn` -- **Nissan Skyline GT-R V-spec (R34)**
* `hnsnn` -- **Honda NSX Type S ZERO (J)**

Unlike any "full" Gran Turismo, menus in GT2000 are fully hardcoded and laid out only through code. Thanks to this and to RTTI data being left behind,
I was able to understand how the menus are structured and how to expand them.

My Car Select mod:
* Lets users select the car in-game with DPad left/right.
* Features all available colors for each car. Although AI drivers always used fixed colors, all car models feature a selection of colors taken straight from Gran Turismo 2.
  Notably, Honda NSX has 12 available colors, which is quite a bit compared to Evo V's 5 available colors!
* Keeps the starting grid unchanged, so the player starts in the 6th position regardless of their car of choice.
* Remembers the selected car after the race, like the stock game does with the selected color.
* Makes the selection look fully native by including a fade-out effect when selecting cars, much like in Gran Turismo 3.
* As UI assets for other cars are not present in the files, Lancer Evo badges, performance characteristics, and color names are hidden for other cars.

{% include figures/video.html link="https://i.imgur.com/OGVFrYv.mp4" attributes="controls" caption="This is Gran Turismo 2000, but it looks almost like Gran Turismo 3 demos." %}

Currently, I only offer this mod as a PNACH patch. I might also release it as an xdelta patch later so it can be used like a romhack.

{:.disclaimer.warning}
At this time, Car Select is not compatible with the RetroAchievements set for GT2000. I will ensure it either gets updated as soon as possible,
or earning achievements gets blocked when Car Select is active.

## Widescreen fix

GT2000 is technically the only Gran Turismo on the PlayStation 2 not to support 16:9 widescreen. A widescreen hack exists for it already,
but I wasn't satisfied with how it adjusts the FOV and does nothing to the UI, so I created my own. In my widescreen fix:
* The game FOV is switched to Hor+ everywhere, including the menus and replays; FOV is no longer manually increased to match the original game's 4:3 vertical FOV.
* All menu and HUD elements, except for the fonts, have been adjusted for widescreen. This also includes the intro movie.

Fonts proved to be impossible to rescale for widescreen -- GT2000's font rendering is taken straight from Gran Turismo 2, and that system
does not support resizing the fonts, as the PS1 did not support sprite scaling at all.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/gt2000-cheats/screens/Gran Turismo 2000 [Trial]_PAPX-90203_20250726165118.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/gt2000-cheats/screens/Gran Turismo 2000 [Trial]_PAPX-90203_20250726165131.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/gt2000-cheats/screens/Gran Turismo 2000 [Trial]_PAPX-90203_20250726165149.jpg" thumbnail="auto" %}
</figure>

While currently I only offer a patch for 16:9 widescreen, in the future I may publish an online generator similar to
the [Bonus Codes]({% link pages/bonuscodes.md %}) that can automatically create PNACHs for arbitrary aspect ratios specified by the user.
I have no ETA on this, but it's something I'd like to offer for multiple games, like GT2, GT2000, and Juiced!

## No time limit

In theory, the 120-second time limit of this demo was lifted years ago, and even removed from the UI. In practice, all the existing cheats
are flawed, as the game has **two** timers managing the playtime:
1. The timer visible in the HUD that ends the race shortly after 120 seconds elapse.
2. The replay recorder is limited to 121 seconds, and it will also switch the game to play the replay back once the recorder fills up fully.

Until now, all cheat codes available online only lifted the first timer, and they did nothing to the automatic replay playback, so in practice,
the time limit was still there, just hidden. With my cheat, both timers are lifted, so the race is now truly endless.

## Trigger control mappings

Much like GT4 Prologue, GT2000 lacks remappable controls. As I was working with the input code for the **Automatic DualShock mode** cheat,
I figured remapping the controls to the modern triggers-based scheme should be easy, especially since the game already opts in to use pressure-sensitive buttons.

With this cheat, control mappings reflect the default modern controls scheme from Gran Turismo 7:
* <kbd>R2</kbd> -- Accelerate
* <kbd>L2</kbd> -- Brake
* {{ pad-circle }} -- Handbrake
* {{ pad-cross }} -- Shift Up
* {{ pad-square }} -- Shift Down
* {{ pad-triangle }} -- Reverse

Triggers are given the correct sensitivity, too, so they work equally across the full range of inputs.

## Automatic DualShock mode

Many people who have played Gran Turismo 2000 previously (especially in PCSX2) may be unaware of the fact that it *does* support analog controls,
but unlike any other PS2 Gran Turismo (and most other racing games on the platform), they are not enabled by default and the user
needs to enable them every time by pressing the <kbd>Analog</kbd> button.

On real hardware, this is obvious, as the LED on the DualShock 2 is off, but it's way less clear in PCSX2;
on top of that, software like Windows Game Bar and Steam Big Picture like to "take control" of the <kbd>Guide</kbd>
button on modern gamepads and make using it in PCSX2 annoying.

With this patch, the game automatically enables the Analog mode on startup and locks it.

## Throttle/brake on the right stick

If controlling the car with face buttons or triggers isn't your cup of tea, most Gran Turismo games also offer an alternative -- throttle and braking
can also be controlled with the right stick. With this patch, GT2000 also gets this feature.

This patch can be used alongside **Trigger control mappings**, but doesn't require it.

# Download

All listed cheats can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/gt/gran-turismo-2000.md %}" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download cheat codes for Gran Turismo 2000</a>

***
