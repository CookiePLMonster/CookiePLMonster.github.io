---
title: SilentPatch
game-series: "scarface"
excerpt: "Fixed graphical corruptions and noticeable performance improvements."
date: 07-05-2022
---

Scarface: The World is Yours is one of these games which nowadays are unplayable out of the box.
Graphical corruptions present on nearly all modern machines makes the game impossible to play without using
unofficial fixes. However, until now those were working the issue around and could result in slightly degraded
performance.

SilentPatch for Scarface fixes this issue in the least invasive way possible, and comes with an array of improvements
to the game's performance. In the best case, those fixes might **double** game's performance and eliminate
most of the hitches present when driving around!

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the `settings.ini` file.

## Featured fixes:
* Game-breaking graphical corruptions have been fixed, making the game playable on modern multicore machines
* <i class="fas fa-cog"></i> Allowed the game to use all CPU cores (instead of locking to one core), dramatically improving performance.
In an unlikely case this causes issues, CPU core affinity can be restored to default by adding `SingleCoreAffinity=1` to the INI file
* Removed an unneeded multithreaded flag from the D3D device, possibly improving performance slightly
* Introduced a cache for some D3D resources used by the game, dramatically reducing the amount of stutter when roaming around the city
* Made the game list all selectable resolutions instead of a cherry picked list
* Moved the game's settings from the Registry to settings.ini in the game directory - this resolves possible issues with saving settings
* <i class="fas fa-cog"></i> Added an option to adjust the camera speed from settings.ini via a `CameraSpeedMultiplier` option
* <i class="fas fa-cog"></i> Added an option to adjust on-foot Field of View from settings.ini via a `FOV` option

## Credits
* [ermaccer](https://github.com/ermaccer) - `CameraSpeedMultiplier` and `FOV` options

{% include figures/image.html link="https://i.imgur.com/XnNcJpM.png" thumbnail="https://i.imgur.com/XnNcJpMh.png" %}

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/SilentPatchScarface/releases/latest/download/SilentPatchScarface.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/CookiePLMonster/SilentPatchScarface" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
