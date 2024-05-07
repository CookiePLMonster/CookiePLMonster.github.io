---
title: "Access Code Fix"
game-series: ['toca-race-driver-2', 'toca-race-driver-3']
date: 03-04-2024
---

This plugin fixes a bug in TOCA Race Driver 2 and 3 where the access code wasn't generated correctly on 64-bit systems
and/or Windows 10, rendering bonus codes unusable. For better randomness of bonus codes, the console behaviour of picking
a random access code has been restored, since many users nowadays share the same `ProductId` after upgrading to Windows 10/11.

## Research and Notes

On Windows, the game attempts to query the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion->ProductId` value to generate an access code (4 digits).
This is invalid for two reasons:
1. This registry key is not present on Windows 10 anymore, since it has always been a mirrored key, presumably for legacy reasons.
   The correct registry key to use here was always `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion->ProductId`.
2. `ProductId` is one of the keys that are not mirrored on 64-bit systems to a 32-bit registry key, so the game was unable to query it as-is.

This plugin corrects both issues, querying the key from a correct place and explicitly specifying to query from a native registry view.

For a full list of cheat codes, see [Bonus Codes]({% link pages/bonuscodes.md %}).

{% include setup-instructions.html %}

***

<a href="https://github.com/Nenkai/GameCheat-Unlockers/releases/latest/download/RDAccessCodeFix.zip" class="button">{{ site.theme_settings.download_icon }} Download</a>

<a href="https://github.com/Nenkai/GameCheat-Unlockers/tree/main/RDAccessCodeFix" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
