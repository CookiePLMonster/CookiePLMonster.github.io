---
layout: page
title: "Yakuza"
subtitle: "Mods & Patches"
excerpt: "My modifications and patches for Yakuza games."
image: "assets/img/games/yakuza.jpg"
feature-img: "assets/img/games/bg/yakuza.jpg"
game-series: "yakuza"
order: 10
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include schema/item-grid.html items=items page=page %}
{% include mods-grid.html items=items %}
