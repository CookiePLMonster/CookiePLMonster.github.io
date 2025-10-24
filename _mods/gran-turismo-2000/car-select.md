---
title: Car Select
game-series: "gran-turismo-2000"
order: 0
date: 26-07-2025
---

{::options auto_id_prefix="{{ page.id | split: '/' | last }}-" /}

{:.disclaimer.info}
This patch is shipped with PCSX2 starting with v2.5.247.

{:.credit}
Built upon the original research of **Xenn765**.

This patch adds a full car select feature to the game, allowing the players to choose from a list of six cars:
* Lancer Evolution V GSR '98 (the default car)
* Toyota Altezza RS200 '98
* Subaru Legacy B4 RSK '98
* Mazda RX-7 Type RS '98
* Nissan Skyline GT-R V-spec (R34)
* Honda NSX Type S ZERO (J)

## Features

* Lets users select the car in-game with DPad left/right.
* Features all available colors for each car. Although AI drivers always used fixed colors, all car models feature a selection of colors taken straight from Gran Turismo 2.
  Notably, Honda NSX has 12 available colors, which is quite a bit compared to Evo V's 5 available colors!
* Keeps the starting grid unchanged, so the player starts in the 6th position regardless of their car of choice.
* Remembers the selected car after the race, like the stock game does with the selected color.
* Makes the selection look fully native by including a fade-out effect when selecting cars, much like in Gran Turismo 3.
* As UI assets for other cars are not present in the files, Lancer Evo badges, performance characteristics, and color names are hidden for other cars.

{% include figures/video.html link="https://i.imgur.com/OGVFrYv.mp4" attributes="controls"%}

{% include setup-instructions.html platform="ps2" %}

***

<a {% include buttons/github-blob-url.html repo="CookiePLMonster/Console-Cheat-Codes" path="master/PS2/Gran%20Turismo%202000/Car%20select/PAPX-90203_55CE5111_carselect.pnach" %} class="button">{% include elements/flag.html flag="jp" %} NTSC-J</a>

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/tree/master/PS2/Gran%20Turismo%202000/Car%20select" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
