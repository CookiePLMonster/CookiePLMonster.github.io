---
layout: page
title: "Consoles"
excerpt: My cheats and modifications for various console games.
image: "assets/img/misc/consoles.jpg"
game-series: "consoles"
order: 100
---

{% assign items = site.games | where:"parent-series", page.game-series %}

# PlayStation games
*Recommended emulator: DuckStation ([Desktop](https://github.com/stenzek/duckstation/), [Android](https://play.google.com/store/apps/details?id=com.github.stenzek.duckstation))*

{% assign ps1_games = items | where_exp: "item", "item.order < 10" %}
{% include mods-grid.html items=ps1_games cell-size="33%" %}

***

# PlayStation 2 games
*Recommended emulator: [PCSX2](https://pcsx2.net/) (Desktop), [AetherSX2](https://play.google.com/store/apps/details?id=xyz.aethersx2.android) (Android)*

{% assign ps2_games = items | where_exp: "item", "item.order >= 10" | where_exp: "item", "item.order < 100" %}
{% include mods-grid.html items=ps2_games cell-size="33%" %}