---
title: Dynamic Day/Night Cycle
game-series: "tokyo-xtreme-racer-2025"
excerpt: "Fully dynamic time of day."
date: 04-02-2025
---

This Lua script enables a full day/night cycle in the Ultra Dynamic Sky UE5 plugin, used by the game.

## Features

* Full 24-hour day/night cycle with realistic sunrise and sunset times reflecting the path of the sun in real-life Tokyo.
* Adjustable simulation speed, by default configured to 30x speed (1 real second = 30 in-game seconds).
* An option to synchronize the in-game time with the system clock.
* "Dusk-Night-Dawn" mode, where the simulation loops only through the night.
* Randomized clouds/fog each night.
* Persisted time of day and weather in Parking Areas. The time resets only once the player returns to the garage.
* An option to freeze time with <kbd>Alt</kbd> + <kbd>F</kbd>.
* Fully compatible with manual time/weather adjustments done by Car_Killer's [Time of Day/Weather Control script](https://gist.github.com/PrzemekWolw/d1c79bc9822b30c12a1bf03d1f568f9e){:target="_blank"}.

## Credits
* [Car_Killer](https://github.com/PrzemekWolw){:target="_blank"} - the original Time of Day/Weather Control script

<figure class="media-container small">
{% include figures/image.html link="https://i.imgur.com/I1VoWCX.jpg" thumbnail="https://i.imgur.com/I1VoWCXh.jpg" %}
{% include figures/image.html link="https://i.imgur.com/zgQZC1G.jpg" thumbnail="https://i.imgur.com/zgQZC1Gh.jpg" %}
{% include figures/image.html link="https://i.imgur.com/DYYKHS6.jpg" thumbnail="https://i.imgur.com/DYYKHS6h.jpg" %}
{% include figures/image.html link="https://i.imgur.com/nXAxHUM.jpg" thumbnail="https://i.imgur.com/nXAxHUMh.jpg" %}
</figure>

{% include figures/video-iframe.html link="https://www.youtube.com/embed/7y1ftTF0ZZs" %}

# Setup instructions

1. Download UE4SS and extract the archive to `TokyoXtremeRacer/Binaries/Win64` in the game directory. You **must** use the UE4SS version from this page, as it contains multiple fixes
   essential for this mod to work that are not yet part of the mainline UE4SS.
2. Download Dynamic Day/Night Cycle and extract the archive to `TokyoXtremeRacer/Binaries/Win64/ue4ss/Mods` in the game directory.
   This directory was extracted from the UE4SS archive in the previous step.
3. To adjust the configuration options, open `TokyoXtremeRacer/Binaries/Win64/ue4ss/Mods/TXR_DayNightCycle\scripts\main.lua` with Notepad and reconfigure
   the variables at the very top of the script.

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/releases/latest/download/UE4SS-TXR25.zip" class="button">{{ site.theme_settings.download_icon }} Download UE4SS</a>
<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/releases/latest/download/TXR_DayNightCycle.zip" class="button">{{ site.theme_settings.download_icon }} Download Day/Night Cycle</a>

<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/blob/main/TXR_DayNightCycle/scripts/main.lua" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
