---
layout: post
title: "Dreamcast Restoration 2.0 & SilentPatch for Crazy Taxi"
excerpt: "Restore licensed brands from the Dreamcast version, and fix some bugs while we're at it."
thumbnail: "assets/img/games/bg/crazy-taxi.jpg"
feature-img: "assets/img/games/bg/crazy-taxi.jpg"
image: "assets/img/games/bg/crazy-taxi.jpg"
date: 2021-08-08 19:30:00 +0200
tags: [Releases, Articles]
---

*TL;DR - if you are not interested in an overview of Dreamcast Restoration 2.0 and SilentPatch,
scroll down to the [**Download**](#download) section for a download link for both mods.*

***

In case a single mod release was not enough, this time I present to you a simultaneous release of two mods -- **Dreamcast Restoration 2.0** and **SilentPatch** for the Steam version of
**Crazy Taxi**! For this reason, this post is split into two sections, one per mod.

# Part 1 -- Dreamcast Restoration 2.0

The original arcade version of Crazy Taxi, as well as the initial ports to home consoles (Dreamcast, PlayStation 2, GameCube) and PC, all featured prominent product
placement -- several destinations the customers could want to go to were modelled after real-life brands, such as Pizza Hut, KFC or FILA.
However, in the case of 2010s releases on Xbox 360, PlayStation 3, and Steam, these brands haven't been re-licensed and thus were replaced with fake brands.

For the longest time, these ports were stuck with fake brands, but this changed earlier this year when [Alexvgz](https://www.youtube.com/channel/UCqDbjGuaY4awoKs8J-6DBUA)
released his Dreamcast Restoration mod -- replacing the textures and hex editing the destination names to match the original names as closely as possible.
While the result is mostly satisfactory, this approach meant several shortcomings exist:

1. Texture replacements don't cover everything -- Pizza Hut and FILA buildings have their models altered, so replacing textures doesn't allow making them look identical to the original versions.
    <p align="center">
    <img src="{% link assets/img/posts/ct-dc-sp/chrome_l6DOIbsoeS.jpg %}">
    </p>
2. Hex edited names are subject to size limits (you cannot make the string longer than the original one). This means some of the names had to be shortened. 
    <p align="center">
    <img src="{% link assets/img/posts/ct-dc-sp/chrome_iF77rjtDiv.jpg %}">
    </p>
3. Unlike Pizza Hut, KFC, Levi's, and Tower Records, FILA did not just get renamed, but instead cut completely as a possible destination for customers. This is weird, as the game's code reveals
that FILA has indeed been renamed to *Shoe Rack*, which suggests its complete removal may have been an afterthought.

In hopes of being able to use my expertise to help with these, I got in touch with Alexvgz and initially pitched an idea to use an ASI plugin only to rename destinations, leaving texture replacements as-is.
This worked fine due to the way code injection works (pointing the game at new strings instead of modifying these strings), but soon after we found out we can do better than that.

Before I proceed, a few words on how these replacements are handled. With a few exceptions (aforementioned Pizza Hut and FILA), these replacements are done by loading new textures from an (appropriately named)
`NewTexture` directory; the original textures are still in the game files, unused! Therefore, an obvious thing to try first is to disable these overrides and let the game load the original textures.
At that time, we weren't sure if it's viable, but I kept looking.

When looking randomly around the game code in search of any clues on the texture replacements, I found a function that looked suspiciously like it'd be replacing specific Pizza Hut textures:
```c
if ( hash == 0xCC0B3A0 )
{
  path = "NewTexture\\Pizzah3.dds";
```

Turns out, removing these replacements got Pizza Hut closer to the way it originally looked -- undoing the changes to the logo text, but with the hat (and the roof logos) still missing:
<p align="center">
<img src="{% link assets/img/posts/ct-dc-sp/Crazy_Taxi_2grdPKJ56M.jpg %}">
</p>

This however was a great starting point -- now I know that I need to look for some sort of hashes/UIDs. Searching for one of these brought me to a suspiciously looking function,
that looks almost as if it's moving/scaling something...

```c
switch ( v8 )
{
  case 0xCBFC740:
    goto LABEL_87;
  case 0xCBFDF60: // One of Pizza Hut hashes/UIDs
    v156 = 1;
    if ( v166 != 0x4483139B )
      goto SKIP_MODEL;
    v14 = v157;
    v157[23] = 1736.7159;
    v14[31] = 1721.381;
    v14[47] = 1721.381;
    v14[39] = 1736.7159;
    v15 = 1776.417;
    v14[57] = 1776.417;
    v16 = 1741.417;
LABEL_330:
    v14[65] = v16;
    v11 += 3;
    v14[81] = v16;
    v14[73] = v15;
    goto LABEL_365;
  case 0xCBFE360:
    goto LABEL_75;
}
```

While I cannot confirm this with absolute certainty, I think this theory turned out to be true -- removing this code restored the original appearance of Pizza Hut fully!
<p align="center">
<img src="{% link assets/img/posts/ct-dc-sp/Crazy_Taxi_JtWQkuJuCM.jpg %}">
</p>

Later, after looking into the very same function more I was able to restore FILA logos and interior props in the same way. Success!

At this point, FILA and Pizza Hut were fully restored, but buildings relying on texture replacements were still "censored".
A naive solution of just removing the archives in `NewTexture` resulted in textures being black, so I knew the game's code has to have some sort of a list with special cased textures.
After even more poking and prodding, I eventually found it! With another two functions (one for world textures, another for UI) modified not to special case any textures,
all the original brands have been restored purely from code, no file replacements needed:

<p class="mod-screenshot" align="center">
<a href="https://i.imgur.com/D8oQHkc.jpg"><img src="https://i.imgur.com/D8oQHkcl.jpg"></a>
<a href="https://i.imgur.com/1j3BgjC.jpg"><img src="https://i.imgur.com/1j3BgjCl.jpg"></a>
<a href="https://i.imgur.com/YPt9wLw.jpg"><img src="https://i.imgur.com/YPt9wLwl.jpg"></a>
</p>

This only leaves FILA, as at that point customers still didn't want to go there, picking Popcorn Mania or Tower Records instead. However, by a stroke of luck (and tracking memory writes
back to their source) I eventually spotted this chunk of code in a function that appears to be assigning destinations to passengers...
```c
if ( selectedMap != 0 )
{
  v9 = 2; // FILA, Original map
  v10 = 3;
}
else
{
  v10 = 10;
  v9 = 11; // FILA, Arcade map
}
if ( v9 == *v8 )
{
  // Pick new destination (probably)...
}
```

These IDs are no coincidence -- skip this chunk of code, and specific passengers again want to go to FILA! As mentioned earlier, this destination has a "censored" name (the thumbnail wasn't updated though),
even though this destination effectively goes unused.
<p align="center">
<img src="{% link assets/img/posts/ct-dc-sp/Crazy_Taxi_pHWw3tk0Xy.jpg %}">
</p>

With this change, and later with restoring the original destination names, a brand new **Dreamcast Restoration 2.0** is ready! A joint effort by myself and Alexvgz, now not requiring any file replacements,
is available for download on my Crazy Taxi page, so either continue reading for Part 2 or go straight to the [**Download**](#download) section for a download link.

# Part 2 -- SilentPatch

When working on Dreamcast Restoration 2.0, I couldn't help but notice a few annoyances about this version of the game. For arguably the most severe of them, the
[PCGamingWiki page](https://www.pcgamingwiki.com/wiki/Crazy_Taxi_(Steam)) for the Steam version of Crazy Taxi says:

> <i class="fas fa-thumbs-down"></i> Lacks proper analog controls. While the sticks can be used, it is interpreted digitally. See Crazy Taxi Analog Controller Unofficial Fix to add proper analog controls.

The fix in question exists for several years already, but it's never been perfect. For once, it's shipped as an EXE replacement (and therefore the original Dreamcast Restoration "bundled" it).
It also doesn't seem to be fully reliable -- it works fine for me (except for occasional erroneous driver anims), but it never worked fine for Alexvgz. Therefore, I knew right then it
most likely can be improved. On top of that, I've been constantly annoyed by the fact I can't properly Alt+F4 from the game, etc.

And so, together with the first mod, a new SilentPatch is now out. You may scroll down for a full changelog and a download link, or stick around for a brief summary of the most "interesting"
bug fixes.

## Fixing analog controls
The existing Analog Controller Unofficial Fix from Cryoburner works by retrieving the original XInput gamepad values, storing them, and later overriding the input values from the game
with these saved ones. This works surprisingly well, but as mentioned earlier, does not appear to be 100% reliable. When I decided I want to integrate a fix for the same bug in SilentPatch,
I decided to dig into the root cause of this problem, so I could make this fix fully reliable and identical to the console ports.

After some investigation, I found out that the analog input technically works in the game already (just like it does in the 2014 console releases) but the deadzones are misconfigured.
The game has two thresholds for analog input:
* Deadzone - no input below this range
* Full range - full input above this range

The full range zone sets the input to `-1.0`/`1.0` and it also simulates the press of a corresponding DPad button -- that's what e.g. allows to navigate menus with the analog stick.
The issue in the PC version is that these two thresholds are equal! This makes the game go from "no input" to "full input + DPad" states instantly.

I modified the full range threshold to be very close to the maximum analog stick value, and now analog steering works fine with no need to short circuit the analog state anywhere.
As a bonus, menu navigation now seems to work more like in the Dreamcast version.

The issue with triggers was similar, but not identical. In this case, the game willingly discards the pressure sensitive input (even in the console versions!), instead only checking
if it's bigger than `0.5`. I was able to mirror the way the game handled analog sticks and preserve the original value of triggers input. This fix is more similar to the one
from the Unofficial Fix, but still not identical.

## Fixing a crash with steering wheels
Another major issue with this port is a complete inability to use DirectInput steering wheels (or maybe any DirectInput devices). While the configurator app detects DInput devices properly
and even allows to map them, launching the game with such device connected causes a crash! I looked into it, and the function that crashes looks more or less like this...
```c
if (arg2 != -1)
{
  // ...
  if (field_114 != nullptr)
  {
    if ( (*(field_114 + 24))(&v3->field_DC, 0x20000140) < 0 )
        return 0;
  }
}

if (arg3 != -1)
{
  // ...
  if (field_114 != nullptr) // Pay close attention to this line
  {
    if ( (*(field_118 + 24))(&v3->field_DC, 0x20000140) < 0 )
        return 0;
  }
}
```

This might not be immediately obvious, but to me, this looks like a copypaste error. The game maintains two pointers to some objects (presumably of the same type),
but when checking for `nullptr` it always uses the first pointer! I wouldn't be surprised if the original code looked like this:
```cpp
if (object1 != nullptr)
{
  object1->SomeCall();
}
// ...
if (object1 != nullptr) // Copypaste error!
{
  object2->SomeCall();
}
```

As you may have guessed, fixing this single issue allows the game to boot with a steering wheel connected 🎉 \\
Initially, the experience on a steering wheel was sub-optimal, as the same deadzone issues also existed in the DirectInput code.
After some finetuning, I was able to fix those, allowing for proper analog steering, throttle/brake pedal input; enabling the players to experience the game
just like it was in the arcades. Mapping Drive/Reverse to a shifter also works fine, further making the experience arcade-like!

## Classic cheats
The original Dreamcast version, as well as the first PC port, came with several cheats. While the ones activated in the main menu (such as the "another day" mode)
have been carried over to the 2014 release correctly, the ones activated in-game did not. This left players unable to change the camera modes and enable the speedometer in the Steam version of the game.

Thankfully, these features are left in the game code as-is, but they are unobtainable. SilentPatch restores all 3 camera modes and the speedometer feature and uses the same key combinations
as the classic PC port. I replicated the classic hotkeys so now old cheat pages/guides from the original PC versions are also relevant for the Steam version.

<p class="mod-screenshot" align="center">
<img src="{% link assets/img/posts/ct-dc-sp/Crazy_Taxi_9YB2IulTNS.jpg %}">
<img src="{% link assets/img/posts/ct-dc-sp/Crazy_Taxi_5XZmpAqqal.jpg %}">
</p>

## Full changelog
Aside from the fixes mentioned, SilentPatch for Crazy Taxi also fixes a few other issues. The full changelog is as follows:
* Issues with analog steering and pressure sensitive triggers have been fixed. This applies both to XInput and DirectInput controllers.
* A crash when starting the game with specific DirectInput devices (e.g. steering wheels) has been fixed.
* Analog stick deadzones have been refined slightly to improve steering responsiveness and make it feel closer to the Dreamcast release.
* Alt + F4 now works correctly.
* When using the Windowed mode, the window size has been corrected to avoid distorting the image.
* When using the Windowed mode, maximizing is now disallowed by disabling the Maximize button rather than by making it non-functional.
* Restored several missing cheats/hotkeys from the original PC version. These are:
  * Reset Camera (`Shift+Alt+F5`)
  * Cinematic Camera (`Shift+Alt+F6`)
  * First Person Camera (`Shift+Alt+F7`)
  * Show Speedometer (`Shift+Alt+F8`)

# Download

Both modifications can be downloaded in *Mods & Patches*. Click here to head to the game's page directly:

<a href="{% link _games/crazy-taxi.md %}" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download Dreamcast Restoration 2.0 and SilentPatch for Crazy Taxi</a> \\
After downloading, all you need to do is to extract the archives to the game's directory, and that's it! Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).

***

For those interested,
full source codes of both mods has been published on GitHub, so it can be freely used as a point of reference: \\
<a href="https://github.com/CookiePLMonster/CT-DC" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See Dreamcast Restoration 2.0 on GitHub</a>
<a href="https://github.com/CookiePLMonster/SilentPatchCT" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See SilentPatch on GitHub</a>
