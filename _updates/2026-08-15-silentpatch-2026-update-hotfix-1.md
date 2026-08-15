---
title: "GTA SilentPatch 2026 Update Hotfix #1"
game-series: ["gta-iii", "gta-vc", "gta-sa"]
---

The first hotfix for the 2026 update for [SilentPatch for the Grand Theft Auto games]({%link pages/silentpatch.md %}) is now out.
This hotfix includes a few new smaller fixes, and addresses several known issues introduced by the latest update,
**including a critical issue with the Purple Nines in GTA III still spawning after the mission**,
and fixes incompatibilities with multiple mods, most notably with Maxo's Vehicle Loader. Updating is strongly advised.

{:.flexible-buttons}
<a href="{% link _games/gta/gta-iii.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA III</a>
<a href="{% link _games/gta/gta-vc.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA Vice City</a>
<a href="{% link _games/gta/gta-sa.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download for GTA San Andreas</a>

**If in GTA III you used the latest build of SilentPatch and saved your game after finishing 'Rumble', Purple Nines persisted in your save.
Once you update SilentPatch, you may use this CLEO script to undo the damage caused by this issue. Simply put this CLEO script in your game,
load the affected save, then save again. After that, the script may be safely deleted:**

<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/PurpleNinesFix.cs" class="button">{{ site.theme_settings.download_icon }} Download CLEO repair script</a>

# New fixes
* *(GTA SA):* Trains can now be saved in garages, and the game no longer crashes when spawning stored trains.
* *(GTA SA):* SBFYSTR and SWFYSTR now have their correct voices.
* *(GTA SA):* The GANGS and CRIMES section names are no longer swapped when exporting stats to stats.html (contributed by **sndth**).
* *(GTA VC):* Fixed a memory corruption in the ice cream attractor effect generation function. This resulted in less customers getting generated in the Distribution mission.
* *(GTA III):* Two broken graffiti attractors in Portland now work correctly, so pedestrians can stare at them.
* *(GTA III):* Cutscene borders now scale to resolution correctly. This issue looked especially bad when `ConsoleBottomTextPlacements` was enabled.
* *(GTA III):* Colored big messages (seen in 'Uzi Money' and 'Espresso-2-Go') now fade properly.
* *(GTA III):* Cutscenes no longer repair engines of blown up cars.
* *(GTA III):* Entering the Ambulance no longer reduces the player's health if it's at over 100HP.

# Regression and mod compatibility fixes
* *(GTA SA):* Fixed a startup crash in SA-MP.
* *(GTA SA):* Cursor clipping fix is now disabled in SA-MP, which should fix issues with custom dialog boxes.
* *(GTA SA):* `SmallSteamTexts` no longer defaults to enabled in 1.0.
* *(GTA SA):* CJ's new shooting lines now work when **fastman92 Limit Adjuster** is installed.
* *(GTA SA):* The car dirt fix has been simplified to reduce changes to the game data structures. This ensures better compatibility with mods.
* *(GTA SA):* Characters no longer use the new "sprayed" pain sound when they're whipped by CJ holding the spray can, tear gas, or fire extinguisher.
* *(GTA III, GTA VC, GTA SA):* `UseDesktopRefreshRate` now only takes effect when no other mod changes the target refresh rate.
   This should improve compatibility with Framerate Vigilante.
* *(GTA VC):* Fixed a crash near water when **Maxo's Vehicle Loader** is installed.
* *(GTA III):* **Fixed a regression that caused Purple Nines to re-appear after finishing any mission, even after finishing 'Rumble'.**
* *(GTA III):* Fixed an oversize version number in the 1.1 and Steam executables.
* *(GTA III):* Improved LC01 detection.
