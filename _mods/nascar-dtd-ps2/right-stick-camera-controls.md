---
title: Camera controls on the right stick
game-series: "nascar-dtd-ps2"
order: 2
date: 09-10-2021
---

{:.disclaimer.info}
When "uninstalling" this cheat, please follow the instructions in the PNACH file!
Removing it without first making the code unmap the newly added controls will leave camera controls permanently mapped in the savegame.

{:.disclaimer.info}
This patch is shipped with PCSX2 starting with v2.5.367.

When investigating the game's code for the shoulders mapping cheat, I noticed that NASCAR DtD (but not NASCAR Heat 2002 or Test Drive EoD)
still updates button mappings for Look Left/Look Right actions, albeit it always updates them with an empty mapping.
I looked into that more closely and found that these actions are fully functional but unused.
With this cheat, I replace the stock functionality of the right analog stick (Throttle/Brake) with key bindings to look around.

<div class="media-container small">
{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-lookaround-2.jpg" %}
{% include figures/image.html link="/assets/img/posts/console-codes-2/nascar-lookaround-1.jpg" %}
</div>

{% include setup-instructions.html platform="ps2" %}

***

<a {% include buttons/github-blob-url.html repo="CookiePLMonster/Console-Cheat-Codes" path="master/PS2/NASCAR%20Dirt%20to%20Daytona/Camera%20controls%20on%20right%20stick/SLUS-20441_2EA87CC5_lookaround.pnach" %} class="button">{% include elements/flag.html flag="us" %} NTSC-U</a>

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/blob/master/PS2/NASCAR%20Dirt%20to%20Daytona/Camera%20controls%20on%20right%20stick" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
