---
title: SilentPatch
game-series: "cmr-3"
excerpt: "Remastered edition of the game at home."
date: 27-07-2023
---

{% assign bekoha_link = "[Bekoha](https://twitter.com/Bek0ha){:target='_blank'}" %}
{% assign hd_ui_url = "https://bekoha.github.io/cmr3" %}
{% assign lostraniero_link = "[LoStraniero91](https://www.youtube.com/@LoStraniero91){:target='_blank'}" %}
{% assign pierre_terdiman_link = "[Pierre Terdiman](http://www.codercorner.com/blog){:target='_blank'}" %}
{% assign automaniak_link = "[AuToMaNiAk005](https://www.youtube.com/@AuToMaNiAk005){:target='_blank'}" %}


Developed right for the 20th anniversary of Colin McRae Rally 3, SilentPatch delivers more than just a set of fixes -- with full widescreen support,
numerous compatibility fixes, new technical features, Quality of Life improvements, and a scratch-made high definition UI optimized for 4K displays,
it brings an experience comparable to an unofficial remaster of this classic 2002 rally game.

## Featured fixes:

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file. The other new options have been added to in-game menus instead.

### Essential fixes:
* The game now lists all available display resolutions, lifting the limit of 128 resolutions and the 4:3 aspect ratio constraint.
* The game will now try to pick the closest matching resolution instead of crashing on startup if launched with an invalid resolution specified in the config.
* The game now defaults to desktop resolution on the first boot.
* Several issues related to the sun rendering have been fixed - sun flickering with anti-aliasing enabled has been fixed, and a consistent hitch when the sun was about to appear on screen was resolved.
* Fixed multiple distinct issues causing water reflections to appear either too dark or completely black.
* Fixed car shadows appearing overly sharp, or not appearing at all when anti-aliasing is enabled.
* Fixed a crash when switching between display adapters with different numbers of resolutions, and made the resolutions list automatically refresh when switching adapters, eliminating a possible crash.
* The game now handles arbitrary aspect ratios correctly - with all 3D elements and the entire UI fixed for widescreen and positioning dynamically.
* Fixed a possible out of bounds read when the supplied translation file did not contain all the strings the game needs (for example, when using the PL executable with EN data).
* Improved the overall precision of in-game timers.
* Fixed an issue where split-screen would not work correctly on modern PCs with fast enough CPUs unless the game was forced to use a single CPU core.

### Miscellaneous fixes:
* <i class="fas fa-cog"></i> Environment maps on cars now always reflect the sky, like on the PS2; making reflections look more natural and correcting an issue where the big TV screens displayed a grey sky.
* Line rendering now respects the display resolution, making line thickness proportional to resolution and improving their visibility.
* Half pixel issues have been corrected across the UI, improving the overall clarity of the interface, and fixing numerous issues where fullscreen backgrounds would leave a single pixel-wide line (or a seam in the middle) with multisampling enabled.
* Improved the visual consistency of numerous race UI elements.
* Improved the visual consistency of the digital tachometer by using a scissor feature for rendering, improving its accuracy and resolving a possible flicker.
* Support for texture replacements and new fonts has been improved - the game can now handle higher resolution assets without glitching.
* UI elements and fonts with sharp pixels now use nearest neighbor filtering instead of linear filtering for improved clarity.
* Improved the presentation of line boxes used e.g. in the onscreen keyboard and Car Setup, fixing gaps, overlapping lines, and misplaced fill.
* Legend lines on the Telemetry screen now fade out together with the rest of the menu.
* Fixed numerous spacing inconsistencies in menu texts.
* Fixed a broken split-screen Time Trial results screen (Czech executable only).
* Fixed "Player X has retired" texts going off the screen at resolutions above 640x480.
* Fixed an issue where the resolution change countdown went into negatives when fading out.
* Fixed an issue on wider aspect ratios where repeated menu entries would not fade correctly.
* Fixed an issue only showing in the Polish release where leaving the 'Co-driver's voice' screen would flicker the menu animations.
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works.
* Removed a debug feature where invalid codepoints flickered randomly.
* The error message displayed when the game fails to load specific game files now doesn't freeze the game and can be closed with <kbd>Alt</kbd> + <kbd>F4</kbd>.

### Enhancements:
* The game is now fully portable, as the settings have been redirected from the registry to the INI file.
* <i class="fas fa-cog"></i> Car shadows are now slightly sharper, matching the way they are rendered in Colin McRae Rally 2005.
* <i class="fas fa-cog"></i> Menu navigation on the gamepad has been remapped from the analog stick to the directional pad like it is in the console releases.
* New Graphics options added: Field of View (separate for external and internal cameras), Digital Tachometer, Vertical Split-screen.
* New Advanced Graphics options added: Windowed/borderless mode (fully resizable), Vertical Sync, Refresh Rate, Anisotropic Filtering.
* Changed the Bonus Codes URL to point towards [a cheat generator hosted by myself]({% link pages/bonuscodes.md %}){:target="_blank"} since the original URLs are not active anymore.
* Added an option to toggle the HUD by pressing <kbd>F5</kbd>.

### Language Pack:
* Added support for all official text translations used together - English, French, German, Spanish, Italian, Polish, and Czech.
* Added support for all official co-drivers together - English, French, German, Spanish, Polish (Janusz Kulig), Polish (Janusz Wituch), and Czech.
* Re-added support for Nicky Grist's pace notes in the Polish re-release.
* Revised some capitalization inconsistencies in all languages.
* Revised Italian translation.
* Included translation lines for all new menu options added by SilentPatch.

### HD UI - by Bekoha:
* Made with 4K resolution in mind.
* Font atlases remade using original fonts.
* Support for EFIGS, Polish and Czech languages.
* Banners redrawn for every stage.
* Majority of in-game UI elements replaced.

## Credits
* {{ bekoha_link }} for the entirety of the HD UI work and general support
* {{ lostraniero_link }} for improving the entire Italian translation
* {{ automaniak_link }} for his past efforts in fixing CMR3 for widescreen resolutions
* {{ pierre_terdiman_link }} for a [*Textured Lines In D3D*](https://www.flipcode.com/archives/Textured_Lines_In_D3D.shtml) code snippet
* Various people contributing new translation lines in German, French, Spanish, Italian, and Czech
* *abbydiode* and *Cpone* for additional testing
* Several ex-CMR3 developers who are aware of this project and were able to share their feedback 🙂

{% include video.html link="https://www.youtube.com/embed/ipXwyzwV9k0" %}

## Setting up the game & SilentPatch {#silentpatch-setup}
Please follow the following instructions **in order**:

{:start="0"}
0. Prepare your game executable for compatibility with SilentPatch:
   1. Make sure that you have an official 1.1 patch installed beforehand. If needed, you can download it from [PCGamingWiki](https://community.pcgamingwiki.com/files/file/2506-colin-mcrae-rally-3-patch/){:target="_blank"}. You need to re-apply this patch to your game if you've used an unofficial no-CD executable. DRM-free releases are already pre-patched.
   2. Download the `DRM-free Patcher`, extract it to the game directory and run `setup.bat` to patch your game executable to DRM-free. Follow the on-screen instructions.
1. Download `SilentPatch` and extract it to the game directory. Overwrite files if prompted.
2. _(Optional)_ Download the `Language Pack` and extract it to the game directory. Overwrite files if prompted.
3. _(Optional, Polish 2 CD release only)_ Download the `Nicky Grist Pack` and extract it to the game directory. **This is needed ONLY for the Polish 2 CD release, all the other versions
   include those files already!**
4. _(Optional, but strongly recommended)_ Download `HD UI (by Bekoha)` and extract it to the game directory. Overwrite files if prompted.

{% include setup-instructions.html %}

### Mandatory components:
<a href="https://github.com/CookiePLMonster/SilentPatchCMR3/releases/latest/download/SilentPatchCMR3.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download SilentPatch</a>
<a href="https://github.com/CookiePLMonster/SilentPatchCMR3/releases/latest/download/CMR3Patcher.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download DRM-free Patcher</a>

### Addons:
<a href="{{ hd_ui_url }}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download HD UI (by Bekoha)</a>
<a href="https://github.com/CookiePLMonster/SilentPatchCMR3/releases/latest/download/CMR3LanguagePack.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download Language Pack</a>
<a href="https://github.com/CookiePLMonster/SilentPatchCMR3/releases/latest/download/CMR3NickyGristPack.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download Nicky Grist Pack</a>

<a href="https://github.com/CookiePLMonster/SilentPatchCMR3" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
