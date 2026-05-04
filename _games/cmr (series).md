---
layout: page
title: "Colin McRae Rally"
subtitle: "Mods & Patches"
excerpt: My modifications and patches for Colin McRae Rally games.
image: "assets/img/games/cmr-series.jpg"
feature-img: "assets/img/games/bg/cmr-series.jpg"
game-series: "cmr"
order: 0
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include schema/item-grid.html items=items page=page %}
{% include mods-grid.html items=items %}
