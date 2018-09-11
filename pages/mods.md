---
layout: page
title: "Mods & Patches"
subtitle: My modifications and patches for various games. This page is in very early stages, will be expanded and made prettier soon.
feature-img: assets/img/free_cookie_texture_by_designercow-d4zkzjg.jpg
permalink: /mods/
bootstrap: true
---
 
<div class="posts">
  {% assign items = site.mods | sort: 'mod_order' %}
  {% for mod in items %}
  <div style="border-bottom:1px solid rgba(0,0,0,0.1)">
      <h1 id="{{ mod.id | split: '/' | last }}">
          {{ mod.title }}
      </h1>
      <div class="excerpt">
        {{ mod.content }}
      </div>
  </div>
  {% endfor %}
</div>