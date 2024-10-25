---
title: SilentPatch
title-image: "assets/img/mods/silentpatch-gta.png"
order: -100
game-series: "gta-iii"
excerpt: "Fixes countless issues in your favorite game."
date: 25-10-2024
---

SilentPatch for the 3D-era Grand Theft Auto games is the first and flagship release of the "SilentPatch family", providing numerous fixes for this beloved franchise.
SilentPatch addresses a wide range of issues, from critical fixes for crashes and other blockers to various major and minor improvements identified by
the passionate community in these games over decades. SilentPatch does not alter the core gameplay experience, making it an optimal choice
for both first-time players and the old guard returning for yet another playthrough.

## Featured fixes

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file. These options are enabled by default unless stated otherwise.

### Critical fixes
Compatibility issues, crashes, progression blockers.

* Purple Nines Glitch has been fixed.
* The mouse will no longer go beyond the game window dimensions, making it possible to play the game on multi-monitor setups without problems.
* More precise frame limiter, reducing lag spikes a bit when playing with Frame Limiter on.
* The game now performs a bit better on high FPS. It doesn't freeze on fadeouts anymore, although it still has issues with car physics, gravity, and sounds. Therefore it's still recommended to play with the Frame Limiter set to ON.
* The game will no longer ask for a CD when all audio files are copied to the disk.
* DirectPlay dependency has been removed -- this should improve compatibility with Windows 8 and newer.
* The "<samp>Cannot find enough available video memory</samp>" error showing on some computers has been resolved.
* Path to the User Files directory is now obtained using a dedicated API call rather than a legacy registry entry, future-proofing the games more.
* Fixed an issue that would cause games to freeze if III/VC/SA were running at the same time.
* Fixed a crash after playing the game for a short amount of time without a sound card.

### Other fixes
All the remaining, non-critical fixes.

* In version 1.0, armor cheat is now <kbd>TORTOISE</kbd>.
* In version 1.0, <kbd>BOOOOORING</kbd> cheat now works properly.
* In version 1.0, the Stats menu now has the correct font.
* Mouse sensitivity is now properly saved -- like in the 1.1 and Steam versions.
* Headlight coronas now display properly (as they do on PS2, XBOX, and PC Steam versions).
* Rhino spawned via a cheat code doesn't stay on the map forever anymore.
* Blista can now be lifted by a car crusher crane -- instead, it cannot lift Coach.
* Shooting from M16 in 1st person mode now increments the bullets fired stat properly (so you can't make the Accuracy stat go over 100%).
* Wet road reflections render properly again (just like with Road Reflections Fix).
* Reintroduced light glows under weapon/health/armor pickups, bribes, hidden packages, and money pickups -- they showed only on PS2 due to a bug in all PC versions.
* The game will not create more than 32 blips at once now -- while this never happened in an unmodded game, it could have happened due to exploits and potentially corrupted the save.
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works properly.
* Some car panels now are detached after the car's explosion (like they were meant to be but the code forcibly fixed them immediately after damage).
* Metric-to-imperial conversion constants have been replaced with more accurate ones.
* Pathfinding for cars chasing the player has been improved (most notably, it may result in "Bait" being much more playable).
* Bombs in cars stored in garages now save properly.
* Car generator counters now work properly for generators with a fixed number of spawns.
* Keyboard input latency decreased by one frame.
* Fixed corona lines rendering on non-NVIDIA graphics cards.
* Corrected FBI Car secondary siren sound.
* Enlarged the bounding box of Catalina's chopper and the police chopper to prevent it from being cut off on screen edges.
* Fixed cranes and night windows disappearing when viewed from up close.
* Fixed a glitch allowing lightless taxis to spawn in traffic.
* All text shadows now scale to resolution correctly.
* Garage-related and rampage-related texts now scale to the resolution properly.
* The trace (Destination) blip is now scaling to the resolution properly.
* The radar's horizontal position and its disc texture now scale to resolution correctly, resolving color bleed issues at high resolutions.
* Credits now scale to resolution correctly, and they don't cut to an empty screen at the very end anymore.
* Mission title and 'Mission Passed' texts now stay on screen for the same duration, regardless of screen resolution.
* `FILE_FLAG_NO_BUFFERING` flag has been removed from IMG reading functions -- speeding up streaming.
* Free resprays will not carry on a New Game now.
* Fixed ambulance and firetruck dispatch timers -- they reset on New Game now.
* Timers reset on a New Game now.
* Cars can now turn right from one-way roads (contributed by **Nick007J**).
* Bilinear filtering is now applied to the player's skin.
* Adjusted the probability of traffic vehicles turning on their lights to match the PS2 version, including a low chance that they may never turn them on.
* Fixed an issue where vehicles exploded twice if the driver left the car before the explosion.
* Script randomness is now 16-bit instead of 15-bit. This fixes checkpoint paths in  "Bling-bling Scramble" and ambulance routes in "Plaster Blaster" having variations previously inaccessible on PC.
* Lines read in `CPlane::LoadPath` and `CTrain::ReadAndInterpretTrackFile` are now null-terminated, fixing issues with plane/train paths under specific conditions in a modded game.
* Environment mapping is now applied to vehicle extras. This gives Stinger a reflective, metallic roof.
* Pedestrians trying to dive to avoid an oncoming car now dive correctly to the side, rather than jumping towards the threat.
* Drivers now behave correctly when shot at. In the PC versions, they would always speed away, but now they can also do nothing, like in the PS2 version. Additionally, a third, previously inaccessible behavior where drivers abandon the car and flee on foot is now working correctly.
* Dodo keyboard controls are now active when the All Cars Fly cheat is enabled.
* Temporary pickups (like money) are now properly cleaned up if there are too many of them, fixing a possible object leak.
* Car reflections are now displayed correctly in the Steam version (integrated Steam Car Colour Fix from **Sergeanur**).
* Made Claude sit when riding in a Speeder, the same as **Fire_Head**'s SitInBoat. This change also applies to Skimmer if III Aircraft is installed.
* All FBI Kurumas now spawn in a dark grey color with unpainted bumpers, rather than pitch black.
* Detached limbs now have properly working LODs, instead of rendering the normal and low-detail models at the same time.
* Low Brightness options now load and save correctly, instead of reverting to overly bright values.
* Support for the `brakelights` dummy has been restored, allowing brake and reverse lights to work as they did in the PS2 version, rather than always sharing the same placement with the tail lights.
* <i class="fas fa-cog"></i> Fixed siren corona placements in Firetruck, Ambulance, and Enforcer.
* <i class="fas fa-cog"></i> Fixed taxi light corona placement for Taxi.
* <i class="fas fa-cog"></i> Fixed police chopper's searchlight placement.

### Enhancements
Any changes that don't strictly fix game bugs.

* If the settings file is absent, the game will now default to your desktop resolution instead of 640x480x16.
* All censorships from German and French versions of the game have been removed.
* <i class="fas fa-cog"></i> Made the game select metric/imperial units based on system locale settings.
* <i class="fas fa-cog"></i> Sliding mission titles and odd job texts from the GTA III beta can now be re-enabled (off by default).

***

## Credits

SilentPatch includes code contributions from:
* aap
* DK22Pac
* Fire_Head
* Nick007J
* NTAuthority
* Sergeanur
* spaceeinstein
* Wesser

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/SilentPatchIII.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>
<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/SilentPatchDDraw.zip" class="button">{{ site.theme_settings.download_icon }} Download DDraw Component</a>

<a href="https://github.com/CookiePLMonster/SilentPatch" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>

<a href="https://gtaforums.com/topic/669045-silentpatch/" class="button forums" target="_blank">{{ site.theme_settings.gtaf_icon }} Discuss on GTAForums</a>
