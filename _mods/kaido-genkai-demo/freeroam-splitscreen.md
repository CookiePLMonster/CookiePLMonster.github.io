---
title: Freeroam Split-Screen
game-series: "kaido-genkai-demo"
date: 09-06-2026
version: Build 1
---

{::options auto_id_prefix="{{ page.id | split: '/' | last }}-" /}

This Lua script enables a proof-of-concept split-screen mode in freeroam, for up to 4 players.

## Usage
* <kbd>Ctrl</kbd> + <kbd>Y</kbd> -- Spawn an additional player.
* <kbd>Ctrl</kbd> + <kbd>U</kbd> -- Despawn the last player.
* <kbd>Ctrl</kbd> + <kbd>Left Arrow</kbd>/<kbd>Right Arrow</kbd> -- Select the last spawned player's car.

## Known issues and limitations

* Two (or more) controllers are required. Keyboard + Gamepad are not supported.
* Performance may be sub-par, especially with more than 2 players.
* Light flares will look glitchy for the other players if the first player doesn't also see them on-screen.
* Only Freeroam is supported, and interactions with people in the world are disabled on purpose.
* Spawning the additional player in races **will** cause issues.

{% include figures/image.html thumbnail="assets/img/mods/kaido-genkai-freeroam-splitscreen/splitscreen.webp" %}

## Setup instructions

1. Download **UE4SS** and extract the archive to `KaidoGenkai/Binaries/Win64` in the game directory.
2. Download **Freeroam Split-Screen** and extract the archive to `KaidoGenkai/Binaries/Win64/ue4ss/Mods` in the game directory.
   This directory was extracted from the UE4SS archive in the previous step.
3. To adjust the configuration options, open `KaidoGenkai/Binaries/Win64/ue4ss/Mods/KG_SplitScreen/scripts/main.lua` with Notepad and reconfigure
   the variables at the very top of the script.

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/releases/latest/download/UE4SS-KG.zip" class="button">{{ site.theme_settings.download_icon }} Download UE4SS</a>
<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/releases/latest/download/KG_SplitScreen.zip" class="button">{{ site.theme_settings.download_icon }} Download Freeroam Split-Screen</a>

<a href="https://github.com/CookiePLMonster/UE4SS-Bakery/blob/main/KG_SplitScreen/scripts/main.lua" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
