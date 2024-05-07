---
layout: post
title: "SilentPatch for TOCA 2 Touring Cars"
excerpt: "Revisiting a retro racing game with a range of compatibility fixes and full widescreen support."
thumbnail: "assets/img/games/bg/toca-2.jpg"
feature-img: "assets/img/games/bg/toca-2.jpg"
image: "assets/img/games/bg/toca-2.jpg"
game-series: "toca-2"
date: 2021-05-09 20:25:00 +0200
tags: [Releases, Articles]
---

*TL;DR - if you are not interested in a brief explanation of one of the compatibility issues the game had,
scroll down to the [**Download**](#changelog-and-download) section for a download link.*

***

In the spirit of the initial purpose of SilentPatches, this release revisits an old game for once - **TOCA 2: Touring Cars** (released as **TOCA 2: Touring Car Challenge** in North America) from 1998.
The patch corrects several compatibility issues with modern computers, previously requiring a manual fix, and adds full widescreen support.
Original issues have also been corrected, and I also added some quality of life improvements, bringing the game closer to what more modern racing games can offer.

{% include figures/video-iframe.html link="https://www.youtube.com/embed/QVSzsOuwAA8" %}

While most of the fixes I've done for TOCA 2 are ordinary and not worth covering, the single most severe compatibility issue the game had is unique, and I think
it's worth explaining.

# Fixing the way time flows

While TOCA 2 generally aged well (like most games from Codemasters), it has one severe bug when running it on modern machines -- it locks up when loading races and quitting the game!
Thankfully, people quickly figured out a fix in form of a small hex edit. That's what the game's [PCGamingWiki page](https://www.pcgamingwiki.com/wiki/TOCA_2_Touring_Cars) suggests
at the time I publish this article:

> ### Crash on loading
> <i class="fas fa-wrench"></i> **Unpatched**
> 1. Open `TC2.exe` with hex editor.
> 2. Scroll down to offset `0x706ED` (row 000706E0, column 0D) and change `7E` to `EB`.
> 3. Save the file.

`EB` is a hex code for the `short jmp` assembly opcode, that means this fix makes the game jump over some code. Turns out, this code is a simple delay loop which gets skipped when said hex edit patch
is in use -- in pseudocode, it looks like this:

```cpp
void Wait(int duration)
{
  totalTimeElapsed = 0;
  QueryPerformanceCounter(&PerformanceCount);
  lastTime = PerformanceCount.LowPart;
  if ( duration > 0 ) // This is where the hex edit inserts a jump
  {
    do
    {
      QueryPerformanceCounter(&PerformanceCount);
      if ( PerformanceCount.LowPart <= lastTime )
        timePart = PerformanceCount.LowPart - lastTime - 1;
      else
        timePart = PerformanceCount.LowPart - lastTime;
      totalTimeElapsed += timePart;
      elapsed = MulDiv(totalTimeElapsed, 3276800, gTimeFrequency);
      lastTime = PerformanceCount.LowPart;
    }
    while ( elapsed < duration );
  }
}
```

At the first glance, I was quick to jump to an obvious conclusion -- performance timers are 64-bit values and this code only operates on the bottom 32-bit (`LowPart`) of it!
However, this isn't the root cause of this issue. Notice how, for some unknown reason, this code counts time in steps (instead of operating on `currentTime - startTime`, would've been simpler!),
and had this suspicious block of code:
```cpp
if ( PerformanceCount.LowPart <= lastTime )
  timePart = PerformanceCount.LowPart - lastTime - 1;
else
  timePart = PerformanceCount.LowPart - lastTime;
```

In my opinion, this block of code was added to prevent the timer from "getting stuck" if the current time and "last time" are equal (hence the check), but if you take
a close look at the code executed when those times are identical, it ends up subtracting two equal numbers, and thus reduces to:
```cpp
timePart = X - X - 1;
```

which in turn times `timePart = -1`! This elapsed time then gets added to the total time elapsed, and thus the delay... counts time backward 🤦
I'm sure the original intent was to advance the time at least by 1 unit every time, and so it becomes clear it's a case of a missing bracket -- had the code been written as
```cpp
if ( PerformanceCount.LowPart <= lastTime )
  timePart = PerformanceCount.LowPart - (lastTime - 1);
else
  timePart = PerformanceCount.LowPart - lastTime;
```

it would have worked as intended!

SilentPatch fixes this issue by rewriting the function not to use those partial increments, and to use the entire 64-bit value. This results in a much simpler code that will never break:
```cpp
void Wait(int duration)
{
  if (duration > 0)
  {
    int64_t diffTime;
    LARGE_INTEGER startTime;
    QueryPerformanceCounter(&startTime);
    do
    {
      LARGE_INTEGER time;
      QueryPerformanceCounter(&time);
      diffTime = time.QuadPart - startTime.QuadPart;
      diffTime *= 3276800;
      diffTime /= gTimeFrequency;
    }
    while (diffTime < duration);
  }
}
```

# Changelog and download

This SilentPatch fixes plenty more issues, though. The full changelog is as follows; fixes marked with <i class="fas fa-cog"></i> can be configured/toggled via the INI file.
* In-game timers have been rewritten to fix a freeze when starting the race or leaving the game, occurring on modern machines. Previously this issue required hex editing to work it around.
* The game now handles all arbitrary aspect ratios without the need for hex editing. Both the 3D elements and UI have been fully fixed for widescreen.
* The game now lists all available resolutions, lifting the limit of dimensions (originally up to 1600x1200) and the limit of 24 resolutions.
* HUD scaling has been made more consistent on high resolutions, so the UI now looks identical regardless of resolution.
* CD checks have been removed. When a Full installation is in use, the game now can be played without a CD, without the need to use a no-CD executable.
* Fixed multiple distinct crashes occurring when minimizing the game excessively.
* Fixed a crash when minimizing the game during a Support Car race. The crash happened because those cars don't have a name decal on the rear windshield.
* <kbd>Alt</kbd> + <kbd>F4</kbd> now works properly.
* The process icon is now fetched from the toca2.exe file, giving the game an icon of a checkered flag.
* <i class="fas fa-cog"></i> Field of View can now be adjusted via the INI file, with separate values for external cameras and the two interior cameras. You can select any value in the 30.0 - 150.0 range.
* <i class="fas fa-cog"></i> HUD scaling and menu text scaling can now be adjusted via the INI file.
* <i class="fas fa-cog"></i> Metric/imperial units can now be freely switched via the INI file. The new default behaviour is to use the user's OS setting to determine whether to use metric or imperial, but the choice can also be overridden via the INI file.
* <i class="fas fa-cog"></i> In-car rearview mirrors now can be forced to show regardless of the HUD settings. This feature can be toggled via the INI file.
* <i class="fas fa-cog"></i> In-car rearview mirror resolution can now be changed via the INI file, up to 512x256. Do note that higher resolutions might make the game slow if dgVoodoo isn't used.
* <i class="fas fa-cog"></i> The center interior camera now uses a full range of steering animations and gear shifting animations, just like the main interior camera. This feature can be toggled via the INI file.
* <i class="fas fa-cog"></i> Driver's hands and the steering wheel can now be toggled on/off via the INI file independently. This feature might be useful for specific steering wheel setups to avoid a "duplicate steering wheel".

# Acknowledgements

Fixes related to the widescreen support have been based on the work of [AuToMaNiAk005](https://www.youtube.com/user/AuToMaNiAk005) -- his extremely useful widescreen/ultrawide tutorials saved me a lot
of time researching the way TOCA 2 handles aspect ratios and lists resolutions.

***

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/toca-2.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for TOCA 2 Touring Cars</a>

After downloading, all you need to do is to extract the archive to the game's directory, and that's it! I highly recommend checking the INI files for a range of useful settings to change,
e.g. rear view mirror resolution or FOV. Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).

***

For those interested, the full source code of the mod has been published on GitHub, so it can be freely used as a reference:
<a href="https://github.com/CookiePLMonster/SilentPatchTOCA2" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
