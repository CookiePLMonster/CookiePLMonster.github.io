---
title: SilentPatch
title-image: "assets/img/mods/silentpatch-gta.png"
order: -100
game-series: "gta-vc"
excerpt: "Fixes countless issues in your favorite game."
date: 2-11-2024
---

SilentPatch for the 3D-era Grand Theft Auto games is the first and flagship release of the "SilentPatch family", providing numerous fixes for this beloved franchise.
SilentPatch addresses a wide range of issues, from critical fixes for crashes and other blockers to various major and minor improvements identified by
the passionate community in these games over decades. SilentPatch does not alter the core gameplay experience, making it an optimal choice
for both first-time players and the old guard returning for yet another playthrough.

## Featured fixes

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file. These options are enabled by default unless stated otherwise.

### Critical fixes
Compatibility issues, crashes, progression blockers.

* Fixed an issue where installing the game on `A:` or `B:` drive made the game ask for the CD.
* The mouse should not lock up randomly when exiting the menu on newer systems anymore.
* The mouse will no longer go beyond the game window dimensions, making it possible to play the game on multi-monitor setups without problems.
* More precise frame limiter, reducing lag spikes a bit when playing with Frame Limiter on.
* The game now performs a bit better on high FPS. It doesn't freeze on fadeouts anymore, although it still has issues with car physics, gravity, and sounds. Therefore it's still recommended to play with the Frame Limiter set to ON.
* DirectPlay dependency has been removed -- this should improve compatibility with Windows 8 and newer.
* The game will not crash on startup if Data Execution Prevention is enabled for all applications anymore.
* The "<samp>Cannot find enough available video memory</samp>" error showing on some computers has been resolved.
* Path to the User Files directory is now obtained using a dedicated API call rather than a legacy registry entry, future-proofing the games more.
* Fixed an issue that would cause games to freeze if III/VC/SA were running at the same time.

### Other fixes
All the remaining, non-critical fixes.

* The mouse vertical axis sensitivity now matches horizontal axis sensitivity.
* The mouse vertical axis does not lock during camera fade-ins now.
* Wet road reflections render properly again (just like with Road Reflections Fix).
* Reintroduced light glows under weapon/health/armor pickups, bribes, hidden packages, and money pickups -- they showed only on PS2 due to a bug in all PC versions.
* Corrected crime codes for police dispatch audio -- police dispatch now refers to player crimes correctly.
* Fixed a bug causing cheat-spawned melee weapons to be forcibly replaced by other melee weapons upon walking into a pickup.
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works properly.
* Some car panels now are detached after the car's explosion (like they were meant to be but the code forcibly fixed them immediately after damage).
* Metric-to-imperial conversion constants have been replaced with more accurate ones.
* Pathfinding for cars chasing the player has been improved.
* Bombs in cars stored in garages now save properly.
* Car generator counters now work properly for generators with a fixed number of spawns.
* Extras on bikes now behave correctly, following bike lean and not floating in the air.
* Keyboard input latency decreased by one frame.
* Fixed corona lines rendering on non-NVIDIA graphics cards.
* Corrected FBI Washington siren sound.
* Fixed a glitch allowing lightless taxis to spawn in traffic.
* Allowed extra6 parts to be picked when a random extra is to be picked.
* Made Drive-By use the correct sounds based on what machine gun is used.
* Some props in Malibu Club, Ocean View Hotel, and Pole Position Club have been restored; more environment shows outside when the player is in the interior too (just like on PS2).
* All text shadows, onscreen counter bar shadows, and the loading screen outline now scale to resolution correctly.
* The trace (Destination) blip outlines are now scaling to the resolution properly.
* The radar's horizontal position, the disc texture, and the shadow now scale to resolution correctly. The radar disc was also shrunk slightly to fix gaps and make the icons sit better on the edge.
* Credits now scale to resolution correctly.
* Mission title and 'Mission Passed' texts now stay on screen for the same duration, regardless of screen resolution.
* The inner padding of the text boxes with a background now scales to resolution correctly.
* The vertical offset of the weapon name text in Ammu-Nation now scales to resolution correctly.
* The downward-pointing destination blip in the Map Legend now displays with a correct outline.
* `FILE_FLAG_NO_BUFFERING` flag has been removed from IMG reading functions -- speeding up streaming.
* Free resprays will not carry on a New Game now.
* Fixed ambulance and firetruck dispatch timers -- they reset on New Game now.
* The rain stream effect on roads, which displays for a short period after the rain stops, now resets on loading a save. This prevents the effect from showing when the weather in the loaded save is sunny.
* Adjusted the probability of traffic vehicles turning on their lights to match the PS2 version, including a low chance that they may never turn them on.
* Fixed an issue where vehicles exploded twice if the driver left the car before the explosion.
* Script randomness is now 16-bit instead of 15-bit.
* Lines read in `CPlane::LoadPath` and `CTrain::ReadAndInterpretTrackFile` are now null-terminated, fixing issues with plane/yacht paths under specific conditions in a modded game.
* Environment mapping is now applied to vehicle extras.
* Mouse sensitivity is no longer reset on starting a New Game.
* Asset money pickup text has been given a generic red color, resolving a bug where it changed colors every frame.
* Fixed an issue where the minigun pickup had a bright pink glow instead of a purple one, and had an additional white glowing spot on the barrel.
* Fixed an issue where the muzzle flashes from guns faced the wrong direction (contributed by **Wesser**).
* Fixed an issue where looking at a shopkeeper while using Classic controls counted as aiming at them (contributed by **Wesser**).
* Fixed the LOD model of the construction site displaying underneath the damaged building model after "Demolition Man".
* Fixed the "Greetings from Vice City" outro splash displaying longer than intended -- now displays for 2.5 seconds.
* Fixed an issue where Tommy wouldn't shake his fist at incoming traffic when holding Brass Knuckles, yet would do it when holding a chainsaw.
* Fixed an issue where Tommy wouldn't shake his fist at stopped traffic when holding any weapons introduced in Vice City.
* Hitting vehicles and objects with a screwdriver now produces an impact sound.
* Pedestrians and Tommy are now much more talkative, like in the PS2 version (integrated Ped Speech Patch from **Sergeanur**).
* Tear gas can now deal damage to Tommy and other mission characters, like in the PS2 version.
* <i class="fas fa-cog"></i> Fixed siren corona placements in Police, Firetruck, Ambulance, Enforcer, Vice Cheetah, and FBI Washington.
* <i class="fas fa-cog"></i> Added siren corona to FBI Washington.
* <i class="fas fa-cog"></i> Fixed taxi light corona placement for Taxi.
* <i class="fas fa-cog"></i> Fixed police chopper's searchlight and red tail light placement.
* <i class="fas fa-cog"></i> Fixed numerous model glitches by disabling backface culling on detached vehicle parts, ped models, and a subset of map models specified in the INI file.

### Enhancements
Any changes that don't strictly fix game bugs.

* If the settings file is absent, the game will now default to your desktop resolution instead of 640x480x16.
* All censorships from German and French versions of the game have been removed.
* <i class="fas fa-cog"></i> Made the game select metric/imperial units based on system locale settings.
* <i class="fas fa-cog"></i> Sliding mission titles and odd job texts from the GTA III beta can now be re-enabled (off by default).
* <i class="fas fa-cog"></i> An unused 'Minimal HUD' feature can now be re-enabled (off by default).

***

## Credits

SilentPatch includes code contributions from:
* aap
* B1ack_Wh1te
* DK22Pac
* Fire_Head
* Nick007J
* NTAuthority
* Sergeanur
* spaceeinstein
* Wesser

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/SilentPatchVC.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>
<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/SilentPatchDDraw.zip" class="button">{{ site.theme_settings.download_icon }} Download DDraw Component</a>

<a href="https://github.com/CookiePLMonster/SilentPatch" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>

<a href="https://gtaforums.com/topic/669045-silentpatch/" class="button forums" target="_blank">{{ site.theme_settings.gtaf_icon }} Discuss on GTAForums</a>
