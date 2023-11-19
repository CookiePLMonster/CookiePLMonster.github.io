---
title: "SilentPatch"
game-series: "ea-sports-wrc"
excerpt: "Fix graphical artifacts on GTX 10 series cards."
date: 22-11-2023
---

**<span style="white-space:nowrap"><i class="fas fa-info-circle"></i> At</span> the time of submitting this mod, this bug is listed in the official
[Known Issues](https://answers.ea.com/t5/General-Discussion/EA-SPORTS-WRC-Release-Notes/m-p/13145127/thread-id/559) list.
To avoid any unintended side effects in case a future patch fixes this bug officially, SilentPatch will auto-disengage and display uninstallation instructions
once the next official patch is <span style="white-space:nowrap">released. <i class="fas fa-info-circle"></i></span> \\
<span style="white-space:nowrap"><i class="fas fa-info-circle"></i> If</span> you are not using a GeForce 9 or 10 series graphics card or a Titan X Pascal,
this patch will not give you any <span style="white-space:nowrap">improvements. <i class="fas fa-info-circle"></i></span>**


EA Sports WRC launched with a graphical bug exclusive to GeForce GTX 9 and 10 series cards, causing the decals, driver numbers, and their names to render broken.
SilentPatch addresses this issue, and it also improves performance of the Livery Editor tenfold.

## Featured fixes:

* Broken liveries, driver numbers, and driver name stickers on GeForce GTX 9 and 10 series cards have been fixed.
* Performance issues in the Livery Editor on GeForce GTX 9 and 10 series cards have been fixed.

{% include figures/juxtapose.html left="/assets/img/posts/ea-wrc/screens/thumb/20231119194714_1.jpg" left-label="GTX 1070 (Default)"
                right="/assets/img/posts/ea-wrc/screens/thumb/20231119194407_1.jpg" right-label="GTX 1070 (SilentPatch)" %}

## Setting up SilentPatch
1. Extract the archive to the game directory, so the `d3d11.dll` file resides next to the `WRC.exe` file.
2. On Steam/EA App, add `-dx11` to the game's launch arguments.

{% include setup-instructions.html %}

<a href="https://github.com/CookiePLMonster/SilentPatchEAWRC/releases/latest/download/SilentPatchEAWRC.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download</a> \\
<a href="https://github.com/CookiePLMonster/SilentPatchEAWRC" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
