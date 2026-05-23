---
layout: page
title: "Mods and Patches"
display_title: "Mods & Patches"
subtitle: My modifications and patches for various games.
excerpt: My modifications and patches for various games.
permalink: /mods/
---

Looking for an easy-to-browse list? Check out the [**Mod Index**]({% link pages/mod-index.html %})!
For details about the latest updates, visit the [**Updates**](/updates/) page.

***

{% assign games = site.games | where: "parent-series", empty %}
{% assign nongames = site.games | where: "parent-series", "non-game" %}

{% assign all_list_entries = games | concat: nongames %}
{% include schema/item-grid.html items=all_list_entries page=page %}

{% include mods-grid.html items=games style="larger" %}

***

{% include mods-grid.html items=nongames style="larger" %}
