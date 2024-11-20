---
layout: page
title: "GTA SilentPatch 2024 Update Hotfix #1"
game-series: ["gta-iii", "gta-vc", "gta-sa"]
---

The first hotfix for [SilentPatch for the Grand Theft Auto games]({%link pages/silentpatch.md %}) is now out.
Includes a few new fixes, but most importantly, multiple fixes for regressions introduced in this update, and compatibility improvements with other mods and game versions.

# New fixes
* *(GTA SA):* Hydra's jet thrusters no longer randomly fail to appear (contributed by **B1ack_Wh1te**).
* *(GTA III, GTA VC):* The inner padding of the text boxes with a background now scales to resolution correctly. Build 33 introduced this fix in San Andreas, now it has been ported to the other two games too.
* *(GTA VC):* The vertical offset of the weapon name text in Ammu-Nation now scales to resolution correctly.
* *(GTA VC):* The downward-pointing destination blip in the Map Legend now displays with a correct outline.
* *(GTA VC):* Several more models have been added to the `DrawBackfaces` exclusion list.
* *(GTA III):* The position of the dialog question text in the main menu now scales to resolution correctly.

# Regression and mod compatibility fixes
* *(GTA SA):* Fixed a crash with the 1.0 EU executable when the resolution picker dialog was about to appear.
* *(GTA SA):* Fixed a crash when **Renderhook** was installed and the resolution picker dialog was about to appear.
* *(GTA SA):* Fixed the game losing keyboard focus if the resolution picker dialog was skipped.
* *(GTA SA):* The gamepad crosshair now also scales to resolution when aiming with melee weapons, not only guns.
* *(GTA SA):* Custom license plates no longer break if SilentPatch is installed through Modloader.
* *(GTA SA):* Map menu cursor no longer fails to reach the map edges when **Widescreen HOR+ Support** is installed.
* *(GTA SA):* Help text boxes no longer crash the game when **Widescreen HOR+ Support** is installed.
* *(GTA SA):* Wheels detaching from cars during explosions are now visible again.
* *(GTA SA):* "Burn And Lap" and "Cone Coil" driving school tests no longer leave several cones at the school yard.
* *(GTA VC):* Stallion's leather roof is no longer shiny if a stock car rendering pipeline is used (i.e. **SkyGfx** is not in use).
* *(GTA VC):* **plugin-sdk** is now aware of the radar placement changes made by SilentPatch. This fixes incompatibilities with **Interactive Pause Menu Map** and the **GPS Mod**.
* *(GTA III):* SilentPatch now loads correctly when **GPS Mod** is installed.
