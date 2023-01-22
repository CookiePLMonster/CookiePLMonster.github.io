---
layout: post
title: "Remastering Colin McRae Rally 3 with SilentPatch"
excerpt: "A fresh take on the classic rally game with widescreen support, high definition UI, and countless bug fixes."
thumbnail: "assets/img/posts/spcmr3/cmr3-img.jpg"
feature-img: "assets/img/posts/spcmr3/cmr3-img.jpg"
image: "assets/img/posts/spcmr3/cmr3-img.jpg"
game-series: "cmr-3"
date: 2023-01-15 16:15:00 +0100
twitter: {card: "summary_large_image"}
tags: [Releases, Articles]
juxtapose: true
---

_TL;DR - this article is longer than any other blog post I've published to date, so be ready for a long read. If you aren't currently
interested in a deep dive through the game's history, internals and fixes, **scroll down to the [Changelog and download](#changelog-and-download)
section for a download link.**_

***

*[Vert-]: Vertical Minus; a method for adjusting aspect ratio for widescreen by reducing vertical FOV
*[Hor+]: Horizontal Plus; a method for adjusting aspect ratio for widescreen by increasing horizontal FOV

* [Introduction](#introduction)
* [Chapter 1: In search of a perfect executable](#in-search-of-a-perfect-executable)
* [Chapter 2: Regional releases and their oddities](#regional-release-oddities)
  * [Polish (3 CD) release](#polish-release)
  * [Polish (2 CD) re-release](#polish-re-release)
  * [Czech release](#czech-release)
* [Chapter 3: Fixes, so many fixes](#fixes)
  * [Fixes & improvements](#fixes-fixes)
  * [New options](#fixes-new-options)
* [Chapter 4: The perfect remaster -- adding an HD interface](#hd-interface)
  * [Scaling issues](#scaling-issues)
  * [Font filtering](#font-filtering)
  * [Half pixel issues](#half-pixel-issues)
* [Chapter 5: Merging regional releases together](#merging-regional-releases)
* [Changelog and download](#changelog-and-download)
* [Credits and acknowledgments](#acknowledgments)

{% assign bekoha_link = "[Bekoha](https://twitter.com/Bek0ha){:target='_blank'}" %}
{% assign hd_ui_url = "https://bekoha.github.io/cmr3" %}
{% assign krusantusz_link = "[Krusantusz](https://twitter.com/KarolWjcik19){:target='_blank'}" %}
{% assign memorix_link = "[Memorix101](https://twitter.com/memorix101){:target='_blank'}" %}
{% assign ribshark_link = "[RibShark](https://twitter.com/RibShark){:target='_blank'}" %}
{% assign lostraniero_link = "[LoStraniero91](https://www.youtube.com/@LoStraniero91){:target='_blank'}" %}
{% assign pierre_terdiman_link = "[Pierre Terdiman](http://www.codercorner.com/blog){:target='_blank'}" %}
{% assign automaniak_link = "[AuToMaNiAk005](https://www.youtube.com/@AuToMaNiAk005){:target='_blank'}" %}

# Introduction {#introduction}

{{ "2022-10-25" | date: "%B %Y" }} was [the 20th anniversary of Colin McRae Rally 3](https://twitter.com/EASPORTSRally/status/1584889076762697730).
A little over two months later, I'm happy to reveal the biggest SilentPatch since GTA San Andreas.
In this release, developed together with {{ bekoha_link }}, we deliver more than just a set of fixes -- with full
widescreen support, numerous compatibility fixes, new technical features, Quality of Life improvements, and a scratch-made high definition
UI optimized for 4K displays, we bring an experience comparable to an unofficial remaster of this classic 2002 rally game.

Originally, this project didn't start as a SilentPatch. Instead, I only intended to document the different releases of the game,
but given the anniversary timing and the attention Colin McRae Rally 3 received around that time, it was hard to pass on an opportunity
to give it a new life, especially once Bekoha expressed interest in retouching the game's fonts and UI.

For this reason, this blog post details the entire journey -- from scavenging for different versions of the game,
documenting them, through the process of fixing the game, and finally merging regional releases together.
Feel free to take a break between chapters, as it's going to be a lot -- it's the longest post published on my blog to date.

This post may get technical at times, but don't get discouraged; I intend it to be clear and informative for everyone -- players, game developers, and reverse engineers.

***

But first, a few words about the game for the uninitiated. Colin McRae Rally 3 is a racing game from Codemasters, released originally
for the PS2 and Xbox on {{ "2002-10-25" | date: page.date-format }}, later ported to PC by Six by Nine Ltd.
and released there on {{ "2003-06-13" | date: page.date-format }}.[^cmr3-release-date] It was received well and was succeeded by two more sequels in 2003 and 2004
before the franchise moved on to a Colin McRae DiRT series.

Unlike Colin McRae Rally 2.0, where the game shined on PC, CMR3 was an enhanced console port. Nonetheless, I have fond memories from playing
this game as a kid (although they've blurred together with memories from CMR04 and CMR2005). Curiously, back in the day,
[this was considered a sub-par port](https://web.archive.org/web/20190404033201/https://arstechnica.com/civis/viewtopic.php?f=22&t=661429),
and some people did not enjoy the long wait for the PC port, especially since by then CMR04 was just a few months away from release.
I find this comment the most amusing...

> Unfortunately it's a sign of the times and it's sad to see Codemaster's, once big supporter's of the PC, becoming member's of the lazy developer's club.

...since it sounds like something that could have been said online in July 2022, not July 2003 -- I guess some things never change 😜

[^cmr3-release-date]: As per: <https://en.wikipedia.org/wiki/Colin_McRae_Rally_3>

# Chapter 1: In search of a perfect executable {#in-search-of-a-perfect-executable}

It's commonly known that DRM on retail discs sucked. The three leading DRM solutions all came with a varying level of breakage,
and these days, two of them are intentionally disabled by Windows; furthermore, one of those DRM solutions is so contrived
it can make a Windows 10/11 machine unbootable (shout out to TOCA Race Driver 2 & 3). Much like I did
[for the TOCA Race Driver games](https://twitter.com/__silent_/status/1547975239379718145), I wanted to know if the trilogy
of later Colin McRae Rally games were all released DRM-free somewhere:
* Colin McRae Rally 04 is easy -- much like TOCA Race Driver and TOCA Race Driver 2, [it was re-released in Italy by FX Interactive](http://redump.org/disc/60860/),
opting for "physical" DRM (ring on the disc's surface to make copying unreliable and time consuming) instead of a software solution.
* Colin McRae Rally 2005 was released DRM-free on GOG.com, so even though the game has since been delisted, getting a hold of the DRM-free executable is not hard.
* This left only Colin McRae Rally 3 in an unknown state, as at that time all CMR3 discs submitted to Redump had SecuROM DRM -- [except for the Polish release](http://redump.org/disc/93705/).

I initially brushed off that hint, since I thought this listing is incomplete or incorrect. After all, I own a Polish CMR3 release from back in the day -- it uses SafeDisc[^safedisc-antipiracy],
making it impossible to launch without workarounds or a no-CD executable, and it comes on **three** discs, while this listing only had two.

[^safedisc-antipiracy]: Integrated so poorly that the launch version [triggered its own anti-piracy](https://www.gry-online.pl/S030.asp?ID=3092), and the game required a hotfix to be playable 😂

However, turns out that this wasn't an error, as a later re-release of the game did indeed come on 2 CDs:

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Anyone around with this specific version of Colin McRae Rally 3? I suspect this 2x CD re-release (compared to a 3x CD original) might be DRM-free, or at least might contain just a simple CD check. <a href="https://t.co/n7MQIAuTmJ">pic.twitter.com/n7MQIAuTmJ</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1578800516523388928?ref_src=twsrc%5Etfw">October 8, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

With the help of {{ krusantusz_link }}, I got access to this executable for analysis. While it indeed is DRM-free, its usability with assets of the "international" version is
limited -- with the range of issues ranging from a hardcoded French co-driver (replaced with Polish in the actual release)...

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Turns out this release is indeed fully DRM-free, and its executable also works with an English version! Well, almost, and to get what&#39;s the catch you need to watch with sound on.<br><br>I hope it&#39;s patchable, as DRM-free exes &gt; no-CD exes all the way <a href="https://t.co/6bABq0Atvy">https://t.co/6bABq0Atvy</a> <a href="https://t.co/tinKdKicbR">pic.twitter.com/tinKdKicbR</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1578873780973473792?ref_src=twsrc%5Etfw">October 8, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

...various UI issues...

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-broken-pl-keyboard.png" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-broken-secrets-screen.png" %}
</div>

...through crashes on various screens, e.g. Telemetry and Controls. While salvageable, this means that the Polish release has received a non-trivial amount of code changes.

Shortly after that, I also bought my own second hand copy of the eXtra Klasyka release, so now I'm a proud owner of two CMR3 PL copies:
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-copies.jpg" caption="Because why not?" %}

If the rabbit hole of different versions ended here, this would have been a story of how I created an international DRM-free executable by "internationalizing" the Polish one
and removing CD Projekt's modifications to it (more on that later). There **is** one more version, though -- CMR3 was also re-released in Germany on a single DVD. As SecuROM worked with DVDs
just fine, we expected this release to have DRM identical to the original -- however, [Memorix101 proved us wrong](https://twitter.com/memorix101/status/1581632281311334400?s=20).
Together with {{ ribshark_link }} we tracked down a copy for sale and [submitted its metadata to Redump](http://redump.org/disc/98620/) -- at which point it became clear
that this re-release is so late, its disc was mastered after [the release of Colin McRae Rally 2005](https://en.wikipedia.org/wiki/Colin_McRae_Rally_2005)!

At this point, I've already been "internationalizing" the Polish executable, so this work was technically rendered useless (for now). Regardless, thanks to the German version,
we got *The Perfect CMR3 Version* we wanted -- an easy to install, DRM-free, future proof release that ensures the game remains accessible indefinitely.
My initial goal was done.

# Chapter 2: Regional releases and their oddities {#regional-release-oddities}

Note: Although the DVD version was only sold in Germany, its content is identical to the international release,
so I don't consider it a regional release per se.

## Polish (3 CD) release {#polish-release}
As mentioned earlier, the Polish release is more than a straightforward text and speech translation. Aside from making Polish the only
language in the game, CD Projekt (or Codemasters) introduced several changes to the international version, localizing the game further:

* Localized onscreen keyboard and keyboard typing -- the international version displays a basic keyboard regardless of a selected in-game language:
{% include juxtapose.html left="/assets/img/posts/spcmr3/cmr3-english-keyboard.png" left-label="International"
                right="/assets/img/posts/spcmr3/cmr3-polish-keyboard.png" right-label="Polish"
                caption="These screenshots are from a patched game, but you get the idea." %}

* Menu cubes received new graphics to match Polish wording:
<div class="screenshot-container small">
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_NP59FE2Oim.png" left-label="International"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_Rea1oHQcc6.png" right-label="Polish"
                start-position="75%" %}
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_maqdLz06dg.png" left-label="International"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_FhPHLUBq8f.png" right-label="Polish"
                start-position="75%" %}
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_ccriJQ3022.png" left-label="International"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_mByVxA6C4k.png" right-label="Polish"
                start-position="75%" caption="Polish cubes are exceptionally rude." %}
</div>

* The Secrets screen was modified to refer to CD Projekt's resources rather than the Codemasters' ones -- this is what resulted in a previously shown "Call your Germany"
issue if a PL executable is used with English localization:

{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_s6Ph0TjTCs.png" left-label="International"
                right="/assets/img/posts/spcmr3/Rally_3PC_bdpquWzrTJ.png" right-label="Polish" %}

* By the way, have you noticed how Polish fonts are spaced further apart than international ones? Odd change, but I assume they had a reason to do so.
* Polish introduces 40 new localization strings for texts that were previously hardcoded to English. This is what caused an unpatched PL executable to crash with English localization.
* As other languages have been removed, the Language screen is renamed to "Co-driver's voice" and gives you a choice between Nicky Grist, the original English co-driver,
  and Janusz Kulig, the voice of a popular Polish rally driver.

## Polish (2 CD) re-release {#polish-re-release}
Around a year after the original release, Colin McRae Rally 3 was re-released in Poland under an eXtra Klasyka label (as you may have noticed above).
Aside from being completely DRM-free, it also ships on 2 discs instead of 3. While I initially thought this is solely due to better compression,
this isn't the case -- the changes in this release are:
* The removal of Nicky Grist as a selectable co-driver
* The change of the Polish co-driver's voice from Janusz Kulig to Janusz Wituch

I couldn't find any in-game comparisons online [other than the Polish dubbing wiki](https://polski-dubbing.fandom.com/wiki/Colin_McRae_Rally_3),
so here is one:

<div class="video-container" id="polish-codrivers">
<iframe src="https://www.youtube.com/embed/hiMuxipp5X4" frameborder="0" allowfullscreen></iframe>
</div>

The removal of Nicky Grist explains why the game was now shipped on 2 CDs -- while localized co-drivers only use one-shot samples that
are played at specific triggers during the stage, Nicky Grist's pace notes are full audio recordings, created for each stage individually.
This makes Grist's notes sound much more natural than the other co-drivers, at the cost of much higher file size -- while each localized
co-driver is typically between 1.5 MB and 2 MB in size, Grist's pace notes are 435 MB!

What about Janusz Kulig, though? We will of course never know for sure if this change was dictated by licensing,
but one more plausible reason may be a little clearer for those familiar with the Polish rallying scene.
For those unfamiliar, it's best to show it on a timeline of what I **think** has happened:

1. **{{ "2003-06-26" | date: page.date-format }}** - The original PL Colin McRae Rally 3 featuring Janusz Kulig gets released.[^pl-release]
2. **{{ "2004-02-13" | date: page.date-format }}** - Janusz Kulig, a Polish rally driver, dies in a road accident after his car collides with a train on a level crossing.[^kulig-date]
3. **After {{ "2004-04-01" | date: "%B %Y" }}** - Colin McRae Rally 3 gets re-released in eXtra Klasyka, featuring Janusz Wituch -- a prolific voice actor, also starring
   in TOCA Race Driver and TOCA Race Driver 2.[^pl-release] [^klasyka-release]

While there is no definite proof to support that claim, it seems reasonably likely that CD Projekt quickly opted for a new co-driver after Kulig's death.
Their choice to feature Janusz Wituch may or may not have been related to the fact he was presumably recording lines for TOCA Race Driver 2 around that time -- as
it was released in Poland on {{ "2004-06-24" | date: page.date-format }}.[^toca2-release]

[^pl-release]: As per: <https://polski-dubbing.fandom.com/wiki/Colin_McRae_Rally_3>
[^kulig-date]: As per: <https://en.wikipedia.org/wiki/Janusz_Kulig>
[^klasyka-release]: As per the compilation date of the Polish DRM-free executable: <https://twitter.com/__silent_/status/1579400184810770432>
[^toca2-release]: As per: <https://polski-dubbing.fandom.com/wiki/ToCA_Race_Driver_2>

## Czech release {#czech-release}
A Czech release, published by CD Projekt, also exists -- albeit the details on it are sparse:
<div align="center">
<blockquote class="twitter-tweet" data-theme="light"><p lang="en" dir="ltr">Let&#39;s see if I can once again seek help through Twitter - do any of you own this? A Czech release of Colin McRae Rally 3. <a href="https://t.co/M2CFIqeCZN">https://t.co/M2CFIqeCZN</a> <a href="https://t.co/fDD4LSOlIz">pic.twitter.com/fDD4LSOlIz</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1588315889228599296?ref_src=twsrc%5Etfw">November 3, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

Albeit much like the Polish release it was released by CD Projekt in eXtra Klasika, I don't know if it ever was released outside of it (it likely was, though).
From the technical side, this Czech release is much less interesting than the Polish one -- compiled on {{ "2004-08-31" | date: page.date-format }},
it's not a special version but rather a translated international release replacing Spanish with Czech. None of the changes from CD Projekt are present in this release,
although it's clear that it must have been translated from Polish, not from English -- as the Czech translation file contains (now unused) strings introduced in the Polish release!

That said, there **is** something interesting about this release, and I only noticed it during the final tests of SilentPatch -- although the contents of the Czech
executable appear to be identical to the international executable, it has at least one unique UI bug, not present anywhere else! I have no idea how this happened,
but the results screens for time trials are completely broken in this release.[^sp-czech-fix]

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_Kuqw351FSw.png" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_fHCSJQmaYu.png" %}
</div>

I'm disappointed, as this screen was not even changed for the localized release -- it's a completely unwarranted regression.

[^sp-czech-fix]: Of course, SilentPatch fixes those, but still 😥

# Chapter 3: Fixes, so many fixes {#fixes}

In this section, I want to highlight the most interesting and unusual improvements present in the patch. This is **not** a full changelog -- for that,
refer to [**Changelog and download**](#changelog-and-download).

## Fixes & improvements {#fixes-fixes}

{: #fix-widescreen}
Console versions of CMR3 included a Widescreen option in Graphics Options, switching the aspect ratio from 4:3 to 16:9. While this option is gone from the PC versions,
it's still functional -- it's just that this option is underwhelming to begin with (also in the console versions), as it only corrects the 3D aspect ratio,
and the only UI element it corrects is the co-driver arrow. That said, it's not the worst, as it opts to fix the aspect ratio by increasing the horizontal FOV,
rather than by shrinking it vertically:

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_F84XcsPYJ9.jpg" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_mSVB76OLLL.jpg" %}
</div>

Curiously, the PC demo **did** list 16:9 resolutions, unlike the full version of the game -- but unlike the console versions, it is Vert-;
the co-driver arrow also appears to be broken. In my opinion, it's possible that because of issues like this it was decided that the full
version should limit the available options:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-demo-ws.jpg" %}

SilentPatch doesn't rely on the stock widescreen support at all -- instead, much like in
[SilentPatch for Colin McRae Rally 2.0]({% link _games/cmr/cmr-2.0.md %}#silentpatch){:target="_blank"}, I scale the game to arbitrary aspect ratios.
The entire UI and menus are positioned dynamically, ensuring that everything looks consistent regardless of resolution. This required an obscene amount of work,
as literally all the UI and menus had their layouts designed with a constant 4:3 aspect ratio -- therefore, SilentPatch takes control of nearly all the UI and menus
to keep elements aligned consistently regardless of the aspect ratio:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-wide.jpg" caption="W I D E" style="natural" %}

For more screenshots showcasing widescreen support, check [the next chapter](#hd-interface).

***

{: #fix-sun-colors}
The PC version of Colin McRae Rally 3 had a strange bug where [the sun would flash in random colors](https://www.youtube.com/watch?v=3ci8sFPCLpU){:target="_blank"}
(**WARNING:** rapidly flashing colors) if the FSAA (anti-aliasing) option was enabled. This happens regardless of whether anti-aliasing is enabled in-game, or forced externally;
dgVoodoo would also not help resolve it, proving that it's **not** a Direct3D 9 bug.

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-sun1.jpg" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-sun2.jpg" %}
</div>

I tracked down this issue to the game's occlusion queries that would return values much higher than what the game had expected when multisampling is enabled
(due to queries returning the number of **samples**, not **pixels**).
I find it hard to blame the developers for this, as even the official Microsoft docs got it wrong! Since then,
I have [submitted a pull request to correct the docs](https://github.com/MicrosoftDocs/win32/pull/1388){:target="_blank"}, and my proof in form of a fix for CMR3
was enough for the change to be accepted 😃 This link also includes a more technical writeup on this issue, in case you want to learn more about it.

Interestingly, this bug has been "fixed" officially in the sequels, but I was able to verify that it's not fixed "properly"[^spcmr04] -- instead of accounting for
the value of multisampling, the game now clamps the result of the occlusion query to `(0.0 - 1.0)`. On one hand, this prevents the sun from being miscolored;
on the other hand, sun occlusion is now wrong with multisampling enabled, which means the sun visibility increases quicker the higher the multisampling value is.

[^spcmr04]: Finding reasons to work on more patches even before this one is finalized 🙄

***

{: #fix-sun-hitch}
This isn't the only issue related to the sun rendering -- aside from broken colors, the sun occlusion would cause a consistent and noticeable hitch every time
the sun would either appear on screen or go off screen:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-frametime-bad.jpg" style="natural" %}

This bug, fixed only in Colin McRae Rally 2005, is caused by the game waiting for the sun occlusion query to return its results as soon as it's finished.
I don't need to provide pseudocode, as the code flow looks nearly identical to
[this Query State sample code from MSDN](https://learn.microsoft.com/en-us/windows/win32/direct3d9/queries#check-the-query-state-and-get-the-answer-to-the-query){:target="_blank"}.
The important memo that the game ignores goes as follows (emphasis mine):

> Note that applications should pay special attention to the large cost associated with flushing the command buffer because this causes the operating system
> to switch into kernel mode, thus incurring a sizeable performance penalty. **Applications should also be aware of wasting CPU cycles by waiting for queries to complete.**
>
> Queries are an optimization to be used during rendering to increase performance. **Therefore, it is not beneficial to spend time waiting for a query to finish.**
> If a query is issued and if the results are not yet ready by the time the application checks for them, the attempt at optimizing did
> not succeed and rendering should continue as normal.

In this case, the game waits for the query to finish **twice per frame**, therefore forcibly syncing the CPU with the GPU two times per frame for no reason.
With this in mind, it's strange that this hitch isn't more consistent than that -- the sync is done every frame, and so technically it should be blocking each time.
This is exactly what happens when dgVoodoo is used to make the game use Direct3D 11, but I couldn't get it to ever happen in Direct3D 9 -- perhaps due to a runtime
or a driver level optimization/hack:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-frametime-d3d11.jpg" style="natural"
  caption="These timings are even worse than by default, but in a way, they also make \"more sense\"." %}

The fix is trivial in theory, but a little harder to implement -- instead of always waiting for the latest result, the game should keep the old sun
occlusion data (and not start another query) for as long as the new result is not ready. This means that the value of the sun occlusion (and therefore, its brightness)
lags behind the camera by 2-3 frames. However, in practice this is not noticeable during gameplay, and resolves any hitches completely:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-frametime-good.jpg" style="natural" caption="The stutter struggle is no more." %}

*Something I only noticed just now when writing this post: I don't know if the huge difference in CPU9 and CPU11 usage is related to this fix.
However, it likely is -- the old code essentially included a CPU spin lock waiting for the GPU, and the quote from the docs I included above specifically
points out "wasting CPU cycles by waiting for queries to complete".*

***

{: #fix-shadows}
Thought we're done with issues caused by anti-aliasing? So did I, but as it turns out -- I was wrong.

Car shadows in CMR3 are simple but effective. They are essentially rendered in two phases:
1. Render the car from the sun's perspective, with depth testing and writing disabled, and with no color -- always drawing full white.
2. Take the 256x256 car shadow render target, downsample it to a smaller 128x128 target, and then upscale it again to achieve a blur effect. Repeat this step *n* times (**8** in the stock CMR3).

Although the effect isn't complex, it seemingly breaks with anti-aliasing enabled -- upon starting the game with FSAA, shadows were there but they were too sharp;
even worse, changing the display mode with FSAA enabled would make the shadow vanish entirely for that game session:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-shadow-comparison.png"
    caption="From left to right - Shadows without FSAA (looking correct), shadows with FSAA (too sharp), shadows after changing graphics options (not there at all)." %}

Turns out the issue lies in the "softening" pass. In theory, both shadow passes should be performed with depth test and depth write disabled;
this means that all draws should go through regardless of depth, and depth should not be updated by these draws.
Although the game sets up the depth states for shadow rendering correctly, an error in the 2D drawing functions made downsampling perform with a depth test enabled.[^gta-sa-sun]
Furthermore, in cases where a render target has no depth buffer associated with it, the game's graphics engine uses a fallback instead and binds the backbuffer's depth buffer!
Therefore, downsample draws used this as depth:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-shadow-depth.jpg"
    caption="You don't have to know what a depth buffer is to realize that this looks nothing like a car shadow." %}

In theory, this should only make draws fail if the top left part of the screen was obscured (making the depth test fail),
but with FSAA it gets worse since it resulted in matching a non-multisampled shadow buffer with a multisampled depth buffer. I don't know exactly if D3D9
is required to handle this mismatch correctly, but seeing how this can break shadows in multiple ways -- I suspect the results here are undefined.

Those familiar with GTA San Andreas might have a déjà vu, as [this game had an identical bug](https://gtaforums.com/topic/556386-relsa-multi-sampling-fix/)
affecting mirrors.

SilentPatch fixes this issue and goes a step further -- admittedly, those "sharp shadows" look kind of nice, but at the same time, I didn't want to disable
the softening pass entirely. Thankfully, Colin McRae Rally 2005 reduces the number of soften passes from 8 to 2, making shadows a little sharper.
I "backported" this change to Colin McRae Rally 3, making shadows a little more defined:

{% include juxtapose.html left="/assets/img/posts/spcmr3/cmr3-soft-shadows.jpg" left-label="Stock (Soft)"
                right="/assets/img/posts/spcmr3/cmr3-sharp-shadows.jpg" right-label="SilentPatch (Sharper)" %}

If you prefer to keep the stock, blurrier shadows, this change can be disabled from the `SilentPatchCMR3.ini` file -- by adding these lines at the very bottom of the file:

```ini
[Advanced]
SHARPER_SHADOWS=0
```

[^gta-sa-sun]: Sounds very similar to how the sun lens flare was broken in the PC version of GTA San Andreas, right?

***

{: #fix-water}
A few stages in CMR3 run next to lakes or across rivers. At the highest details, those come with a nice cubemap-based reflection and a subtle animation,
producing an appearance of a reflective, moving water surface. However, on PC those reflections don't always look the same:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-water-comparison.png" caption="From left to right - normal water, water after changing graphics options, water after Alt+Tab." %}

Depending on your actions, reflections may appear darker or even be completely black. I investigated this issue in detail, and it is caused not by one,
but **three** separate bugs! While one of them is a nitpick and may not even affect visuals, the other two are worth covering.

Presumably for performance reasons, the reflection cubemap is rendered only once, and it contains the sky and the horizon. This creates an issue during a device lost event,
i.e. when minimizing a fullscreen game window -- historically, a device lost event invalidates all render targets, so they need to be recreated after restoring
the game window. CMR3 is aware of that and gracefully recreates most render targets -- but not the reflection cubemap! This results in the reflection being pitch black,
making the water look horrendous. Making the game re-render the reflection after a device lost resolves the issue.

The other issue is also related to the device lost event, but it happens when the device resets (either due to Alt+Tab or a display mode change) outside of the race.
Since reflections are rendered at the start of the race, they should be unaffected by a reset in menus and render just fine. However, they are rendered slightly miscolored:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-water-reflections.png" style="natural"
    caption="Left - reflections rendered correctly, right - miscolored reflections after a device reset." %}

Because of the one-shot nature of those reflections (and, of course, making them re-render every frame "fixes" this bug), it was extremely hard to catch on a graphics capture.
However, once done, PIX provided a hint -- one of the lighting render states is different between the "good" reflection render and a "bad" one:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-reflection-renderstates.png" style="natural"
    caption="Left - correct reflections, right - miscolored reflections." %}

This essentially means that the scene is rendered to the cubemap with incorrect, possibly unpredictable, lighting -- but why? The game code correctly sets the emissive
source before rendering the cubemap, and yet it's still wrong.

The answer is slightly complicated, and it boils down to **cache coherency**. CMR3's rendering engine has a layer of abstraction over Direct3D 9 designed to cache
the state the game wants to put the rendering pipeline at, and ensures that any state changes call reach D3D9 only when necessary. However, sometimes the game cache
needs to be evicted or updated, as the D3D9 runtime discards its state. One such event is... the device reset (emphasis mine):

> Calling IDirect3DDevice9::Reset causes all texture memory surfaces to be lost, managed textures to be flushed from video memory, **and all state information to be lost.**

The developers behind a PC port of CMR3 were aware of this, so the game submits **all** cached render states to D3D9 again after a device reset,
therefore making sure that the runtime state matches what the game expects. Except... a few device states have been missed! Those are:

```
D3DSAMP_BORDERCOLOR - for all 8 samplers
D3DRS_EMISSIVEMATERIALSOURCE
D3DRS_BLENDOP
```

While I don't know if the other two are ever used (despite being cached), `D3DRS_EMISSIVEMATERIALSOURCE` is the exact render state that is incorrect when
the reflections are dark. The fact they were not updated after a device reset means that the game thought the D3D9 runtime is in a different state
than it truly is, and thus it's not setting the render state if it thought it's "pointless" -- hence the state cache losing coherency.

Fixing the Reset function to correctly reconcile those 3 missing states fixes the issue, so now water looks the same at all times:

{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_QIF2GtpZGv.jpg" caption="This might not be Far Cry, but the water still looks nice." %}

***

{: #fix-environment-map}
If you've played CMR3 on PlayStation 2 or watched any footage of it, you may have noticed that the game looked a little more vibrant there,
most prominently when it comes to car reflections. Albeit present on PC and Xbox, they always seemed a little dull. To verify, I ran the same car and stage on PC
and in the PCSX2 emulator, and pulled the reflection data before and after it's been mapped on a sphere:
<div class="screenshot-container natural">
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-ps2-ref.png" caption="PlayStation 2; 512x512 reflection, 128x128 sphere" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-pc-stock-ref.png" caption="PC (stock); 256x256 reflection & sphere" %}
</div>

They have clearly been rendered differently, but the most noticeable difference is in the sky -- PS2's reflection has a normal sky,
while on PC it's always a grey box, except for night stages.

PS2 reflections are rendered in a really simple way:
1. Take the entire rendered frame up to the point of drawing reflections (that's why the car shadow is present on the reflection).
2. Project that frame buffer on a sphere drawn to a separate render target.
3. Render the lens flare, if applicable.

PC opts for a more involved solution:
1. Clear a separate render target to grey, unless it's a night stage. Oddly enough, instead of using a camera clear, this is done by drawing a rectangle spanning the entire render target -- no idea why.
2. If it's a night stage, render the sky.
3. Render most of the scene again with a very low draw distance.
4. Project that on a sphere drawn to yet another render target.
5. Render the lens flare, if applicable.

At first, it might seem like the PC reflections are done better, but I believe this change was made purely for technical, not visual, reasons.
Unlike on PS2, on PC taking a frame "rendered up to a specific point" is not trivial, especially with older rendering APIs like Direct3D 9.
Most games from the era render directly to a back buffer, and using that surface as an input resource for another draw (to project it on a sphere)
is virtually impossible without copying it, which can be a costly and/or memory intensive operation.

That's not to say that doing it the PS2 way is impossible, of course -- CMR3 could have rendered to a separate render target that is simultaneously
a render target and a texture. That does the trick, but comes with a few disadvantages:
* A color target + depth target the size of a screen is required, which can take a lot of precious VRAM.
* It is not possible to create a resource that is simultaneously multisampled, can be rendered to, and bound as an input resource. To keep multisampling,
  **yet another** intermediate render target would be required.

Neither of those two is an issue for modern games (I implemented this exact thing in another game just a few months ago) -- but the situation in 2003,
when you only had 32-64 MB VRAM to use, was likely very different.

What about the sky on PC, however? Once again it's hard to say, but it is possibly a performance optimization, allowing reflections to draw less.
Curiously, split-screen uses a full sky in reflections -- which I found peculiar until I remembered that the Xbox version uses identical reflections
**and** that split-screen on consoles runs at 30 FPS. If this truly was a performance optimization, then it may not have been needed when the target frame rate is lower.

For SilentPatch, I went ahead and enabled sky rendering for reflections at all times:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-pc-sp-ref.png" caption="PC (with SilentPatch); 256x256 reflection & sphere" style="natural" %}

Not only does this change make the car reflections more vibrant, but it also "fixes" the TV displays in cutscenes -- as they reuse the reflection map,
they now display the sky correctly!

<div class="screenshot-container">
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_GTMDAOirDs.jpg" left-label="Stock"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_qooRyN7dkN.jpg" right-label="SilentPatch" %}
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_baj8DEkpAw.jpg" left-label="Stock"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_oCjhhdT7ja.jpg" right-label="SilentPatch" %}
</div>

If for some reason you prefer the stock reflections, this change can be disabled from the `SilentPatchCMR3.ini` file -- by adding these lines at the very bottom of the file:

```ini
[Advanced]
ENVMAP_SKY=0
```

***

{: #fix-lines-width}
(In)famously, Direct3D has no option of altering the line thickness of draws; therefore, line draws are always 1px thick. CMR3 uses lines widely (pun
unintended) -- they are used both in 2D (in menus and graphs), and in 3D (for antennas). This wasn't an issue on consoles, as well as on PC when played
at 640x480 -- but the larger the selected resolution is, the more noticeable it becomes that those lines become relatively thin and hard to read.
SilentPatch resolves this issue by implementing line thickness:

<div class="screenshot-container">
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_pDJxlRZjOl.png" left-label="Stock"
                right="/assets/img/posts/spcmr3/Rally_3PC_0QekVJ7utN.png" right-label="SilentPatch" %}
{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC_d5pB0mWR2G.jpg" left-label="Stock"
                right="/assets/img/posts/spcmr3/Rally_3PC_7AyM6Gu0Lo.jpg" right-label="SilentPatch" %}
</div>

***

{: #fix-menu-elements}
The default CMR3 menus look notoriously inconsistent. SilentPatch fixes many inconsistently formatted texts (e.g. `CONTROLS:` on one screen, `CONTROLS :` on another)
and imperfect menu elements -- with "line boxes" being exceptionally imperfect:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-boxes.png" caption="The stock boxes look like they have a ribbon in the bottom right IMO." style="natural" %}

***

{: #fix-split-screen}
Just like the previous games in the franchise, Colin McRae Rally 3 comes with a split-screen feature. The issue is, on most modern PCs by default it looks like this:

{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_C8cj6w58pT.jpg" caption="That's not what I meant when I said that I like the Horizon games." %}

This issue, fixed in Colin McRae Rally 04, can also be worked around by setting the game affinity to just a single core. However, since that's not a threading issue,
this likely only buys the user some time, and in the future, this method might stop working too.

How was it fixed in CMR04? It's one of the only fixes I've admittedly not understood fully, but it seems to be related to the physics update tick ending up at a
0 ms delta value (which means 0 ms have passed between updates). CMR04 seems to correct this by replacing relatively inaccurate `timeGetTime` functions with a more accurate
`QueryPerformanceCounter`; however, this wasn't enough to fix CMR3, so I also additionally offset the first physics update tick by one second.
This means that the game thinks the very first physics tick took one second, but in practice, this changes nothing, as that one tick is performed just after the cars
are spawned -- and this happens before the screen starts to fade from white.

***

{: #fix-multiple-displays}
CMR3 comes with support for multiple displays and allows the user to specify what display to render the game to, but unless all your displays are identical,
your typical multi-monitor experience was likely to look like this:

{% include screenshot.html link="/assets/img/posts/spcmr3/ZOKTH5ovZ7.png" caption="Yes, I would like to run the game at (NULL)." %}

The addition of a Refresh Rate option in SilentPatch only made this issue worse, so despite using a single-display system myself, I had to take a look.
Turns out the issue is simple -- although the game correctly refreshes the list of available resolutions as soon as you switch the selected display adapter,
it... doesn't update the number of available resolutions. This, depending on whether the newly selected adapter has more or fewer display modes,
could result in either being unable to select the higher resolutions or in an instant crash (as shown above). SilentPatch fixes the issue by
updating the display mode counts and makes sure that the selected resolution cannot ever go over the number of listed display modes.

***

{: #fix-message-pump}
The last issue I wanted to highlight never showed up in the original game, but it's somewhat fascinating, and could serve as a cautionary tale for other developers.

Initially, after implementing the windowed mode, I'd observe an issue where the game window flashes black every few seconds.
This only happened in normal windowed mode, and not borderless, even though the two are technically nearly identical.
I initially thought it was an issue caused by NVidia Shadowplay, as the issue seems to have been caused by something sending this series
of messages to the game window:

```
S WM_WINDOWPOSCHANGING lpwp:0019FA8C
R WM_WINDOWPOSCHANGING
S WM_ERASEBKGND hdc:0F01208B
R WM_ERASEBKGND fErased:True
S WM_WINDOWPOSCHANGED lIpwp:0019FA84
S WM_SIZE fwSizeType:SIZE_RESTORED nWidth:1280 nHeight:720
R WM_SIZE
R WM_WINDOWPOSCHANGED
S WM_GETICON fType: True
R WM_GETICON hicon:00000000
S WM_GETICON fType: True
R WM_GETICON hicon:00000000
S WM_GETICON fType:False
R WM_GETICON hicon:00000000
S WM_WINDOWPOSCHANGING Ipwp:0019FA8C
R WM_WINDOWPOSCHANGING
S WM_ERASEBKGND hde:7D0123DE
R WM_ERASEBKGND fErased:True
S WM_WINDOWPOSCHANGED lIpwp:0019FA84
S WM_SIZE fwSizeType:SIZE_RESTORED nWidth:1280 nHeight:720
R WM_SIZE
R WM_WINDOWPOSCHANGED
S WM_WINDOWPOSCHANGING Ipwp:0019FA8C
```

The key to understanding is the fact those are not **position** changes, but **style** changes -- and sometimes I'd also see the window border
briefly change the style to the one used by windows that are hung. Indeed, the issue was essentially revealed by this feature of Windows:

{% include screenshot.html link="/assets/img/posts/spcmr3/3bb3002a-31fa-4ad9-9b7b-247b7f2550c2-1.png" style="natural" %}

Traditionally, Windows thinks the window is hung when its window messages are not pumped often enough, typically 5 seconds.
However, at no point, the game was truly unresponsive, and so the chain of events that I **think** has happened there is:
1. The game processes gameplay logic and renders.
2. The game waits for a message to arrive (without pumping).
3. If any messages are present, process them.
4. Repeat from point 1.

The issue lies in point 2. -- the game somehow must be waiting for new messages without pumping them.
Therefore, Windows thinks the app is hung and sends several messages to indicate that fact via a window style change.
This in turn causes the game to spot that new messages are present, and process them; however,
processing messages is an indicator of a window that's working normally, so that backtracks the "app is hung" state!
The cycle repeats every few seconds, causing periodic flashes.

The proper fix would be to always pump messages, without waiting for them -- but since I wanted to keep the fix non-invasive
and at the same time comprehensive, I opted to "poke" the game window with an empty timer message every 2 seconds to keep
it always active. Not the cleanest, but makes it impossible to overlook any places in the code to patch, which arguably is
the highest priority when retrofitting fixes like this.

That said, please don't implement this fix in your app -- fix it properly instead 👼

## New options {#fixes-new-options}

{: #new-portable-settings}
Starting with a small one -- the game is now fully portable and saves settings to a `SilentPatchCMR3.ini` file located in the game directory,
instead of saving to the system registry. If you wished to put CMR3 on a flash drive and carry it with you, now you can.

***

{: #new-graphics-options}
Graphics Options have been expanded with several new options. My patches shipped with new options for a long time,
both [SilentPatch for Colin McRae Rally 2.0]({% link _games/cmr/cmr-2.0.md %}#silentpatch){:target="_blank"} and
[SilentPatch for TOCA 2 Touring Cars]({% link _games/toca-2.md %}#silentpatch){:target="_blank"} previously included
options like FOV control and more. However, this time those options are present in the game options.

The new options are:
* Tachometer (Analog/Digital) -- much like in CMR2.0, the tachometer is now customizable. The digital tachometer was previously exclusive
  to 2 player split-screen.
* Split-screen (Horizontal/Vertical) -- another option inspired by CMR2.0. Previously, the game always used a horizontal split-screen
  when playing in 4:3, and a vertical one when playing in 16:9; this means that the vertical split-screen remained unused on PC.
  Since the game now adjusts itself to arbitrary aspect ratios, separating this into a new option made the most sense.
* Field of View control -- the default field of view for all in-game cameras is 75 degrees, and now I added an option to set
  your preferred FOV in the range of 30 - 150 degrees. External and internal cameras get their separate options -- something not done even
  in DiRT Rally 2.0.

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_cWlcxCu7Qg.jpg" caption="Digital tachometer" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_UDHzvaVeTM.jpg" caption="Vertical split-screen" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-min-fov.jpg" caption="30 degrees FOV" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-max-fov.jpg" caption="120 degrees FOV" %}
</div>

***

{: #new-advanced-graphics-options}
Advanced Graphics Options have received a set of new options inspired by later CMR games and modern games in general.

{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_XzfqxTVQMs.png" caption="This isn't DiRT Rally 2.0, but a good old CMR3." %}

Those are:
* Display mode (Fullscreen, Windowed, Borderless) -- using the stock game's windowed mode that remained unfinished in the code,
  presumably a scrapped idea and/or a debug feature.
* Refresh Rate
* Vertical Sync -- the game's UI [has some issues with high frame rates](https://twitter.com/__silent_/status/1598446635130015751){:target="_blank"},
  but the car physics seem to work well even at hundreds of frames per second!
* Anisotropic Filtering -- [unlike the option in CMR2005](https://twitter.com/__silent_/status/1598781224826200064){:target="_blank"}, this one actually works[^spcmr04] 🤔

{% include juxtapose.html left="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_z0PIV5ZtkM.jpg" left-label="AF OFF"
                right="/assets/img/posts/spcmr3/Rally_3PC.1.1.drmfree_7rtPTroLY3.jpg" right-label="AF x16"
                caption="It's the details that matter." %}

The new options default to English if you're using an international or a Czech version, and Polish if you're using a Polish version.
However, the Language Pack comes with translations for all new strings added to the game. Please check
[Chapter 5: Merging regional releases together](#merging-regional-releases) for more info.

# Chapter 4: The perfect remaster -- adding an HD interface {#hd-interface}

A set of fixes and perfect widescreen support make for a nice patch, but it's not enough to call this a remaster. However, this changed once Bekoha offered
to work on retouching the UI and fonts in high quality. The original assets were clearly made with a 640x480 resolution in mind; so when playing at high resolutions
the game itself looked gorgeous, but the UI was lacking.

{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_6Israqewxa.jpg" caption="Feels like something is missing here." %}

Bekoha's HD UI addresses this by replacing most interface assets with faithful high quality recreations:
<div class="screenshot-container natural">
{% capture url_speed %}{{ hd_ui_url }}/screenshots/speed.png{% endcapture %}
{% capture url_timer %}{{ hd_ui_url }}/screenshots/timer.png{% endcapture %}
{% capture url_results %}{{ hd_ui_url }}/screenshots/results.png{% endcapture %}
{% capture url_greece %}{{ hd_ui_url }}/screenshots/greece.png{% endcapture %}
{% include screenshot.html link=url_speed %}
{% include screenshot.html link=url_timer %}
{% include screenshot.html link=url_results %}
{% include screenshot.html link=url_greece %}
</div>

More comparison screenshots (also showcasing SP's widescreen support) can be found on Bekoha's website: \\
<a href="{{ hd_ui_url }}/screenshots" target="_blank" class="button"><i class='fas fa-globe'></i> CMR3 HD UI Screenshots</a>

***

Of course, if replacing textures was as easy as just putting them in the game, I wouldn't be writing about it here, **and** someone else would've
likely released HQ fonts/UI years ago. Instead, to get HD textures to look the way we wanted them to, we had to solve not one, but three separate issues.

## Scaling issues {#scaling-issues}
Theoretically, replacing textures in CMR3 is easy. Font files are loose DDS files, while the UI textures are DDS files packaged in BigFile archives that have been
well understood for nearly two decades. However, a naïve texture replacement produces results that are hardly optimal:

<div class="screenshot-container small">
{% include screenshot.html link="/assets/img/posts/spcmr3/qBsfV0cO.png" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/mpc-hc64_2022-11-25_00-44-43.png" %}
{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC_nV6WYwJk2u.png" caption="In case you forget who is the sponsor." %}
</div>

Albeit unusual for PC games, this behavior is perfectly explainable. The original UI design was pixel perfect, with no scaling involved -- which
means that all UI textures displayed 1:1 to what they are in files. For obvious reasons, this does not translate well to PC where the output resolution
is configurable, but there the draws only get linearly scaled, with the setup unchanged. This means that internally, the game still issues UI draws
using the texture dimensions as a draw size, producing oversize UI elements (screenshots #1 and #3), or specifying UV coordinates
in pixels directly, producing cut off elements (screenshot #2).

The solution here is simple -- since the UI has already been "finalized" with specific texture dimensions in mind, scaling can be implemented trivially
by lying to the game about the texture sizes, and always pretending the texture dimensions are the same as the original!

```cpp
static const std::map<std::string_view, TexData, std::less<>> textureDimensions = {
	{ "Arrow1Player", { 32, 16 } }, { "ArrowMultiPlayer", { 32, 16 } }, { "ArrowSmall", { 16, 16 } },
	{ "Base", { 128, 128, true } }, { "certina", { 64, 8 } }, { "Colour", { 128, 128, true } },
	{ "Ck_base", { 128, 64 } }, { "Ck_00", { 32, 32 } }, { "Ck_01", { 32, 32 } },
	{ "Ck_02", { 32, 32 } }, { "Ck_03", { 32, 32 } }, { "Ck_04", { 32, 32 } },
	{ "Ck_05", { 32, 32 } }, { "colin3_2", { 256, 64 } }, { "ct_3", { 64, 64, true } },
	{ "dialcntr", { 32, 32 } }, { "infobox", { 128, 128 } }, { "MiniStageBanner", { 128, 32 } },
	{ "osd_glow", { 32, 32 } }, { "rescert", { 128, 32 } }, { "swiss", { 128, 8 } },
	{ "AUS", { 32, 16 } }, { "FIN", { 32, 16 } }, { "GRE", { 32, 16 } },
	{ "JAP", { 32, 16 } }, { "SPA", { 32, 16 } }, { "SWE", { 32, 16 } },
	{ "UK", { 32, 16 } }, { "USA", { 32, 16 } },
};
auto it = textureDimensions.find(name);
if (it != textureDimensions.end())
{
	result->m_width = it->second.width;
	result->m_height = it->second.height;
}
```

Because the UV data sent to the rendering API is normalized, this lie allows the game to keep the internal
setup unchanged, while the actual rendering stays unaffected and makes full use of the high fidelity resource.

## Font filtering {#font-filtering}
Contrary to a popular belief, upscaling is not always the best solution for a high quality interface.
Detailed textures benefit from it the best, but for pixel art there usually is a better solution -- nearest neighbor scaling:

{% include screenshot.html link="/assets/img/posts/spcmr3/2-Figure2-1.png"
 caption="Source: [Evaluation of Different Image Interpolation Algorithms](https://www.semanticscholar.org/paper/Evaluation-of-Different-Image-Interpolation-Prajapati-Naik/882eb0f08c5643279459183be0ea3e1496a73cf5)" %}

For any textures considered pixel art, scaling them via nearest neighbor filtering (as opposed to linear filtering) retains the effect of sharp pixels
without the need to ship assets that effectively duplicate pixels multiple times:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-nearest-filtering.png" caption="These are the same font assets, just filtered differently." style="natural" %}

SilentPatch opts to always use nearest filtering on a set of textures and fonts predefined by us, so they look sharper than in the stock game even without the HD UI installed.

## Half pixel issues {#half-pixel-issues}
Direct3D 9 comes with a rather annoying texturing phenomenon dubbed "half pixel offset", where textures display slightly wrong unless the draw is offset by half a pixel.
It has finally been corrected on the API level in Direct3D 10 and newer and it has never been an issue in OpenGL, so it's a commonly overlooked issue -- and CMR3 is no different.
The issue is documented very well, you can read about it more here:
* [Directly Mapping Texels to Pixels](https://learn.microsoft.com/windows/win32/direct3d9/directly-mapping-texels-to-pixels){:target="_blank"} from Microsoft
* [Solving DX9 Half-Pixel Offset](https://aras-p.info/blog/2016/04/08/solving-dx9-half-pixel-offset){:target="_blank"} from Aras Pranckevičius

While CMR3 is subject to this issue, with linear filtered textures I couldn't spot it at any resolution.
However, it all changes once nearest filtering is used -- textures appear blurry on the edges even though it should be impossible when nearest filtering is used
(top image). Applying that specific fix to all UI elements ensures they always stay as sharp as possible (bottom image). Pay attention to the blurred edges, especially on
**1**, **L**, and **R**:

{% include screenshot.html link="/assets/img/posts/spcmr3/cmr3-half-pixel-big.png" thumbnail="/assets/img/posts/spcmr3/cmr3-half-pixel.png"
    caption="This close to greatness... Click to open this image at 300% scaling, as, ironically, browsers use linear scaling when zooming in." style="natural" %}

# Chapter 5: Merging regional releases together {#merging-regional-releases}

With all fixes and high definition UI in place, it was time for the icing on the cake -- producing a single ultimate package of releases combining the regional editions,
not unlike what a real remaster could potentially do. For this, I only consider known official releases, so fan translations are not considered.

The Language Pack includes all 7 official translations (counting English), and 8 co-drivers, including the two Polish co-drivers [presented above](#polish-codrivers).
The Polish re-release also receives support for Nicky Grist's pace notes much like the original Polish release, although due to the high file size, Grist's audio files
are a separate download. All regional changes made for the Polish release, such as localized cube textures and the OSD keyboard, are also present;
not only that, but the Czech localization also receives its own OSD keyboard, while the official release did not:

{% include screenshot.html link="/assets/img/posts/spcmr3/Rally_3PC.1.1.czech_B6U6sUBX6Y.png" %}

Since the regional releases ship their own atlases of fonts, and the Polish release goes as far as updating the codepoints from **Windows-1252** (Western Europe)
to **Windows-1250** (Central Europe), the initial plan was to merge them all and update the game to use UTF-8. However, we ruled against it for several reasons:
* The `PCF` format is not complicated to reverse engineer, but making a tool that can correctly repack it from a human readable format is another matter.
* Changes like this can be extraordinarily risky and could potentially break compatibility with the existing saves and track records.
* Even if they didn't break compatibility with "old" records when SilentPatch is installed, it would be highly likely that "new" records would break the stock game.

Therefore, SilentPatch adds support for "regional" fonts for each language. Both Language Pack and HD UI ship Polish fonts in `fonts/fonts_P`, and Czech fonts in `fonts/fonts_C`.
These alternate sets of fonts are used regardless of whether the Language Pack is installed or not,
so the HD UI can only ship a single set of files that works for as long as SP is installed.

***

Aside from including regional languages and co-drivers, the Language Pack also improves the existing translations.
Therefore, it makes sense to install the Language Pack even if you don't plan to use Polish or Czech localizations:

* Codemasters introduced a "Return to Centre" option in the official 1.1 patch and hardcoded that string.
  Language Pack extracts it to the localization files, so all languages now received a translated string.
* The Telemetry screen hardcodes a "NA" text in the international release; this was later moved to the localization file for the Polish release.
  Language Pack unifies this, and now all languages received a translated string.
* The Polish release moved more key names (such as "Left", "Right", "Up", and "Down" arrow keys) to the localization file.
  Language Pack unifies this, and now all languages received a translated string.
* Thanks to {{ lostraniero_link }}, the Italian translation has been completely revised and uses more accurate and fitting translations.

# Changelog and download {#changelog-and-download}

You made it all the way, congratulations 😁 (or maybe you just skipped to here from a TL;DR, that's fine too)

The full mod's changelog is as follows; fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.
The other new options have been added to in-game menus instead.

### Essential fixes:
* The game now lists all available display resolutions, lifting the limit of 128 resolutions and the 4:3 aspect ratio constraint.
* The game will now try to pick the closest matching resolution instead of crashing on startup if launched with an invalid resolution specified in the config.
* The game now defaults to desktop resolution on the first boot.
* Several issues related to the sun rendering have been fixed - sun flickering with anti-aliasing enabled has been fixed, and a consistent hitch when the sun was about to appear on screen was resolved.
* Fixed multiple distinct issues causing water reflections to appear either too dark or completely black.
* Fixed car shadows appearing overly sharp, or not appearing at all when anti-aliasing is enabled.
* Fixed a crash when switching between display adapters with different numbers of resolutions, and made the resolutions list automatically refresh when switching adapters, eliminating a possible crash.
* The game now handles arbitrary aspect ratios correctly - with all 3D elements and the entire UI fixed for widescreen and positioning dynamically.
* Fixed a possible out of bounds read when the supplied translation file did not contain all the strings the game needs (for example, when using the PL executable with EN data).
* Improved the overall precision of in-game timers.
* Fixed an issue where split-screen would not work correctly on modern PCs with fast enough CPUs unless the game was forced to use a single CPU core.

### Miscellaneous fixes:
* <i class="fas fa-cog"></i> Environment maps on cars now always reflect the sky, like on the PS2; making reflections look more natural and correcting an issue where the big TV screens displayed a grey sky.
* Line rendering now respects the display resolution, making line thickness proportional to resolution and improving their visibility.
* Half pixel issues have been corrected across the UI, improving the overall clarity of the interface, and fixing numerous issues where fullscreen backgrounds would leave a single pixel-wide line (or a seam in the middle) with multisampling enabled.
* Improved the visual consistency of numerous race UI elements.
* Improved the visual consistency of the digital tachometer by using a scissor feature for rendering, improving its accuracy and resolving a possible flicker.
* Support for texture replacements and new fonts has been improved - the game can now handle higher resolution assets without glitching.
* UI elements and fonts with sharp pixels now use nearest neighbor filtering instead of linear filtering for improved clarity.
* Improved the presentation of line boxes used e.g. in the onscreen keyboard and Car Setup, fixing gaps, overlapping lines, and misplaced fill.
* Legend lines on the Telemetry screen now fade out together with the rest of the menu.
* Fixed numerous spacing inconsistencies in menu texts.
* Fixed a broken split-screen Time Trial results screen (Czech executable only).
* Fixed "Player X has retired" texts going off the screen at resolutions above 640x480.
* Fixed an issue where the resolution change countdown went into negatives when fading out.
* Fixed an issue on wider aspect ratios where repeated menu entries would not fade correctly.
* Fixed an issue only showing in the Polish release where leaving the 'Co-driver's voice' screen would flicker the menu animations.
* Alt+F4 now works.
* Removed a debug feature where invalid codepoints flickered randomly.
* The error message displayed when the game fails to load specific game files now doesn't freeze the game and can be closed with Alt+F4.

### Enhancements:
* The game is now fully portable, as the settings have been redirected from the registry to the INI file.
* <i class="fas fa-cog"></i> Car shadows are now slightly sharper, matching the way they are rendered in Colin McRae Rally 2005.
* <i class="fas fa-cog"></i> Menu navigation on the gamepad has been remapped from the analog stick to the directional pad like it is in the console releases.
* New Graphics options added: Field of View (separate for external and internal cameras), Digital Tachometer, Vertical Split-screen.
* New Advanced Graphics options added: Windowed/borderless mode (fully resizable), Vertical Sync, Refresh Rate, Anisotropic Filtering.
* Changed the Bonus Codes URL to point towards [a cheat generator hosted by myself]({% link pages/bonuscodes.md %}){:target="_blank"} since the original URLs are not active anymore.

### Language Pack:
* Added support for all official text translations used together - English, French, German, Spanish, Italian, Polish, and Czech.
* Added support for all official co-drivers together - English, French, German, Spanish, Polish (Janusz Kulig), Polish (Janusz Wituch), and Czech.
* Re-added support for Nicky Grist's pace notes in the Polish re-release.
* Revised some capitalization inconsistencies in all languages.
* Revised Italian translation.
* Included translation lines for all new menu options added by SilentPatch.

### HD UI - by Bekoha:
* Made with 4K resolution in mind.
* Font atlases remade using original fonts.
* Support for EFIGS, Polish and Czech languages.
* Banners redrawn for every stage.
* Majority of in-game UI elements replaced.

I've created a brief showcase of the patch in video form, you can watch it here:
<div class="video-container">
<iframe src="https://www.youtube.com/embed/ipXwyzwV9k0" frameborder="0" allowfullscreen></iframe>
</div>

> Unlike most of my other mods, installing this one is a little more involved. Due to the presence of DRM-free executables,
> I only officially support those, and instead, I provide a ready solution to upgrade the latest official DRM'd executables to the DRM-free versions.
> If you don't do this before installing SilentPatch, you will be greeted with a warning message on startup.
> The mod's download page includes detailed setup instructions to walk you through this process step by step.

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly: \\
<a href="{% link _games/cmr/cmr-3.md %}#silentpatch" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for Colin McRae Rally 3 (and addons)</a> \\
Please follow the installation instructions **carefully** and extract the components into your game directory in order.
Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).


# Credits and acknowledgments {#acknowledgments}

* {{ bekoha_link }} for the entirety of the HD UI work and general support
* {{ krusantusz_link }} for help with the Polish eXtra Klasyka release
* {{ memorix_link }} and {{ ribshark_link }} for help with the German DVD release
* {{ lostraniero_link }} for improving the entire Italian translation
* {{ automaniak_link }} for his past efforts in fixing CMR3 for widescreen resolutions
* {{ pierre_terdiman_link }} for a [*Textured Lines In D3D*](https://www.flipcode.com/archives/Textured_Lines_In_D3D.shtml) code snippet
* Various people contributing new translation lines in German, French, Spanish, Italian, and Czech
* *abbydiode* and *Cpone* for additional testing
* Several ex-CMR3 developers who are aware of this project and were able to share their feedback 🙂

***

For those interested, the full source code of the mod has been published on GitHub, so it can be freely used as a point of reference: \\
<a href="https://github.com/CookiePLMonster/SilentPatchCMR3" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>

***
