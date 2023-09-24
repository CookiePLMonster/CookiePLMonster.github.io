---
layout: page
title: "Need for Speed"
excerpt: My modifications and patches for Need for Speed games.
image: "assets/img/games/need-for-speed-series.jpg"
feature-img: "assets/img/games/bg/need-for-speed-series.jpg"
game-series: "need-for-speed"
order: 1
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items cell-size="33%" %}