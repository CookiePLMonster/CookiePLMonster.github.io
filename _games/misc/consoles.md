---
layout: page
title: "Consoles"
excerpt: My cheats and modifications for various console games.
image: "assets/img/misc/consoles.jpg"
order: 100
---

# PlayStation games {#ps1}
*Recommended emulator: DuckStation ([Desktop](https://github.com/stenzek/duckstation/), [Android](https://play.google.com/store/apps/details?id=com.github.stenzek.duckstation))*

{% assign ps1_items = site.games | where:"parent-series", "console-ps1" %}
{% include mods-grid.html items=ps1_items cell-size="33%" %}

***

# PlayStation 2 games {#ps2}
*Recommended emulator: [PCSX2](https://pcsx2.net/) (Desktop), [AetherSX2](https://play.google.com/store/apps/details?id=xyz.aethersx2.android) (Android)*

{% assign ps2_items = site.games | where:"parent-series", "console-ps2" %}
{% include mods-grid.html items=ps2_items cell-size="33%" %}

***

# PlayStation Portable games {#psp}
*Recommended emulator: [PPSSPP](https://www.ppsspp.org/) (Desktop, Android)*

{% assign psp_items = site.games | where:"parent-series", "console-psp" %}
{% include mods-grid.html items=psp_items cell-size="33%" %}
