---
layout: post
title: "Discovering cheat codes in Midnight Club: L.A. Remix"
excerpt: "Official cheat codes found 15 years after the release."
thumbnail: "assets/img/games/bg/midnight-club-la-remix.jpg"
feature-img: "assets/img/games/bg/midnight-club-la-remix.jpg"
image: "assets/img/games/bg/midnight-club-la-remix.jpg"
game-series: "midnight-club-la-remix"
date: 2023-12-27 18:35:00 +0100
twitter: {card: "summary_large_image"}
tags: Research
---

* TOC
{:toc}

# Introduction

As of the time of writing this post, it was yesterday when I learned that [Midnight Club: L.A. Remix](https://en.wikipedia.org/wiki/Midnight_Club:_Los_Angeles#Midnight_Club:_L.A._Remix)
has a dedicated menu to input the cheat codes, but no known codes exist.
[Numerous claims about different cheat codes circulate](https://web.archive.org/web/20231227135328/https://gamefaqs.gamespot.com/psp/945896-midnight-club-la-remix/answers/14171-cheats),
but they appear to be all fake. Inspired by the recent findings in [Gran Turismo 4](https://twitter.com/Nenkaai/status/1639763447826071554)
and [Gran Turismo PSP](https://www.reddit.com/r/granturismo/comments/1869me9/gt_psp_cheat_codes_found_all_cars_and_maximum/), I dived into MCLA Remix to look for the cheat codes.

A brief look around the game's code reveals the game has **11 previously unknown cheat codes**, with 12 more prototype-only cheat codes that are locked by default!
The game locks them behind a check against the serial hardcoded in the executable -- and only allows to use those cheat codes on the prototype (`ULET`/`ULUT`) builds.

# List of cheat codes

*This list can also be found in [Bonus Codes]({% link _bonuscodes/midnight-club-la-remix.md %}).*

These are the cheat codes supported by the game out of the box:
{% assign mcla_remix_cheats = site.data.cheat-codes['midnight-club-la-remix'] %}

<div class="bonuscodes output">
    <div class="border tr"></div>
    <div class="content">
      <dl>
         {% for cheat in mcla_remix_cheats['cheats'] %}
            <div><dt>{{ cheat.description }}:</dt> <dd>{{ cheat.name }}</dd></div>
         {% endfor %}
      </dl>
    </div>
    <div class="border bl"></div>
</div>

Prototype-only cheat codes check against the prototype serial. They can be accessed once this check is patched out:
<div class="bonuscodes output">
    <div class="border tr"></div>
    <div class="content">
      <dl>
         {% for cheat in mcla_remix_cheats['prototype-cheats'] %}
            <div><dt>{{ cheat.description }}:</dt> <dd>{{ cheat.name }}</dd></div>
         {% endfor %}
      </dl>
    </div>
    <div class="border bl"></div>
</div>

To unlock the prototype cheat codes in the final game builds, use the following cheats in [PPSSPP](https://www.ppsspp.org/) or in cwCheat on your PSP/PS Vita:
```
_S ULUS-10383
_G Midnight Club: L.A. Remix [US]
_C1 Unlock prototype cheats
_L 0x20067094 0x00000000

_S ULES-01144
_G Midnight Club: L.A. Remix [EU]
_C1 Unlock prototype cheats
_L 0x20067094 0x00000000

_S ULJS-00180
_G Midnight Club: L.A. Remix [JP]
_C1 Unlock prototype cheats
_L 0x20068A54 0x00000000

_S ULJM-05904
_G Midnight Club: L.A. Remix (Rockstar Classics) [JP]
_C1 Unlock prototype cheats
_L 0x20068A54 0x00000000
```

***

Most of the cheats are quite standard and not that interesting, but the **Stronger special ability effects** cheat is an exception -- it makes a Roar ability look quite entertaining:
{% include figures/video.html link="/assets/img/posts/mcla-remix-cheats/mcla-roar.mp4" attributes="controls"
        caption="This effect is usually not *that* strong." %}

Additionally, the 5 secret biker head models appear to be reused from the PSP version of Midnight Club 3: DUB Edition:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/mcla-remix-cheats/ULUS10383_00000.jpg" %}
{% include figures/image.html link="/assets/img/posts/mcla-remix-cheats/ULUS10383_00001.jpg" %}
{% include figures/image.html link="/assets/img/posts/mcla-remix-cheats/ULUS10383_00002.jpg" %}
{% include figures/image.html link="/assets/img/posts/mcla-remix-cheats/ULUS10383_00003.jpg" %}
{% include figures/image.html link="/assets/img/posts/mcla-remix-cheats/ULUS10383_00004.jpg" %}
</figure>

# The obfuscation algorithm

The cheat strings use an obfuscation algorithm to "hide" them, presumably to make them harder to spot when disassembling the executable.
The algorithm used is simple and reversible -- to document all the cheat codes, I wrote a small decryption program, and later simplified it and cleaned it up
with the help of [Nenkai](https://github.com/Nenkai).

The encryption and decryption routines are as follows:

```python
def encryptCheat(cheat):
    output = ""

    inputSalt = ord('E')
    for ch in cheat:
        char = ord(ch) + inputSalt
        outputSalt = ord('{' if char < ord('A') else 'A')
        output += chr(((char - ord('A')) % 58) + outputSalt)
        inputSalt += 1
    return output

def decryptCheat(cheat):
    output = ""

    inputSalt = ord('E')
    for ch in cheat:
        charOrd = (ord(ch) - ord('A') - inputSalt) % 58
        output += chr(charOrd + ord('A'))
        inputSalt += 1
    return output

if __name__ == "__main__":
    print('Cheats:')
    cheats = [
        'nAAtxtvFMCvH',
        'xyzICwF',
        'CmtsKyIML',
        'DFnMDDKsKAzP',
        'DGFvx',
        'rDnBxJv',
        'DwvrAyus',
        'DwvrAyut',
        'DwvrAyuu',
        'DwvrAyuv',
        'DwvrAyuw',
    ]
    for ch in cheats:
        print(f'{ch}: {decryptCheat(ch)}')

    print('')
    print('Prototype cheats:')
    prototype_cheats = [
        'lxy',
        'nmz',
        'qBF',
        'nmFv',
        'nuGwtI',
        'AmEHH',
        'nmEG',
        'lxyqpIy',
        'KAAs',
        'lsEC',
        'CAnF',
        'yAEApB'
    ]
    for ch in prototype_cheats:
        print(f'{ch}: {decryptCheat(ch)}')
```
