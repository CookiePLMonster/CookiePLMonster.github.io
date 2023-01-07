---
layout: post
title: "Second release of SilentPatch for Scarface: The World is Yours"
excerpt: "Much needed stability improvements, after the initial version of the patch made it worse."
thumbnail: "assets/img/posts/scarface-r2/scarface-r2-header.jpg"
feature-img: "assets/img/posts/scarface-r2/scarface-r2-header.jpg"
image: "assets/img/posts/scarface-r2/scarface-r2-header.jpg"
twitter: {card: "summary_large_image"}
game-series: "scarface"
date: 2022-02-12 21:45:00 +0100
tags: [Releases]
---

*TL;DR - if you are not interested in a brief explanation of the issue introduced by the first build of SilentPatch,
scroll down to the [**Download**](#changelog-and-download) section for a download link.*

***

Nearly 2 years ago, I released [the first version of SilentPatch for Scarface]({% post_url 2020-03-29-silentpatch-scarface %}).
It was met with a positive response since it made the game playable for many, but... I also messed up.

One of the fixes was to undo the CPU affinity changes the game made to itself, forcing itself to run on only one core.
This promised great performance benefits, and it delivered, but it also came at a price:

<p align="center">
<img src="{% link assets/img/posts/scarface-r2/glitches.jpg %}"><br>
<em>Where did the road go? Oh, looks like streaming has locked up.</em>
</p>

<p align="center">
<img src="{% link assets/img/posts/scarface-r2/redbox.jpg %}"><br>
<em>There should be text here, but changing the CPU affinity broke it.</em>
</p>

Depending on luck, PC configuration, and possibly also the stars, users would encounter a range of newly introduced issues like:
* Streaming locking up
* Infinite loading screens
* Profiles not loading
* Random crashes

Turns out, those are entirely on me and they are all side effects of allowing the game to run on any CPU core,
opening a Pandora's box full of race conditions in the game that are probably harmless while contained to a single core,
but not as much when it can run on 8+ threads.

However, the alternative (that is undoing that change and confining the game to a single core) is also bad. 
Here's Scarface (with CPU affinity locked to one core) running on an i9-12900K,
at the time of writing this post one of the best consumer CPUs on the market -- it struggles to keep stable 60 FPS even in the intro mission!

<p align="center">
<img src="{% link assets/img/posts/scarface-r2/perf.jpg %}"><br>
<em markdown="1">Fun fact -- it's just as slow as it [was in 2020 on an i7-6700K]({% post_url 2020-03-29-silentpatch-scarface %}#part-two--performance).</em>
</p>

Can we do better than this? Turns out, apparently so.
Fast forward from March 2020 to January 2022, **CrabJournal** [submits a Pull Request](https://github.com/ThirteenAG/WidescreenFixesPack/pull/1045)
to a Widescreen Fix for Need for Speed Underground 2. Much like Scarface, UG2 has issues running on multiple threads,
and a common fix of changing the CPU affinity decreases performance to unacceptable levels. However, CrabJournal's idea for affinity changes
seems to combine stability and performance. To quote the PR:

> The common fix is setting single core affinity on the WHOLE process, which is causing a performance issue: my 2.5 GHz Kaby Lake can't even provide 60 FPS.
> Current NFSU2 WSFix version is also setting single core affinity on the whole process.
> In this pull request, only threads that are created directly by the game get a single core affinity, which is completely solving both game crashes and performance issues.

CrabJournal added a distinction between threads created by the game and coming e.g. from the system DLLs, drivers, or other third party software.
This may not seem like much, but modern GPU drivers create **a lot** of threads -- in my case, Nvidia's driver creates an entire thread pool for itself,
creating over 16 threads alone! In practice, letting all this code unrelated to the game is a huge efficiency win.
This approach to affinity is essentially no different from
[the way Cxbx-Reloaded manages thread affinity](https://github.com/Cxbx-Reloaded/Cxbx-Reloaded/blob/a25e455289d2599fd07f6b6271be3a6a2e4bbaeb/src/common/win32/Threads.cpp#L197-L228).

I integrated a near-identical change to Scarface and sure enough, it seems to work well! On my machine, I previously could reproduce the streaming issue consistently.
However, with this change applied, my game is both fast **and** stable.

<p align="center">
<img src="{% link assets/img/posts/scarface-r2/goodperf.jpg %}"><br>
<em>That's better.</em>
</p>

The change was also tested by several users who previously encountered issues. In all cases, the issues disappeared, but I still want to play it safe this time.
Starting with Build 2, users can add a `SingleCoreAffinity=1` option to `settings.ini` to opt-out of the affinity changes and revert to locking the game
to a single CPU core. This goes without saying, only do so if still encounter issues and suspect the affinity changes are the culprit,
as the game may be annoyingly slow when pinned to a single core.

# Changelog and download
A full changelog of this release is rather short:
* Fixes to CPU core affinity have been remade, now only locking the game threads to one core, while leaving others be.
  In an unlikely case this causes issues, CPU core affinity can be restored to default by adding `SingleCoreAffinity=1` to the `settings.ini` file.

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/scarface.md %}#silentpatch" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for Scarface</a> \\
Upon downloading, all you need to do is to extract the archive to the game's directory and that's it!
When asked whether to overwrite files, select Yes.

***

For those interested,
full source code of the patch has been published on GitHub, so it can be freely used as a point of reference: \\
<a href="https://github.com/CookiePLMonster/SilentPatchScarface" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>