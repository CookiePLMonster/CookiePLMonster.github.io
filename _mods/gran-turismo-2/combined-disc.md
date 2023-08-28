---
title: "Combined Disc"
game-series: "gran-turismo-2"
excerpt: "Arcade and Simulation Modes on one disc."
order: 3
date: 08-03-2022
---

Gran Turismo 2, other than being one of the more fondly remembered installments of the franchise, has one unique aspect
not seen in any other Gran Turismo to date -- it's split between two discs.
This modification combines both discs for an ultimate and complete version of Gran Turismo 2.

<div class="media-container small">
{% include screenshot.html link="/assets/img/posts/gt2-combined/arcade-mode.jpg" %}
{% include screenshot.html link="/assets/img/posts/gt2-combined/gt-mode.jpg" %}
</div>

{% include video.html link="https://www.youtube.com/embed/jByvSCDQLdY" %}

Due to the nature of this mod, the setup process is slightly more involved than the usual:
1. Download the setup script. **Do note that GTVolTool used by this script is Windows only.**
2. Install **Python 3.8.0** or newer. If you don't have it installed yet, Python can be downloaded from here:
   * Standalone: <https://www.python.org/downloads/>
   * Microsoft Store: <https://www.microsoft.com/p/python-310/9pjpw5ldxlz5>
3. Run `setup.py` by double-clicking it like any other executable file. If due to your local setup the script does not run,
launch it with `python setup.py` or `python3 setup.py` in the Command Prompt.
4. Follow the on-screen instructions. The script will bring up a system file picker to select files by default, but this may be changed by starting the script with a `-t` parameter.
  Remember that you may easily "type" the full path to the file by dragging it to the command line window - it's useful for easily putting full paths to the Arcade and Simulation discs.
5. Wait for the setup to complete. Please be patient - it takes a while, as it needs to repack discs and the game assets.

## Version compatibility
The modification is compatible with all game versions, **except for NTSC-J v1.0**.

## Hardware compatibility
* PSP/PS Vita can use the full version of the mod in PBP format.
* On PS1, the full version is compatible with [XStation](https://castlemaniagames.com/products/xstation) and [PSIO](https://ps-io.com/).
  You should opt for the lightweight version (without FMVs) **only** if burning the image on a physical CD.

Combined Disc is also compatible with [RetroAchievements](https://retroachievements.org/game/11278)! Those using it for their GT2 playthroughs may safely move
to using the Combined Disc and achievements will continue to work as expected.

## Credits
* [Ash_735](https://twitter.com/Ash_735) - menu textures
* [DAGINATSUKO](https://daginatsuko.com/) - CD label

<a href="https://github.com/CookiePLMonster/GT2-Combined-Disc/releases/latest/download/GT2-Combined-Disc.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download</a> \\
<a href="https://github.com/CookiePLMonster/GT2-Combined-Disc" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a> \\
<a href="{% link assets/img/posts/gt2-combined/gt2-combined-disc-label.png %}" class="button" role="button">{{ site.theme_settings.download_icon }} CD label (4K)</a>
