---
title: Shoulders control mapping
game-series: "test-drive-eod-ps2"
order: 0
date: 09-10-2021
info-label: BUNDLED
disclaimer-info: "This patch is shipped with PCSX2 starting with v1.7.5746."
---

NASCAR Heat 2002, the first PS2 game from Monster Games, shipped with 4 control schemes to choose from.
One of those control schemes was called "Shoulders", and mapped throttle/brake to <kbd>R2</kbd>/<kbd>L2</kbd>.
This translates really well to modern gamepads, allowing the player to use triggers for precise throttle control.

For unknown reasons, Test Drive: Eve of Destruction removed this control scheme.
What makes this decision even more puzzling is a fact that Test Drive EoD was also released on Xbox,
a console with pressure sensitive triggers in place of PS2's shoulder buttons!

With this code, I modified one of the alternate controls sets to swap <kbd>L1</kbd>/<kbd>R1</kbd> with <kbd>L2</kbd>/<kbd>R2</kbd>.

{% include figures/image.html link="/assets/img/posts/console-codes-2/td-shoulders.jpg" %}

{% include setup-instructions.html platform="ps2" %}

***

<a {% include buttons/github-blob-url.html repo="CookiePLMonster/Console-Cheat-Codes" path="master/PS2/Test%20Drive%20Eve%20of%20Destruction/Shoulders%20control%20mapping/SLUS-20910_5D0244D3_shoulders.pnach" %} class="button">{% include elements/flag.html flag="us" %} NTSC-U</a>

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/tree/master/PS2/Test%20Drive%20Eve%20of%20Destruction/Shoulders%20control%20mapping" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>