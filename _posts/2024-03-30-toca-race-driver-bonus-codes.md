---
layout: post
title: "Bonus Codes Generators for TOCA Race Driver"
excerpt: "Reversing RSA using Wolfram Alpha."
feature-img: "assets/img/bonuscodes/bonuscodes-banner.svg"
thumbnail: "assets/img/bonuscodes/bonuscodes-banner.svg"
image: "assets/img/bonuscodes/bonuscodes-banner.png"
game-series: ["toca-race-driver", "toca-race-driver-2", "toca-race-driver-3"]
date: 2024-03-30 15:30:00 +0100
twitter: {card: "summary_large_image"}
tags: [Research, Releases]
mathjax: true
---

* TOC
{:toc}

# Bonus Codes

Hello! This post is just a quick update to announce the addition of new Bonus Codes generators added to the website.
With the addition of the TOCA Race Driver games, there are now 6 games available:
* [Colin McRae Rally 3]({% link _bonuscodes/cmr-3.md %}){:target="_blank"}
* [Colin McRae Rally 04]({% link _bonuscodes/cmr-04.md %}){:target="_blank"}
* [Colin McRae Rally 2005]({% link _bonuscodes/cmr-2005.md %}){:target="_blank"} (including Colin McRae Rally 2005 Plus)
* [TOCA Race Driver]({% link _bonuscodes/toca-race-driver.md %}){:target="_blank"}
* [TOCA Race Driver 2]({% link _bonuscodes/toca-race-driver-2.md %}){:target="_blank"} (including Race Driver 2006)
* [TOCA Race Driver 3]({% link _bonuscodes/toca-race-driver-3.md %}){:target="_blank"} (including TOCA Race Driver 3 Challenge)

To recap -- Bonus Codes was a Codemasters' take on traditional cheat codes. While most other games had specific cheat codes
published by the developers online and in the gaming magazines, Codemasters invented a system where players could buy their "personalized"
cheat codes online or through a phone helpline. For example, that's how this looked in Colin McRae Rally 3 -- the screenshot comes from a game
with SilentPatch installed, unmodded games pointed the player towards
[codemasters.com/bonuscodes/](https://web.archive.org/web/20101201054958/http://codemasters.com/cheats/index.php?&page=1){:target="_blank"} instead:
{% include figures/image.html link="/assets/img/posts/bonuscodes/screens/Rally_3PC_F2XZEABRTM.png" thumbnail="/assets/img/posts/bonuscodes/screens/thumb/Rally_3PC_F2XZEABRTM.jpg" %}

The website was still up around 2011, offering a full set of cheat codes for one game for £2.99.
These days, it's not possible to buy those cheats at all, so the only surviving resources are
some cheats for specific access codes shared by individuals over the years. That's where my generators come in -- allowing users to generate their cheat codes
directly in the web browser.

Thanks to Wayback Machine, we can assemble a mostly complete list of games using Bonus Codes. Aside from the games I already cover on the website,
those games most likely also used Bonus Codes. Some of them **may** have been using regular cheat codes, but Wayback Machine hasn't preserved enough web pages to know.
* Brian Lara International Cricket 2005
* Clive Barker's Jericho
* Colin McRae DiRT
* Race Driver: GRID
* Heatseeker
* Hospital Tycoon
* LMA Manager 2007
* Manchester United Soccer 2005
* Micro Machines V4
* Mike Tyson Heavyweight Boxing
* MTV Music Generator 3 – This is the Remix
* Operation Flashpoint: Resistance
* Perimeter
* Second Sight
* Soldiers: Heroes of World War II

There are also a few games I know are missing from the 2011 version of the website but include Bonus Codes.
These are:
* LMA Manager 2003
* LMA Manager 2004
* LMA Manager 2005
* LMA Manager 2006

I am hoping to eventually publish Bonus Codes generators for as many games as I can, but not all of them may be technically doable.
That said, I said the same about TOCA Race Driver 3 -- until recently. In this case, the recent developments are entertaining
enough that they deserve their section in the post.

# How were TOCA Race Driver 3's cheats cracked?

When I first published generators for the Colin McRae Rally trilogy, I also looked into TOCA Race Driver 3 (but not 1 or 2),
and found out that the generation there is entirely different. CMR games were easy to cover -- these games use a symmetric generator,
or in other words, they generate all the codes for the user's specific access code, and then they check if the sequence entered
by the player matches any of them. Therefore, for my generators, I only had to accurately reimplement the in-game generation functions.
This has also been done by others decades ago -- cheat code generators for all 3 games, as well as TOCA Race Driver 1 & 2,
date back to the early 2000s. [**MobCat**](https://github.com/MobCat/Codemasters-Cheat-Database){:target="_blank"} also hosts
[an online database of precomputed Bonus Codes](https://www.mobcat.zip/CodemastersDB/){:target="_blank"} for those games.

However, TOCA Race Driver 3 is different. For this game, Codemasters switched to an asymmetric generator,
using [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)){:target="_blank"}; the same cryptographic algorithm
that is practically the foundation of online security. This worked great -- to this day, I am not aware of a single generator
or a database of codes.

For a while, I expected the generator to be impossible to reverse engineer, as while the game holds the public key in its executable,
only Codemasters had its private key. Only recently I revisited their implementation of the RSA algorithm present in the game,
and it turned out to be flawed in a way that made the process of obtaining the private key trivial.
To explain this, I need to quickly explain how public and private RSA keys work.

At the most fundamental level, data is encrypted via RSA with a pair of keys, one for each side of the communication.
Data encrypted with the private key can only be decrypted with the public key, and vice versa.
Therefore, with only the public key at hand, it is impossible to encrypt data the same way the private key does,
and in turn, impersonate the holder of the private key.

The process of generating the pair of keys goes as follows:
1. Big prime numbers $$ p $$ and $$ q $$ are picked. They are kept **secret**.
2. $$ n = pq $$ is calculated.
3. $$ e $$ is picked. For the sake of this explanation, we only need to care that the common value selected for this variable is $$ 65537 $$.
   This is also the case for TOCA.
4. $$ (n,e) $$ is our public key. This is the key present in the game's executable.
5. $$ d = e^{-1}\pmod{(p-1)(q-1)} $$ is calculated and kept **secret**. This is our private key, in this case, known only to the developers.

The process of encrypting and decrypting data is then straightforward. The data is encrypted with the private key by calculating
$$ M' = M^d \pmod{n} $$ -- this (with some transformations) is what was given to the player as their personal cheat code.
Later, the game decrypts the encrypted message (as in, the cheat code) by calculating $$ M = M'^e \pmod{n} $$.
If the message decrypted with the public key matches the user's access code and is interpreted as valid, the cheat activates.

Since $$ d $$ is easy to calculate if the primes used to calculate $$ n $$ are known,
the security of the key hinges on $$ p $$ and $$ q $$ being exceptionally difficult to guess.
This is typically achieved by picking huge numbers -- for example, RSA-1024 uses $$ n $$ that is 1024 bits long,
which makes for 309 decimal digits. As of the time of writing this article, this is a large enough number
that it's never been factorized (primes $$ p $$ and $$ q $$ have never been brute-forced).

If TOCA Race Driver 3 used a similarly large number, the algorithm would have been impossible to reverse engineer.
However, their RSA key is much smaller. How many digits does their public key $$ n $$ have?

*20*.

The key used by the game is 8.5 bytes long (the topmost byte only uses 4 bits),
which technically makes the number RSA-68. This a number so relatively small it has never been even considered
in the [RSA Factoring Challenge](https://en.wikipedia.org/wiki/RSA_Factoring_Challenge){:target="_blank"},
and so small that Wolfram Alpha
[does prime factorization of that number even without explicitly being asked to](https://www.wolframalpha.com/input?i=26952959852310653999).
That's how I "cracked" the key; I was curious to see what Wolfram Alpha would tell me about this number,
but instead, it's done everything for me right off the bat. With primes factorized, recalculating the private key
is trivial, and I could update my generators to cover TOCA Race Driver 3's algorithm.

TOCA Race Driver 3 cheats hold one more trivia. The game featured an entire section of Honda championships
and a cross-promo campaign with Honda, where players could unlock those championships for free with a generator
hosted at [honda.co.uk/racedriver/ (archived)](https://web.archive.org/web/20061223081102/http://www.honda.co.uk/racedriver/){:target="_blank"}.
These Honda-specific codes use a different RSA key than the remaining cheats.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/bonuscodes/honda1.jpg" %}
{% include figures/image.html link="/assets/img/posts/bonuscodes/honda2.jpg" %}
<figcaption markdown="span">Honda Demo is available for download, together with StarForce DRM. Don't try it on Windows 10.</figcaption>
</figure>

In the Bonus Codes Generator, I also included a checkbox to only generate the Honda codes,
to emulate the 2006 experience of getting those free cheats (minus all the personal data Honda wanted in return).

# Note for PC players

TOCA Race Driver 2 & 3 have a bug where the access code fails to generate properly on 64-bit systems and always displays
`4294967` (in Race Driver 2) or `????` (in Race Driver 3). For a fix, see [TOCA Race Driver (series)]({% link _games/toca-race-driver (series).md %}).
**If** I ever make a SilentPatch for these games, this fix will be included there too -- but for now, a standalone fix is enough.
