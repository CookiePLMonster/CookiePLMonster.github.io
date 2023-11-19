---
layout: page
title: "Colin McRae Rally"
excerpt: My modifications and patches for Colin McRae Rally games.
image: "assets/img/games/cmr-series.jpg"
feature-img: "assets/img/games/bg/cmr-series.jpg"
game-series: "cmr"
order: 0
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items cell-size="33%" %}