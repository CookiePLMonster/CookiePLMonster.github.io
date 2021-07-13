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
*Recommended emulator: DuckStation*

{% assign ps1_games = items | where_exp: "item", "item.order < 10" %}
{% include mods-grid.html items=ps1_games cell-size="33%" %}

***

# PlayStation 2 games
*Recommended emulator: PCSX2*

{% assign ps2_games = items | where_exp: "item", "item.order >= 10" | where_exp: "item", "item.order < 100" %}
{% include mods-grid.html items=ps2_games cell-size="33%" %}