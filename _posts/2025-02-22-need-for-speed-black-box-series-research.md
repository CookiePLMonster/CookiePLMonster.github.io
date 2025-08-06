---
layout: post
title: Black Box-era Need for Speed -- series research
date: 2025-02-22 15:20:00 +0100
last_modified_at: 2025-03-12 19:35:00 +0100
excerpt: Miscellaneous pieces of info about the Black Box-era Need for Speed games.
game-series: ["need-for-speed-underground", "need-for-speed-underground-ps2", "need-for-speed-most-wanted-ps2",
            "need-for-speed-carbon-ps2", "need-for-speed-prostreet-ps2", "need-for-speed-undercover-ps2"]
image: "assets/img/games/bg/need-for-speed-carbon.jpg"
thumbnail: "assets/img/games/bg/need-for-speed-carbon.jpg"
feature-img: "assets/img/games/bg/need-for-speed-carbon.jpg"
tags: [Research]
---

{:.sidenote}
Last update: {% include elements/time.html date=page.last_modified_at %}

This is a [Research]({% link pages/categories.html %}#Research)-style post -- as I go through more games, I will keep updating it with new findings.

* TOC
{:toc}

# Loyalty career bonuses

Most games from the Black Box era grant a cash bonus if saves from the previous games are found. However, online information about this feature is incomplete,
and games themselves have some bugs and leftovers related to that.

## NFS Most Wanted (including Black Edition)

$10.000 is awarded if a save from NFS Underground 2 is found. On the PS2, the game checks for the following set of serials depending on the current build configuration:
* `SLES-52725` in the European build.
* `SLUS-21065` in the American build.
* `SLPM-65766` in the Japanese build. Seems like Sha-Do Underground 2 does not give bonuses, unless this has been specifically addressed in the Japanese releases.
* `SLKA-25241` in the Korean build.
* `SLAJ-25054` in the Asian build.

## NFS Carbon (including Collector's Edition)

$10.000 is awarded if a save from NFS Most Wanted is found. On the PS2 (other platforms unconfirmed), this feature has a bug -- **by default,
this feature only works with base Most Wanted saves, as the NTSC-U versions check for Most Wanted Black Edition using a wrong serial (`SLAJ-25075`),
while PAL-E versions do not include a BE serial at all!**
I submitted [a patch to the PCSX2 patch database](https://github.com/PCSX2/pcsx2_patches/pull/499){:target="_blank"} to fix this.

The game also has a function to list Underground 2 saves that uses the same list of serials as Most Wanted,
so it may have been planned to grant bonuses for either UG2 or MW saves. However, those remain unused, either intentionally or through an oversight.

## NFS ProStreet

Carbon's bug has been fixed in NTSC-U (**but not PAL**), and the game (at least in the old-gen releases) grants the player 3 Repair Markers and 1 Totalled Marker
when saves from any of the following games are found:
* NFS Most Wanted
* NFS Most Wanted Black Edition (fixed in the PAL release with my above fix)
* NFS Carbon
* NFS Carbon Collector's Edition

Once again, the game can detect Underground 2 saves, but this functionality remains unused.

This feature has a caveat -- **creating a new profile and starting the career through the <kbd>START</kbd> option will NOT grant you loyalty bonuses.**
You **must** start a new career through the <kbd>NEW CAREER</kbd> option.

## NFS Undercover (PS2)

Exient's PS2/Wii version of NFS Undercover is NFS Carbon in disguise, and so the code carries over all the checks from Carbon (including a wrong serial for MW Black Edition).
However, these go unused, and the game grants no loyalty bonuses at all.

# NFS Underground Magazine 22

For my NFS Underground playthrough, I looked into the infamous Drift Score magazine unlock conditions. Turns out they were bugged, and I now released a SilentPatch
for PC and PS2 versions of the game fixing this bug, as well as a few others.

Due to the significance of this bug fix, I detailed it in [a separate post]({% post_url 2025-03-12-need-for-speed-underground-magazine-22-silentpatch %}).

***

# Post changelog

* {% include elements/time.html date="2025-03-12" %} -- NFS Underground Magazine 22 issues researched.
* {% include elements/time.html date=page.date %} -- initial version. Later edited to clarify missing MW Black Edition serials in PAL releases of Carbon and ProStreet.
