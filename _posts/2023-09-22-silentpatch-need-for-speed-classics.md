---
layout: post
title: "SilentPatch for NFS2: Special Edition, NFS3: Hot Pursuit, NFS4: High Stakes and NFS: Porsche Unleashed"
excerpt: "Four classic games patched in one go."
thumbnail: "assets/img/posts/spnfs90s/sp-img.jpg"
feature-img: "assets/img/posts/spnfs90s/sp-img.jpg"
image: "assets/img/posts/spnfs90s/sp-img.jpg"
game-series: ["need-for-speed-2-special-edition", "need-for-speed-3", "need-for-speed-4", "need-for-speed-porsche"]
date: 2023-09-24 14:50:00 +0200
twitter: {card: "summary_large_image"}
tags: [Releases]
---

*TL;DR - if you are not interested in a brief explanation of the issues fixed by SilentPatch,
scroll down to the [**Download**](#changelog-and-download) section for a download link.*

***

Recently, after playing an emulated PS1 version of Need for Speed II with [RetroAchievements](https://retroachievements.org/game/17528),
I wished to revisit a PC version with an excellent [Modern Patch](https://web.archive.org/web/20220131033002/https://verokster.blogspot.com/2019/11/need-for-speed-ii-second-edition-patch.html)
from Verok. Although this patch fixes a wide array of compatibility issues, I still ran into problems -- I couldn't map any buttons on my Xbox One controller, although I could map
the analog stick and triggers. Troubleshooting this issue quickly snowballed into the process of finding (and fixing) more bugs, many of which turned out to be shared across multiple games.
Therefore, what was intended to be originally a patch for NFS2: Special Edition now spans four Need for Speed games:
* Need for Speed 2: Special Edition
* Need for Speed 3: Hot Pursuit
* Need for Speed: High Stakes (also known as Road Challenge)
* Need for Speed: Porsche Unleashed (also known as Porsche 2000)

Since Modern Patches exist for all four supported games, I didn't have to do much. However, during development I was also made aware of some issues **introduced**
by NFS2/Porsche Modern Patches (as far as we know, NFS3/NFS4 patches are spotless 🙂), so now I also patch the patch. *Yo dawg...*

# Highlights

* These old games are known to have issues with multicore CPUs. In the case of NFS3, Modern Patch fixes the race conditions and can run freely,
  but the other games didn't get this treatment so they're being limited to run to just one core. This can lead to performance issues even on modern PCs,
  as previously seen in [Scarface]({% post_url 2022-02-12-silentpatch-scarface-r2 %}) -- therefore, SilentPatch applies a similar approach to one previously used in Scarface.
  In NFS2SE and NFS4, only the "problematic" movie decoding threads are pinned to the same core as the main game thread, while the other threads are allowed to run freely.
  This results in a good compromise between stability and performance. \\
  By default, SilentPatch is set up to use the configuration file from Modern Patch, so if you use these two fixes together, you'll automatically get the best possible experience
  with SilentPatch reading the configuration file of Modern Patch and overriding its affinity changes to my own. However, if you wish to change it, SilentPatch reads a `SingleProcAffinity`
  setting from the INI file of the Modern Patch.

* NFS2: Special Edition has an issue (fixed in the sequels) where controller button mappings don't work with controllers reporting more than 15 buttons,
  although the game should be able to handle up to 32 buttons. This rendered my Xbox One controller partially unusable, as it reports 16 buttons.
  I fixed the issue and [documented it in the NFSIISE project](https://github.com/zaps166/NFSIISE/issues/104). As a bonus,
  I also made the game not close if a controller was disconnected during the race, as the sequels never did that.

* As good as NFS2SE's Modern Patch is, it unfortunately also introduced at least one issue. Online races became a sub-par experience because they were rendered as if they were
  a split-screen race:
  {% include figures/image.html link="/assets/img/posts/spnfs90s/split-screen.jpg"
    caption="This is a reconstruction, but this is exactly how online races used to look." %}
  SilentPatch hooks into Modern Patch (if installed) and patches this issue.

* Need for Speed: Porsche Unleashed can crash on some Windows 10/11 PCs while enumerating controllers on startup. Curiously, it's a rare case where the game did nothing wrong
  and the issue is a regression of the `dinput.dll` library introduced sometime during the Windows 10 lifecycle.
  This affects [many games using this version of the DirectInput library](https://www.pcgamingwiki.com/wiki/Swedish_Touring_Car_Championship#Game_crashes_and.2For_freezes_on_the_initial_splash_screen) and the fix is to use a DirectInput-to-DirectInput8 wrapper. In SilentPatch, I also took an alternate approach and fixed it
  by changing the device enumeration to only list gamepads, so the game does not require a wrapper to run. As a bonus,
  this also fixed an issue where the game enumerated... more than it should, even with `dinputto8`.
  For example, on my PC it would even enumerate USB audio and AIO devices:
  <blockquote class="twitter-tweet" data-align="center"><p lang="en" dir="ltr">Good job detecting my AIO as an input device, NFS Porsche <a href="https://t.co/WXxVCv2JKi">pic.twitter.com/WXxVCv2JKi</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1556361034549661696?ref_src=twsrc%5Etfw">August 7, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

# Changelog and download

This has only been a highlight of the most noteworthy issues. The full changelog for all supported games is as follows;
fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.

### Essential fixes:
* <i class="fas fa-cog"></i> Locked all (NFS3/NFS Porsche) or specific problematic threads (NFS2SE/NFS4) to one core, while allowing worker threads to use any CPU cores - combining good stability and performance. This option has to be enabled by adding `SingleProcAffinity=1` to an INI file named like the game's executable. This change is fully compatible with Modern Patches and overrides its single core-affinity solution.
* (NFS2SE) Fixed a potential race condition on starting the movie decoding thread.
* (NFS2SE) Fixed a bug preventing controller button mappings from working correctly with gamepads that report more than 15 buttons (such as the Xbox One controller).
* (NFS2SE) Fixed the game closing when the controller disconnects during the race.
* (NFS2SE, Verok's Modern Patch only) Fixed an issue where online races were displayed only on the top half of the screen as if they were split-screen races.
* (NFS Porsche) Fixed a startup crash due to DirectInput controller enumeration being broken under specific circumstances on Windows 10 and newer.
* (NFS Porsche) Fixed severe performance issues on Windows 10 and newer when rebinding controls.
* (NFS Porsche, Verok's Modern Patch only) Fixed unresponsive keyboard inputs after <kbd>Alt</kbd> + <kbd>Tab</kbd> during the race.
* (NFS Porsche, Verok's Modern Patch only) Fixed a severe memory leak in OpenGL1 and OpenGL3 thrash drivers occurring after every race.

### Miscellaneous fixes:
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works correctly.
* <kbd>Num Lock</kbd>, <kbd>Caps Lock</kbd>, and <kbd>Scroll Lock</kbd> don't get forcibly disabled on game launch anymore.
* (NFS2SE/NFS3/NFS4) Fixed issues with stuttery/unresponsive mouse cursor in menus when using mice with high polling rates.
* (NFS2SE/NFS3/NFS4) Fixed a controller polling bug resulting in potential incompatibilities with DirectInput wrappers such as Xidi.

### Enhancements:
* Pasting text into text boxes now works with <kbd>Ctrl</kbd> + <kbd>V</kbd>.

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly. Each game page also links to their respective Modern Patch,
which I strongly recommend using together with SilentPatch. That said, they are not mandatory and SP is compatible with stock games too.

{:.flexible-buttons}
<a href="{% link _games/need-for-speed/need-for-speed-2-special-edition.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for NFS2: Special Edition</a>
<a href="{% link _games/need-for-speed/need-for-speed-3.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for NFS3: Hot Pursuit</a>
<a href="{% link _games/need-for-speed/need-for-speed-4.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for NFS4: High Stakes</a>
<a href="{% link _games/need-for-speed/need-for-speed-porsche-unleashed.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for NFS: Porsche Unleashed</a>

After downloading, all you need to do is to extract the archive to the game's directory, and that's it! Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).


***

For those interested,
the full source code of the mod has been published on GitHub, so it can be freely used as a reference:
<a href="https://github.com/CookiePLMonster/SilentPatchNFS90s" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
