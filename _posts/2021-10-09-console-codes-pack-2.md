---
layout: post
title: "New modifications for Gran Turismos, NASCAR Dirt to Daytona, and more"
excerpt: "October drop of cheat codes."
thumbnail: "assets/img/posts/console-codes-2/banner.jpg"
feature-img: "assets/img/posts/console-codes-2/banner.jpg"
image: "assets/img/posts/console-codes-2/banner-full.jpg"
twitter: {card: "summary_large_image"}
game-series: ["gran-turismo", "gran-turismo-2", "gran-turismo-3", "gran-turismo-concept", "gran-turismo-4-prologue", "gran-turismo-4", "tourist-trophy", "nascar-dtd-ps2", "test-drive-eod-ps2"]
date: 2021-10-09 14:15:00 +0200
tags: [Releases]
---

<aside class="sidenote" markdown="1">
TL;DR - if you are not interested in an overview of my newly released cheat codes,
scroll down to the [**Download**](#download) section for download links.
</aside>

***

* TOC
{:toc}

# Introduction

Hello! This post might be slightly chaotic, as it's about a whole pack of random cheat codes I made over the past month.
Bear with me and maybe you'll spot a code that's interesting to you.

Let's proceed to the codes. I sorted them per platform, and then per game. Most PS2 codes released apply to multiply games, and this also has been outlined.

# PlayStation

## Simulation timescale in Arcade

{:.disclaimer}
Applies to: Gran Turismo (NTSC-U 1.1, PAL)

American and European versions of Gran Turismo have a weird difference to the original Japanese release -- in those Arcade Mode is noticeably faster than the Simulation mode.
I investigated it and found that in these versions, Arcade Mode runs at 125% speed, although naturally without speeding up the in-game timer. With this code, Arcade Mode
is restored to 100% speed, just like in the Japanese version of GT1.

This clip from Submaniac93 illustrates the differences well, so I'll just use that in place of a gameplay presentation:
{% include figures/video-iframe.html link="https://www.youtube.com/embed/x-HdmE6tF0A" %}

## True Endurance

{:.disclaimer}
Applies to: Gran Turismo 2

Gran Turismo 2 has a single timed Endurance race -- **Millenium In Rome 2 Hours Endurance**. However, while limited to 2 hours, this race can also end after 99 laps, whichever comes first.
With this cheat, this race becomes a true timed Endurance race: like in PS2 Gran Turismos, the lap counter now only shows finished laps and the race ends after 2 hours, regardless of how many laps
were finished.

{% include figures/image.html link="/assets/img/posts/console-codes-2/gt2-true-endurance.jpg" caption="Begone \"Lap 1/99\"." %}

# PlayStation 2

## Deinterlace/Autoboot in 480p (updated)

{:.disclaimer}
Applies to: Gran Turismo 4 Prologue (NTSC-J), Gran Turismo 4 (PAL), Gran Turismo 4 Online (NTSC-U)

First, an update rather than a new cheat. Recently, I discovered that my current GT4 PAL deinterlace cheat was editing a variable
in a wrong way, relying on luck rather than stability because of dynamic allocations. I now updated this cheat to modify code setting up the 480p video mode variable,
rather than editing the variable itself.

I have also ported part of the cheat to GT4 Online, so now it's not necessary to select *Progressive (480p)* on every game boot.
While a cheat for GT4O already exists online, it has the same mistake (editing dynamically allocated data), so it was never reliable for me.

Additionally, I also ported my existing Gran Turismo 4 Prologue PAL deinterlace cheat to the NTSC-J version.

## Adjustable units

{:.disclaimer}
Applies to: Gran Turismo 3, Gran Turismo Concept, Gran Turismo 4 Prologue, Gran Turismo 4 First Preview (partially)

We had to wait until Gran Turismo 4 to have a proper measurement units selection menu in the game. Before that units were locked to the specific game version,
most notably locking NTSC-U versions of the games to use imperial units.
While in Gran Turismo 1 and 2 units were fully hardcoded, turns out Gran Turismo 3 and later include code handling multiple speed, power, and torque units,
although they are predetermined by the user's choice of language.

With these codes, measurement units may be freely picked, just like in Gran Turismo 4.
Whether it means using metric units in the NTSC-U versions, or imperial in PAL versions, the cheat code can be modified to force any selection of such.
For Gran Turismo 4 First Preview, this code only allows for modifying power and torque units, as speed/distance units can already be changed in the game's options menu.

{:.disclaimer}
Please remember to read the instructions included in the PNACH file and adjust the code to your preferences!

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/console-codes-2/gt3-units.jpg" %}
{% include figures/image.html link="/assets/img/posts/console-codes-2/gt4p-units.jpg" %}
</div>

## Adjusted triggers sensitivity

{:.disclaimer}
Applies to: Gran Turismo 3, Gran Turismo Concept, Gran Turismo 4 Prologue, Gran Turismo 4, Tourist Trophy, Gran Turismo 4 Online

Since Gran Turismo games have always offered full control remapping, it's possible to utilize triggers on modern controllers for throttle/brake,
much like most modern games do. However, unlike in newer Gran Turismos, doing this in the PS2 games results in a mediocre experience -- analog sensitivity
is tailored for analog buttons of the DualShock 2 controller, and therefore inputs are heavily scaled. In practice, this means that anything over ~half the trigger
press is already registered as a 100% input, so precise throttle control is hard. With this code, I've removed this scaling as much as reasonably possible,
so now 100% input registers from a near full press of the trigger, therefore making the experience closer to how the later Gran Turismo games handle it.

## Remappable controls

{:.disclaimer}
Applies to: Gran Turismo 4 Prologue

OK, in the previous section I lied a little. Gran Turismo 4 Prologue, despite being a (somewhat) full release, does **not** feature control remapping.
The game internally loads and saves mappings, but no menus exist, leaving the feature unused.

With this code, I "exposed" mappings to the PNACH file, so users may freely map controls however they wish.
By default, the code ships with stock mappings, so make sure to modify the code to your needs.

{:.disclaimer}
Please remember to read the instructions included in the PNACH file and adjust the code to your preferences!

{% include figures/image.html link="/assets/img/posts/console-codes-2/gt4p-remapping.jpg"
            caption="Believe me, this screen shows remapped controls, as I'm gently pressing throttle on the right trigger." %}

## Shoulders control mapping

{:.disclaimer}
Applies to: NASCAR: Dirt to Daytona, Test Drive: Eve of Destruction

For the first time, modifications for a console game that is **not** Gran Turismo! 😁

NASCAR Heat 2002, the first PS2 game from Monster Games, shipped with 4 control schemes to choose from.
One of those control schemes was called "Shoulders", and mapped throttle/brake to R2/L2.
This translates really well to modern gamepads, allowing the player to use triggers for precise throttle control
(just like I mentioned [above](#adjusted-triggers-sensitivity)).

For unknown reasons, the next two games using the game engine,
[NASCAR: Dirt to Daytona](https://en.wikipedia.org/wiki/NASCAR:_Dirt_to_Daytona) and [Test Drive: Eve of Destruction](https://en.wikipedia.org/wiki/Test_Drive:_Eve_of_Destruction)
both removed this control scheme (Test Drive got something resembling it, with throttle/brake on R1/L1 and not R2/L2).
What makes this decision even more puzzling is a fact that NASCAR DtD was also released on GameCube and Test Drive EoD was also released on Xbox,
and both are consoles with pressure sensitive triggers in place of PS2's shoulder buttons!

With this code, I restored a full "Shoulders" controls set for both games. NASCAR: Dirt to Daytona gets a full mapping copied from NASCAR Heat 2002,
while Test Drive: Eve of Destruction gets a custom modification of one of the alternate mapping, swapping bumper buttons for triggers.
Test Drive additionally also restores analog throttle/brake, a feature that was toggleable in NASCAR, while Test Drive removed the option
and locked both to Digital. Leaving it this way would defeat the purpose of using triggers to accelerate/brake in the first place,
so it's now been restored too.

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-shoulders.jpg" %}
{% include figures/image.html link="/assets/img/posts/console-codes-2/td-shoulders.jpg" %}
</div>

## Camera controls on the right stick

{:.disclaimer}
Applies to: NASCAR: Dirt to Daytona

When investigating the game's code for the shoulders mapping cheat, I noticed that NASCAR DtD (but not NASCAR Heat 2002 or Test Drive EoD)
still updates button mappings for Look Left/Look Right actions, albeit it always updates them with an empty mapping.
I looked into that more closely and found that these actions are fully functional but unused.
With this cheat, I replace the stock functionality of the right analog stick (Throttle/Brake) with key bindings to look around.

{:.disclaimer.warning}
When "uninstalling" the cheat, please follow the instructions in the PNACH file!
Removing it without first making the code unmap the newly added controls will leave camera controls permanently mapped in the savegame.

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-lookaround-2.jpg" %}
{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-lookaround-1.jpg" %}
</div>

## Extended valid birth date range

{:.disclaimer}
Applies to: NASCAR: Dirt to Daytona

The last cheat released today is a huge nitpick 😁 When creating a new driver profile in NASCAR DtD, the birth years of the player are limited
to the **1925-1986** range. In 2021 that limit doesn't really make sense anymore (I can't set my driver's birth date to my own!),
so in this cheat, I lifted it enough to future proof it for a very long time -- with valid dates now being in the **1900-2100** range.

{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-birthdate.jpg" %}

# Download
All listed cheats can be downloaded from *Mods & Patches*. Click here to head to the *Consoles* page, from where you can go to the specific games' pages:

<a href="{% link _games/misc/consoles.md %}" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download cheat codes</a>
