---
title: SilentPatch
title-image: "assets/img/mods/silentpatch-godfather.png"
game-series: "godfather"
excerpt: "Movies working flawlessly on Windows 10!"
date: 01-03-2018
---

This early 2006 game shipped with a movie player using an obscure DirectDraw feature - hardware overlays.
Unfortunately for users, Windows XP was the last OS to support those, so when Windows Vista came out
in late 2006, The Godfather would start crashing on launch! Every next Windows release followed,
so the only way to play this game without being forced to remove videos (and thus lose
some content) is to play on 2000 or XP!

SilentPatch aims to fix this annoyance, so now movie player works flawlessly on any operating system.
This is not the only fix included, however.

## Featured fixes:
### Crash and bug fixes
* Movie player has been rewritten to work on any operating system
* Game has been disallowed from writing registry keys to `HKEY_LOCAL_MACHINE` - those writes were
  relayed to VirtualStore, potentially creating hard to troubleshoot crashes

### Quality of life improvements
* In addition to making movie player usable, it now can be configured to preserve aspect ratio of
  displayed movies instead of stretching them. Refer to SilentPatchGF INI file for more details
* An option to skip intro movies has been added to SilentPatchGF INI file
* An option to change FPS cap has been added to SilentPatchGF INI file (game defaults to 30FPS, but
  it appears like using 60FPS does not cause any major issues)
* Log file has been relocated to main game directory - so game does not attempt to write to `C:\` when
  it crashes
* Game is now fully portable - dependency on installation path in registry has been removed
* Game now defaults to desktop resolution on the first launch - so it will not default to 800x600 anymore

<div align="center" class="video-container">
<iframe src="https://www.youtube.com/embed/tkCyBY5z5dc" frameborder="0" allowfullscreen></iframe>
</div>

<div class="container">
<div class="row form-group"><a href="https://github.com/CookiePLMonster/SilentPatchGF/releases/download/BUILD-1/SilentPatchGF.zip" class="btn btn-primary btn-lg" role="button">Download</a></div>
<div class="row form-group"><a href="https://github.com/CookiePLMonster/SilentPatchGF" class="btn btn-success btn-lg" role="button">See source on GitHub</a></div>
</div>