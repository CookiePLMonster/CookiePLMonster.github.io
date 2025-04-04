---
title: SilentPatch
game-series: "cmr-2.0"
excerpt: "Widescreen support and more."
date: 08-08-2015
---

Here we have the first non-GTA related game in the SilentPatch series, this time I have gone back to one of the very first games I played and made it compatible with modern systems.

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.

## Featured fixes
* The game now handles all aspect ratios properly.
That means the game will not be horribly scretched when playing in widescreen anymore.
* <i class="fas fa-cog"></i> The game now defaults to borderless windowed mode. This change gets rid of a DirectDraw bug on Windows 8 and newer,
which would make the game run in a window even if fullscreen is requested, also affecting performance negatively.
Fullscreen borderless windowed mode does not have any of these issues, and looks identical to real fullscreen.
Both windowed and borderless can be toggled via `SPCMR2.ini` file.
* When playing in windowed mode (borderless or not), the game can handle <kbd>Alt</kbd> + <kbd>Tab</kbd> properly now.
* All dependencies on registry keys have been removed. This makes the game fully portable and also fixes an
occasional issue, where the game would not launch without Administrator privileges (due to an incorrect way
the game was reading registry keys).
* Logging has been removed for good (since it would never log anything anyway). The game used to create
a log file in `C:\` which would often make the game require Administrator privileges to run.
* <i class="fas fa-cog"></i> Regions can now be switched via the INI file. Depending on the game version, it has different region directories
included in CountrySpecific directory. Now, if you have more than one region installed, you can easily switch
between them.
* <i class="fas fa-cog"></i> Field of View can now be adjusted via the INI file. You can select any value in 30.0 - 150.0 range.
* Support for non-Full installation methods has been removed. On the plus side, the game will never ask for a CD now.

{% include figures/image.html link="https://i.imgur.com/4mdV2aV.jpg" thumbnail="https://i.imgur.com/4mdV2aVh.jpg" %}
{% include figures/video-iframe.html link="https://www.youtube.com/embed/p0HMeN27Rcw" %}

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/SilentPatchCMR2/releases/latest/download/silentpatch_cmr2.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/CookiePLMonster/SilentPatchCMR2" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>