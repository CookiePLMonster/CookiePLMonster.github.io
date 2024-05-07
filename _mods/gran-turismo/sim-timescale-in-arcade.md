---
title: "Simulation timescale in Arcade"
game-series: "gran-turismo"
order: 1
date: 09-10-2021
---

American and European versions of Gran Turismo have a weird difference to the original Japanese release -- in those Arcade Mode is noticeably faster than the Simulation mode.
I investigated it and found that in these versions, Arcade Mode runs at 125% speed, although naturally without speeding up the in-game timer. With this code, Arcade Mode
is restored to 100% speed, just like in the Japanese version of GT1.

A clip from Submaniac93 illustrating the differences well:
{% include figures/video-iframe.html link="https://www.youtube.com/embed/x-HdmE6tF0A" %}

{% include setup-instructions.html platform="ps1" %}

***

<a {% include buttons/github-blob-url.html repo="CookiePLMonster/Console-Cheat-Codes" path="master/PS1/Gran%20Turismo/Sim%20timescale%20in%20Arcade/NTSC-U%201.1.cht" %} class="button">{{ site.theme_settings.us_flag }} NTSC-U 1.1</a>

<a {% include buttons/github-blob-url.html repo="CookiePLMonster/Console-Cheat-Codes" path="master/PS1/Gran%20Turismo/Sim%20timescale%20in%20Arcade/PAL.cht" %} class="button">{{ site.theme_settings.eu_flag }} PAL</a>

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/tree/master/PS1/Gran%20Turismo/Sim%20timescale%20in%20Arcade" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
