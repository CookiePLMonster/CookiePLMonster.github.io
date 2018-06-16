---
layout: page
title: Mods
subtitle: My modifications for various games. This page is in very early stages, will be expanded and made prettier soon.
feature-img: assets/img/free_cookie_texture_by_designercow-d4zkzjg.jpg
permalink: /mods/
bootstrap: true
---
 
<div class="posts">
  {% assign items = site.mods | sort: 'mod_order' %}
  {% for mod in items %}
  <div style="border-bottom:1px solid rgba(0,0,0,0.1)">
      <h1>
          {{ mod.title }}
      </h1>
      <div class="excerpt">
        {{ mod.content }}
      </div>
  </div>
  {% endfor %}
</div>