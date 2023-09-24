This modification addresses several numerous more or less several bugs in the classic Need for Speed games from the late 90s - starting from Need for Speed 2: Special Edition,
through Need for Speed: Porsche Unleashed. Since all those games already have their established unofficial patches, I concentrated my efforts on issues either omitted by those patches,
or (in the case of NFS2SE and NFS Porsche) caused by them.

{% case include.game %}
   {% when 'need-for-speed-2-special-edition' %}
      {% assign modern_patch_url = "https://community.pcgamingwiki.com/files/file/2448-need-for-speed-ii-second-edition-patch-by-verok-verokster-105/" %}
   {% when 'need-for-speed-3' %}
      {% assign modern_patch_url = "https://veg.by/en/projects/nfs3/" %}
   {% when 'need-for-speed-4' %}
      {% assign modern_patch_url = "https://veg.by/en/projects/nfs4/" %}
   {% when 'need-for-speed-porsche' %}
      {% assign modern_patch_url = "https://community.pcgamingwiki.com/files/file/2708-veroks-verokster-need-for-speed-v-porsche-unleashed-patch-v106/" %}
{% endcase %}

<i class="fas fa-info-circle"></i> **[Modern Patch]({{ modern_patch_url }}) is strongly recommended, although not mandatory. SilentPatch can work with or without it.{% if include.game == 'need-for-speed-porsche' %} Do note that with Modern Patch installed, multiplayer races don't work correctly and they crash very often.{% endif %}** <i class="fas fa-info-circle"></i>

## Featured fixes:

Fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.

### Essential fixes:
{% if include.game == 'need-for-speed-2-special-edition' or include.game == 'need-for-speed-4' %}* <i class="fas fa-cog"></i> Locked specific problematic threads to one core, while allowing worker threads to use any CPU cores -- combining good stability and performance. This option has to be enabled by adding `SingleProcAffinity=1` to an INI file named like the game's executable. This change is fully compatible with Modern Patches and overrides its single core-affinity solution.
{% else %}* <i class="fas fa-cog"></i> Locked all game threads to one core, while allowing worker threads to use any CPU cores -- combining good stability and performance. This option has to be enabled by adding `SingleProcAffinity=1` to an INI file named like the game's executable. This change is fully compatible with Modern Patches and overrides its single-core affinity solution.{% endif %}
{% if include.game == 'need-for-speed-2-special-edition' %}
* Fixed a potential race condition on starting the movie decoding thread.
* Fixed a bug preventing controller button mappings from working correctly with gamepads that report more than 15 buttons (such as the Xbox One controller).
* Fixed the game closing when the controller disconnects during the race.
* (Verok's Modern Patch only) Fixed an issue where online races were displayed only on the top half of the screen as if they were split-screen races.
{% endif %}
{% if include.game == 'need-for-speed-porsche' %}
* Fixed a startup crash due to DirectInput controller enumeration being broken under specific circumstances on Windows 10 and newer.
* Fixed severe performance issues on Windows 10 and newer when rebinding controls.
* (Verok's Modern Patch only) Fixed unresponsive keyboard inputs after <kbd>Alt</kbd> + <kbd>Tab</kbd> during the race.
* (Verok's Modern Patch only) Fixed a severe memory leak in OpenGL1 and OpenGL3 thrash drivers occuring after every race.
{% endif %}

### Miscellaneous fixes:
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works correctly.
* <kbd>Num Lock</kbd>, <kbd>Caps Lock</kbd> and <kbd>Scroll Lock</kbd> don't get forcibly disabled on game launch anymore.
{% if include.game != 'need-for-speed-porsche' %}
* Fixed issues with stuttery/unresponsive mouse cursor in menus when using mice with high polling rates.
* Fixed a controller polling bug resulting in potential incompatibilities with DirectInput wrappers such as Xidi.
{% endif %}

### Enhancements:
* Pasting text into text boxes now works with <kbd>Ctrl</kbd> + <kbd>V</kbd>.

{% include setup-instructions.html %}

<a href="https://github.com/CookiePLMonster/SilentPatchNFS90s/releases/latest/download/SilentPatchNFS90s.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download</a> \\
<a href="https://github.com/CookiePLMonster/SilentPatchNFS90s" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
