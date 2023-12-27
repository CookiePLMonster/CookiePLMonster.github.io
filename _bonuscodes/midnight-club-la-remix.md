---
layout: page
title: "Midnight Club: L.A. Remix"
subtitle: "Cheat Codes"
excerpt: "Cheat Codes for Midnight Club: L.A. Remix."
image: "assets/img/bonuscodes/midnight-club-la-remix.jpg"
order: 10
---

{% assign mcla_remix_cheats = site.data.cheat-codes['midnight-club-la-remix'] %}

<div class="bonuscodes-output">
    <div class="border tr"></div>
    <div class="content">
      <ul>
         {% for cheat in mcla_remix_cheats['cheats'] %}
            <li><b>{{ cheat.description }}:</b> <code>{{ cheat.name }}</code></li>
         {% endfor %}
      </ul>
    </div>
    <div class="border bl"></div>
</div>

Prototype-only cheat codes check against the prototype serial. They can be accessed once this check is patched out:
<div class="bonuscodes-output">
    <div class="border tr"></div>
    <div class="content">
      <ul>
         {% for cheat in mcla_remix_cheats['prototype-cheats'] %}
            <li><b>{{ cheat.description }}:</b> <code>{{ cheat.name }}</code></li>
         {% endfor %}
      </ul>
    </div>
    <div class="border bl"></div>
</div>

To unlock the prototype cheat codes in the final game builds, use the following cheats in [PPSSPP](https://www.ppsspp.org/) or in cwCheat on your PSP/PS Vita:
```
_S ULUS-10383
_G Midnight Club: L.A. Remix [US]
_C1 Unlock prototype cheats
_L 0x20067094 0x00000000

_S ULES-01144
_G Midnight Club: L.A. Remix [EU]
_C1 Unlock prototype cheats
_L 0x20067094 0x00000000

_S ULJS-00180
_G Midnight Club: L.A. Remix [JP]
_C1 Unlock prototype cheats
_L 0x20068A54 0x00000000

_S ULJM-05904
_G Midnight Club: L.A. Remix (Rockstar Classics) [JP]
_C1 Unlock prototype cheats
_L 0x20068A54 0x00000000
```
