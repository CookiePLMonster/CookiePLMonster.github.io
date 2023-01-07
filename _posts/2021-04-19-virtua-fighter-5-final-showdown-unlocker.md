---
layout: post
title: "Virtua Fighter 5: Final Showdown Unlocker for Yakuza 6 and Yakuza: Like a Dragon"
excerpt: "Turning the arcade into a full console game!"
thumbnail: "assets/img/games/bg/vf5fs.jpg"
feature-img: "assets/img/games/bg/vf5fs.jpg"
image: "assets/img/games/bg/vf5fs.jpg"
game-series: ["yakuza-6", "yakuza-lad", "vf5fs"]
date: 2021-04-19 23:00:00 +0200
tags: [Releases]
---

*TL;DR - if you are not interested in a brief explanation of how was this possible,
scroll down to the [**Download**](#download) section for a download link.*

***

Every modern Yakuza game has arcade machines with real games from SEGA. In the case of Yakuza 6 and Yakuza: Like a Dragon, one of the games the player can play is a full arcade
version of [Virtua Fighter 5: Final Showdown](https://en.wikipedia.org/wiki/Virtua_Fighter_5).

There is more to it, however. While working on a different project (mentioned below) and looking around the Yakuza 6 version of the game's code,
I noticed a... single flag that was named rather promising. Thanks to Yakuza: Like a Dragon briefly shipping on Steam with debug symbols,
I knew exactly what this flag was named:

```cpp
g_is_arcade_mode = g_game_config.game_mode != 0;
```

According to the game's code, Yakuza 6 (and Yakuza: LAD) usually uses **mode 1** when booting games from within Club SEGA and **mode 2** when booting a 2p
game from the main menu. **Mode 0** is inaccessible from the vanilla game, but what does it do when activated?

Turns out it does more than anyone had expected -- it activates a complete, nearly fully working console version of the game!

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Now an absolute banger - Virtua Fighter 5 in Yakuza 6 and Yakuza LAD appears to be FULL CONSOLE VERSION 😱 By default, it can only boot to Arcade Mode or VS Mode directly, but boot it to mode 0 and this happens. Netplay/leaderboards/achievements obviously don&#39;t work... (1/2) <a href="https://t.co/vB6aKBqKlr">pic.twitter.com/vB6aKBqKlr</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1383886736585940997?ref_src=twsrc%5Etfw">April 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

A few interesting insights:
* The game appears to be based upon the Xbox 360 port, with references to Xbox LIVE left in the menus.
* Unlike the console ports, this version of the game has a fully functional Exit Game option.
* The game does not contain any DLC data, attempting to force unlock them softlocks the game.

This discovery got people hyped (as evidenced by the amount of engagement on the tweet), so I couldn't leave it at the mercy of another project of mine that might or might not work.
Since it's a single byte change, I went ahead and created a small plugin for Yakuza 6 and Yakuza: LAD, changing the mode used by arcade machines from 1 to 0.
With a single flag change, you now can play the full console version from inside Club SEGA!
<div align="center" class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/7oNsZClpZ_E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Now, bear in mind that the sole purpose of this plugin is to unlock the game **as-is** for everyone. At the moment I have no plans to address any of the issues and shortcomings there are.
Those include, but are not limited to:
* Saving doesn't work
* To start the game, coins must be inserted twice (Y/Triangle on the gamepad)
* English texts are cut off, as this build of VF5FS seems to be a Japanese SKU with English texts
* Pause menu is tricky to access and resuming the game does not unfreeze gameplay

# Download

The modification can be downloaded from *Mods & Patches*. Click here to head to the game's page directly (the same download works for **Yakuza 6 and Yakuza: Like a Dragon**):

<a href="{% link _games/yakuza/yakuza-6.md %}#vf5fs-unlocker" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download VF5FS Unlocker</a> \\
After downloading, all you need to do is to extract the archive to the game's directory, and that's it! Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).
**This plugin only works with the Steam version of the games!**

# What's next?

As those arcade games are DLL files separate from the game executable, for the past week I've been experimenting with running Virtua Fighter 5 standalone;
in fact, that's how I found this unused "console mode" in the first place!
At the moment, my standalone game reaches the title screen only, so it's too early to say whether it's going to be doable or not.

<div align="center">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">3 weeks ago, I was wondering if arcades from Yakuza 6 could run standalone. Today, I finally have Virtua Fighter 5 reach the title screen 🎉 Audio and input are not functional yet, but that&#39;s a great start! <a href="https://t.co/zVo13ux0Kw">pic.twitter.com/zVo13ux0Kw</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1383456664557293572?ref_src=twsrc%5Etfw">April 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

I plan to continue looking into that though, and if I manage to progress it further I will be publishing the results!

***

For those interested,
full source code of the mod has been published on GitHub, so it can be freely used as a point of reference: \\
<a href="https://github.com/CookiePLMonster/VF5FS-Unlocker" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
