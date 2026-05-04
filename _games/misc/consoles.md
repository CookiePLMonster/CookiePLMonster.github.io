---
layout: page
title: "Consoles"
excerpt: My cheats and modifications for various console games.
image: "assets/img/misc/consoles.jpg"
game-series: "consoles"
parent-series: "non-game"
order: 0
---

{% assign ps1_items = site.games | where:"parent-series", "console-ps1" %}
{% assign ps2_items = site.games | where:"parent-series", "console-ps2" %}
{% assign gc_items = site.games | where:"parent-series", "console-gc" %}
{% assign psp_items = site.games | where:"parent-series", "console-psp" %}

{% assign all_console_items = ps1_items | concat: ps2_items | concat: gc_items | concat: psp_items %}
{% include schema/item-grid.html items=all_console_items page=page %}

# PlayStation games {#ps1}

{:.sidenote}
Recommended emulator: DuckStation ([Desktop](https://github.com/stenzek/duckstation/){:target="_blank"}, [Android](https://play.google.com/store/apps/details?id=com.github.stenzek.duckstation){:target="_blank"})

{% include mods-grid.html items=ps1_items %}

***

# PlayStation 2 games {#ps2}

{:.sidenote}
Recommended emulator: [PCSX2](https://pcsx2.net/){:target="_blank"} (Desktop), [AetherSX2](https://play.google.com/store/apps/details?id=xyz.aethersx2.android){:target="_blank"} (Android)

{% include mods-grid.html items=ps2_items %}

***

# GameCube games {#gc}

{:.sidenote}
Recommended emulator: [Dolphin](https://dolphin-emu.org/){:target="_blank"} (Desktop, Android)

{% include mods-grid.html items=gc_items %}

***

# PlayStation Portable games {#psp}

{:.sidenote}
Recommended emulator: [PPSSPP](https://www.ppsspp.org/){:target="_blank"} (Desktop, Android)

{% include mods-grid.html items=psp_items %}
