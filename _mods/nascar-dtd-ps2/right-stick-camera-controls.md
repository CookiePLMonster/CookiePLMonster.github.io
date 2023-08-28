---
title: Camera controls on the right stick
game-series: "nascar-dtd-ps2"
order: 1
date: 09-10-2021
---

When investigating the game's code for the shoulders mapping cheat, I noticed that NASCAR DtD (but not NASCAR Heat 2002 or Test Drive EoD)
still updates button mappings for Look Left/Look Right actions, albeit it always updates them with an empty mapping.
I looked into that more closely and found that these actions are fully functional but unused.
With this cheat, I replace the stock functionality of the right analog stick (Throttle/Brake) with key bindings to look around.

**Note: When "uninstalling" the cheat, please follow the instructions in the PNACH file!
Removing it without first making the code unmap the newly added controls will leave camera controls permanently mapped in the savegame.**

<div class="media-container small">
{% include screenshot.html link="/assets/img/posts/console-codes-2/nascar-lookaround-2.jpg" %}
{% include screenshot.html link="/assets/img/posts/console-codes-2/nascar-lookaround-1.jpg" %}
</div>

{% include setup-instructions.html platform="ps2" %}

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/blob/master/PS2/NASCAR%20Dirt%20to%20Daytona/Camera%20controls%20on%20right%20stick/2EA87CC5_lookaround.pnach" class="button" role="button" target="_blank">{{ site.theme_settings.us_flag }} NTSC-U</a>
