---
layout: page
title: "Mods & Patches"
subtitle: My modifications and patches for various games.
excerpt: My modifications and patches for various games.
permalink: /mods/
---

Looking for an easy-to-browse list? Check out the [**Mod Index**]({% link pages/mod-index.html %})!
For details about the latest updates, visit the [**Updates**](/updates/) page.

***

{% assign games = site.games | where: "parent-series", empty %}
{% include mods-grid.html items=games style="larger" %}

***

{% assign nongames = site.games | where: "parent-series", "non-game" %}
{% include mods-grid.html items=nongames style="larger" %}
