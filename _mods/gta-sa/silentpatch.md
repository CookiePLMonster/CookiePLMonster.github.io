---
title: SilentPatch
title-image: "assets/img/mods/silentpatch-gta.png"
order: -100
game-series: "gta-sa"
excerpt: "Fixes countless issues in your favorite game."
date: 2-11-2024
---

{::options auto_id_prefix="{{ page.id | split: '/' | last }}-" /}

SilentPatch for the 3D-era Grand Theft Auto games is the first and flagship release of the "SilentPatch family", providing numerous fixes for this beloved franchise.
SilentPatch addresses a wide range of issues, from critical fixes for crashes and other blockers to various major and minor improvements identified by
the passionate community in these games over decades. SilentPatch does not alter the core gameplay experience, making it an optimal choice
for both first-time players and the old guard returning for yet another playthrough.

## Featured fixes

Fixes marked with <i class="fab fa-steam-symbol"></i> are supported in 1.0, Steam, and Rockstar Games Launcher versions. Fixes without that symbol require 1.0.
Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file. These options are enabled by default unless stated otherwise.

### Critical fixes
Compatibility issues, crashes, progression blockers.

* <i class="fab fa-steam-symbol"></i> The 14ms frame delay has been removed. As a result, the game now locks properly on 30 FPS instead of 25 FPS.
* <i class="fab fa-steam-symbol"></i> More precise frame limiter, reducing lag spikes a bit when playing with the Frame Limiter on.
* <i class="fab fa-steam-symbol"></i> The mouse should not lock up randomly when exiting the menu on newer systems anymore.
* <i class="fab fa-steam-symbol"></i> DirectPlay dependency has been removed -- this should improve compatibility with Windows 8 and newer.
* <i class="fab fa-steam-symbol"></i> Path to the User Files directory is now obtained using a dedicated API call rather than a legacy registry entry, future-proofing the games more.
* <i class="fab fa-steam-symbol"></i> Fixed an issue that would cause games to freeze if III/VC/SA were running at the same time.
* <i class="fab fa-steam-symbol"></i> Fixed an occasional crash when minimizing the game while standing next to a mirror.
* <i class="fab fa-steam-symbol"></i> Fixed a crash on car explosions -- most likely to happen when playing with a multi-monitor setup.
* <i class="fab fa-steam-symbol"></i> Fixed a crash when entering advanced display options on a dual monitor machine after: starting the game on the primary monitor in maximum resolution, exiting, starting again in maximum resolution on the secondary monitor. The secondary monitor's maximum resolution had to be greater than the maximum resolution of the primary monitor.
* <i class="fab fa-steam-symbol"></i> Fixed an occasional crash occurring when standing next to escalators.
* <i class="fab fa-steam-symbol"></i> Fixed a crash occurring when the vending machine was continuously used for an extended period.
* <i class="fab fa-steam-symbol"></i> Fixed a streaming-related deadlock, which could occasionally result in the game being stuck on a black screen when entering or exiting interiors (this is the issue people used to fix by setting CPU affinity to one core).
* <i class="fab fa-steam-symbol"></i> A significant memory leak when taking photos with an in-game camera has been fixed.
* <i class="fab fa-steam-symbol"></i> Fixed a crash that occurred when mashing the replay button near groups of gang members holding items.
* <i class="fab fa-steam-symbol"></i> Fixed a crash that occurred when starting a cutscene after playing a replay where CJ wore different clothes from what he is currently wearing.
* <i class="fab fa-steam-symbol"></i> Fixed a crash that occurred when playing back a replay with CJ having a different body type (fat/muscular/normal) than his current one.
* Game timers now tick more accurately, making them not freeze if the framerate exceeds 1000 frames per second; in other words, this fixes occasional freezes on fadeouts if playing with the Frame Limiter off.
* A heap corruption in one place is now fixed (did not affect gameplay but could potentially make the game crash).
* Traveling far away from the map will no longer trigger the extra gang territories glitch, nor will it corrupt the Taxi Driver submission.
* A 1.0 no-DVD-only bug where recruiting gang members would stop working after activating a replay has been fixed (contributed by **Wesser**).
* Fixed a 1.01 only tiny memory leak which occurred every time the player switched a radio station.
* <i class="fas fa-cog"></i> The gym glitch ("You have worked out enough..." showing infinitely) has been fixed.
* <i class="fas fa-cog"></i> Saving in Madd Dogg's mansion will no longer trigger the missing basketball glitch.
* <i class="fas fa-cog"></i> Fixed an occasional soft lock in "Mountain Cloud Boys" -- the player will not freeze after arriving at the meeting anymore.
* <i class="fas fa-cog"></i> Possible soft lock in "Sweet's Girl" initial cutscene fixed.
* <i class="fas fa-cog"></i> Fixed a script error in how Driving and Bike Schools destroyed the cones used in lessons, where random objects from the map could be destroyed instead. This glitch was most famously known as the "Blackboard glitch" (contributed by **Wesser**).
* <i class="fas fa-cog"></i> Fixed a script error in "Air Raid" where the player's heavy weapon (like a minigun) would disappear after the mission.

### Other fixes
All the remaining, non-critical fixes.

* <i class="fab fa-steam-symbol"></i> The mouse's vertical axis sensitivity now matches the horizontal axis sensitivity.
* <i class="fab fa-steam-symbol"></i> The mouse's vertical axis does not lock during camera fade-ins now.
* <i class="fab fa-steam-symbol"></i> Fixed sun lens flare effect not appearing with AMD/Intel graphics cards.
* <i class="fab fa-steam-symbol"></i> Fixed an issue introducing graphical artifacts from ped animations with high RAM usage -- the so-called "streaming memory bug".
* <i class="fab fa-steam-symbol"></i> Fixed a bug causing cheat-spawned melee weapons to be forcibly replaced by other melee weapons upon walking into a pickup.
* <i class="fab fa-steam-symbol"></i> Some car panels now swing after the car's explosion (like they were meant to be but the code forcibly fixed them immediately after damage).
* <i class="fab fa-steam-symbol"></i> <kbd>Num5</kbd> is now bindable (like in the 1.01 patch).
* <i class="fab fa-steam-symbol"></i> Fixed a glitch where random cars would end up being impounded to the garage, replacing player's vehicles.
* <i class="fab fa-steam-symbol"></i> Impound garages can now only impound cars and bikes, as other vehicle types are either too big or cannot leave the garage.
* <i class="fab fa-steam-symbol"></i> A muzzle flash will now show up when firing the last bullet from the clip.
* <i class="fab fa-steam-symbol"></i> Script sprites now have bilinear filtering applied.
* <i class="fab fa-steam-symbol"></i> Car generator counters now work properly for generators with a fixed number of spawns.
* <i class="fab fa-steam-symbol"></i> Randomizer error causing peds not to spawn in some areas has been fixed.
* <i class="fab fa-steam-symbol"></i> Randomizer error causing prostitutes to be quiet during solicitation has been fixed.
* <i class="fab fa-steam-symbol"></i> Text boxes can now show together with a Mission Passed text.
* <i class="fab fa-steam-symbol"></i> Mirror reflection doesn't break with Anti-Aliasing enabled anymore.
* <i class="fab fa-steam-symbol"></i> With Visual FX Quality set to Very High, mirror reflection quality has been bumped.
* <i class="fab fa-steam-symbol"></i> The Anti-Aliasing option has been altered -- instead of listing 1, 2, and 3 options (which in fact are 2x/2x/4x MSAA), the game will now show proper MSAA values from 2x up to 16x (depending on max MSAA level supported by the graphics card).
* <i class="fab fa-steam-symbol"></i> Colliding with another car will now damage proper parts on both cars -- previously, both cars got damaged the same way.
* <i class="fab fa-steam-symbol"></i> Slightly reduced stencil shadows memory overhead.
* <i class="fab fa-steam-symbol"></i> Fixed an AI issue where enemies became too accurate after the player had been in the car earlier.
* <i class="fab fa-steam-symbol"></i> <kbd>Alt</kbd> + <kbd>F4</kbd> now works properly.
* <i class="fab fa-steam-symbol"></i> `FILE_FLAG_NO_BUFFERING` flag has been removed from IMG reading functions -- speeding up streaming.
* <i class="fab fa-steam-symbol"></i> Metric-to-imperial conversion constants have been replaced with more accurate ones.
* <i class="fab fa-steam-symbol"></i> Dancing minigame timings have been improved, now they do not lose accuracy over time depending on the PC's uptime.
* <i class="fab fa-steam-symbol"></i> Car generators placed in interiors are now placed correctly -- this 'unhides' two vehicles in Madd Dogg's mansion, which were always there but they were not visible.
* <i class="fab fa-steam-symbol"></i> Bombs in cars stored in garages now save properly.
* <i class="fab fa-steam-symbol"></i> Streaming has been greatly improved during Supply Lines mission (or more general, any time when using an RC vehicle) -- it now behaves as expected, as opposed to displaying LODs way too quickly.
* <i class="fab fa-steam-symbol"></i> The health triangle displaying when aiming at peds is now properly orientated (it's now upside down) for peds the player can recruit.
* <i class="fab fa-steam-symbol"></i> Setting a BMX on fire will no longer set CJ on fire.
* <i class="fab fa-steam-symbol"></i> Keyboard input latency decreased by one frame.
* <i class="fab fa-steam-symbol"></i> Coronas now properly rotate as the camera gets closer to them, like on the PS2.
* <i class="fab fa-steam-symbol"></i> Light shadows from fire now show up properly.
* <i class="fab fa-steam-symbol"></i> Fixed parachute animations.
* <i class="fab fa-steam-symbol"></i> "Keep weapons after wasted" and "keep weapons after busted" are now reset on the New Game.
* <i class="fab fa-steam-symbol"></i> Fixed a glitch allowing bikes without engines to spawn.
* <i class="fab fa-steam-symbol"></i> Allowed extra6 parts to be picked when a random extra is to be picked.
* <i class="fab fa-steam-symbol"></i> Fixed in-car camera mouse behavior when looking left/right/behind.
* <i class="fab fa-steam-symbol"></i> Steam and RGL versions have proper aspect ratios now.
* <i class="fab fa-steam-symbol"></i> Steam/RGL versions will now default Steer with Mouse option to disabled, like in 1.0/1.01.
* <i class="fab fa-steam-symbol"></i> Wind animations now apply to CJ's clothes when driving a Quadbike (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Quadbike's handlebar movement now matches CJ's steering animations when driving at low speeds (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Fixed the sitting radio station change animation playing in boats where CJ stands upright (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Pickups, car generators, and stunt jumps spawned through the text IPL files now reinitialize on a New Game. Most notably, this fixes several pickups (like fire extinguishers) going missing after starting a new game.
* <i class="fab fa-steam-symbol"></i> Fixed crosshair issues when the sniper rifle is equipped and a photo is taken by a gang member (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Fixed an issue where biker cops kept shooting at the player even after losing the wanted level.
* <i class="fab fa-steam-symbol"></i> Fixed an SCM interpreter issue where a request to spawn a biker cop with a type `PEDTYPE_COP` spawned a normal cop instead (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Racing checkpoints are now correctly colored even if no enex markers were displayed on-screen before.
* <i class="fab fa-steam-symbol"></i> Adjusted the probability of traffic vehicles turning on their lights to match the PS2 version, including a low chance that they may never turn them on.
* <i class="fab fa-steam-symbol"></i> Fixed an issue where vehicles exploded twice if the driver left the car before the explosion.
* <i class="fab fa-steam-symbol"></i> Script randomness is now 16-bit instead of 15-bit.
* <i class="fab fa-steam-symbol"></i> Fixed black shooting stars, they are now white as originally intended.
* <i class="fab fa-steam-symbol"></i> Improved the behavior of exploded cars losing their wheels -- now the car sinks from the side of the detached wheel instead of always sinking from the front left side. The rear right wheel can now also be detached during an explosion.
* <i class="fab fa-steam-symbol"></i> Slightly improved the spawning logic of planes. While they can still crash after spawning, this should now occur less frequently.
* <i class="fab fa-steam-symbol"></i> Hovering with a jetpack is now possible using the keyboard controls by holding the next/previous weapon buttons simultaneously (<kbd>Q</kbd> + <kbd>E</kbd> by default).
* <i class="fab fa-steam-symbol"></i> In missions set during the riots, gang members in the player's group will no longer be targeted by the police helicopter, fixing a glitch where they'd abandon the player unexpectedly.
* <i class="fab fa-steam-symbol"></i> Fixed a bug where stealing the car from the passenger side while holding the throttle and/or brake button would kill the driver, or briefly resurrect them if they were already dead.
* <i class="fab fa-steam-symbol"></i> Credits now scale to resolution correctly.
* <i class="fab fa-steam-symbol"></i> Mission title and 'Mission Passed' texts now stay on screen for the same duration, regardless of screen resolution.
* <i class="fab fa-steam-symbol"></i> The heat haze effect now rescales correctly when changing the resolution in-game.
* <i class="fab fa-steam-symbol"></i> The underwater ripple effect is now consistent across all resolutions.
* <i class="fab fa-steam-symbol"></i> Heat-seeking missile crosshair and the weapon crosshair shown while aiming with a gamepad now properly scale to resolution.
* <i class="fab fa-steam-symbol"></i> The boundaries of the cursor on the Map screen, and the cursor itself now scale to resolution correctly (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> The inner padding of the text boxes with a background now scales to resolution correctly (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Nitrous will no longer regenerate faster when reversing the car (contributed by **Wesser**).
* <i class="fab fa-steam-symbol"></i> Hydra's jet thrusters no longer randomly fail to appear (contributed by **B1ack_Wh1te**).
* Detached vehicle parts will now keep the same color and lighting as the vehicle they came from.
* Detached vehicle parts are now rendered from both sides.
* Resolved single-pixel wide seams showing on the Map screen with Anti-Aliasing enabled.
* Several vehicles now have extra animated components: Phoenix hood scoops, Sweeper brushes, Newsvan antenna, radars on several boats, and extra flaps on Stuntplane and Beagle.
* Animated engine components on Bandito, BF Injection, and Hotknife will not animate if the engine is off.
* Firetruck (firela variant) now has a functional ladder -- it can be raised by moving the right analog stick down/pressing <kbd>Num2</kbd>.
* artict3 trailers can now be chained (as it was most likely intended since the model has a hook dummy which was not functional until now).
* Tug now has a functional tow bar (the model has a hook dummy which was not functional until now).
* DFT-30 left middle wheel now displays properly (the game now accepts a typo present in its hierarchy).
* Dumper's suspension is now animated (the game now accepts a typo present in its hierarchy).
* Uranus tail light coronas are now placed correctly, instead of lighting up in the car's interior (the game now accepts a typo present in its hierarchy).
* Stats counted in kilograms are now displayed correctly.
* 16:9 resolutions are now selectable (like in the 1.01 patch).
* Wet road reflections render properly again (just like with Road Reflections Fix).
* Hunter's interior does not disappear when viewed through the glass door panel.
* Weapons are now visible when viewed through a vehicle window.
* Holding a weapon will not cause some objects to be incorrectly lit anymore.
* Blown-up vehicles are now correctly colored and no longer shine (like in the 1.01 and Steam versions).
* Dirty cars are now able to get clean (like in the 1.01 patch).
* Each car has a unique number plate now.
* Custom number plates now show up correctly in all cases.
* Custom number plates are now also allowed on bikes.
* Number plates are now bilinear filtered, resulting in a smoother look.
* Vehicle lights do not get dark after being initially lit anymore (like on the PS2).
* Moonphases now show up correctly, like on the PS2 version (only when playing in 32-bit color mode).
* Toggling car lights on does not make windows invisible when viewed from inside anymore.
* Illumination value from timecyc.dat now accepts any float value in 0.0-2.0 ranges, not just 0.0, 1.0, and 2.0.
* In addition, if the illumination value is absent from the timecycle (like on a stock PC timecycle), the game will now default to 1.0.
* Lights now get cast on vehicles and peds properly -- previously, they would disappear under some conditions.
* Muzzle flash looks better now.
* Coronas no longer have a Z test forced all the time -- as a result, the sun glare now matches the original PS2 version.
* With User Tracks automatic scan enabled, MP3 playback will now work properly if QuickTime is not installed.
* PCM WAVE has been expanded to also accept additional profiles (Now 8/16/24bits, Mono/Stereo, and up to 48Khz).
* PCM WAVE files with an ID3-TAG will now also work with the game.
* Temple and Queens are now correctly called on the police scanner.
* Impound garages now function correctly, allowing the player to recover his last vehicle after it had vanished after a mission started.
* In addition, impound garages will now store the player's car when he's busted.
* The streamed entity list has been expanded a bit, so now the game world shouldn't flicker when looking down with high Draw Distance settings anymore.
* Mouse rotates an airborne car only with the Steer with Mouse option enabled.
* The Towtruck tow hitch does not get bugged after it has been fixed anymore.
* Plane doors don't corrupt after the plane has been fixed anymore.
* Fixing a plane will now reset its moving props to an undamaged state.
* Several vehicle components (most notably, Rumpo's front bumper and Bandito's moving prop) will not get glitched after the vehicle has been fixed anymore.
* Weapons and a jetpack now cast proper shadows.
* Crosshair doesn't mess up the weapon icon when on a jetpack anymore.
* Free resprays will not carry on a New Game now.
* Fixed ambulance and firetruck dispatch timers -- they reset on New Game now.
* Several stat counters now reset on New Game -- so the player will not level up quicker after starting New Game from a save.
* The "To stop Carl..." message now resets properly on New Game.
* Previously present only on the PS2, the 'Cars drive on water' cheat is now toggleable -- its string is <kbd>SEAROADER</kbd>.
* Very long loading times will now loop loading screens, as opposed to fading to white.
* Rhino does not gain extra wheels after being fixed anymore.
* Pushing pedestrians against the wall with a vehicle will not trigger passenger's voice lines anymore -- instead, now they are triggered when the player runs over pedestrians.
* Pay 'n Spray will no longer clean the car BEFORE the garage doors close -- now it cleans them while the car is hidden behind the garage door.
* Fixed a bug where paint jobs would vanish from cars stored in a garage if they were stored without looking at them.
* <i class="fas fa-cog"></i> Helicopter rotors and plane propellers now work correctly. They now have a blurring effect present in Vice City and the PS2 version of San Andreas.
* <i class="fas fa-cog"></i> Dual rear wheels now show up properly (Yosemite, Tanker, etc.).
* <i class="fas fa-cog"></i> Quadruple Stunt Bonus now works correctly.

### Enhancements
Any changes that don't strictly fix game bugs.

* <i class="fab fa-steam-symbol"></i> If the settings file is absent, the game will now default to your desktop resolution instead of 800x600x32.
* <i class="fab fa-steam-symbol"></i> When playing on Visual FX Quality higher than Low, the game will now cast up to 6 lights on each model both indoors and outdoors (on Low details, the game's stock behavior has been kept -- allowing up to 4 lights per model outdoors and 6 indoors).
* <i class="fab fa-steam-symbol"></i> Censorships from Steam and RGL versions for German players have been removed.
* <i class="fab fa-steam-symbol"></i> Remade the monitor selection dialog, adding several quality-of-life improvements -- such as remembering the selected screen, modern styling, and an option to skip the dialog appearing on every game launch.
* <i class="fab fa-steam-symbol"></i> The Steam/RGL version of the game will no longer reject 1.0/1.01 saves (still, a compatible SCM is needed for the save to work).
* <i class="fab fa-steam-symbol"></i> <i class="fas fa-cog"></i> Sliding mission titles and odd job texts from the GTA III beta can now be re-enabled (off by default).
* <i class="fab fa-steam-symbol"></i> <i class="fas fa-cog"></i> An unused 'Minimal HUD' feature can now be re-enabled (off by default).
* IMGs bigger than 4GB are now handled properly.
* User Tracks now supports the FLAC codec (Only 8/16/24bits, Mono/Stereo, and up to 48Khz).
* <i class="fas fa-cog"></i> EAX/NVIDIA splashes are now removed.
* <i class="fas fa-cog"></i> Subtitle and Radio text sizes can now be toggled between the original release and the updated Steam version.
* <i class="fas fa-cog"></i> Area name color now matches the gang color of the gang that owns that territory (off by default).
* <i class="fas fa-cog"></i> The "True Invincibility" option has been added -- with the option enabled, police helicopters will not hurt the player when they have an Invincibility cheat enabled (off by default).
* <i class="fas fa-cog"></i> Made the game select metric/imperial units based on system locale settings.
* <i class="fas fa-cog"></i> Sun reflections on peds and vehicles now change direction depending on the time of day, like in III and VC (off by default).

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

<a href="https://github.com/CookiePLMonster/SilentPatch/releases/latest/download/SilentPatchSA.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/CookiePLMonster/SilentPatch" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>

<a href="https://gtaforums.com/topic/669045-silentpatch/" class="button forums" target="_blank">{{ site.theme_settings.gtaf_icon }} Discuss on GTAForums</a>

Requires [ASI Loader](#asiloader) (or [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/latest/download/Ultimate-ASI-Loader.zip) for the Rockstar Games Launcher version).
