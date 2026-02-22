---
title: "D2GI"
game-series: "king-of-the-road"
date: 22-02-2026
first-release: 23-12-2019
version: v0.4
order: 0
info-label: CONTRIBUTION
---

{::options auto_id_prefix="{{ page.id | split: '/' | last }}-" /}

{:.credit}
D2GI made by REDPOWAR. I expanded it with support for King of the Road (digital releases) and with many new fixes, such as the North Harbor bridge illumination
and an optimized minimap renderer.

D2GI adapts the game for modern PCs by wrapping DirectDraw7 + Direct3D7 to Direct3D9. It's developed to replace the existing wrappers from GOG and dgVoodoo.

## Featured fixes

* Fixes graphical artifacts ("Rainbow" bug, broken transparency, etc.).
* Supports any resolution and aspect ratio.
* Windowed mode, borderless, fullscreen.
* 32-bit color rendering.
* Fixes the "horizontal rain".
* Adds Multisample Anti-Aliasing (MSAA).
* Adds Anisotropic Filtering.
* Replaces the minimap renderer with a new, optimized renderer with smooth scrolling and MSAA support.
* Fixes the North Harbor bridge illumination, previously broken in the "King of the Road" releases.
* Fixes performance regressions introduced in patch 8.2.
* Compatible with most newer game versions, such as 8.2, KotR 1.3, 7.3.

{% include figures/image.html link="/assets/img/mods/d2gi/ddphoto_2026-02-12_19-04-41.jpg" thumbnail="auto" %}

{% include setup-instructions.html %}

***

<a href="https://github.com/REDPOWAR/D2GI/releases/download/v0.4/D2GI_v0.4.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/REDPOWAR/D2GI" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
