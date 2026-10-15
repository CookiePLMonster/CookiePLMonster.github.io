---
layout: post
title: Tokyo Xtreme Racer -- series research
date: 2025-01-13 23:00:00 +0100
last_modified_at: 2026-10-15 14:00:00 +0200
excerpt: Miscellaneous pieces of info about the classic Tokyo Xtreme Racer games.
game-series: ["tokyo-xtreme-racer", "tokyo-xtreme-racer-2", "tokyo-xtreme-racer-zero", "tokyo-xtreme-racer-drift"]
image: "/assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
thumbnail: "/assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
feature-img: "/assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
tags: [Research]
mathjax: true
---

{:.sidenote}
Last update: {% include elements/time.html date=page.last_modified_at %}

As a new Tokyo Xtreme Racer [is just around the corner](https://store.steampowered.com/app/2634950/Tokyo_Xtreme_Racer/){:target="_blank"},
I spent some time playing the classic TXR games. As I go through the games in order, I wanted to note some things I encountered.

This is a [Research]({% link pages/categories.html %}#Research)-style post -- as I go through more games, I will keep updating it with new findings.
This post is reserved for the "classic" games only; I will most likely have another post about the 2025 Tokyo Xtreme Racer in the future!

* TOC
{:toc}

# Tokyo Xtreme Racer (Dreamcast)

## Faulty car unlocks

When localizing Shutokō Battle for the West, Crave also changed several gameplay aspects of the game. Unlike in the Japanese release,
in Tokyo Xtreme Racer you unlock several cars by beating the opponents who own them. One of those rivals is **Midnight Cinderella**,
whose TYPE-FDD can be purchased after you win the race.

Even though I obviously beat this rival, the car never unlocked for me. I never ended up figuring out the exact cause of this,
but I know I wasn't the only one. Other people also encountered this issue, others had the rival cars unlock too early
before they defeated the rival driving them.

This doesn't surprise me in the slightest -- considering how this aspect of the game has been changed by the publisher during
the localization process, it is highly likely they implemented it wrong and introduced a few rare bugs.

***

# Tokyo Xtreme Racer 2 (Dreamcast)

## Aspect Ratio inconsistencies

While TXR2 has a "native" widescreen option, named **Wide TV**, its behavior is strange. When Dreamcast (real or emulated)
uses a VGA output, this option doesn't work at all. In VGA, the game always outputs a 4:3 image, and it looks exactly how you would expect:

{% include figures/image.html link="/assets/img/posts/txr-research/vga.jpg" style="natural" %}

When using Composite or RGB outputs, the option works, but the results are rather strange:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr-research/normal.jpg"
        caption="**Normal TV** produces a horizontally stretched image." %}
{% include figures/image.html link="/assets/img/posts/txr-research/wide.jpg"
        caption="**Wide TV** produces a horizontally squashed image, as expected of anamorphic widescreen present in such retro platforms." %}
</figure>


I did not get the chance to look into the game's code, so I started experimenting with stretching the images instead, using the formulas from
the [Pixel aspect ratio](https://en.wikipedia.org/wiki/Pixel_aspect_ratio){:target="_blank"} page on Wikipedia. Treating Dreamcast's output signal
as 720x480 and rescaling from there, I was able to get better results:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/txr-research/normal-par.jpg"
        caption="When scaling with a PAR of $$ {640 \over 720} = 0.\overline{8} $$, **Normal TV** looks better, but not the same as VGA." %}
{% include figures/image.html link="/assets/img/posts/txr-research/wide-par.jpg"
        caption="When scaling with a PAR of $$ {853 \over 720} \approx 1.1847 $$, **Wide TV** looks nearly identical to VGA." %}
</figure>

So what's going on with **Normal TV**? I initially couldn't figure out the maths behind it, but then I figured I'd try to scale it,
incorrectly, with an inverse of the scaling used for **Wide TV**: $$ {720 \over 853} \approx 0.844 $$. This... gave me an exact match!

{% include figures/image.html link="/assets/img/posts/txr-research/normal-par2.jpg" style="natural" %}

This makes me suspect that the game scales for Composite output more or less like:

```c
float arCorrection = 853.0 / 720.0;
if (WideTV)
   AR *= arCorrection;
else
   AR /= arCorrection;
```

If this is true, it's completely incorrect and is likely producing incorrect image on CRT TVs. If I look into the game's code in the future,
I might be able to confirm or deny this suspicion properly, but as of the time of writing this post, I haven't tried to disassemble any Dreamcast games.

My conclusion: **When emulating, don't bother with the in-game widescreen option. Just use VGA output and a widescreen cheat.**

***

# Tokyo Xtreme Racer: Zero (PlayStation 2)

Nothing here yet, but I published a few PCSX2 patches for this game! Head over to
[Tokyo Xtreme Racer: Zero]({% link _games/txr/tokyo-xtreme-racer-zero.md %}) if you want to take a look.

***

# Tokyo Xtreme Racer: Drift (PlayStation 2)

## Soundtrack differences

For the longest time, it was believed that for TXR Drift, Crave changed the soundtrack assignments deliberately.
I looked into that, and the reality seems to be a lot more boring -- Drift appears to be based on a non-final Kaidō Battle code,
but used the final music data, and the two ended up being "out of sync". This is clear when the soundtrack assignments are shown in a table:
the Night music assignments are off by two.

{% capture songs-table %}
| Music           | Kaidō Battle                | TXR Drift                                |
| --------------- | --------------------------- | ---------------------------------------- |
| Transmission    | Game Title                  | Game Title                               |
| Blue Dream      | Main Menu                   | Main Menu                                |
| Silver Surfer   | Sponsors                    | Sponsors, Parking Lot (Night)            |
| Spark           | Track Intro                 | Track Intro                              |
| Baseball Kids   | Conquest Menu (Day)         | Conquest Menu (Day)                      |
| Hell Outta Here | Parking Lot (Day)           | Parking Lot (Day), Conquest Menu (Night) |
| Banger          | Race Music (Day)            | Race Music (Day)                         |
| Rodeo Drive     | Race Music (Day)            | Race Music (Day)                         |
| You Know        | Race Music (Day)            | Race Music (Day)                         |
| Vanish Into     | Race Music (Day, Raining)   | Race Music (Day, Raining)                |
| Miss Shift      | Race Music (Day, Snowing)   | Race Music (Day, Snowing)                |
| Trust No One    | Replay (Day)                | Replay (Day)                             |
| Lovely Smashin' | Win                         | Win                                      |
| Mission         | Conquest Menu (Night)       | Race Music (Night)                       |
| Gotta Goin' On  | Parking Lot (Night)         | Race Music (Night)                       |
| Ghostly         | Race Music (Night)          | Race Music (Night)                       |
| Groovy Rotation | Race Music (Night)          | Race Music (Night)                       |
| Trail Off       | Race Music (Night)          | Race Music (Night)                       |
| Banzai Robo     | Race Music (Night)          | Tricker/Tricky Intro                     |
| Howl            | Race Music (Night)          | Lose                                     |
| Pyro Mania      | Tricker/Tricky Intro        | Slasher Intro                            |
| Waiting         | Lose                        |                                          |
| Meifumadou      | Slasher Intro               | Emotional/Drift King Intro               |
| Insane          | Slasher Battle              |                                          |
| Phantom         | Emotional/Drift King Intro  | Replay (Night)                           |
| Go For Broke    | Emotional/Drift King Battle |                                          |
| Deadly          | Replay (Night)              |                                          |
| Going Home      | End Credits                 | End Credits                              |
| Bro             | Cruise (Day)                | Cruise (Day)                             |
| Sis             | Cruise (Night)              | Cruise (Night)                           |
{% endcapture %}

{% include elements/details.html summary="Music in KB and TXT Drift. **Click to expand.**" content=songs-table %}

Internally, I suspect that the enum used for the soundtrack IDs in TXR Drift comes from an earlier version of the game
that didn't have any unique music for **Conquest Menu (Night)** and **Parking Lot (Night)**. On the table, you can see that:
* For those two, TXR Drift uses music already used elsewhere.
* After those, all music assignments are shifted by two.

That is not the only issue present in TXR Drift. More things regressed compared to Kaidō Battle:
* TXR Drift has a bug where boss-exclusive battle music gets forcibly overwritten with generic music selection
before the race starts. This results in several audio tracks being left completely unused.
* The music player cuts off the final two songs, making "Deadly" and "Going Home" inaccessible.
* The music player also names most of the songs incorrectly, further hinting at TXR Drift's code being dated back to when the soundtrack selection was different.

{% include figures/image.html link="/assets/img/posts/txr-research/Tokyo Xtreme Racer Drift_SLUS-21236_20261015130613.webp" thumbnail="auto"
      caption="Many track names don't match KB or the official TXR Drift soundtrack." %}

I published a PNACH patch correcting all those mistakes and bringing full soundtrack parity between KB and TXR Drift.
Despite this **technically** being a small SilentPatch, I decided to leave the patch named "Japanese Soundtrack",
as the past belief was that those changes were intentional and not caused by bugs.

You can get the patch from *Mods & Patches*:

<a href="{% link _games/txr/tokyo-xtreme-racer-drift.md %}#jp-soundtrack" class="button" target="_blank">{{ site.theme_settings.download_icon }} Download Japanese Soundtrack</a>

***

# Post changelog
* {% include elements/time.html date="2026-10-15 14:00:00 +0200" %} -- soundtrack research in TXR Drift.
* {% include elements/time.html date=page.date %} -- initial version.
