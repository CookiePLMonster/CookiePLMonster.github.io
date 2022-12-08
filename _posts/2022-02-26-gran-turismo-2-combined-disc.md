---
layout: post
title: "Gran Turismo 2 Combined Disc"
excerpt: "What if PlayStation CDs were 1GB and Gran Turismo 2 came on a single disc?"
game-series: "gran-turismo-2"
date: 2022-02-26 19:30:00 +0100
thumbnail: "assets/img/posts/gt2-combined/gt2-combined-logo.png"
feature-img: "assets/img/posts/gt2-combined/gt2-combined-logo.png"
image: "assets/img/posts/gt2-combined/gt2-combined-logo-square2.png"
tags: [Releases]
---

*TL;DR - if you are not interested in a brief explanation of the Combined Disc,
scroll down to the [**Download & Instructions**](#download--instructions) section for a download link and setup instructions.*

***

Gran Turismo 2, other than being one of the more fondly remembered installments of the franchise, has one unique aspect
not seen in any other Gran Turismo to date -- it's split between two discs.

<p align="center">
<img src="{% link assets/img/posts/gt2-combined/two-discs.jpg %}">
</p>

The amount of added content in comparison to the first game
was so big that Polyphony could not fit it on a single 660MB CD, and therefore the game has separate discs for Arcade
and Simulation/Gran Turismo Modes.

As we are reaching Gran Turismo 7 release date (at the time of writing this post, it's scheduled for release next week),
I thought -- can we do any different? Is it possible to combine both discs and show how would the game look if PS1 discs
could store more data?

# Split discs vs assets

To show why Polyphony was forced to split the discs, it's worth noting what each disc includes.
Unsurprisingly, the majority of the data is shared, there is not much data unique to each disc.

Data on both discs:
* Full game code, including Arcade/Simulation specific code overlays.
* All in-game assets -- cars, sounds, localization texts, etc.
* Main menu assets.
* Arcade Mode assets (even on the Simulation Disc!).

Data exclusive to the Simulation Disc:
* Simulation Mode assets.

Data exclusive to the Arcade Disc:
* FMVs -- intro, credits, Arcade Mode track previews.

As you can see, the Simulation Disc can be considered more "complete" of the two, as it contains assets from both modes.
In practice, with a Simulation Disc, all it takes to get to Arcade Mode is a simple edit of the Main Menu code to load
Arcade Mode instead of Simulation. As I teased on Twitter, I had a proof of concept of this change back in late August:

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hold up... this is *not* a Gran Turismo 2 Arcade Disc <a href="https://t.co/EGjDjTNNpe">pic.twitter.com/EGjDjTNNpe</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1431627926202630148?ref_src=twsrc%5Etfw">August 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

# Attempting the combination for real

For the Combined Disc to be complete, we need to do the following, using the Simulation Mode Disc as a base:
1. Add missing files from the Arcade Disc
2. Add a new main menu entry to start Arcade Mode
3. Modify textures and localizations to refer to Arcade/Sim Mode instead of Disc 1/2

The first part is easy -- with **MKPSXISO[^mkpsxiso]** I can just unpack both discs and then repack the Simulation Disc with Arcade's `STREAM.DAT` added.
This results in an image that is way too big to fit on a physical CD but is still technically valid.
Thus, even though no real PS1 game was like that, emulators are fine with it:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/disc-size.jpg %}"><br>
<em>The real limit of the ISO9660 format is 99:59.74, so this combined disc pushes this format to the limit.</em>
</p>

[^mkpsxiso]: Now you see why I spent so much time perfecting this tool.

For menu entries, adding a new menu action isn't much harder than modifying the existing one. For comparison,
that's all the code required to switch from the main menu to Arcade/Sim Mode screens:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/code-comparison.jpg %}"><br>
<em>Left - Arcade, right - Simulation</em>
</p>

The initial implementation used two identical Start Game buttons, just recolored from red to blue, to match the colors of the discs:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/start-game-buttons.jpg %}">
</p>
However, later I found out that those were in fact buttons from different languages (e.g. US English and UK English),
and so this would have broke when porting the mod to the PAL version -- for example, had this been used in the PAL version in English,
the second Start Game would've shown in French.
To do it properly, I dissected the texture atlas format used by the game to pack all menu buttons into a single texture.
The original atlas is a TIM texture packing individual textures with their palettes (seen as "garbage" on the bottom):
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/title_item_2.jpg %}">
</p>
To tackle this, I extracted the atlas definitions from the executable and developed a tool to cut them into individual images:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/textures.jpg %}">
</p>
Then, once the packer tool was made, [Ash_735](https://twitter.com/Ash_735) could bring the mod to the next level
by creating proper Arcade Mode and Simulation Mode buttons. When packed back to a new atlas, the results are impressive.
The layout is entirely unlike the original packing, but this doesn't matter since atlas definitions are updated either way:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/title_item.png %}">
</p>
The in-game result, combined with the removal of a "SIMULATION MODE DISC" from the menu background, could likely pass as an official version of the game:
<p class="mod-screenshot" align="center">
<img src="{% link assets/img/posts/gt2-combined/arcade-mode.jpg %}">
<img src="{% link assets/img/posts/gt2-combined/gt-mode.jpg %}">
</p>

Fun side note -- the color coding of red Arcade and blue Simulation buttons matches both the appearance of CDs (as seen above)
and the demo versions of GT2:
<p align="center">
<img src="{% link assets/img/posts/gt2-combined/demo.jpg %}">
</p>

# Download & Instructions

Gran Turismo 2 Combined Disc can be downloaded here: \\
<a href="{% link _games/gt/gran-turismo-2.md %}#combined-disc" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download Gran Turismo 2 Combined Disc</a>

<div align="center" class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/jByvSCDQLdY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

The modification is compatible with all game versions, **except for NTSC-J v1.0**. Compatibility with mods has also been verified, Combined Disc was verified to work fine with
those mods (and probably more):
* [Gran Turismo 2 Plus](https://www.gtplanet.net/forum/threads/mod-gran-turismo-2-plus-bug-fixes-restored-content-and-new-content-beta-6-1-released.378282/)
* [Gran Turismo 2.1](https://www.gtplanet.net/forum/threads/mod-gran-turismo-2-1.399625/)

Combined Disc is also compatible with [RetroAchievements](https://retroachievements.org/game/11278)! Those using it for their GT2 playthroughs may safely move
to using the Combined Disc and achievements will continue to work as expected.

On real hardware:
* PSP/PS Vita can use the full version of the mod in PBP format.
* On PS1, the full version is compatible with [XStation](https://castlemaniagames.com/products/xstation) and [PSIO](https://ps-io.com/).
  You should opt for the lightweight version (without FMVs) **only** if burning the image on a physical CD.

If you are using cheat-based mods (like all my other GT2 mods), stick to codes created for the Simulation Mode.
**All** my mods have been verified with the Combined Disc and they are expected to work fine.

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
6. Enjoy!
