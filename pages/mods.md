---
layout: page
title: "Mods & Patches"
subtitle: My modifications and patches for various games.
excerpt: My modifications and patches for various games.
permalink: /mods/
---

Looking for an easy-to-browse list? Check out the [**Mod Index**]({% link pages/mod-index.html %})!
For details about the latest updates, visit the [**Updates**]({% link pages/updates.md %}) page.

***

{% assign all_games = site.games | where: "parent-series", "" %}
{% assign games = all_games | where_exp: "item","item.order < 100" %}
{% include mods-grid.html items=games %}

***

{% assign consoles = all_games | where_exp: "item","item.order >= 100" %}
{% include mods-grid.html items=consoles %}
