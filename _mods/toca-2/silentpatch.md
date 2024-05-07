---
title: "SilentPatch"
game-series: ["toca-2"]
excerpt: "Fixed compatibility issues, full widescreen support, and more."
date: 09-05-2021
---

In the spirit of the initial purpose of SilentPatches, this release revisits an old game for once - TOCA 2 Touring Cars from 1998.
The patch corrects several compatibility issues with modern computers, previously requiring a manual fix, and adds full widescreen support.
Original issues have also been corrected, and I also added some quality of life improvements, bringing the game closer to what more modern
racing games can offer.

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.

## Featured fixes
* In-game timers have been rewritten to fix a freeze when starting the race or leaving the game, occurring on modern machines. Previously this issue required hex editing to work it around.
* The game now handles all arbitrary aspect ratios without the need for hex editing. Both the 3D elements and UI have been fully fixed for widescreen.
* The game now lists all available resolutions, lifting the limit of dimensions (originally up to 1600x1200) and the limit of 24 resolutions.
* HUD scaling has been made more consistent on high resolutions, so the UI now looks identical regardless of resolution.
* CD checks have been removed. When a Full installation is in use, the game now can be played without a CD, without the need to use a no-CD executable.
* Fixed multiple distinct crashes occurring when minimizing the game excessively.
* Fixed a crash when minimizing the game during a Support Car race. The crash happened because those cars don't have a name decal on the rear windshield.
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works properly.
* The process icon is now fetched from the toca2.exe file, giving the game an icon of a checkered flag.
* <i class="fas fa-cog"></i> Field of View can now be adjusted via the INI file, with separate values for external cameras and the two interior cameras. You can select any value in the 30.0 - 150.0 range.
* <i class="fas fa-cog"></i> HUD scaling and menu text scaling can now be adjusted via the INI file.
* <i class="fas fa-cog"></i> Metric/imperial units can now be freely switched via the INI file. The new default behaviour is to use the user's OS setting to determine whether to use metric or imperial, but the choice can also be overridden via the INI file.
* <i class="fas fa-cog"></i> In-car rearview mirrors now can be forced to show regardless of the HUD settings. This feature can be toggled via the INI file.
* <i class="fas fa-cog"></i> In-car rearview mirror resolution can now be changed via the INI file, up to 512x256. Do note that higher resolutions might make the game slow if dgVoodoo isn't used.
* <i class="fas fa-cog"></i> The center interior camera now uses a full range of steering animations and gear shifting animations, just like the main interior camera. This feature can be toggled via the INI file.
* <i class="fas fa-cog"></i> Driver's hands and the steering wheel can now be toggled on/off via the INI file independently. This feature might be useful for specific steering wheel setups to avoid a "duplicate steering wheel".

## Credits
* [AuToMaNiAk005](https://www.youtube.com/user/AuToMaNiAk005) - for his extremely useful widescreen/ultrawide tutorials I used as a base for my implementation of widescreen & high resolutions support

{% include figures/video-iframe.html link="https://www.youtube.com/embed/QVSzsOuwAA8" %}

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/SilentPatchTOCA2/releases/latest/download/SilentPatchTOCA2.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/CookiePLMonster/SilentPatchTOCA2" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
