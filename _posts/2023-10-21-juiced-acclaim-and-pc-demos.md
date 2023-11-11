---
layout: post
title: "Exploring the history of Juiced through prototypes and PC demos"
excerpt: "Looking into Acclaim and THQ demos and into the history of Juice Games in general."
thumbnail: "assets/img/games/bg/juiced-acclaim.jpg"
feature-img: "assets/img/games/bg/juiced-acclaim.jpg"
image: "assets/img/games/bg/juiced-acclaim.jpg"
game-series: ["juiced-demo", "juiced-acclaim-ps2"]
date: 2023-10-21 15:05:00 +0200
twitter: {card: "summary_large_image"}
tags: [Research, Releases]
juxtapose: true
---

* TOC
{:toc}

{% assign ps2online_link = "[PS2Online](https://ps2online.com/)" %}
{% assign sp_name = "SilentPatch & Enhanced PC Demo" %}

{% assign eagle_link = "**Eagle**" %}
{% assign juiced_modding_community_link = "[**Juiced Modding Community**](https://discord.com/invite/pu2jdxR/)" %}
{% assign f4mi_link = "[**f4mi**](http://f4mi.com/)" %}

{% assign may_2004_download_links = "[DOWNLOAD](https://archive.org/download/gamefiles.blueyonder.co.uk/gamefiles.blueyonder.co.uk.tar/gamefiles.blueyonder.co.uk%2Fblueyondergames%2Fdemos%2Fjuiced_demo.zip) (retrieved)" %}
{% assign june_2004_download_links = "[DOWNLOAD](https://files.hiddenpalace.org/1/11/Juiced_%28Jun_2%2C_2004_prototype%29.7z),
          [MIRROR](https://archive.org/download/acclaim-qa-pc/Juiced%20%28June%202%2C%202004%29%20%28Build%20PCJUIOFD003%29.7z)" %}
{% assign july_2004_download_links = "[DOWNLOAD](https://download.cnet.com/juiced-final-demo/3000-7513_4-10295963.html),
            [MIRROR](https://www.pcworld.pl/ftp/juiced-official-demo.html)" %}
{% assign january_2005_download_links = "[DOWNLOAD](https://www.gamepressure.com/download.asp?ID=7430),
            [MIRROR](https://www.pcworld.pl/ftp/juiced-demo-nr-2.html)" %}
{% assign april_2005_download_links = "[DOWNLOAD](https://www.moddb.com/downloads/juiced-updated-demo),
            [MIRROR](https://www.ausgamers.com/files/download/16587/juiced-demo-v2)" %}
{% assign may_2005_download_links = "[DOWNLOAD](https://www.gamepressure.com/download.asp?ID=7892),
            [MIRROR](https://www.moddb.com/games/juiced/downloads/juiced-demo-2-0-to-2-1-patch)" %}

*[FPU]: Floating-Point Unit; part of the CPU responsible for floating-point calculations
*[ASIN]: Amazon Standard Identification Number

# Introduction

Usually, when I dissect games on this blog, I don't give much attention to demos. However, due to its troubled
development cycle, [Juiced](https://en.wikipedia.org/wiki/Juiced_(video_game)) is an exceptional case.
Because of the game changing publishers right before the original release date, the game has changed considerably
-- and thanks to PC demos and leaked PS2/Xbox prototypes, we have a unique opportunity to experience the game in its original form.

This post is the first in the series of [Research]({% link pages/categories.html %}#Research)-style posts.
I intend to keep updating posts in this category as new information comes in instead of publishing new posts about the same game,
so keep an eye on this category from time to time 😉
In this post, instead of focusing on modifying Juiced, I want to showcase the game and its history through the evolution of
all 6 PC demos that are available online. They all have minor compatibility issues, so for that, I'm releasing
the first strictly demo-oriented SilentPatch with two clear goals:
1. Fix the demos just enough for them to be playable without compatibility issues. I wish to preserve those demos in their original state,
  so I focused solely on critical bugs. This means that separate <kbd><samp>Quit</samp></kbd> and <kbd><samp>Quit Game</samp></kbd> options
  present in the Acclaim demos are here to stay for the sake of history 😉 Despite the limited scope of this SilentPatch, it should still make for an entertaining
  read -- since the bugs I fixed range from incorrect math behind the field of view calculations, compatibility bugs, through (for the first time)
  a possible compiler/optimizer bug breaking the game's code!
2. (Optionally) unlock the demos as much as possible. Early demos had widescreen support from the console versions left unused,
  and they all ship more content than was made available officially. Since I want to use those PC demos as a showcase of "the game that never came to be",
  I want everyone to enjoy them to the fullest.

Not interested in demos and you'd rather experience the full prototype builds? I have something for you too.
As part of my research, I was playtesting those builds too, and later I created several small patches for the PS2 versions -- including a 60 FPS
hack and **a patch to make those prototypes playable online via {{ ps2online_link }}!**
The latest builds to surface online are developed so far that you can even play them through the Internet.


# Chapter 1: Who was Juice Games? What is Juiced?

The history of Juiced and Juice Games isn't told in full without mentioning [Rage Software](https://en.wikipedia.org/wiki/Rage_Games).
This British studio was responsible (among other games) for racing games like [E-racer](https://en.wikipedia.org/wiki/E-racer)
or [Off-Road Redneck Racing](https://en.wikipedia.org/wiki/Off-Road_Redneck_Racing), however, they were also working on
[Lamborghini](https://en.wikipedia.org/wiki/Lamborghini_(video_game)) -- a racing game [announced in May 2002](https://www.ign.com/articles/2002/05/24/e3-2002-first-lamborghini-shots)
that promised to feature every single car model from this Italian automaker.[^lamborghini-cars]

<figure class="media-container small">
{% include screenshot.html link="https://files.hiddenpalace.org/8/80/LamborghiniDec10_4.png" %}
{% include screenshot.html link="https://files.hiddenpalace.org/e/e9/LamborghiniDec10_7.png" %}
</figure>

Unfortunately, Rage Software
[went bankrupt](https://www.gamespot.com/articles/rage-software-closes-its-doors/1100-2908866/) in January 2003, just before they could release the game.
Lamborghini became a lost media, with only an Xbox Demo surviving, at least until May 2022, when a nearly finished beta build
[has been published on HiddenPalace](https://hiddenpalace.org/Lamborghini_(Dec_10,_2002_prototype)).

Not long after, part of the Rage Software staff founded Juice Games.
Even on their [official website](https://web.archive.org/web/20081003032009/http://www.juicegames.com:80/html/company.html),
they were always upfront about their Rage Software roots:

> With a back catalogue that includes TFX, EF2000 **and the critically acclaimed but unreleased Lamborghini**,
> Juice Games developed the multi-million unit selling Juiced franchise.

Sometime in 2003, the team secured funding from [Fund4Games](https://www.gamesindustry.biz/fund4games-a-new-funding-model-for-development)
and a publishing deal with [Acclaim Entertainment](https://en.wikipedia.org/wiki/Acclaim_Entertainment) (who needed a new racing title after losing
the publishing rights for Burnout) for their new game, **Juice**.
While the game was never officially referred to by this name, thanks to a very early prototype we know this name was in use at least until November 2003.

{% include video.html link="https://www.youtube.com/embed/4rx5WTrZkTs" %}

By the time Juice Games officially [announced the game in January 2004](https://www.ign.com/articles/2004/01/22/juice-games-announces-juiced),
it was already known by its final name and set for a Fall 2004 release. The development process under Acclaim was relatively well documented,
with multiple websites showcasing the game in its early state[^ign-preview] [^gamespot-preview] [^eurogamer-preview], and with demos on all platforms releasing around July 2004.
In fact, you could say that they released one demo too many -- on {{ "2004-06-09" | date: page.date-format }},
[a PC demo was released](https://www.ign.com/articles/2004/06/09/juiced-demo-released) early by the German division of Acclaim,
then [promptly delisted](https://web.archive.org/web/20040521201131/http://www.acclaim.de:80/) on {{ "2004-06-11" | date: page.date-format }}. and scrubbed from the internet thoroughly:

> **Juiced Demo**
>
> The Juiced demo was taken from the server because it does not show the final status of the game.
> A new demo will be available as soon as possible. Thank you for your interest!

A "final" Acclaim demo was eventually [released on {{ "2004-07-14" | date: page.date-format }}](https://www.ign.com/articles/2004/07/14/updated-juiced-demo),
in a much better state than the first one. While Acclaim has done a good job replacing the early demo with a proper build,
some downloads survived thanks to [Wayback Machine](https://archive.org/web/) and we can experience this early demo with all its issues -- but more on that later 😉

Thanks to [many prototypes surfacing online](https://hiddenpalace.org/Category:Juiced_prototypes), we know that by August 2004 the game was nearly complete,
and reviews stated [the game was to be released in September 2004](https://www.gamespot.com/articles/juiced-preview/1100-6104070/).

> We'll bring you more on Juiced as its early September release date approaches.

[An Amazon listing](https://www.amazon.com/Acclaim-Ent-Juiced-complete-package-PlayStation/dp/B0001XASGC) attributed to Acclaim Entertainment exists
and lists the release date as {{ "2004-09-07" | date: page.date-format }}, although this listing doesn't use Acclaim's cover art.
Interestingly, [THQ listings](https://www.amazon.co.uk/THQ-Juiced-PS2/dp/B000219OCC/) also exist and they have a different ASIN, but that may just be an US vs. EU Amazon.

{% include screenshot.html link="https://cdn.mobygames.com/promos/7167894-juiced-other-playstation-2-preliminary-box-art.jpg"
        style="natural" caption="Even the original box art was revealed." %}

September release never happened, though -- instead, Acclaim [filed for bankruptcy in October 2004](https://www.cnet.com/tech/gaming/game-maker-acclaim-files-for-bankruptcy/)
and the game's future became unknown. This has all happened so late so some boxed copies of the game [ended up turning up online years later](https://www.reddit.com/r/gamecollecting/comments/3r9y36/picked_up_the_cancelled_version_of_juiced_on_the/), although there is no evidence of the game reaching the store shelves.

{% include video.html link="https://www.youtube.com/embed/wNuw6uVv8ng" %}

<figure align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">- work for Rage Software<br>- develop a Lamborghini game nearly to completion<br>- studio bankrupts, game never releases<br>- move on to found Juice Games<br>- develop Juiced for Acclaim nearly to completion<br>- publisher bankrupts, new publisher modifies the game<br><br>Folks had the worst luck :( <a href="https://t.co/wIwmERTVb7">pic.twitter.com/wIwmERTVb7</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1704429355684766178?ref_src=twsrc%5Etfw">September 20, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</figure>

Before long, [THQ](https://en.wikipedia.org/wiki/THQ) and Take-Two [both bid](https://www.gamespot.com/articles/take-two-squeezing-juiced/1100-6108179/) to acquire rights to Juiced;
Electronics Arts also attempted to join the bid but failed to meet the deadline (and, honestly, it's good that they didn't manage to buy a direct competitor
to their own Need for Speed: Underground). [THQ eventually won](https://www.gamedeveloper.com/pc/thq-wins-i-juiced-i-bidding-war) and moved the release date to Summer 2005,
giving Juice Games [5 more months](https://www.eurogamer.net/i-juiced-june2005) to make changes to the game. If the reviews were to be trusted,
that new iteration [was received better than the Acclaim's version](https://www.gamespot.com/articles/juiced-updated-hands-on/1100-6117203/).
The public was also able to see the changes themselves first through a round of demos released in January 2005, then in May 2005, just before the game's release.
The game was eventually released on {{ "2005-06-13" | date: page.date-format }} in North America and {{ "2005-06-17" | date: page.date-format }} in Europe.

***

This brief recap of the game's history brings me to the clue of this article. Even though Acclaim's Juiced and THQ's Juiced are not entirely different games,
the game went through some significant design changes. With no known full PC builds surviving, demos is all we have on this platform.
In my analysis, I'll go through all 6 known PC demos and compare them one by one in the order of their internal timestamps.

[^lamborghini-cars]: [RAGE WILL LAUNCH OFFICIAL LAMBORGHINI GAME -- LamboCARS.com](https://www.lambocars.com/rage-will-launch-official-lamborghini-game/)
[^ign-preview]: [Juiced - IGN](https://www.ign.com/articles/2004/01/27/juiced-4)
[^gamespot-preview]: [Juiced Preview - GameSpot](https://www.gamespot.com/articles/juiced-preview/1100-6104070/)
[^eurogamer-preview]: [Juiced \| Eurogamer.net](https://www.eurogamer.net/p-juiced)


# Chapter 2: Acclaim Demos

All 3 Acclaim demos have content parity, at least when it comes to officially unlocked content:
* 3 cars with an option to pre-tune them
* 1 selectable route in San Ricardo

When it comes to locked content shipped with the files, there are a few differences.
In {{ sp_name }}, all exclusive content is "ported" to the latest Acclaim Demo.

SilentPatch includes identical fixes for all 3 demos, and therefore I'll be only [highlighting them on the latest, most polished demo](#acclaim-silentpatch-fixes).
Screenshots included in this chapter are all taken with SilentPatch installed, as otherwise I would have to take them in 4:3.
However, this is the **only** modified visual aspect of those demos.

## May 2004 Demo

* Compilation date: **Thursday, 27 May 2004 10:38:44**
* Download links: {{ may_2004_download_links }}
* Worth testing: **NO**{:style="color:red"} (too buggy)

As mentioned previously, this demo was accidentally [released online early](https://www.ign.com/articles/2004/06/09/juiced-demo-released), and it shows.
Acclaim's attempts to scrub this version off the internet were mostly successful, as the above download link is virtually the only source I could find online.
This build has a range of issues, ranging from regular crashes, graphical artifacts,
and missing PC features, to an unimplemented Quit (<kbd>Alt</kbd> + <kbd>F4</kbd> doesn't work either!). Even ignoring all those, as far as I can tell,
a Nitrous button is completely unmapped in this build, and unlike later builds, this one doesn't give the player an option to redefine controls.

<figure class="media-container small">
{% include screenshot.html link="/assets/img/posts/juiced-research/screens/Juiced_5XeRWcy9N2.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_5XeRWcy9N2.jpg" %}
{% include screenshot.html link="/assets/img/posts/juiced-research/screens/Juiced_5rEPO69pXg.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_5rEPO69pXg.jpg" %}
</figure>

It doesn't even have a game icon.

{% include screenshot.html thumbnail="/assets/img/posts/juiced-research/may-icons.jpg" style="natural" %}

Although this demo has 3 cars available by default, it also ships a 4th car -- **Toyota MR2**. In {{ sp_name }}, this car has been made selectable.
Since I included this car in the mod package, it's now also available in later demos.

{% include screenshot.html id="toyota-mr2" link="/assets/img/posts/juiced-research/screens/Juiced_5eOw0UtSdM.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_5eOw0UtSdM.jpg"
        caption="Fonts don't scale either." %}

Unlike later demos, a <kbd><samp>Videos</samp></kbd> menu entry is available, with 3 small game teasers available -- although their appearance is slightly glitchy.

{% include screenshot.html link="/assets/img/posts/juiced-research/screens/Juiced_RqI3nRZ7o3.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_RqI3nRZ7o3.jpg" %}

{{ sp_name }} unlocks all shipped content in this demo, but there is a twist -- **in this build, the Sprint races work differently.** Rather than taking place on the straight section of the road,
much like drag races in other games (or Sprints in the final version of the game), these Sprints take place on small sections of regular tracks.
Considering that the game mode works identically to the final game (including forced manual shifting), I initially thought it was a bug. However, as found by {{ eagle_link }},
the final game includes unused minimaps for the Sprint races, and one of those minimaps closely resembles a playable track in this build.
It's just speculation, but it is possible that this demo represents a work-in-progress redesign of this game mode,
or it was just not finalized yet and used sections of the existing tracks as placeholders.

<figure class="media-container small">
{% include screenshot.html link="/assets/img/posts/juiced-research/aw.png" %}
{% include screenshot.html link="/assets/img/posts/juiced-research/CH1.png" %}
{% include screenshot.html link="/assets/img/posts/juiced-research/eng.png" %}
<figcaption markdown="span">Credits: {{ eagle_link }}</figcaption>
</figure>

I also have **not** fixed the crashes exclusive to this demo, so it is barely playable even patched. IMO this demo is not worth the effort, except for its rarity.

## June 2004 Demo

* Compilation date: **Wednesday, 23 June 2004 09:22:06**
* Download links: {{ june_2004_download_links }}; the installer doesn't allow picking an installation directory by default, [see below](#acclaim-installers) for a fix
* Worth testing: **NO**{:style="color:red"} (just get the July demo)

This build is a prototype demo retrieved from [Duffy's Dreamcast Collection](https://www.sega-dreamcast-info-games-preservation.com/en/duffy-s-collection-partie-2-acclaim-prototype-iso)
-- a bunch of prototypes from an ex-Acclaim beta tester **Duffy**, who passed away recently. Compared to the May demo, it's much more polished -- all issues I mentioned
(except for the texts not scaling to resolution) have been fixed. Comparison screenshots show several obvious differences.

<figure class="media-container small">
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_laDHj6Gwf9.jpg" left-label="May 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_pkIBVvtInu.jpg" right-label="June 2004" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_y3tpqe9WVS.jpg" left-label="May 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_XJc5v9apQw.jpg" right-label="June 2004" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_YGROHPWmIP.jpg" left-label="May 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_XOMk76rR89.jpg" right-label="June 2004" %}
</figure>

Based on my observations, I could identify the following differences between May and June builds:
* The title screen is slightly different, with <kbd><samp>PRESS ENTER</samp></kbd> relocated to the center of the screen.
* New intro copyright disclaimers.
* Car select UI has been rearranged slightly.
* New keyboard button prompts.
* Car names have been changed.
* Reflections in the car select screen are slightly toned down.
* Videos have been cut.
* Sprint races (unlocked by {{ sp_name }}) now work like in the final game.
* <kbd><samp>Exit Demo</samp></kbd> option has been added.
* Race HUD has been slightly changed not to feature black backgrounds.
* For some reason, motion blur is extremely overdone in this build.
* Pre-race cutscenes have different camera angles.
* Tire smoke is visible, while it was absent from the May build.
* The configurator app is slightly more fleshed out, with Shader Model 2.0 added. However, that introduced a bug where the application requires the Windows XP SP2 compatibility mode to run
  (fixed in SilentPatch).
* Controls can now be remapped, although instead of an in-game remapper, [DirectInput Mapper](https://community.pcgamingwiki.com/files/file/58-microsoft-directinput-mapper)
  ((in)famously removed from Windows Vista and newer) is used. The game must also be running in the windowed mode, or else it obscures the mapper window.

{% include screenshot.html link="/assets/img/posts/juiced-research/screens/Juiced_JGSrHwJ2h9.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_JGSrHwJ2h9.jpg" %}

Aside from the compatibility issues of the configurator app, this build also introduced a peculiar issue where the HUD flickers randomly. Since the July build was also affected,
I will explain this bug in detail [below](#acclaim-silentpatch-fixes).

## July 2004 Demo

* Compilation date: **Friday, 2 July 2004 17:00:06**
* Download links: {{ july_2004_download_links }}; the installer doesn't allow picking an installation directory by default, [see below](#acclaim-installers) for a fix
* Worth testing: **YES**{:style="color:green"}

This demo is similar to the June build, but with a few additional fixes:
* Texts are now scaling to resolution.
* The main menu has been slightly rearranged.
* Excessive motion blur from the June build appears to have been toned down.
* The bloom effect when activating nitrous is noticeably ramped up.
* Lighting (especially on cars) seems to be a little darker, as evidenced by the comparison screenshots.

<figure class="media-container small">
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_5rEPO69pXg.jpg" left-label="May 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_YR3rVipjAJ.jpg" right-label="July 2004" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_JGSrHwJ2h9.jpg" left-label="June 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_VcNQfgLy7o.jpg" right-label="July 2004" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_3pPERfVUUc.jpg" left-label="June 2004"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_9byolLFsSJ.jpg" right-label="July 2004"
                id="june-july-lighting" %}
</figure>

## Fixes included in {{ sp_name }} {#acclaim-silentpatch-fixes}

Since I want those Acclaim demos (especially the latest one) to be enjoyable to their fullest, SilentPatch includes several fixes for the most severe issues present in those builds.
As they are demos, they are inherently a work-in-progress product and so most of those issues shouldn't come as a surprise, for that reason I also have not fixed any gameplay shortcomings.
I want those demos to be playable, but I don't want to distort their "history" by "completing" them. Here are the highlights of this release:

* All shipped content has been unlocked. This increases the amount of in-game content from 1 route in the Race mode and 3 selectable cars to:
  * 4 selectable cars ([Toyota MR2 from the May demo](#toyota-mr2) has been added and made usable).
  * 4 routes in the Race mode + reverse variants + 1 Point-to-Point race.
  * Sprint race.
  * Showoff (Cruise) mode.
  * Solo mode.

  Additionally, the users may enable **all** menus with an INI option but do note that most menus are not finished and will softlock.

* 3 teaser videos from the May demo have been included and re-enabled.

* The laps limit has been lifted from 2 to 6, like in the console prototype builds from a similar timeframe.

* In night and wet races, the limit of on-track cars has been lifted from 4 to 6. This appears to have been a purely performance-focused constraint,
  and with modern PCs, we can easily brute force through it without any noticeable issues.


* {: #acclaim-widescreen} Widescreen from the console builds has been re-enabled and further improved. The default widescreen option slightly distorts the aspect ratio and appears horizontally squashed
  compared to 4:3. SilentPatch corrects this and additionally supports arbitrary aspect ratios, which means ultra widescreen now looks as expected.
  The configuration application can now also select widescreen resolutions when in windowed mode.
  {% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_RlmB8wyX8f.jpg" left-label="Stock"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_44IkcUPlm6.jpg" right-label="SilentPatch" %}

* The default driver name `Player1` can now be overridden via the INI file.

* All known compatibility issues have been fixed. `JuicedConfig.exe` no longer needs Windows XP SP2 compatibility mode to run.

* May 2004 Demo can now be quit by pressing <kbd>Alt</kbd> + <kbd>F4</kbd>.

* All game settings have been moved from registry to `settings.ini`. This makes demos fully portable and prevents them from overwriting
  each other's settings.

* June and July demos introduced a bug where the UI elements flicker randomly, with seemingly no fix.
  {% include figures/video.html link="/assets/img/posts/juiced-research/juiced-flicker.mp4" attributes="controls loop"
      caption="In-game elements can also flicker like this (or worse), making for a miserable experience." %}
  I initially suspected this is similar to an issue present in [Scarface]({% post_url 2020-03-29-silentpatch-scarface %}) (this is the second post in
  a row where Scarface gets a shout-out), and to make matters worse, applying an identical fix (removing the `D3DLOCK_DISCARD` flag when locking the vertex buffers)
  helped. However, that turned out to be a red herring, as the game's usage of this flag was correct. I later identified this issue to be a **potential compiler/optimizer bug!**
  [x86 calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions) have strict requirements regarding the state of the FPU...
  > The x87 floating point registers ST0 to ST7 must be empty (popped or freed) when calling a new function, **and ST1 to ST7 must be empty on exiting a function.**

  ...however, the game's code ignores this requirement when calling into one of the Direct3D 9 functions, either by a mistake in handwritten assembly code (unlikely)
  or due to a compiler bug:
  ```nasm
  mov     esi, eax
  mov     dword ptr [eax+24h], 1
  call    LockVertexBuffer
  fld     st(2) ; The code assumes this value was not changed by the above
                ; function, but this is not guaranteed to be the case!
  mov     ecx, [ebp+0]
  ```
  I authored a fix where `LockVertexBuffer` saves and restores the entire FPU state, and lo and behold -- the issue is fixed.
  This is the first time I fixed a game issue that I suspect was caused by a compiler bug, but I'm not surprised too much;
  I've already encountered such bugs multiple times in my programming career outside of reverse engineering games.

* In-game music plays with crackles and pops in all 3 Acclaim demos. This bug, later fixed in THQ demos, occurs because
  the game requests more data to be loaded from the disc after playback reaches a specific point in the audio track.
  In the case of THQ demos, this happens when passing a mid-point of the 1-second-long chunk of loaded music, but in Acclaim demos this
  marker is set to **one byte** before the end of the track. This obviously doesn't allow the game to stream more data in time,
  and that results in broken music playback. In SilentPatch, I mirrored the change made to the 2005 demos.
  <figure class="media-container small">
  {% include figures/audio.html ogg="/assets/img/posts/juiced-research/music-stock.ogg" mp3="/assets/img/posts/juiced-research/music-stock.mp3"
              caption="By default, the music crackles quite a bit." %}
  {% include figures/audio.html ogg="/assets/img/posts/juiced-research/music-fixed.ogg" mp3="/assets/img/posts/juiced-research/music-fixed.mp3"
              caption="With SilentPatch, it sounds as expected." %}
  </figure>

***

* Last but not least, an issue I did **not** fix (as I said earlier, I decided against altering the work-in-progress state of those demos beyond
  the essential fixes), but I consider it worth mentioning anyway. For some strange reason, parts of the environment are darker when the HUD isn't displaying.
  This comparison is done with the HUD disabled via a hack, but you can replicate the same scenario by using a rearview camera (by default mapped to <kbd>Space</kbd>).
  Furthermore, after <kbd>Alt</kbd> + <kbd>Tab</kbd>, this issue vanishes and the environments are dark regardless of whether the HUD is drawn or not.
  I haven't looked into this issue with PIX, so I am not sure which of the two states is "correct", but in my opinion the darker state makes the affected objects
  (especially the car) blend with the rest of the environment better.
  {% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_KPTyoqw3g8.jpg" left-label="HUD"
                right="/assets/img/posts/juiced-research/screens/thumb/Juiced_2w2s8Ynrza.jpg" right-label="No HUD"
                caption="This looks somewhat similar to the [June/July comparison](#june-july-lighting)." %}

## Demo installer issues {#acclaim-installers}
{:.no_toc}

By default, June and July demos' installers don't include an option to change the installation directory and instead, they always install the game to
`C:\Program Files (x86)\Acclaim Entertainment\JuicedDemo`. Since these installers use InstallShield, I created a Transform file to re-enable
the Destination Folder screen.
{% include screenshot.html thumbnail="/assets/img/posts/juiced-research/msiexec_HaLbpb5KTv.png" style="natural" %}
I strongly recommend downloading it from [Downloads](#downloads) and running the installer via `run.bat`,
instead of installing them to Program Files -- it's not a good idea, especially with such older, UAC-unaware games and with SilentPatch
redirecting settings to the INI file.


# Chapter 3: THQ Demos

Just like with Acclaim, all 3 demos from THQ have content parity. However, this content has been entirely refocused and instead of
a free custom race form of the earlier demos, THQ demos are linear:
* The initial race puts the player in a Nissan Skyline in a night 1v1 race against a Toyota Supra.
  The player also gets an option to bet with their rival -- a mechanic also present in the Acclaim version of the game,
  but not covered by their demo at all.
* After the race, the player gets a chance to freely tune their Skyline.
* Once they are done, a second race against 3 opponents (this time set in the morning) starts.
* After the second race, the demo ends.

{% include screenshot.html link="/assets/img/posts/juiced-research/screens/jan-2005-tuning.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/jan-2005-tuning.jpg" %}

It's clear that this demo showcases the game better, as the player gets a taste of what the career mode looks like, and they can experiment with the game's tuning system
on their own, instead of relying on auto-mod from the Acclaim demo.

## January 2005 Demo

* Compilation date: **Friday, 28 January 2005 15:07:00**
* Download links: {{ january_2005_download_links }}
* Worth testing: **SOMEWHAT**{:style="color:DarkOrange"} (slightly different from the final game, runs with nearly no compatibility issues)

Out of the box, this demo will refuse to boot on PCs with more than 4 logical CPU cores (fixed in SilentPatch).
However, this demo does **not** exhibit the compatibility issues present in the final game -- that is, <kbd>Alt</kbd> + <kbd>Tab</kbd> does not crash the game
and the `Juiced requires virtual memory to be enabled` is not present.

This demo is also the only one to feature more than one executable -- `Juiced.exe` is compiled with SSE2 instructions, but there is also `Juiced_NOSSE2.exe`.
The final game doesn't ship multiple executables.

There isn't much to talk about in this version otherwise, as it's mostly identical to the final game.
However, while working on unlocking its content, I accidentally reached a semi-broken Career screen -- despite its brokenness,
its layout is distinctly different from the final game, more resembling a career screen from the Acclaim prototypes!

{% include screenshot.html link="/assets/img/posts/juiced-research/screens/jan-2005-career.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/jan-2005-career.jpg" %}

## April 2005 Demo (v2.0)

* Compilation date: **Thursday, 14 April 2005 15:54:25** (4 days before the full game)
* Download links: {{ april_2005_download_links }}
* Worth testing: **NO**{:style="color:Red"} (if you really want to try it, don't bother without installing a v2.1 patch)

Content-wise, this demo is fleshed out further, but on the technical side it only gets worse -- unlike the January demo,
this one includes all the incompatibilities of the final game 😕

<figure class="media-container small">
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/jan-2005-fonts.jpg" left-label="January 2005"
                right="/assets/img/posts/juiced-research/screens/thumb/apr-2005-fonts.jpg" right-label="April 2005" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/jan-2005-betting.jpg" left-label="January 2005"
                right="/assets/img/posts/juiced-research/screens/thumb/apr-2005-betting.jpg" right-label="April 2005" %}
{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/jan-2005-widescreen.jpg" left-label="January 2005"
                right="/assets/img/posts/juiced-research/screens/thumb/apr-2005-widescreen.jpg" right-label="April 2005" %}
</figure>

Generally, this demo appears to be identical to the final game, with all design locked in place.
Based on my observations, I could identify the following content differences between January and April builds:

* Copyrights have been updated from 2004 to 2005.
* Car reflections have been updated.
* Fonts and UI sounds have been replaced. As far as I know, the old UI sounds have later been used in [Juiced: Eliminator](https://en.wikipedia.org/wiki/Juiced:_Eliminator).
* Music in the garage screen has been updated to be different from the main menu music.
* Weird changes have been made to widescreen support -- in the January build, the game scaled properly to 16:9, but in this build (and the final game), scaling is incorrect!
  According to [PCGamingWiki](https://www.pcgamingwiki.com/wiki/Juiced#Widescreen_resolution), the Widescreen option in the full version
  of the game is for 16:10, not 16:9. I'm not sure why they changed it, and why they didn't leave both 16:9 and 16:10 as options instead.

## May 2005 Demo (v2.1)

* Compilation date: **Wednesday, 18 May 2005 09:13:12** (30 days after the full game, 51 days before patch v1.01)
* Download links: {{ may_2005_download_links }}; patches the above v2.0 demo to v2.1
* Worth testing: **SOMEWHAT**{:style="color:DarkOrange"} (if you **really** can't try the full game)

Officially, this patch exclusive for the demo version is supposed to only improve performance:

> Juiced by Juice Games - demo v2.0 -> v2.1 patch
>
> It has come to our attention that some people may have experienced performance
> problems with Version 2 of the Juiced PC Demo.
>
> THQ are pleased to announce that a patch to update Version 2 of the demo to
> Version 2.1.
>
> PLEASE NOTE THIS PATCH WILL UPDATE VERSION 2 OF THE PC DEMO ONLY.

However, there is more to it -- the demo patch was compiled **1 month** after the initial PC version of the full game,
and it also seems to include more changes later seen in the regional releases in Czechia, Poland, and Russia,
and possibly also some fixes later rolled out in a v1.01 patch.

<figure class="media-container small">
<figure markdown="1" class="fig-entry">
```nasm
mov [esp+34h+var_14], offset aControlsDx9ETx ; "controls_dx9_e.txt"
mov [esp+34h+var_10], offset aControlsDx9FTx ; "controls_dx9_f.txt"
mov [esp+34h+var_C], offset aControlsDx9GTx ; "controls_dx9_g.txt"
mov [esp+34h+var_8], offset aControlsDx9ITx ; "controls_dx9_i.txt"
mov [esp+34h+var_4], offset aControlsDx9STx ; "controls_dx9_s.txt"
```
<figcaption>April demo only supports FFIGS.</figcaption>
</figure>
<figure markdown="1" class="fig-entry">
```nasm
mov [esp+40h+var_20], offset aControlsDx9ETx ; "controls_dx9_e.txt"
mov [esp+40h+var_1C], offset aControlsDx9FTx ; "controls_dx9_f.txt"
mov [esp+40h+var_18], offset aControlsDx9GTx ; "controls_dx9_g.txt"
mov [esp+40h+var_14], offset aControlsDx9ITx ; "controls_dx9_i.txt"
mov [esp+40h+var_10], offset aControlsDx9STx ; "controls_dx9_s.txt"
mov [esp+40h+var_C], offset aControlsDx9CTx ; "controls_dx9_c.txt"
mov [esp+40h+var_8], offset aControlsDx9PTx ; "controls_dx9_p.txt"
mov [esp+40h+var_4], offset aControlsDx9RTx ; "controls_dx9_r.txt"
```
<figcaption>May demo supports FFIGS, Czech, Polish, and Russian!</figcaption>
</figure>
</figure>

But here's the catch -- while the demo's code supports the additional languages and even attempts to pick them by default based
on the user's system locale, they... don't ship the language files! The result is that on my OS with a Polish locale selected,
I was consistently crashing on startup and couldn't run this demo at all until I "reverted" support for those 3 languages with SilentPatch 🙃
This almost made me drop support for this patch until a trace with [Process Monitor](https://learn.microsoft.com/sysinternals/downloads/procmon)
revealed that the game tried to access `controls_dx9_p.txt` and failed. This, combined with the fact that the game booted fine on Windows Sandbox
(that did **not** use a Polish locale) proved that the issue lies there, and thus is trivially fixable by "cutting" those 3 languages from the demo. Phew.

## Fixes included in {{ sp_name }} {#thq-silentpatch-fixes}

* All shipped content has been unlocked. Since these demos don't include Custom Races, customization is done through the `SilentPatchJuicedDemo.ini` file
  and concerns only the second race. The following options are available:
  * 4 routes in the Race mode + reverse variants + 1 Point-to-Point race + its reverse variant.
  * Sprint race.
  * Showoff (Cruise) mode.
  * Solo mode.
  * Customizable time of day, weather, number of laps, and number of AI opponents.

  Additionally, the users may enable **all** menus with an INI option but do note that most menus are not finished and will softlock.

* The player's starter car can now be customized by editing the `scripts\CMSPlayersCrewCollection2.txt` file. The following cars
  are available: `gtr`, `nsx`, `supra`, `vette_zo6`, `viper`.
  {% include screenshot.html link="/assets/img/posts/juiced-research/screens/jan-2005-viper.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/jan-2005-viper.jpg" %}

* Demos have optionally been made endless. Instead of the game exiting after the second race, it returns to the garage and gives an option
  of tuning the car again and starting another race. Combined with the aforementioned content unlocks, this lets the player try multiple different
  routes and game modes in a single session, as the race configuration options in the INI file can be modified while the game is running.

* The default driver name `Player` can now be overridden via the INI file.

* A startup crash in the January 2005 demo occurring on PCs with more than 4 logical CPU cores has been fixed.

* `Juiced requires virtual memory to be enabled` error from the April and May 2005 demos has been fixed.

* Startup crashes in the May 2005 demo occurring when the OS locale is set to Czech, Polish or Russian have been fixed.

* `JuicedConfig.exe` no longer needs Windows XP SP2 compatibility mode or a Windows compatibility shim to run.
  This improves compatibility with environments where compatibility shims are not enabled by default, e.g. on Wine/Proton.

* All game settings have been moved from registry to `settings.ini`. This makes demos fully portable and prevents them from overwriting
  each other's settings.


# Chapter 4: PS2 Prototypes, briefly

As I mentioned earlier, many PS2 and Xbox prototypes of Acclaim's Juiced have surfaced online. Although they all come from the tail end
of the game's development under the original publisher, they seem to be slightly different from one another. However, comparing all these prototypes
in detail would be an enormous task, much bigger than the demo comparisons presented above (that already are quite lengthy). Most of the differences
are likely also purely technical and not that entertaining for a casual reader.

That said, during the course of the entirety of this research, I came across a few findings specifically in the PS2 prototypes
that warranted some attention, and I'm publishing them in the form of patches for the two prototypes that by the time of writing this
are available online -- {{ "2004-06-11" | date: page.date-format }} and {{ "2004-07-28" | date: page.date-format }} builds.

## 60 FPS

While the Xbox prototypes and the final game (on all platforms) target 60 FPS, both PS2 prototypes are locked to 30 FPS.
This patch lifts the FPS cap, allowing the game to hit 60 FPS. When using this cheat in PCSX2, the default configuration tailored for the final version
of Juiced prevents these prototypes from maintaining a stable 60 FPS, even with an overclocked emulated CPU.
For an optimal experience, several settings should be changed as follows.
**Please make sure to use Per-Game Settings to change those, as changing those settings globally is guaranteed to cause problems with other games,
including the final version of Juiced:**
* Set <kbd><samp>EE Cycle Rate</samp></kbd> to **130%**.
* Enable <kbd><samp>Enable Instant VU1</samp></kbd>.
* Disable <kbd><samp>Enable Game Fixes</samp></kbd> (in the <kbd><samp>Advanced</samp></kbd> tab).

## Progressive Scan

The {{ "2004-07-28" | date: page.date-format }} build and the final version of Juiced include an option to switch the game to use Progressive Scan
by holding **X**{:style="color:rgb(124, 178, 232);font-family:monospace, monospace"} + **△**{:style="color:rgb(64, 226, 160);font-family:monospace, monospace"},
while the {{ "2004-06-11" | date: page.date-format }} build doesn't implement this option yet. With this cheat, Progressive Scan is enabled also on this build.

## Fixed Widescreen

Just like I [mentioned earlier](#acclaim-widescreen), all Acclaim's versions of the game have slightly defective widescreen support and
the aspect ratio is "overcorrected", causing the image to be squashed. With this patch, the widescreen proportions match 4:3 perfectly,
the same as I did for PC demos.

{% include juxtapose.html left="/assets/img/posts/juiced-research/screens/thumb/Juiced_SLUS-20872_20231004174952.png" left-label="4:3"
            right="/assets/img/posts/juiced-research/screens/thumb/Juiced_SLUS-20872_20231004174845.jpg" right-label="16:9 (Stock)" %}

## DNAS Bypass

On the PlayStation 2, online multiplayer was protected by [Dynamic Network Authentication System (DNAS)](https://en.wikipedia.org/wiki/DNAS),
an authentication protocol that ensured pirated game copies couldn't access the online functionality.
Sony kept this service up for long after the PS2's end of life, but finally took it offline on {{ "2016-04-04" | date: page.date-format }},
leaving unmodified games unable to play online. As DNAS was not responsible for the actual online functionality, only for authentication,
DNAS Bypass codes have been created for various games to circumvent the authentication entirely. Thanks to the {{ ps2online_link }} project,
the final version of Juiced has a DNAS Bypass patch that allows people to play online through [OpenSpy](http://openspy.net/), but that patch didn't work for the prototypes.

With my DNAS Bypass, Acclaim prototypes can connect to OpenSpy and online play is possible just like in the final game! Prototypes and retail games see each other's lobbies,
but they cannot enter them -- so it is not possible to accidentally ruin someone else's fun by joining their game with the wrong version of the game.
My tests were also done only on the June build; July build can go online too, but I've not had much success creating a lobby.

{% include screenshot.html link="/assets/img/posts/juiced-research/screens/Juiced_SLUS-20872_20230921212557.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_SLUS-20872_20230921212557.jpg" %}

# Downloads {#downloads}

{{ f4mi_link }} has created a showcase of {{ sp_name }} and the improvements it makes to Acclaim's Juiced Demo -- check it out if you want to see the new content in action:
{% include video.html link="https://www.youtube.com/embed/4lQ76h8KEkI" %}

All known PC demos of Juiced, as well as {{ sp_name }} can be downloaded from *Mods & Patches*. Click here to head to the game's page directly: \\
<a href="{% link _games/juiced/juiced (demo).md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download Juiced Demos and {{ sp_name }}</a>

For patches targetting the PlayStation 2 prototypes, go here: \\
<a href="{% link _games/juiced/juiced-acclaim-ps2.md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Juiced (Acclaim, PS2) Downloads</a>

# Credits and acknowledgments

* {{ f4mi_link }} for researching the history of Juiced and making sure that my summary is accurate, and for preparing the showcase video
* {{ juiced_modding_community_link }} for helping me find and dissect those demos and for answering all of my many questions regarding the game

***
