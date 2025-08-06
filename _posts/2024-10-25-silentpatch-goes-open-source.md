---
layout: post
title: "SilentPatch for Grand Theft Auto goes open source!"
excerpt: "A long overdue update packed with new fixes and a public source code release."
feature-img: "assets/img/posts/sp-2024-update/sp_opensource_banner.jpg"
thumbnail: "assets/img/posts/sp-2024-update/sp_opensource_banner.jpg"
image: "assets/img/posts/sp-2024-update/sp_opensource_banner.jpg"
game-series: ["gta-iii", "gta-vc", "gta-sa"]
date: 2024-10-25 14:00:00 +0200
last_modified_at: 2024-11-02 14:00:00 +0100 
twitter: {card: "summary_large_image"}
tags: [Releases, Articles]
juxtapose: true
---

<aside class="sidenote" markdown="1">
TL;DR: This article details the various fixes introduced in this update, making it a relatively long read.
If you want to jump straight to SilentPatch or check the source code, **go to the
[Download and source code](#download-and-source-code) section for the links.**
</aside>

***

{::options toc_levels="1..2" /}

*[ASLR]: Address Space Layout Randomization
*[enex]: Entry/Exit

**{% include elements/time.html date="2024-11-02" %} update:**{:.upcase} Hotfix #1 has been released for GTA III, Vice City, and San Andreas!
This hotfix addresses several known issues introduced by the latest update, and addresses compatibility issues with multiple modifications.
Updating is strongly recommended.

* TOC
{:toc}

# Introduction

Tomorrow, on {% include elements/time.html date="2024-10-26" text="October 26th, 2024" %}, GTA San Andreas turns 20 years old. I haven't had the chance to play it upon its release in {% include elements/time.html date="2004-01-01" preset=site.date.year %} -- I was a kid
who, back then, played exclusively on PC and would play Vice City whenever my parents allowed me. My first experience with San Andreas was
in {% include elements/time.html date="2005-01-01" preset=site.date.year text="mid-2005" %} when the game was released on PC; little did I know back then how influential GTA in general, but most specifically San Andreas,
would later be for my life and my professional career -- and that nearly two decades later, well into my adult life, I would still be fixing
it to make it as enjoyable an experience as I possibly can.

**Today, on {% include elements/time.html date="2024-10-25" text="October 25th" %}, I'm honored to publish the biggest update of SilentPatch for the classic Grand Theft Auto trilogy to date,
with the full source code now available on GitHub under the MIT license!**
While I originally planned for the open source release to go live [in January]({% post_url 2023-12-29-silentpatch-10th-anniversary %}),
a combination of an increased update scope and several real-life issues happening in the background resulted in this much of a delay,
for which I sincerely apologize.

However, this delay comes with a silver lining -- what I initially planned to be a simple upload of the source code
cleaned up for a public release turned into the biggest content update I've ever released.
This release contains not only a wide selection of new fixes; I also went back to many older fixes and upgraded them to be safer, simpler,
more compatible with other modifications, and free of side effects. Numerous minor regressions introduced by SilentPatch are now resolved,
ensuring the patch goes open source in as perfect a state as possible.

In this blog post, I'll break down the most significant fixes introduced in this update, a culmination of approximately 10 months of development
(although not without breaks), and a lot of testing over **nine** Release Candidate builds. My explanations may get a bit more technical
than usual, but I did my best to keep them digestible. No code names this time! The last time I tried that,
my code name of choice aged poorly very quickly 😑.

***

Before we move on, a small unrelated announcement -- regular visitors to the blog may have noticed that it has been updated a bit!
Most of the changes are purely cosmetic, but there are also a few things that should be immediately noticeable:
1. PNACH codes in *Consoles* can now be downloaded directly! There is no need to go through GitHub anymore.
2. Fonts have been slightly updated.
3. Buttons have been redesigned. They are now thicker, consistently placed, and don't have useless padding around them.
4. Embedded Tweets now respect the Dark Mode setting.
5. My [Portfolio]({% link pages/portfolio.md %}) has been updated with the latest work projects I've been involved in,
   including the one I'm currently on when I'm not patching games on the side.

# New fixes

## Shared fixes

Numerous fixes included in this update apply to multiple games from the trilogy. Those are:

{:.additional-toc}
* [I'm a good citizen, and I always keep my headlights on](#im-a-good-citizen-and-i-always-keep-my-headlights-on)
* [Did that car explode twice!?](#did-that-car-explode-twice)
* [Ooh, shiny!](#ooh-shiny)
* [Credits roll! *...ZZzzzZZZ....*](#credits-roll-zzzzzzzz)
* [Mission passed! Now please let me play, I get it](#mission-passed-now-please-let-me-play-i-get-it)
* [Minimal HUD](#minimal-hud)
* [Other fixes](#other-fixes-shared)

### I'm a good citizen, and I always keep my headlights on

{:.sidenote}
Affects: All trilogy games.

To provide some variety in the game world, traffic vehicles act with a degree of randomness. One of the random decisions
they make is when they turn the lights on at night, or when it gets foggy or rainy. For each vehicle in the world,
a random "threshold" gets picked, deciding how dark, rainy, or foggy it has to be for the vehicle to turn the headlights on.

However, this tiny feature suffers from a difference in how randomness works on PC vs PS2 -- the range of randomness
is lower on PC (`0-32767`) than it is on PS2 (`0-65535`), but the code calculating the thresholds has not been updated.
This keeps the variance in decisions, but unintentionally gets rid of an interesting outcome -- on the PS2, during rainy or foggy conditions,
some vehicles may decide to never turn their headlights on! On PC, because the range of randomness is smaller, they will all eventually
turn on their headlights.

SilentPatch rescales the code calculating the thresholds to match the PS2 behavior, so starting with this update,
you may encounter some unlawful drivers who don't use their lights even when they really should:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta3_BmzkrTlOVp.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta-vc_msp2NecMU8.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_dCmPAXdhFO.jpg" thumbnail="auto" %}
</figure>

***

### Did that car explode twice!?

{:.sidenote}
Affects: All trilogy games.

The entire trilogy had a weird bug where cars would sometimes explode more than once for no discernible reason.
Together with **Nick007J** we dived into this issue and figured out that it's caused by the following chain of events:
1. The vehicle is set on fire.
2. The driver bails out. Before they finish their bailing animation, the vehicle explodes and changes its status to "wrecked".
3. The driver finished their bailing animation. This changes the vehicle status to "abandoned", **overwriting the previous state**.
4. Changing the vehicle's status doesn't replenish its health, so it's set on fire again, and explodes shortly after.

From these steps, the fix becomes apparent: SilentPatch now doesn't allow the game to transition the vehicle state from "wrecked"
back to "abandoned", fixing this issue.

Unfortunately, this fix also corrects another well-known issue that for once I did **not** intend to fix:[^harmless-bugs] it is no longer possible
to execute a famous trick allowing the player to drive exploded vehicles in GTA III and Vice City:

{% include figures/video-iframe.html link="https://www.youtube.com/embed/DQP7cbLk8hg" style="narrower" %}

With this fix, the first vehicle explosion simply kills the player 😥

[^harmless-bugs]: Another example of a bug I deliberately left intact would be the [car crusher glitch](https://www.youtube.com/watch?v=PAQblkQvNfI){:target="_blank"}
    -- it's amusing, harmless, and requires an elaborate setup, so there's almost no chance of an unaware player stumbling upon it by accident.

***

### Ooh, shiny!

{:.sidenote}
Affects: GTA III, GTA Vice City.

In III and Vice City, environment mapping wasn't applied to vehicle extras. This resulted in all extras appearing matte
(with no specularity), which is fine for parts like leather roofs on Stallion and Mesa Grande, but not necessarily
on metallic extras, like Stinger's roof, that now matches the way Yakuza Stinger looks:

{% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta3_j3mlIPWdar.jpg" left-label="Stock"
            right="/assets/img/posts/sp-2024-update/juxtapose/10_gta3_KRUzeezr03.jpg" right-label="SilentPatch" %}

However, there is a catch: theoretically, non-reflective parts should just have their specularity set to zero,
but this isn't done with multiple stock models. For this reason, the INI file now includes an exception list `ExtraCompSpecularityExceptions`
where models with non-reflective extras can be specified. By default, this is Stallion (for III and Vice City)
and Mesa Grande (for Vice City). Additionally, I also made sure that these exceptions don't apply to glass materials,
which gives Mesa Grande a reflective rear windshield:

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta-vc_8GsQjiOJpW.jpg" thumbnail="auto" %}

For custom models, the fix is simple: just make sure that your extras have specularity and the environment map coefficient set correctly.
This value is simply ignored on extras without SilentPatch.

***

### Credits roll! *...ZZzzzZZZ....*

{:.sidenote}
Affects: All trilogy games.

Congratulations, you completed the final mission and beat the game! Now it's time to watch the credits.
*"Ugh, why are they so small and slow?"*, you think to yourself. Well played, you just spotted a bug!
The credits don't scale to resolution, so they appear smaller and slower the higher your selected resolution is,
to the point where they are nearly unreadable at 4K.

Starting with this SilentPatch update, credits scale to the resolution correctly and thus now look just like on the PS2.
Because they now move at a consistent speed regardless of resolution, their run time now also matches the original release.
Additionally, in GTA III, credits would run for a bit longer than needed, so for the last camera cut, the game would show it
and immediately fade out again, as the credits have already rolled to completion. To fix this, I made the credits scroll a few percent faster,
so they end on the previous camera cut instead.

{% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/compact_gta_sa_uEnA1Q6eVX.jpg" left-label="Stock"
            right="/assets/img/posts/sp-2024-update/juxtapose/compact_gta_sa_lW8hg9vrwc.jpg" right-label="SilentPatch"
            caption="What is this, credits for ants?" %}

***

### Mission passed! Now please let me play, I get it

{:.sidenote}
Affects: All trilogy games.

This is one of the issues that make the lives of speedrunners harder: in all three trilogy games,
the bigger your selected resolution is, the longer the mission title and mission completion/failure texts stay on the screen!
At first, this sounds completely crazy and I wouldn't blame anyone for thinking it's a lie or placebo -- alas, it's true.

It all only comes together thanks to one of the pre-release clips from GTA III. Pay attention to the "Reward" text:
{% include figures/video-iframe.html link="https://www.youtube.com/embed/R0bczv7HGgw" style="narrower" %}

At some point, this text (called "odd job text" internally), mission titles, and the mission completion/failure text
were intended to slide from left to right. Although this feature never made it to the final game, much of the code remained.
When the games were ported to PC, a (perhaps automated) attempt was made to scale the sliding animation to arbitrary resolutions.
However, this attempt was incomplete -- while the scaling margins scale, the sliding speed does not.
Texts stay on screen longer, because the game waits for the slide to complete, even though the results of those calculations
are not used in the end.

In this update, SilentPatch fixes this logic, so now the "sliding speed" remains consistent regardless of the resolution.
Additionally, since I had to modify this code either way, two new INI (and [debug menu](https://github.com/aap/debugmenu){:target="_blank"})
options were added to all 3 games -- `SlidingMissionTitleText` and `SlidingOddJobText` may be used to re-enable this cut feature.
Even though the mission passed texts technically can slide too, they were always centered, so sliding does not look right,
and therefore it makes no sense to enable it.

<figure class="media-container small">
{% include figures/video.html link="/assets/img/posts/sp-2024-update/10_gta3_zw2w48UrzV.mp4" attributes="controls" %}
{% include figures/video.html link="/assets/img/posts/sp-2024-update/10_gta-vc_u7eV9X6byH.mp4" attributes="controls" %}
</figure>

***

### Minimal HUD

{:.sidenote}
Affects: GTA Vice City, GTA San Andreas.

The games have an unused, yet mostly finished mode of displaying the HUD -- when it's enabled, only the clock displays continuously.
Money, the weapon icon, wanted level stars, and the energy bars only display when their statuses change (e.g. you lose health, or pick up money),
and after that, they fade out after several seconds. SilentPatch fixes multiple visual bugs this feature exhibited,
and can optionally enable it via the INI file.

Even with my fixes, it's still hard to call it "production ready" -- health and armor don't show up when replenishing health or losing oxygen (in San Andreas),
and, unlike in GTA IV, it's not possible to show the entire HUD on demand, so you are unable to peek at your health or money whenever you wish.

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_aV44c4zODc.jpg" thumbnail="auto" caption="Very... minimal." %}

Minimal HUD in San Andreas isn't introduced in this update -- it existed in SilentPatch since **late 2017** and was first made public in Build 29 released
[in May 2018]({% post_url 2018-05-20-silentpatch-r29 %}). However, for some reason, I never documented this option,
so it remained "hidden" and the users had to add it to the INI file by themselves.
With this build, I finally officially documented it, so it appears in the configuration file, and consequently,
also in the [debug menu](https://github.com/aap/debugmenu){:target="_blank"}.

However, it **is** new for Vice City -- as only recently I was made aware that this feature existed also there! Therefore, in this update,
Minimal HUD can now also be enabled in VC. Be mindful that the same shortcomings as in San Andreas apply.

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta-vc_o7iNtRF2Ce.jpg" thumbnail="auto" %}

***

### Other fixes {#other-fixes-shared}

* *(All trilogy):*{:.sidenote} Script randomness has now been made 16-bit, like on the PS2, instead of 15-bit.
  The results are the most noticeable in GTA III:
  * "Bling-bling Scramble" has three possible checkpoint paths on the PS2, but the script could only pick two on the PC.
  * The ambulance in "Plaster Blaster" can pick three possible destinations on the PS2, but only two on the PC.

  This fix makes those two missions reach feature parity with the original PS2 version.
* *(GTA III, GTA VC):*{:.sidenote} Text lines read in `CPlane::LoadPath` and `CTrain::ReadAndInterpretTrackFile` are now null-terminated.
  This technical-sounding issue has an amusing and easily noticeable effect: under very specific conditions that are only possible
  to happen in modded games, the Z values of predefined train, plane, and yacht paths could be read incorrectly,
  leading to them resetting back to 0. Funny enough, I unknowingly hit that issue 11 years ago, when working on III Aircraft -- and even
  recorded it in one of the test gameplays! In this video, starting from 0:40, you may observe the plane flying at sea level,
  exactly because of... some long file names causing this issue:
  {% include figures/video-iframe.html link="https://www.youtube.com/embed/NcXtlT6UcsQ?start=40" %}

***

## Grand Theft Auto III

{:.additional-toc}
* [Boat driving animations](#boat-driving-animations)
* [Platform-specific diving for your life?](#platform-specific-diving-for-your-life)
* [Platform-specific speeding for your life??](#platform-specific-speeding-for-your-life)
* [Stealth FBI cars](#stealth-fbi-cars)
* ["Nasty game" with improvements](#nasty-game-with-improvements)
* [Why is this radar so ugly?](#why-is-this-radar-so-ugly)
* [Are car models broken on PC? No, the code is](#are-car-models-broken-on-pc-no-the-code-is)
* [Other fixes](#other-fixes-gta-iii)

### Boat driving animations

Careful observers likely noticed a long time ago that in GTA III, Speeder is the only boat with a driver's seat.
This doesn't stop Claude from standing inside that seat, though, as only in Vice City Rockstar had introduced a flag indicating
that the boat driver should use the sitting animation. **Fire_Head** also noticed this issue years ago
and made a fix for it. In this update of SilentPatch, Fire_Head's work has been integrated:

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_FQVyBT9nb0.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_FQVyBT9nb0.jpg"
      caption="In the stock game, Claude looked rather restless when driving a Speeder." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_om6I5fB06p.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_om6I5fB06p.jpg"
      caption="Now, he can finally sit down. He is still steering the boat with his mind powers, though." %}
</figure>

Together with this change, Fire_Head also backported a small fix from Vice City: now, a small delay between entering
the boat and the game considering Claude to be inside one has been removed; the game was waiting for the entering animation to finish,
but boats don't have one, so that made no sense. This fix has also been integrated into SilentPatch.

Good news for III Aircraft users -- for this change, SilentPatch applies an identical fix to Skimmer.

***

### Platform-specific diving for your life?

The PC version of GTA III has an interesting gameplay regression compared to the original PS2 release.
Usually, pedestrians can react to incoming cars in three ways -- they can:
* Turn towards the car and raise their hands,
* Try to step out of the way,
* Try to dive to the side, out of the car's way.

On PC, raising hands and stepping away works fine. However, pedestrians dive... towards the car instead!

{% include figures/video.html link="/assets/img/posts/sp-2024-update/10_gta3_Xp6OaZF9uY.mp4" attributes="autoplay muted loop"
      caption="Does this not constitute an insurance fraud? Also hats off to the police arriving at the scene,
              I could never have achieved better comedic timing if I tried doing it on purpose." %}

It's difficult to know exactly what happened in this instance, but I have my guess based on a particular quirk
of this feature: when the "threatening" vehicle is honking, this makes the NPC more alert and they **always** try to dive out of the way.
Coincidentally, in this scenario, the bug doesn't manifest. I can only theorize based on the code differences between PS2 and PC,
but the fact PC is missing some calculations makes me believe that this bug was introduced by a failed code
optimization -- someone may have misread the code, then thought the dive angle was calculated twice, and introduced a bug,
since the two calculations happened under different circumstances.

In this update, SilentPatch restores the missing code from the PS2 release, making the dive behave just like it did originally:

{% include figures/video.html link="/assets/img/posts/sp-2024-update/10_gta3_sRHLrBH1Sn.mp4" attributes="autoplay muted loop" caption="Ouch! That must've hurt." %}

***

### Platform-specific speeding for your life??

In GTA III, drivers may react in several ways to being shot at. When bullets hit their car, they randomly pick one of the three actions:
* Speed up and escape in the car,
* Do nothing,
* Leave the car and flee on foot in panic.

This list may have raised eyebrows -- do you feel like you've never encountered some of these events? If you did, you'd be correct,
as this feature is bugged on all platforms, in more ways than one.

All entities in the game world have a random seed value assigned to them,
allowing different pedestrians and cars to behave differently, yet ensuring that each entity remains consistent in its actions.
On the PS2, this random seed is an integer value in the range `0-65535`, on PC (and likely Xbox too) it's `0-32767`.
The issue with the drivers' behavior lies in the function assigning those behaviors to the random seed:
* `0-34999` -- flee in car.
* `35000-69999` -- do nothing.
* `70000-99999` -- flee on foot.

Do you see the issue now? An incorrect assumption about the range of the random seed led to one (on PS2) or two (on PC/Xbox)
cases being unreachable. In SilentPatch, the ranges have been rescaled for the real range of the random seed,
so now drivers may either ignore the bullets or flee on foot, for the first time.

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta3_N8FrQFphLN.jpg" thumbnail="auto" %}

***

### Stealth FBI cars

In all 3D-era games, FBI vehicles are pitch black. However, this does not apply to some FBI Kurumas in GTA III.
Unlike the later games, in GTA III, the car's `carcols.dat` entry specifies a dark grey body color with unpainted bumpers.
Cars that spawn in roadblocks and cars imported via the Import/Export cranes adhere to this setting,
while the chasing units are forcibly set to black via the game's code. This leads to a discrepancy between the cars depending on where they come from
and also causes the pitch-black Kurumas to permanently change their color when resprayed.

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_0zot9q3bRy.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_0zot9q3bRy.jpg"
      caption="The default color makes the FBI Kuruma look comically dark." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_p3Tcj0dg0M.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_p3Tcj0dg0M.jpg"
      caption="With SilentPatch, details are visible and the color is natural, as it was intended all along." %}
</figure>

I am not sure why the game forces FBI cars to black via code. Perhaps at some point in development FBI used regular civilian cars
painted black, and this was never reverted when they were given their dedicated vehicle? Regardless, SilentPatch now removes this code,
so all FBI cars use the colors specified in `carcols.dat`.

***

### "Nasty game" with improvements

Exclusively in the PS2 and PC versions of GTA III, the player could shoot limbs off the other characters.
However, the detached limbs never looked quite right, but not because the models weren't detailed enough -- a simple code mistake
caused both the normal model and the LOD model to show at once, ignoring the game's LOD system. This has now been fixed.

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_xJxPnJUBRp.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_xJxPnJUBRp.jpg"
      caption="Blocky legs and two hands on each arm? In Liberty City, Halloween lasts all year long." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_kr77vOlWDB.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_kr77vOlWDB.jpg"
      caption="...until now, that is." %}
</figure>

***

### Why is this radar so ugly?

Ever since the very first release, SilentPatch fixed numerous UI elements not scaling to resolution correctly.
This included the text shadows and a few specialized message types. Turns out, more things needed fixing,
although they weren't immediately obvious.

On PS2, the radar disc texture extends 4 pixels around the rendered map. On PC, that map, as well as the radar disc,
scale to resolutions, but that 4px margin does not. Back in the day, this was likely barely noticeable on resolutions like 1024x768,
but with modern resolutions like 4K, the issue becomes so pronounced that the radar disc no longer even covers the map underneath:

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_hH8zWDPtK9.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_hH8zWDPtK9.jpg"
            caption="The only reason this shipped is because it looks less bad at smaller resolutions. In 4K, the stock radar looks unacceptable." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_dZChwtGC9u.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_dZChwtGC9u.jpg"
            caption="With SilentPatch, the radar looks tidy. I also feel like it looks more circular. Do you also see it?" %}
</figure>

You've likely noticed that the positioning has changed too -- that's because the horizontal position also didn't scale to resolution
(even though the **vertical** position does), so the radar was always a constant 40 pixels away from the screen edge.
In this update, both issues are fixed, so the entire radar scales correctly.

***

### Are car models broken on PC? No, the code is

In the GTA modding circles it's relatively well known that a few pieces of code from an early version of Vice City made their way
to the PC version of GTA III; helicopter physics, bike hierarchy (but no other bike leftovers!), etc. For example, III Aircraft was only possible thanks to those leftovers.
This theory has also been confirmed by Obbe Vermeij himself:

<blockquote class="twitter-tweet" data-align="center" data-conversation="none"><p lang="en" dir="ltr">For a number of months, the pc version of gta3 and Vice City shared a codebase.<br>So it&#39;s probably stuff that was done for Vice that &#39;leaked back&#39; into gta3-pc.</p>&mdash; Obbe Vermeij (@ObbeVermeij) <a href="https://twitter.com/ObbeVermeij/status/1848524615574032617?ref_src=twsrc%5Etfw">October 22, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Just a few days before this post goes live, we learned about yet another PS2 vs PC difference that is a consequence of this code mixup: cars in GTA III have separate
`taillights` and `brakelights` dummies,[^more-dummies] while Vice City only kept the former! This had an adverse effect on the way these lights work.
That's how they were intended to function:
* During the day, when the lights are off, brake and reverse lights use the `brakelights` dummy.
* At night, when the lights are on, all lights use the `taillight` dummy, and the tail light's corona changes intensity or color accordingly.
  This also means that the reverse lights "move" to another spot at night.

With the brake lights dummy gone, III on PC fell back to the Vice City behavior: that is, always putting all the lights on a `taillight` dummy.
In this SilentPatch update, I re-introduced the missing code to the PC version, restoring feature parity. It's quite a neat detail,
so I'm glad to see it working again. On many cars, the differences are hard to spot, but on others it's much more prominent:

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_Gj10tW8xHj.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_Gj10tW8xHj.jpg" %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_rrLKsoozpK.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_rrLKsoozpK.jpg" %}
<figcaption markdown="span">Sentinel's rear lamps now see more use. The reverse lights have a dummy placed in the white area of the lamp, but sadly the game does not use it,
and the reverse lights go where the brake lights are.</figcaption>
</figure>

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_XITnO313p6.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_XITnO313p6.jpg" %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_Rj0Hf1WQvL.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_Rj0Hf1WQvL.jpg" %}
<figcaption markdown="span">Patriot's brake lights are placed in quite an unusual spot.</figcaption>
</figure>

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_PWegamZSwR.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_PWegamZSwR.jpg" %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_RFG9vdPTwL.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_RFG9vdPTwL.jpg" %}
<figcaption markdown="span">Multiple large vehicles, like the Enforcer, are supposed to have their brake lights placed up top.</figcaption>
</figure>

[^more-dummies]: `reverselights` and `indicators` dummies also exist on GTA III's models, but they were never used, even on the PS2.

***

### Other fixes {#other-fixes-gta-iii}

* In version 1.0, the Stats menu now has the correct font, like in the 1.1 and Steam versions.
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta3_0emL5bqZA9.jpg" left-label="Stock 1.0"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta3_UtqngYRw3a.jpg" right-label="SilentPatch" %}

* **Nick007J** contributed a fix to `CCarCtrl::PickNextNodeRandomly` (backported from Vice City) that allows traffic
  to turn right from one-way roads. Previously, they could only go straight or turn left.
  {% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta3_9g8QPzE2Gs.jpg" thumbnail="auto" %}

* Bilinear filtering is now applied on the player's skin, just like in Vice City, or when SkyGfx is installed.
  This makes Claude's skin texture look smoother when viewed close up.
  <figure class="media-container small">
   {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_GoqJFGSgSl.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_GoqJFGSgSl.jpg"
            caption="What year is this, 1999?" %}
   {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta3_5N7AMYmlSj.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta3_5N7AMYmlSj.jpg"
            caption="Oh Fido, you look so handsome now." %}
   </figure>

* Temporary pickups (like money) are now properly cleaned up if there are too many of them, fixing a possible object leak.
  This issue, officially fixed in Vice City, is now also resolved in GTA III.
* Dodo keyboard controls were previously not enabled for all cars when the "Flying Vehicles" cheat was activated.
  This issue, officially fixed in Vice City, is now also resolved in GTA III.
* Timers now reset on the New Game, preventing the playtime from carrying over from the saves.
* A semi-placebo fix for broken car reflections in the Steam version of GTA III has been replaced with a proper fix,
  integrating [Steam Car Colour Fix](https://gtaforums.com/topic/816604-steam-car-colour-fix-gta-iii/){:target="_blank"} from **Sergeanur**.
* A bug in the way the game saves the Brightness option has been fixed, allowing lower brightness values to save and load properly.
  Because the game stored a 2-byte long brightness variable as a 1-byte value in the configuration file, the option was only loaded partially.
  This caused increased brightness values to load correctly, while the decreased values appeared overly bright.

***

## Grand Theft Auto: Vice City

{:.additional-toc}
* [Pickups and glows](#pickups-and-glows)
* [Backface culling fixes](#backface-culling-fixes)
* [Construction Site LOD](#construction-site-lod)
* [*Greetings from Vice City...* but not for this long, please!](#greetings-from-vice-city-but-not-for-this-long-please)
* [Giving a finger in style](#giving-a-finger-in-style)
* [Why is this radar so ugly? Part 2](#why-is-this-radar-so-ugly-part-2)
* [Other fixes](#other-fixes-gta-vc)

### Pickups and glows

Vice City had multiple issues with the pickup objects fixed:

* Almost all pickups have predefined text colors for cases where something (like a price or collected revenue) displays over them.
  However, this wasn't the case for the asset money pickup, which led to the pickup text having random colors (on the PS2)
  or flickering colors every frame (on the PC). In this update, a generic red color (also used e.g. by the clothes) has been assigned to this pickup.
  {% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta-vc_IuoYYhgM5A.jpg" thumbnail="auto" %}

* Every weapon type has a unique color of the glow.[^corona] For sniper rifles, the glow is pink, while for heavy weapons, it is purple.
  However, the minigun's glow was much brighter than the one of a flamethrower or an RPG, closer to the glow of a sniper rifle.
  While this initially looked like a wrong color assignment, turns out it's because the pickup of a minigun consists of two models -- the static base
  and a rotating barrel. For some reason, this barrel was given a white glow, so it had an additional white glowing spot and also lightened the overall
  weapon pickup. This has now been corrected.
  <figure class="media-container small">
   {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_7Oq3BKWNDg.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_7Oq3BKWNDg.jpg"
            caption="By default, the minigun's glow is more pink than purple and looks closer to the color of the sniper rifle." %}
   {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_bwQupxNW2C.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_bwQupxNW2C.jpg"
            caption="With SilentPatch, it's consistent with the other heavy weapons." %}
   </figure>

[^corona]: Yes, these glows are infamous coronas.

***

### Backface culling fixes

While it is a useful GPU performance improvement, backface culling wasn't always a thing in the 3D-era GTAs:[^bfc-explanation]
* No original version of GTA III has it enabled.
* GTA Vice City enables it on PC, but not the PS2.
* GTA San Andreas enables it on all platforms.

While Rockstar fixed many models in the PC version of Vice City to render correctly with backface culling, many more were missed.
In this update, I implemented several exceptions to the backface culling, similar to what was done in the mobile versions of GTA III and Vice City:

* Backface culling was always disabled on vehicles, but that did not extend to the detached car parts.
  This was fixed in SilentPatch for San Andreas for the longest time, but now it's also present in Vice City.
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_VVlYLUo8Mr.jpg" left-label="Stock"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_30JyNQR3tZ.jpg" right-label="SilentPatch" %}

* Multiple ped models (including Tommy's outfits) break with backface culling. To fix this, it has been disabled on all peds, much like in San Andreas.
  <figure class="media-container">
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_p2DuCpFU7E.jpg" left-label="Stock"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_zlWjzQNrHN.jpg" right-label="SilentPatch"
          caption="Tommy's collar finally looks right." %}
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_qPHO6hUNMo.jpg" left-label="Stock"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_8ygKMaqc5X.jpg" right-label="SilentPatch"
          caption="This lady got her hat back." %}
  </figure>

* For map models, an exception list similar to `DrawBackfaces.txt` from the mobile releases has been implemented.
  This list includes all the models from the mobile versions, along with many more that have been meticulously identified by **Tomasak**.
  <figure class="media-container">
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_l2OMePiXdQ.jpg" left-label="Stock"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_mXpG88Ncbc.jpg" right-label="SilentPatch"
          caption="This construction site didn't look like it'd pass a safety inspection before." %}
  {% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_kWKdcpmsJ6.jpg" left-label="Stock"
          right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_9DhTaRuvAf.jpg" right-label="SilentPatch"
          caption="The magic windows are no more." %}
  </figure>

[^bfc-explanation]: I explained backface culling [a while ago]({% post_url 2019-02-03-clever-bug-exploitation-backface-culling %}) in the context of cars in San Andreas.

***

### Construction Site LOD

In the infamous "Demolition Man" mission, the player is tasked with destroying a construction site with the use of a remote-controlled helicopter.
Due to a bug in the mission's script, when the regular construction site model gets swapped for the damaged model, the building's LOD model becomes "orphaned"
(as in, it loses a link to its corresponding high-quality model) and starts showing at all times, resulting in the low-quality building rendering "inside" the damaged model.
Starting from this update, the LOD gets re-linked to the newly swapped damaged model and thus retains the correct behavior.

{% include figures/juxtapose.html left="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_WXShkKj3SL.jpg" left-label="Stock"
        right="/assets/img/posts/sp-2024-update/juxtapose/10_gta-vc_C2NDoIpPxA.jpg" right-label="SilentPatch"
        caption="It's one of those \"How did it ship?\" issues." %}

Fun fact -- the behavior where LOD models without a corresponding high-quality model render at any distance is new to Vice City,
and Rockstar most likely introduced it to fix cranes disappearing up close. If that sounds familiar, it's because
[I introduced a similar fix to GTA III in the Corona Update]({% post_url 2019-12-28-silentpatch-corona-update %}#cranes-fix)!

***

### *Greetings from Vice City...* but not for this long, please!

The outro splash in the PC version of Vice City kind of seems to take forever, doesn't it?

{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/outro-vc.webp" style="natural" %}

For this release, I was asked if SilentPatch could shorten the duration of this splash,
and upon looking into the code, I discovered that there is more to this request than just a subjective wish.
The game determines the duration of this splash as follows:

* When the fade-in is complete, the game starts counting time in milliseconds.
* Every 10 milliseconds, a counter increments.
* Once this counter reaches 150, the game exits.

There is a problem, though -- when the game is capped to 30FPS, this function executes every 33.(3) milliseconds,
so the counter increments only 30 times per second. This means that instead of taking **10ms * 150 = 1.5 seconds**,
it actually takes **33.(3)ms * 150 = ~5 seconds**! With the Frame Limiter disabled, or in the main menu (where the game locks to VSync only),
this time would be proportionally shorter.

The fix in SilentPatch is to re-time the fade -- if we increase the counter every 33ms, and count up to 45, the splash takes around 1.5 seconds
regardless of the frame rate. I implemented this fix but then realized that while the original 5s was way too long, 1.5s is also kind of short.
Therefore, SilentPatch now settles on a time of 2.5 seconds (**33ms * 75**).

***

### Giving a finger in style

In both GTA III and Vice City, the protagonists shake their fists[^shake-fist] at incoming traffic vehicles. Usually, this is supposed to happen when the player is unarmed
or holds a melee weapon, pistol, or an SMG. However, in Vice City, this feature had several distinct bugs, now all fixed in SilentPatch:
* Holding Brass Knuckles made Tommy never shake his fist.
* Holding the Chainsaw didn't prevent Tommy from shaking his fist, even though it's a two-handed weapon.
* In one instance, where the game code was not updated to account for weapons introduced in Vice City, Tommy didn't shake his fist at stopped traffic when holding any melee weapons,
  pistols, or SMGs introduced in this game.

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/10_gta-vc_kpGusxKptw.jpg" thumbnail="auto"
      caption="Here, I used the PS2 animations. In a completely stock PC version, this gesture looks... a bit different." %}

[^shake-fist]: In reality, the gesture looks different, but the game refers to it internally as shaking the fist.

***

### Why is this radar so ugly? Part 2

Radar again? Yep, but this time, it's even worse.

The issue [I mentioned earlier in the context of GTA III](#why-is-this-radar-so-ugly) is still present, and on top of that, new issues have appeared:
in Vice City, the radar disc has been rescaled and re-styled -- the outer disc now extends 6 pixels around the map, and a fancy shadow effect has been added 2
pixels below the disc. This worked fine on PS2, but is broken in multiple ways on other platforms:
* The shadow doesn't scale to resolution either, so at high resolutions, it's hardly noticeable.
* Making the radar disc scale reveals another issue: its size of 6 pixels (or 6 "units", when scaling) is too much, and there is now a gap between the bottom half of
  the radar disc and the map! I initially thought I incorrectly scaled this element, but... the same gap shows in the Xbox version! Pay close attention
  to the radar in a timestamped segment of this gameplay video, and you'll notice a 1-2 pixel wide gap, through which the scene can be seen:
  <figure class="media-container">
  {% include figures/video-iframe.html link="https://www.youtube.com/embed/DhWylVJnCvI?start=1243" %}
  <figcaption>The entire HUD of the Xbox version looks kind of bad, but this is a cherry on top IMO.</figcaption>
  </figure>

SilentPatch rolls out multiple fixes to make the radar look consistent and tidy:
* Just like in GTA III, the horizontal placement and the radar disc margin, as well as the shadow, scale to resolution.
* The radar disc has been shrunk by 2 pixels&#8203;/&#8203;"units", so the gap in the bottom never shows up.
* The outline of the destination blip now scales to resolution -- while Vice City fixed the bug where the blip itself didn't scale,
  the outline remained of a constant thickness. Interestingly, when fixing this bug in the first release of SilentPatch for GTA III,
  I also addressed the scaling of the outline, not realizing that it was still partially broken in Vice City.

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_5aU7jfvA1R.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_5aU7jfvA1R.jpg"
            caption="By default, the radar is too close to the edge of the screen, the shadow effect is almost non-existent, and the destination blip has a 1px outline." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_AOgkVUIIjm.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_AOgkVUIIjm.jpg"
            caption="With SilentPatch, the radar's placement and all elements scale to resolution correctly. Its overall appearance is now much more tidy." %}
</figure>

Additionally, the onscreen counter bar's shadow and the loading bar outline now also scale to resolution:
<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_mCJR5mXNXH.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_mCJR5mXNXH.jpg"
            caption="The text looks fine, but the health bar, not so much." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_bohuybDR1p.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_bohuybDR1p.jpg"
            caption="Another tiny consistency win." %}
</figure>

***

### Other fixes {#other-fixes-gta-vc}

* Fixed an issue where muzzle flashes from assault rifles faced the wrong direction. This fix was contributed by **Wesser**.
  <figure class="media-container small">
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_sDxrK7QV45.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_sDxrK7QV45.jpg"
            caption="In the stock game, the muzzle flash effect makes very little sense." %}
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/10_gta-vc_PEqsdrUJ7U.jpg" link="/assets/img/posts/sp-2024-update/screens/full/10_gta-vc_PEqsdrUJ7U.jpg"
            caption="With SilentPatch, it's much better." %}
  </figure>
* Fixed an issue where looking at a shopkeeper while using Classic controls counted as aiming at them. This happened because the
  `IS_PLAYER_TARGETTING_CHAR` script command, updated for Standard controls on PC, didn't previously differentiate between those control styles.
  This fix was also contributed by **Wesser**.
* Starting a New Game would previously reset the mouse sensitivity, the same as when restoring settings to defaults. This has now been resolved.
* In this release, I revisited the Rosenberg Audio fix, famously the very first fix made for SilentPatch.
  The results are surprising -- 12 years later, it turns out this fix **was placebo all along**! Contrary to popular belief, this feature was never broken on PC
  after all, and all of Rosenberg's lines can be heard even without mods. The perceived difference in frequency of those lines may boil down
  to a different randomness function across platforms. Therefore, just for a good measure, together with the removal of a placebo fix,
  I also made this feature use a PS2 randomness function, to ensure the odds of this audio playing match the console.
* [Ped Speech Patch](https://gtaforums.com/topic/817075-ped-speech-patch-gta-vc/){:target="_blank"} from **Sergeanur** has now been integrated into SilentPatch.
  This makes pedestrians and Tommy much more talkative than by default.
  My variation of this fix also includes a fix for improper randomness of the chat initiation action -- the odds of that now match the PS2 version.
* Hitting vehicles and objects with a screwdriver now produces an impact sound.
  Previously, screwdriver was the only weapon that was completely quiet.
* Tear gas can now deal damage to Tommy and other mission characters, like in the PS2 version.
* Thanks to **Tomasak**, more interiors have been updated to have their outside areas visible from the inside.
* The rain stream effect on roads, which displays for a short period after the rain stops, now resets on loading a save. This prevents the effect from showing
  when the weather in the loaded save is sunny.

***

## Grand Theft Auto: San Andreas

While all three games received countless new fixes, this time, San Andreas took center stage.
After all, its 20th anniversary is just around the corner:

{:.additional-toc}
* [Improving vehicles, one animation at a time](#improving-vehicles-one-animation-at-a-time)
* [Can't recruit anyone? That's what you get for playing without a disc!](#cant-recruit-anyone-thats-what-you-get-for-playing-without-a-disc)
* [Fire! Fire! Oh, wait...](#fire-fire-oh-wait)
* [Carl Johnson is an innocent man!](#carl-johnson-is-an-innocent-man)
* [BOOM! Where did that wheel go?](#boom-where-did-that-wheel-go)
* [That's not a bazooka, Zero](#thats-not-a-bazooka-zero)
* [Where are you going, homie? We got work to do!](#where-are-you-going-homie-we-got-work-to-do)
* [UFO, shooting star, or both?](#ufo-shooting-star-or-both)
* [Ninja jacking begone!](#ninja-jacking-begone)
* [Multiple monitors, multiple problems](#multiple-monitors-multiple-problems)
* [I'm dizzy, hazy, and I see funny under the water](#im-dizzy-hazy-and-i-see-funny-under-the-water)
* [Other fixes](#other-fixes-gta-sa)

### Improving vehicles, one animation at a time

For this release, **Wesser** has contributed several fixes related to CJ's animations in vehicles:
* CJ's clothes are being moved by the wind when driving a bike, but not when driving the Quad. This is now corrected.
* When coasting at low speeds, Quad's handlebar movements didn't match CJ's animations. This is now corrected.
* Inverse to a fix [featured previously in GTA III](#boat-driving-animations), changing radio stations while driving a boat
  where CJ stands upright would make him play the sitting animation. This is now corrected, although the game lacks a suitable
  animation for changing radio stations when upright, so now this is done with no animation at all.
  {% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_rucVAWSHi9.jpg" thumbnail="auto"
      caption="You are a wizard, Carl." %}

***

### Can't recruit anyone? That's what you get for playing without a disc!

This is a fun bug, and likely the main reason why speedrunning San Andreas on a 1.01 patch is preferable!
On the surface, it's just a simple error -- once the player activates a replay, recruiting gang members by aiming them and pressing
a button is no longer possible. Although it was never mentioned in the official changelog, no one ever observed this issue in the 1.01 version
of the game, only in 1.0, so it was assumed that it was just fixed there.

However, **Wesser** found out there's more to that.
This is not a game bug -- instead, it was a mistake made when HOODLUM initially defeated SecuROM in the 1.0 executable back in {% include elements/time.html date="2005-01-01" preset=site.date.year %}!
A chunk of code obfuscated by DRM was decrypted incorrectly, resulting in this breakage, which has later been carried over by **listener**
to his famous Compact EXE. Wesser figured out this issue in detail and reimplemented the missing chunk of code that's now also included in SilentPatch.

If only listener was still around to update the Compact EXE... 😔

***

### Fire! Fire! Oh, wait...


Has this ever happened to you? You're minding your business somewhere in San Andreas, then out of nowhere, a **🔥 fire 🔥** breaks out! You don't have a fire extinguisher with you,
but there's a solution: you recall that there are fire extinguishers spawned in all food joints, and there's The Well Stacked Pizza Co. just around the corner!
You mash the sprint button as fast as you can, hoping to save the day, you enter the place and...

**The pickup is not there!? 🧯❌😭**

Fortunately (or unfortunately?) for you, that's not randomness, but a bug. While San Andreas is generally OK at resetting the game state on restarting a new game within the same session,
and SilentPatch further improves the situation by resetting a few more variables that were missed, map IPL files also exhibited a similar bug. While binary IPLs re-initialized fine
due to their streamed nature, text IPLs initialized several in-game spawns only once on game start, and never again -- so starting a new game after loading an existing save
resulted in those spawns simply not being present. Those are:
* Weapon pickups (five in the stock game, including fire extinguishers in kitchens)
* Car generators (none in the stock game, but supported)
* Unique stunt jumps (none in the stock game, but supported)

In this release, SilentPatch keeps track of those IPL definitions and re-initializes them when starting a New Game.
Sadly, the existing saves affected by this issue cannot be automatically fixed, but at least any future playthroughs will have
the missing items spawn reliably.

***

### Carl Johnson is an innocent man!

Back in {% include elements/time.html date="2005-01-01" preset=site.date.year %} or {% include elements/time.html date="2006-01-01" preset=site.date.year %},
when I was casually messing around in San Andreas as a kid, I often found myself in a familiar situation: I'd get a wanted level,
biker cops would come after me, then I'd enter the legendary **AEZAKMI** cheat code to get rid of the pursuit, and yet...
the biker cops would keep shooting at CJ. Annoying, right?

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_xyEWIFtogB.jpg" thumbnail="auto" caption="Rude." %}

In {% include elements/time.html date="2024-01-01" preset=site.date.year %}, I finally dived into this issue, and after some heavy debugging, I realized it happens because of an oddity in
how the specific Drive-By task used by the biker cops is coded: unlike all the other pursuit activities, the drive-by task
is actually the same as the one used by the gang members, and thus it's not coded to automatically finish when the player
loses pursuit!

In SilentPatch, I updated the code to check if a cop aborting pursuit has a `TASK_SIMPLE_GANG_DRIVEBY` task active,
and if they do, cancel it. It works great and fixes one of the game's quirks that used to annoy an 11-year-old Silent 😅.

***

### BOOM! Where did that wheel go?

In GTA III and Vice City, exploding vehicles would always lose their front left wheel. In an attempt to improve this feature
in San Andreas, the developers made it detach a random wheel on explosion instead. However,
Rockstar half-baked this improvement -- the wheel may have detached visually just fine, but as far as the physics was concerned,
the old behavior of always losing the front left wheel persisted. This results in a new visual glitch, where the wrong wheel sinks:

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_2EBUGkr5z3.jpg" thumbnail="auto"
      caption="That... isn't how physics works." %}

In this update, I fixed multiple bugs related to this feature:
* The detached wheel now matches "visually" and "physically".
* The rear right wheel can now also be detached. Previously, the random function would only consider the front wheels and the rear left wheel.

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_VpNpSA8TP6.jpg" thumbnail="auto"
      caption="Much better." %}

This fix also comes with an unintentional but cool side effect -- exploding the vehicle multiple times using cheat codes can make it lose
multiple wheels, eventually leaving a wreck with all four wheels detached!

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_5QScgz55IH.jpg" thumbnail="auto" %}

***

### That's not a bazooka, Zero

"Air Raid", the first mission given to the player by Zero, is an interesting case of Rockstar trying to fix script errors...
and failing. This mission places CJ in a turret mode operating a minigun that is given to him only for the duration of the mission.
In the original PS2 version, and PC 1.0, this mission "steals" the player's heavy weapon entirely, and there is no way to avoid it.
In 2.0, Rockstar attempted to fix it by saving information about the existing weapon on this slot, and it was given back to the player afterward.
However, the script fails to load the weapon model, so the player... is given back an invisible weapon instead. Don't try to use it -- your game will crash!

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_10nRIQhRy2.jpg" thumbnail="auto"
      caption="Don't touch that ~~dial~~ gun." %}

Thankfully, this mistake wasn't severe, and simply saving the game, and then reloading that save, fixes it.
Nonetheless, in this update SilentPatch injects a proper fix to this mission, ensuring that the weapon is preserved,
and the model is loaded correctly.

***

### Where are you going, homie? We got work to do!

Amidst the chaos of the Los Santos riots in the final parts of San Andreas' story, the game presents a rather frustrating quirk.
At random points, gang members in CJ's group can abandon him and flee, seemingly for no reason.
While this might add some interesting dynamics during free roam, it can be a deal breaker during missions. Therefore, **Nick007J** dived into the code
to thoroughly understand these events.
1. At regular intervals, the police chopper flying above the city targets a random gang member. This can be someone from CJ's group or any other random person.
2. The targeted person starts fleeing, trying to escape the chopper.

SilentPatch refines this feature slightly to prevent it from being a hindrance -- during missions, CJ's group can no longer be targeted by the chopper.

***

### UFO, shooting star, or both?

One of the mysteries "haunting" San Andreas since the dawn of time is the presence of unusual black dots rapidly moving in the sky.
People theorized it may be a strange raindrop, a shooting star, or... UFO. This was something I was aware of for a while,
but only after **Bob El Aventurero** made a detailed video trying the unravel this mystery I looked into this phenomenon in more detail:

{% include figures/video-iframe.html link="https://www.youtube.com/embed/3-Dr2zcT3sw" %}

The video touches on the technical side of this effect a bit, stating that it is supposed to be rendered as a single-pixel-wide white line,
but doesn't answer the question as to why it comes out black instead. Turns out it renders as such only because... it attempts to draw using the cloud texture.
Since the line is just a single pixel wide and it has no UV data, it most likely sampled the top left corner of
the cloud texture, ignoring alpha. The fix, as usual, is trivial -- draw the star with no texture. At last, the mystery is put to rest:

{% include figures/video.html link="/assets/img/posts/sp-2024-update/shooting-star.mp4" attributes="autoplay muted loop" %}

***

### Ninja jacking begone!

Twitter user **Radiant Eclipse** asked Obbe Vermeij an interesting question regarding a well-known, yet mysterious bug/feature:

<blockquote class="twitter-tweet" data-align="center"><p lang="en" dir="ltr">Hi <a href="https://twitter.com/ObbeVermeij?ref_src=twsrc%5Etfw">@ObbeVermeij</a>, in GTA SA when you steal a car through the passenger door while holding the run button the driver leaves the car dead. Do you know of this is intentional or is it a bug? I&#39;m asking this because the game never talks about it. I made a short video showing this <a href="https://t.co/WnsqlYEnQE">pic.twitter.com/WnsqlYEnQE</a></p>&mdash; Radiant Eclipse (@RadiantEclips10) <a href="https://twitter.com/RadiantEclips10/status/1794440479901098141?ref_src=twsrc%5Etfw">May 25, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I asked **Nick007J** if he looked into this before, and he did, but without a definite answer -- so we decided to look into this again.
It turns out that in the event of the player holding the throttle and/or brake buttons while jacking the car from the passenger side, the game does the following checks:
* If the driver is alive, make them leave the car dead.
* If the driver is dead, make them step out of the car as normal.

This sounds... backwards, especially since a different code path in the same function had those checks switched around.
We theorized that this was likely just a mistake and the conditions were meant to be swapped, but only once **ultragirl468** ran tests themselves,
we had definite proof. They managed to jack the car from an already dead driver, and...
{% include figures/video.html link="/assets/img/posts/sp-2024-update/sa-jack-car-dead-ped.mp4" style="natural" attributes="controls"
    caption="The driver leaves the car, then promptly dies (again)." %}
This was the proof we needed -- simply inverting the check fixes this issue. Now alive drivers stay alive, and dead drivers stay dead.
This issue was also fixed in the Definitive Edition (but not the "classic" mobile/PS3/X360 releases),
where it behaves the same way as the classic San Andreas with my fix applied.

<div style="display: flex; align-items: center; text-align: center; margin: 1em 0" markdown="1">
<div style="flex: 0.1; border-top: 1px solid var(--line-color)"></div>
You could say that someone... *told Obbe it happened again* ;)
{:style="margin: 0 2.5em; font-size: 1%"}
<div style="flex: 1; border-top: 1px solid var(--line-color)"></div>
</div>

### Multiple monitors, multiple problems

{:.disclaimer.info}
This section contains affiliate links, meaning I get a commission for every purchase made through them.

Recently, I was invited to a promo campaign and received a [JSAUX FlipGo](https://www.jsaux.com/products/flipgo-portable-dual-monitor?sca_ref=6671512.IBblIIjr8x){:target="_blank" rel="nofollow"},
a portable dual-screen monitor. Before I only had a single monitor, so only now I realized how strange the monitor selection dialog in GTA San Andreas is. Since I was now "affected" by it,
I fixed several annoyances present in that dialog and enhanced it with some QoL improvements.

<figure class="media-container small">
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/res-dialog-old.png" caption="The stock dialog looks a bit sad and lists the GPU names, which can be confusing." %}
{% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/res-dialog-new.png" caption="With SilentPatch, the dialog looks modern, uses user-friendly monitor names, and can be skipped."%}
</figure>

* Remade the dialog with modern Common Controls, so it looks native, instead of being limited to Win9x style controls.
* Made the dialog use user-friendly monitor names (on Windows 7 and newer) instead of the DirectX 9 adapter names, which for most people just duplicated the GPU names.
  In my case, I had three `NVIDIA GeForce GTX 1070` entries, and now they are named after the screens.
* The dialog ignored the X control and the <kbd>Esc</kbd> button, now it closes on those properly.
* The dialog now gets keyboard focus on creation.
* The taskbar icon now shows reliably, and the title bar displays a small icon.
* The dialog now remembers the selected screen. Previously, it remembered the resolution index but not the screen index (despite storing this information in the `.set` file),
  so it instead pointed at some random resolution on the first screen.
* The dialog now defaults back to the first screen if a non-existent screen is selected, for example when starting the game after unplugging one of the screens.
* The dialog is now explicitly DPI unaware, so DPI compatibility settings can't prevent it from scaling.
* Most importantly -- **monitor and resolution choices can now be remembered in a separate `.set` file, and the dialog can be suppressed!**
  A tooltip has been added to the new checkbox, instructing the player to delete `device_remembered.set` from GTA San Andreas User Files if they want the dialog to show again.

***

### I'm dizzy, hazy, and I see funny under the water

Thought we were done with the resolution scaling issues, after all the problems I already detailed earlier? Haha, no.

San Andreas post effects are not only the most elaborate out of all 3D-era games but also quite different between PS2 and the other platforms.
That said, the heat haze effect appears to be identical between PS2 and PC... at least if you don't keep changing the resolution in-game.
If you do, weird things can happen -- here's how the effect looks if you run the game in 4K, and then change the resolution to 640x480:

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_hI9FOMH1LF.jpg"
      caption="This edible ain't shi-" %}

A simple game restart solves this, so it's not a critical bug -- nonetheless, it has been fixed in this update of SilentPatch,
so now the effect rescales properly once settings are changed.

***

But, there is more! The ripple effect when the camera is underwater, as nice as it is, also looks slightly distinct at different resolutions.
It's not broken per se, as it mostly scales fine, but the frequency of the wave effect is noticeably higher at high resolutions.
This has now been fixed, so the effect looks consistent:

{% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_i1mMeHdPww.webp"
      thumbnail="/assets/img/posts/sp-2024-update/screens/thumb/compact_gta_sa_i1mMeHdPww.webp"
      caption="From left to right -- stock game at 640x480, stock game at 4K, SilentPatched game at 4K." %}

***

### Other fixes {#other-fixes-gta-sa}

* Stats counted in kilograms now display correctly in the Stats menu.
* Past SilentPatch builds already made the game accept several typos in the vehicle hierarchy, fixing e.g. a missing middle wheel in DFT-30.
  For this release, two more typos are now accepted by the game:
  * `transmision` in Dumper, making the suspension animated, like in the Monster Truck.
  * `tailights` in Uranus, relocating the tail light coronas from the interior of the car to the rear lamps.
* A significant memory leak when taking photos with an in-game camera has been fixed.
* **Wesser** contributed a fix to the gang members taking a photo of CJ. Previously, holding a sniper rifle changed the camera "crosshair"
  to the sniper rifle crosshair. This has now been resolved.
* Racing checkpoints are now correctly colored even if no enex markers were displayed on-screen before.
  This obscure bug was practically impossible to witness in a stock game, but could easily be seen with mods, or in MTA races.
  <figure class="media-container small">
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_UjkQ0BxFYu.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_UjkQ0BxFYu.jpg"
        caption="RenderWare geometry instancing memes are in full swing -- the arrow geometry got instanced without the material colors." %}
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_wYArX9B9LE.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_wYArX9B9LE.jpg"
        caption="With SilentPatch, it's no longer an issue." %}
  </figure>
* Fixed a crash that occurred when mashing the replay button near groups of gang members holding items.
  This involves a rather elaborate list of steps that went wrong in the game logic, but I documented it in detail in the patch source code,
  so I'll just quote my technical explanation here:
  > `CWorld::Process` processes all entries in the moving list, calling `ProcessControl` on them.
	> `CPlayerPed::ProcessControl` handles the gang recruitment which in turn can result in homies dropping cigarettes or bottles.
	> When this happens, they are destroyed **immediately**. If those props are in the moving list right after the PlayerPed,
	> this corrupts a pre-cached `node->next` pointer and references an already freed entity.
	> To fix this, queue the entity for delayed destruction instead of destroying it immediately,
  > and let it destroy itself in `CWorld::Process` later.
* **Wesser** contributed a fix to the SCM interpreter, where spawning a biker cop (`lapdm1`) with a type
  `PEDTYPE_COP` spawned a normal cop instead. This issue doesn't affect the default script but might have affected mods.
* Impound garages can now only impound cars and bikes (and their subtypes), as other vehicle types are either too big or cannot leave
  the garage without exploding. This puts a stop to helicopters and boats being impounded.
  {% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/compact_gta_sa_rern5vrm2H.jpg" thumbnail="auto"
      caption="I... whatever, man." %}
* Several more crashes related to replays have been fixed:
  * A crash occurred when starting a cutscene after playing a replay where CJ wore different clothes from what he is currently wearing.
  * A crash occurred when playing back a replay with CJ having a different body type (fat/muscular/normal) than his current one.
* The spawning logic of planes has been slightly improved. While they can still crash after spawning, this should now occur less frequently.
* Hovering with a jetpack is now possible using the keyboard controls by holding the next/previous weapon buttons simultaneously (<kbd>Q</kbd> + <kbd>E</kbd> by default).
  {% include figures/video.html link="/assets/img/posts/sp-2024-update/compact_gta_sa_vBJEQfYyk5.mp4" attributes="autoplay muted loop"
      caption="I never realized before how much easier the jetpack is to control when you can hover effortlessly." %}
* Heat-seeking missile crosshair and the weapon crosshair shown while aiming with a gamepad now properly scale to resolution.
  <figure class="media-container small">
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_Bhx9LphOdb.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_Bhx9LphOdb.jpg"
        caption="Not unusable, but way too small for comfort." %}
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_SmUshfkuFj.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_SmUshfkuFj.jpg"
        caption="I think it looks much nicer at this size." %}
  </figure>
  <figure class="media-container small">
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_y3MMwTp364.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_y3MMwTp364.jpg"
        caption="At 4K, you can barely see this crosshair to begin with." %}
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_JGca4siWbL.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_JGca4siWbL.jpg"
        caption="At last, now it's usable." %}
  </figure>

* **Wesser** contributed a fix for a well-known script glitch in the Driving and Bike Schools. Previously, an error in how these scripts
  destroyed the cones used in lessons could cause random objects to be removed from the game. This glitch was most famously known
  as the "Blackboard glitch". Unfortunately, SilentPatch cannot repair saves already affected by this issue.
* The cursor on the Map screen now scales to resolution and it can now always reach the top left corner of the map, regardless of resolution. This fix was contributed by **Wesser**.
* The inner 4-pixel padding of the text boxes with a background now scales to resolution correctly. This fix was contributed by **Wesser**.
* Nitrous will no longer regenerate faster when reversing the car. Instead, recharging speed while reversing is now identical to when the car is stationary.
  Once again, this fix was contributed by **Wesser**.

***

# Internal changes

Aside from all the new fixes, for this release, the codebase of SilentPatch has also been heavily modernized,
and multiple fixes have been... *well, fixed*. Some of those changes are well worth highlighting.

**Some of those points might get a little technical**, but they may be useful for modders who want to be mindful
of keeping compatibility with SilentPatch or are looking for tips on how to make their projects
apply code patches in a more resilient way.

* The most severe regression introduced by SilentPatch has finally been addressed. Ever since the first build,
  SilentPatch attempted to fix the '<samp>Cannot find 640x480 video mode</samp>' error.
  While my fix worked fine for users not using DPI scaling, it made things worse for those using that
  feature -- and the game would instead complain about being unable to find impossible resolutions like 1152x867.
  This bug has finally been addressed, and the new fix works correctly regardless of the DPI scaling.

* Migrated several fixes to use `HookEach`. These fixes would hook multiple calls to a function,
  and add my own changes on top. However, previously SilentPatch assumed all those calls were pointing
  to the same function, which is true for an unmodded game, but another modification installed alongside
  SP may have broken this assumption. With `HookEach`, each instance is treated separately, without the risk
  of stomping on another hook, and "stacking" with other modifications gracefully.
  In fact, multiple fixes within SilentPatch also stack on each other like this, and they're completely unaware
  of each other, even when they hook the same call in the code.

* All SilentPatches released after May 2021 use **transactional patterns**. For this release,
  I upgraded the codebase to use those too. Previously, if **any** pattern failed to match while the patch was applied,
  the entire library would unload and either crash the game or just do nothing.
  With transactional patterns, every single fix is applied separately, and if any pattern forming a particular fix fails to match,
  an exception is thrown and the entire fix is aborted without making any changes to the game's memory.

  For the patch code, this simplifies the way fixes are applied to the game and makes it impossible
  for me to accidentally break the entire patch if I forget to account e.g. for another mod making changes to the code.
  This comes with benefits for users too, as compatibility with other mods should be improved even further!
  Other recent SilentPatches showed that with transactional patterns, it's nearly impossible to "break" SP completely.

* SilentPatch for San Andreas introduced this fix several releases ago:
  > * A muzzle flash will now show up when firing the last bullet from the clip.

  However, this introduced a regression where "firing" from an empty gun while on a jetpack still displayed the muzzle flash:
  {% include figures/image.html link="/assets/img/posts/sp-2024-update/screens/gta_sa_nAHcd3qnmv.jpg" thumbnail="auto" %}
  This fix has been remade, addressing the issue.

* SilentPatch for San Andreas has had this fix ever since the first release:
  > * Detached vehicle parts will now remain the same color as the vehicle they came from.

  In this release, this fix has received multiple improvements:
  * Recently, it was discovered that this change would cause the game to crash if a part detached from a modded vehicle
    had more than 15 materials. This has now been resolved.
  * While the colors of the detached parts were always preserved, turns out they were never correctly lit. Furthermore,
    later SilentPatch updates removed the auxiliary vehicle light in favor of properly working directional lighting,
    so the lighting appeared as if it had regressed. In this update, detached parts are now lit the same way the cars are.

* Earlier releases of SilentPatch for San Andreas rolled out multiple fixes for the license plates not working correctly.
  Recently, it's been discovered that this fix would cause the license plates to stop generating if a vehicle with custom plates was fitted with tuning parts.
  I reimplemented this fix from scratch, making it simpler, and in turn also resolving this issue.

* The last release of SilentPatch for San Andreas introduced a fix for the parachute animations. However, at that time this fix came at the expense
  of the removal of Night Vertex Colors from the parachute model, making it appear too bright at night. Thanks to **B1ack_Wh1te**, for this update this
  fix has been revisited and now it combines **both** the correct colors with working animations. Additionally, since this fix caused rendering issues
  in SA-MP, it's now disabled in multiplayer, unless Graphics Restore is installed.
  <figure class="media-container small">
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_V50SgMrU4c.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_V50SgMrU4c.jpg"
        caption="In \"The Corona Update\", the parachute was animated correctly but looked kind of bright." %}
  {% include figures/image.html thumbnail="/assets/img/posts/sp-2024-update/compact_gta_sa_uSsu8BO7Gs.jpg" link="/assets/img/posts/sp-2024-update/screens/full/compact_gta_sa_uSsu8BO7Gs.jpg"
        caption="In this update, both lighting and animations work fine." %}
  </figure>

* In the last update, this fix present in GTA III and Vice City was rewritten:
  > * Reintroduced light glows under weapon/health/armor pickups, bribes, hidden packages, and money pickups -- they showed only on PS2 due to a bug in all PC versions.

  However, back then I didn't notice that my rewrite caused those light glows to disappear when "light boxes" on cars were rendered on-screen
  (because the widescreen fix disables those boxes). I now updated this fix again to resolve this issue
  and bring parity with the San Andreas version of this change.

* In III and Vice City, variable resets like the Pay 'n Spray flag have been upgraded to use the same, less invasive,
  approach as the one used in SilentPatch for San Andreas.

* Patches for GTA III and Vice City have been upgraded to support 32-bit model IDs from
  [fastman92 limit adjuster](https://gtaforums.com/topic/733982-fastman92-limit-adjuster/){:target="_blank"}.
  The San Andreas version was already supported previously.

* Patches for GTA III and Vice City have been updated to support ASLR. Whilst no officially released executable of those games has this security feature enabled,
  some of them contain valid relocation info, and therefore a Windows security option forcing ASLR wherever possible could have caused SilentPatch not to apply correctly.
  This has now been resolved.

  In case you are wondering what is ASLR good for, here's a great example -- an exploit in [BeamNG.drive](https://store.steampowered.com/app/284160/){:target="_blank"}
  (that was additionally made easier and more reliable to pull off due to the game disabling ASLR on one of its libraries[^beamng-drive])
  [has been used to hack Disney](https://www.thedrive.com/news/culture/hackers-exploited-a-pc-driving-sim-to-pull-off-massive-disney-data-breach){:target="_blank"}!
  If ASLR wasn't disabled, this exploit would have been much harder to create; the code comments in the proof-of-concept exploit even mention a "static base address"
  specifically.

* In all 3 games, fixes related to randomness now use the same randomness engine, based on the PS2 algorithm.
  It's unlikely to result in any noticeable differences, but it simplifies the code.

* In all 3 games, the INI options listing vehicle model IDs (like `RotorFixExceptions`) can now also accept model names.

[^beamng-drive]: Regular followers on my Twitter know how vocal I am about this particular issue, to the point of being annoying.
    I don't intend to stop, as it's for the benefit of all the players, including myself.

# Download and source code

The latest SilentPatch builds can be downloaded from the *Mods & Patches* section:

{:.flexible-buttons}
<a href="{% link _games/gta/gta-iii.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA III</a>
<a href="{% link _games/gta/gta-vc.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA Vice City</a>
<a href="{% link _games/gta/gta-sa.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA San Andreas</a>

Those new to SilentPatch are encouraged to check the [Setup Instructions]({% link pages/setup-instructions.md %}){:target="_blank"}.
However, the easiest way to install SP boils down to:
* For GTA III and Vice City, get both downloads for the respective game and extract them to the game directory.
* For GTA San Andreas, players using a 1.0 or Steam version can use [my ASI Loader]({% link _games/gta/gta-sa.md %}#asiloader){:target="_blank"}.
  Rockstar Games Launcher versions of the game need to use
  [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/latest/download/Ultimate-ASI-Loader.zip){:target="_blank"} instead.

Wish to check out the source code instead? Check it out on GitHub. I have also included the compilation instructions and contribution guidelines:

<a href="https://github.com/CookiePLMonster/SilentPatch" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>

**TJGM** has also published a showcase video focusing on San Andreas, covering many of the additions introduced in this update of SilentPatch:
{% include figures/video-iframe.html link="https://www.youtube.com/embed/Yb4_6fVaLrY" %}

# Credits and acknowledgments

This update was only possible thanks to the contributions of many individuals. Multiple modders generously shared their findings and fixes,
which were later integrated into SilentPatch. Others took their time to test the patch through its many iterations to ensure I could ship it
in a near-perfect state:

### Contributors:
* B1ack_Wh1te
* Fire_Head
* Nick007J
* Sergeanur
* Wesser

### Testing and socials:
* [Ash_735](https://x.com/Ash_735){:target="_blank"}
* [TJGM](https://www.youtube.com/@TJGM){:target="_blank"}

### Testing:
* Team at Luigi's Club
* Tomasak
* Wr3nch

Last but not least, a special shout-out to [Obbe Vermeij](https://x.com/ObbeVermeij){:target="_blank"} for all the GTA development
trivia he's shared with the world, and most importantly, for all the work he put into the games we still care about decades later 🙌.

# Future of SilentPatch?

Will there ever be another SilentPatch for the GTA games? *I don't know.* Half a decade passed between "The Corona Update"
and this post, so if that's any indicator, it's likely there won't be. However, I am acutely aware I've said "no more new fixes" at least
twice throughout the lifespan of SilentPatch for San Andreas, so... you never know.

SilentPatch has since thrived as a "brand" outside of GTA, breathing new life into many other old (and newer) games.
Whether or not GTA receives more updates in the future, I'm sure many more releases and blog posts are to come.
May classic games continue to bring joy to both new players and those reliving their childhood memories!

***
