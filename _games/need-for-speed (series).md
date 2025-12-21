---
layout: page
title: "Need for Speed"
excerpt: My modifications and patches for Need for Speed games.
image: "assets/img/games/need-for-speed-series.jpg"
feature-img: "assets/img/games/bg/need-for-speed-series.jpg"
game-series: "need-for-speed"
order: 7
disambiguation:
  this: "the PC versions of Need for Speed games"
  others:
    - desc: "the PS2 versions"
      link: "_games/misc/consoles.md"
      link-name: "Consoles (PS2)"
      anchor: "ps2"
---

{% include elements/disambiguation.html disambiguation=page.disambiguation %}

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items %}