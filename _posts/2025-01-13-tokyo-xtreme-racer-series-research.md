---
layout: post
title: Tokyo Xtreme Racer -- series research
date: 2025-01-13 23:00:00 +0100
excerpt: Miscellaneous pieces of info about the classic Tokyo Xtreme Racer games.
game-series: ["tokyo-xtreme-racer-zero"]
image: "assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
thumbnail: "assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
feature-img: "assets/img/games/bg/tokyo-xtreme-racer-zero.jpg"
tags: [Research]
mathjax: true
---

{:.sidenote}
Last update: {% include elements/time.html date=page.date %}

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

# Post changelog

* {% include elements/time.html date=page.date %} -- initial version.
