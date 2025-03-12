---
layout: post
title: "Solving the mystery of Need for Speed: Underground's Magazine 22 with SilentPatch"
date: 2025-03-12 19:35:00 +0100
excerpt: You no longer need to be superhuman to beat the drift record.
game-series: ["need-for-speed-underground", "need-for-speed-underground-ps2"]
image: "assets/img/posts/silentpatch-nfsug/card-image.jpg"
thumbnail: "assets/img/games/bg/need-for-speed-underground.jpg"
feature-img: "assets/img/games/bg/need-for-speed-underground.jpg"
tags: [Articles, Releases]
mathjax: true
---

* TOC
{:toc}

# The mysterious Magazine 22

## Theory -- the current knowledge

The career mode in NFS Underground has a built-in achievements system in form of the Magazine covers.
There are 27 magazines in the game, 4 tied to the Online reputation system, and the remaining 23 awarded for various feats in the career.
The last four offline magazines are awarded for beating the best track times for Circuit, Sprint, Drag and Drift events on Hard difficulty.
Three of those are reasonably easy to achieve -- I am currently replaying Underground for the first time since 2003, and I beat the best times for
Circuit, Sprint, and Drag without even trying; I just got them after certain Career races.

The Drift Track record magazine is a whole other story. Thanks to the official strategy guide, we knew this magazine tied to the Drift Track record
so there was no mistake here. However, even though the unlock conditions were known, people were not getting the magazine regardless.

Turns out that the requirements for this magazine are much more difficult than originally assumed -- to get the magazine in a Career event,
the high score has to be obtained **in a single lap**. This has been documented online [in old guides](https://bigsword.tripod.com/NFSU/nfsu-magazines.html){:target="_blank"},
people have been talking about the "one lap requirement" [at least since 2005](https://www.neoseeker.com/forums/6608/t515691-magazine-cover-22-impossible/){:target="_blank"},
and it's also been the topic of investigative work on YouTube:
{% include figures/video-iframe.html link="https://www.youtube.com/embed/4m8Hq45rlcI" %}

Recently, this issue saw a resurgence of attention because of the NFS Underground RetroAchievements set that
[tied one of the achievements to this magazine](https://retroachievements.org/achievement/258361/comments){:target="_blank"}. Some of the comments are dire,
showing just how much more difficult this magazine is compared to any other unlock in the game:

> Damn finally got it, took me almost two days xD

> This is the hardest thing I've ever done, it took probably 30 hours of attempts on Drift Track 8 to get for me, and I was already "decent" at drifting.

> This was probably the worst experience I've had in a need for speed game and sooo unnecessary to have as an unlockable in-game.
> I'm not blaming the RA dev, but the NFS:U devs themselves.

## Reality -- sorry, you are all (partially) wrong

For my playthrough, I didn't want to go through all this pain just because of what almost certainly is a bug in the game, so I dived into the code.
I found out that the game unlocks the magazine if the following inequality passes:

$$ \frac{player\_score}{laps} > \operatorname{RoundUp}(\frac{preset\_score}{4}) $$

This check is not wrong per se. The magazines can also be obtained in Quick Race, where events up to 10 laps can be created.
Comparing the scores directly would make the requirements easy to hit with high lap counts, as all the preset scores in the game were set for 4-lap events.
Therefore, this formula makes it clear that the idea is to compare the **average** lap score, so the achievement is still challenging regardless of how many laps there are.

While the function is correct, the way it is used is not, as instead of the total player score, **the best lap score** is passed to the function as $$ player\_score $$!
This aligns with the existing community findings, as with $$ laps = 4 $$, the best lap score effectively must be higher than the preset score (as both are divided by 4).
This more or less means that to get this magazine in the Career, the player must be 4 times better than (most likely) originally intended.

There is one detail everyone missed, though. Contrary to popular belief, you **do not need to necessarily run a 4-lap event while working towards this achievement!**
Everyone incorrectly assumed this since all Drift events in the Career are 4 laps long, but this is simply not true. Therefore, **there is a way to outsmart this issue**
and nullify the effect of this coding mistake: if the player were to run a 1-lap event, the best lap score and the total score would be identical, and the value is not divided by laps,
effectively reducing the check to:

$$ total\_score > \operatorname{RoundUp}(\frac{preset\_score}{4}) $$

See it now? It is relatively easy to get this magazine after all, despite this bug:
1. Head to Quick Race and set up a 1-lap Drift event.
2. Get at least 25% of the high score points within that single lap.
3. Go to the Underground mode and win any event to unlock Magazine 22.

## Fix it! Fix it! Fix it!

Before I move on to fix this issue myself, I wanted to find out if it was fixed officially in any of the many game versions released.
* On PC, this bug is present even in the fully patched game.
* On PS2, there is a single version where this bug was fixed! A Japanese re-release of the game, **Underground J** (or **J-Tune**) changed the high score formula
  not to divide the best score by laps. This means that this version of the game **awards the magazine for getting at least 25% of the high score points in the best lap**,
  regardless of how many laps the event has.

Looking at the code, I am certain the original intention was to compare the average lap score:
* The current calculation of dividing the best lap score by laps makes no sense at all, and I cannot think of any plausible reasons for it.
* Rewarding the player only for the best lap makes more sense, but if this was the intention, I don't think the function unlocking the magazine
  would then be taking the $$ laps $$ parameter. It only makes sense to care about this if you intend to calculate an average score across the entire event.

For SilentPatch, it's an easy fix, with one caveat -- this time, I needed this fixed not only in the PC version
but also in the PS2 version, due to the RetroAchievements set. Who says it couldn't be fixed for both platforms, though?

For this **SilentPatch**, I targeted multiple versions of the game:
* For PC, you get an ASI plugin as usual.
* For PS2, you get a PNACH patch for use with PCSX2.

With this bug fixed, I could finally resume my playthrough and at last, get the magazine without much trouble:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/silentpatch-nfsug/screens/Need for Speed - Underground_SLUS-20811_20250305222148.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/silentpatch-nfsug/screens/Need for Speed - Underground_SLUS-20811_20250305222237.jpg" thumbnail="auto" %}
</figure>

However, that's not the only issue fixed in this SilentPatch.

# Other fixes in SilentPatch, going cross-platform

* High scores for Drift events are shown in the menu incorrectly. Before the player sets a score for the first time, the game shows the total target score for the event
  (the one you have to beat for the Magazine 22), but after that, it shows a number not related to the player's score at all. In the video I linked above, **DanielCarter1615**
  figured out that the game saves... style points. With SilentPatch, the total event score is saved instead:
  {% include figures/image.html link="/assets/img/posts/silentpatch-nfsug/screens/SpeedU_ciZyaYL0kV.jpg" thumbnail="auto" %}
* On PC, under very specific circumstances the game could crash while saving. The game checks the time while saving and formats it according to the user's system date format,
  but it only allocates space for 11 characters. While this is fine with common date formats (for example, on my PC it's `dd.MM.yyyy`), some European locales may have
  longer formats (for example `yyyy. MM. dd.`). SilentPatch sets a fixed date format without punctuation and with abbreviated month names
  (like **{{ page.date | date: "%e %b %Y" | strip }}**), so it looks pretty and unambiguous, while also staying within the limit.
  {% include figures/image.html link="/assets/img/posts/silentpatch-nfsug/screens/full/SpeedU_Y9umqmzq50.jpg"
              thumbnail="/assets/img/posts/silentpatch-nfsug/SpeedU_Y9umqmzq50.jpg" %}
* The original PS2 releases had a bug where long opponent names appeared corrupted in the UI. It showed up only in a race against Samantha:
  {% include figures/image.html link="/assets/img/posts/silentpatch-nfsug/screens/full/Need for Speed - Underground_SLUS-20811_20250302130620.jpg"
              thumbnail="/assets/img/posts/silentpatch-nfsug/Need for Speed - Underground_SLUS-20811_20250302130620.jpg" %}
  This bug was later fixed on PC (possibly in a patch), and the PS2 Korean and J-Tune releases, so only the EU/US/JP PS2 SilentPatch includes it.

# Downloads

SilentPatch for the PC and PS2 versions of Need for Speed: Underground can be downloaded from *Mods & Patches*. Click here to head to the respective pages:

{:.flexible-buttons}
<a href="{% link _games/need-for-speed/need-for-speed-underground.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for the PC version</a>
<a href="{% link _games/need-for-speed/need-for-speed-underground-ps2.md %}#silentpatch" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download SilentPatch for the PS2 version</a>
