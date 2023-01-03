---
layout: page
title: Bonus Codes
excerpt: Cheat codes for Colin McRae Rally 3, Colin McRae Rally 04, and Colin McRae Rally 2005.
feature-img: "assets/img/bonuscodes/bonuscodes-banner.svg"
image: "assets/img/bonuscodes/bonuscodes-banner.png"
permalink: /bonuscodes/
twitter: {card: "summary_large_image"}
hide: true
---

<div class="mods-grid">
	{% assign mods_grid_items = site.bonuscodes | sort: "order" %}
    {% for item in mods_grid_items %}
    {% unless item.hide %}
    <div class="mods-cell" style="flex-basis: 33%; max-height: 450px;">
        <a href="{{ item.url | relative_url }}" class="mods-link" data-keyboard="true"> 
            <img src="{{ item.image | relative_url }}" alt="{{ item.title }}" title="{{ item.title }}">
        </a>
    </div>
    {% endunless %}
    {% endfor %}
</div>
