---
layout: page
title: "Grand Theft Auto"
excerpt: My modifications and patches for Grand Theft Auto games.
image: "assets/img/games/gta.jpg"
feature-img: "assets/img/games/bg/gta.jpg"
game-series: "gta"
order: -10
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items %}