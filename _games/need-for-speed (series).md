---
layout: page
title: "Need for Speed"
excerpt: My modifications and patches for Need for Speed games.
image: "assets/img/games/need-for-speed-series.jpg"
feature-img: "assets/img/games/bg/need-for-speed-series.jpg"
game-series: "need-for-speed"
order: 7
---

{:.disclaimer.info}
This page is for the PC versions of Need for Speed games.
For patches for the PS2 versions of Need for Speed games, see [Consoles (PS2)]({% link _games/misc/consoles.md %}#ps2).

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items %}