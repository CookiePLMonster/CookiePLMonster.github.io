---
title: "SilentPatch & Enhanced PC Demo"
game-series: "juiced-demo"
excerpt: "Experience Acclaim Demo to its fullest."
date: 21-10-2023
---

{% assign juiced_modding_community_link = "[**Juiced Modding Community**](https://discord.com/invite/pu2jdxR/)" %}
{% assign f4mi_link = "[**f4mi**](http://f4mi.com/)" %}

In this first-ever demo-oriented SilentPatch, I target all demo releases of Juiced. Due to this game's troubled development cycle,
demos published under Acclaim Entertainment present a state of the game that is noticeably different from the final game from THQ.
For this reason, I see value in SilentPatch improving the technical state of those demos (including the THQ ones) and unlocking all content included in them.
These early demos are a showcase of Juiced that "never came to be", so I want everyone to enjoy them to the fullest.

## Featured fixes:

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.

### Acclaim Demos
* <i class="fas fa-cog"></i> All shipped content has been unlocked. This increases the amount of in-game content from 1 route in the Race mode and 3 selectable cars to:
  * 4 selectable cars.
  * 4 routes in the Race mode + reverse variants + 1 Point-to-Point race.
  * Sprint race.
  * Showoff (Cruise) mode.
  * Solo mode.
* <i class="fas fa-cog"></i> Widescreen from the console builds has been re-enabled and further improved. The default widescreen option slightly distorts the aspect ratio and appears horizontally squashed compared to 4:3. SilentPatch corrects this and additionally supports arbitrary aspect ratios, which means ultra widescreen now looks as expected.
* All known compatibility issues have been fixed. `JuicedConfig.exe` no longer needs Windows XP SP2 compatibility mode to run.
* Fixed an issue with menus and UI items flickering randomly.
* Fixed an issue with the race background music distorting and crackling at regular intervals.
* <i class="fas fa-cog"></i> All menus can optionally be made accessible. Consider this a debug/testing option, since most menus that are locked are not finished and will softlock or crash the game.
* 3 teaser videos from the May demo have been included and re-enabled.
* The laps limit has been lifted from 2 to 6, like in the console prototype builds from a similar timeframe.
* In night and wet races, the limit of on-track cars has been lifted from 4 to 6.
* <i class="fas fa-cog"></i> The default driver name `Player1` can now be overridden.
* May 2004 Demo can now be quit by pressing <kbd>Alt</kbd> + <kbd>F4</kbd>.
* All game settings have been moved from registry to `settings.ini`. This makes demos fully portable and prevents them from overwriting each other's settings.

### THQ Demos
* <i class="fas fa-cog"></i> All shipped content has been unlocked. Since these demos don't include Custom Races, customization is done through the `SilentPatchJuicedDemo.ini` file and concerns only the second race. The following options are available:
  * 4 routes in the Race mode + reverse variants + 1 Point-to-Point race + its reverse variant.
  * Sprint race.
  * Showoff (Cruise) mode.
  * Solo mode.
  * Customizable time of day, weather, number of laps, and number of AI opponents.
* <i class="fas fa-cog"></i> Demos have optionally been made endless. Instead of the game exiting after the second race, it returns to the garage and gives an option of tuning the car again and starting another race.
* The player's starter car can now be customized by editing the `scripts\CMSPlayersCrewCollection2.txt` file. The following cars are available: `gtr`, `nsx`, `supra`, `vette_zo6`, `viper`.
* A startup crash in the January 2005 demo occurring on PCs with more than 4 logical CPU cores has been fixed.
* `Juiced requires virtual memory to be enabled` error from the April and May 2005 demos has been fixed.
* Startup crashes in the May 2005 demo occurring when the OS locale is set to Czech, Polish or Russian have been fixed.
* `JuicedConfig.exe` no longer needs Windows XP SP2 compatibility mode or a Windows compatibility shim to run. This improves compatibility with environments where compatibility shims are not enabled by default, e.g. on Wine/Proton.
* <i class="fas fa-cog"></i> All menus can optionally be made accessible. Consider this a debug/testing option, since most menus that are locked are not finished and will softlock or crash the game.
* <i class="fas fa-cog"></i> The default driver name `Player` can now be overridden.
* <i class="fas fa-cog"></i> Starting money can be adjusted.
* All game settings have been moved from registry to `settings.ini`. This makes demos fully portable and prevents them from overwriting each other's settings.


## Credits
* {{ f4mi_link }} for preparing the showcase video
* {{ juiced_modding_community_link }} for helping me find and dissect those demos and for answering all of my many questions regarding the game

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/Juiced_xjBpXHGWs2.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_xjBpXHGWs2.jpg" %}
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/Juiced_yL91hpKxkJ.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_yL91hpKxkJ.jpg" %}
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/Juiced_zzGrgkY8YT.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_zzGrgkY8YT.jpg" %}
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/Juiced_nesTl97B8u.png" thumbnail="/assets/img/posts/juiced-research/screens/thumb/Juiced_nesTl97B8u.jpg" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/jan-2005-viper.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/jan-2005-viper.jpg" %}
{% include figures/image.html link="/assets/img/posts/juiced-research/screens/jan-2005-sprint.jpg" thumbnail="/assets/img/posts/juiced-research/screens/thumb/jan-2005-sprint.jpg" %}
</figure>

{% include figures/video-iframe.html link="https://www.youtube.com/embed/4lQ76h8KEkI" %}

## Installing Acclaim Demos {#acclaim-install}

By default, June 2004 and July 2004 demos' installers don't include an option to change the installation directory and instead, they always install the game to
`C:\Program Files (x86)\Acclaim Entertainment\JuicedDemo`. **Destination Folder Transform** modifies the installer flow to re-enable
the Destination Folder screen.
{% include figures/image.html thumbnail="/assets/img/posts/juiced-research/msiexec_HaLbpb5KTv.png" style="natural" %}
To use it, extract the archive to the directory where the installer is, and run it via `run.bat`.

{% include setup-instructions.html %}

<a href="https://github.com/CookiePLMonster/SilentPatchJuicedDemo/releases/latest/download/SilentPatchJuicedDemo.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download SilentPatch</a>
<a href="https://github.com/CookiePLMonster/SilentPatchJuicedDemo/releases/latest/download/InstallerDestinationFolderTransform.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download Installer Destination Folder Transform</a> \\
<a href="https://github.com/CookiePLMonster/SilentPatchJuicedDemo" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
