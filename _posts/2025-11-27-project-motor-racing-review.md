---
layout: post
title: "A technical dive into Project Motor Racing -- we're racing, not farming (with mixed results)"
date: 2025-11-27 13:20:00 +0100
excerpt: One of the only games that moved **away** from Unreal Engine, was it worth it? Gameplay impressions from a gamepad user, benchmarks, highlights, and gripes.
game-series: "project-motor-racing"
image: "assets/img/games/bg/project-motor-racing-alt.jpg"
thumbnail: "assets/img/games/bg/project-motor-racing.jpg"
feature-img: "assets/img/games/bg/project-motor-racing-alt.jpg"
twitter: {card: "summary_large_image"}
tags: [Reviews]
---

* TOC
{:toc}

# Introduction

On {% include elements/time.html date="2025-11-25" text="November 25th" %}, Project Motor Racing was released on PC and consoles.
From the player's perspective, it's just yet another racing sim like many others. But, from my perspective, this game attempts something exceptional:
initially started under the name **GTRevival** and developed largely by the same people as the Project CARS games, powered by Unreal Engine 5,
the project got restarted once Straight4 secured a publishing deal with GIANTS Software (of the Farming Simulator games);
the project got renamed to Project Motor Racing, and instead of UE5, it uses... the GIANTS Engine.

I can't think of many (if any at all) other racing games that used UE5 and moved **away** from it, so obviously, I couldn't pass on the opportunity
to dive into it. Last week, I received a review copy from GIANTS Software, so I can check it and see what came out of this unorthodox switch.

# Gameplay impressions

As the game is already out and you've likely seen the other reviews, that are generally strongly unfavourable, I will flip the structure and start
this section with my final impression -- **I don't think anything in PMR is "terrible"** (with one exception, to be outlined below),
**but the problem is that too many parts feel unfinished, untested, or partly broken;**
in my eyes, the game's current bad reception is a textbook definition of "a death by a thousand cuts."

When I checked the game out on Friday, I felt like I'm beta testing a game that is finished in design and content, but months away from release:
UI bugs are rampant, some options flat out don't work and you can't reset some of them them back to default after changing,
menu controller navigation is lacking in many aspects, AI behaviour seems inconsistent and unbalanced between races.
With a day 1 patch, I know at least some of those issues have been fixed, but the overall vibe of "everything is a placeholder" remains.

To give you an example: PMR is advertised as a sim racing game with a strong single-player career and progression. With wording like this, you would expect
the Career Mode to be crafted in a way that rewards the player and lets them get immersed in the rituals of motorsports, right?
In reality, this is how PMR rewards you for winning a race, for "progressing through the game":

{% capture win_caption %}
{% raw %}The first time I saw this pop-up, I exclaimed "That's it?" That is indeed it. Hope you feel satisfied, because you're not getting more.{% endraw %}
{% endcapture %}

{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124122544_1.jpg" thumbnail="auto"
    caption=win_caption %}

We will never have another TOCA Race Driver 3, I know that much. But come on, this isn't even trying; we can do much better than settling on this "programmer art"
of user experience.

***

To give credit where it's due, my **overall** experience wasn't hopelessly bad. I played the game on PC exclusively on the Xbox One gamepad, only in single player,
and I settled on playing the career mode starting from the slowest cars. Personally, I thought the gamepad controls are *fine* -- not great,
as they make countersteering too difficult, but good enough that someone like me, who isn't exactly high skill in simulation games, can play the game and have fun.
As with practically everything in this game, there is a clear room for improvement, but I wouldn't call it unplayable.

Graphically, the game looks OK at best: it can look extremely dated in some aspects, but not to the level of being distracting,
and at least it's free of upscaling artifacts (by default). Since Unreal Engine 5 was dropped, the entire rendering pipeline is naturally
raster-based (no raytracing), and it shows: daytime looks flat and uninspiring, but at least the sunsets can make the lighting pop.
It's no coincidence that this is also the setting of most of the game's official promotional material...

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251121171748_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251123211008_1.jpg" thumbnail="auto" %}
<figcaption markdown="span">I really like how their grass and overall foliage look, though. That Farming Simulator engine is showing its roots (pun intended).</figcaption>
</figure>

I enjoyed my time throwing Porsche 964s and the GT4 and GTO cars on various tracks, so I was very close to saying that my driving experience was "very good", BUT...

## What's with this AI!?

As I mentioned before, I'm not a particularly skilled player in the sim games. When I "fear the AI", most of the time I mean they are prohibitively fast and
beyond my skill level. In PMR, I found that I can match them at around 80% difficulty, but I feared them in another meaning of that term -- in the current game build,
they actively want to murder the player:

<figure class="media-container small">
{% include figures/video-iframe.html link="https://www.youtube.com/embed/UJV6owxfbFc" %}
{% include figures/video-iframe.html link="https://www.youtube.com/embed/354cISrDtv8" %}
{% include figures/video-iframe.html link="https://www.youtube.com/embed/aAUpwezUCf8" %}
<figcaption markdown="span">This is just a few of the many frustrating moments I had.
I ended up retiring from the Nordschleife 24h race after countless attempts ruined by the murderous AI.</figcaption>
</figure>

Before the release, a few people behind the game swore how lifelike the AI is and how it's the best they've ever seen in a video game.
The current version of the game shows the polar opposite -- these bots are good at driving their cars (sometimes a little too good),
but they obsessively stick to the racing line and have no qualms about ramming you if you're in the way. It's like we are back to
how things looked in Gran Turismo 2, but back then, the stakes were much lower, and you could freely trade punches with the AI without fear of
damaging your car and forfeiting the race.

I even posted some of these clips online and asked better racers than me: "Did I do anything wrong here? Did I divebomb too much and give no chance for the AI
to react?" Nope, at least in the examples I showed above, I was in the clear, and it's the AI behaviour that in real life would have gotten them kicked out of the track.
Oh, and did I mention that if **you** get pushed out of the track by the AI car, **you** end up getting a penalty for exceeding the track limits?
Apparently, the race marshals are in cahoots with these bots.

This has likely been the most prominent problem with Project Motor Racing so far, and practically everyone is outspoken about it.
As of the time of writing this review, the developers have acknowledged that AI needs more spatial awareness and will be working on improving that,
so maybe soon we'll see some change.

## What about mods?

There is one aspect of PMR I can't criticize at all: it's been designed with moddability in mind. Every relevant parameter is out there in plain text,
mod tools (based on the tools for Farming Simulator) are already available, and we will even see mods **on consoles** delivered through the ModHub,
just as in FS25. At the time of writing this review, a few official mods are already available, and they serve as examples of what people can achieve.

With everything being out in the open, everyone peeked into the files straight away and discovered something interesting: despite the claims of
"AI using the same physics as the player" (which appears to be *technically* true), AI cars seem to be given different tire and engine data.
People suspected that the AI generally has more grip than the player, as their starts and cornering on the cold tires are inhuman.

I modified one of the vehicle's Hadron definition data files to give myself the AI tires, and I accidentally turned PMR into a thoroughly enjoyable
arcade racer:

<blockquote class="twitter-tweet" data-align="center" data-conversation="none"><p lang="en" dir="ltr">If you use the AI tire data on the player car and disable tire wear, <a href="https://twitter.com/projectmracing?ref_src=twsrc%5Etfw">@projectmracing</a> turns into Forza Horizon and I think that&#39;s fun as hell. <a href="https://t.co/lpl6eGErzm">pic.twitter.com/lpl6eGErzm</a></p>&mdash; Silent (@__silent_) <a href="https://twitter.com/__silent_/status/1992669249220014261?ref_src=twsrc%5Etfw">November 23, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I genuinely enjoyed trying out a few cars in this "Project CARS 3 Mode," and I would love for it to eventually appear in the game as a separate mode.
It wouldn't make sense for the Career or Ranked Online, of course, but an ability to set up an Arcade Race Weekend and an Arcade Online lobby could be great.
The data is there already, after all. And if it doesn't happen, we can always mod it in.

# The technology

All analysis (except for Steam Deck) and benchmarks were done on the **1.4.0.1** PC version,
dated **{% include elements/time.html date="2025-11-21" %}**. The Day 1 Patch bumped the game up to **1.5.0.0** and should provide some minor CPU performance optimizations,
but I did not re-time my benchmarks with it.

## Game engine and system requirements

As mentioned earlier, PMR is no longer using Unreal Engine 5. We're looking at **GIANTS Engine 10.0**, previously used in Farming Simulator 25, used as a base,
with Straight4's in-house **Hadron** vehicle dynamics model. Just like with NASCAR, I threw PMR at two setups:

* **Intel Core i9-12900K** with an **NVIDIA GeForce RTX 5070 Ti**. This rig sits well above the recommended system requirements.
* **Intel Core i7-6700K** with an **NVIDIA GeForce GTX 1070**. This rig is under the minimum requirements, so I can't expect miracles.

For my impressions, I've been using the primary PC. However, for benchmarking, I used both.
All screenshots in this article were taken on the Ultra quality level, unless stated otherwise.

In general, I did not encounter too many tech issues while trying the game. I did have the game crash around three times and reported them,
but it wasn't anything consistent and reproducible. The game ran at well over 60FPS at 1080p during the races, although I was heavily CPU-bound even on my i9,
while the GPU seldom maxed out, even with VSync disabled.
In the current build, Vertical Sync appears to be broken, and it instead engages an inaccurate frame limiter that introduces jitter, **but** the game also doesn't
tear frames while in the windowed mode, so a combination of VSync off + Borderless Fullscreen allowed me to play without issues.
Earlier review copies reportedly also suffered from intense stutter, but we have received an update just before I got my hands on the game, and this issue must have been resolved,
as I encountered none of that.

The GIANTS Engine has one more upside to it that is quite unusual -- debug visualizations and performance metrics are freely available even in public builds!
Hidden behind a single change in an XML file are some interesting tools:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251121152544_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251121152636_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251121152805_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251121155425_1.jpg" thumbnail="auto" %}
</figure>

Some of them ended up being useful for this review!

## In-game graphics options

Project Motor Racing features a set of options similar to Farming Simulator 25:

<figure class="media-container">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/pmr-display-options.png" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/pmr-graphics-options.png" thumbnail="auto" %}
</figure>

It's good to see a good range of options you would expect from a modern game, and all options can be adjusted on the fly during the race.
Some highlights include:

* Multiple post-processing anti-aliasing options -- **TAA**, **DLAA**, **FSRAA**. Anti-aliasing can also be disabled, which is very welcome.
  The review version also listed **Intel XeSS** as a valid AA option, but it's gone for me in 1.5.0.0; maybe it was locked off on NVIDIA cards.
* Multiple upscaling options -- **FSR1**, **FSR3**, **DLSS4**. Similar to AA, review copies had **Intel XeSS**, but 1.5.0.0 does not.
* **DLSS** and **FSR3** Frame Generation are available, but personally, I don't see much point in using frame generation in a game like this.
* The game scales down very well, going beyond the typical "Low" settings. The best example of that is the **SSAO Quality** option,
  where Low/Medium/High/Very High gets you **XeGTAO**, but there is also a Mobile option, which gets a bog standard **SSAO**:
  <figure class="media-container small">
  {% include figures/image.html link="/assets/img/posts/pmr-review/screens/full/12020224241480761344_20251124203630_1.jpg"
            thumbnail="/assets/img/posts/pmr-review/12020224241480761344_20251124203630_1.jpg" caption="Off" %}
  {% include figures/image.html link="/assets/img/posts/pmr-review/screens/full/12020224241480761344_20251124203639_1.jpg"
            thumbnail="/assets/img/posts/pmr-review/12020224241480761344_20251124203639_1.jpg" caption="SSAO" %}
  {% include figures/image.html link="/assets/img/posts/pmr-review/screens/full/12020224241480761344_20251124203647_1.jpg"
            thumbnail="/assets/img/posts/pmr-review/12020224241480761344_20251124203647_1.jpg" caption="XeGTAO" %}
  </figure>

The only significant option I am missing here is proper multimonitor support -- not even spanning the game across multiple displays,
as that is officially confirmed to be coming in the future, but there isn't even an option to select the output monitor!
You're stuck to playing the game on whatever your primary screen is.

## Graphics presets

The game comes with four graphics presets: **Performance**, **Balanced**, **Quality**, and **Ultra**.
They cover most of the options available in-game, but there is more configuration the user can do:
* The lowest preset is not as low, and the highest preset is not as high as the game can go. Users can tweak graphical fidelity further.
* Every preset enables TAA, so those who want to use a different anti-aliasing solution, upscaling, or framegen need to manually correct it afterwards.
* Every preset leaves Depth of Field disabled.

The presets look as follows:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200200_1.jpg" thumbnail="auto" caption="Performance" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200209_1.jpg" thumbnail="auto" caption="Balanced" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200216_1.jpg" thumbnail="auto" caption="Quality" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200224_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200421_1.jpg" thumbnail="auto" caption="Performance" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200429_1.jpg" thumbnail="auto" caption="Balanced" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200437_1.jpg" thumbnail="auto" caption="Quality" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200447_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

* On **Performance**, the game lacks any shadows, has the most basic AO, and a low draw distance. Honestly?
  That's good, we need more games where the lowest details go really low.
* On **Balanced**, shadows get introduced, particles look denser, proper clouds appear in the sky at night, object draw distance increases,
  and cars generally are shaded nicer.
* On **Quality**, shadow quality, particle density, and objects draw distance increase further.
* On **Ultra**, screen-space reflections are introduced, shadow quality and objects' draw distance increase even more.

But hey, this time we have the profiling data available in the game, so we don't need to settle for comparing only by eye!
I won't be breaking down every single metric here, but you can compare how the CPU and GPU costs of options increase with the details going up.
If you're struggling to hit satisfactory frame rates, this may provide useful insight on what options to turn down.

CPU metrics:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200650_1.jpg" thumbnail="auto" caption="Performance" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200709_1.jpg" thumbnail="auto" caption="Balanced" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200729_1.jpg" thumbnail="auto" caption="Quality" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200803_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

GPU metrics:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200654_1.jpg" thumbnail="auto" caption="Performance" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200715_1.jpg" thumbnail="auto" caption="Balanced" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200732_1.jpg" thumbnail="auto" caption="Quality" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/12020224241480761344_20251124200808_1.jpg" thumbnail="auto" caption="Ultra" %}
</figure>

# Benchmarks and performance

I benchmarked the game on both PCs, on all graphics presets, with TAA and no upscaling.
My benchmarking environment is also the same I used for the above nighttime preset comparisons:
* Porsche 911 GT3 Cup (992).
* Lime Rock Park Road Course.
* 31 Opponents.
* 20:00 race start time.
* Autumn, Rainfall.
* In each benchmark, I started at the back of the pack and followed the AI closely without overtaking them.

Both benchmarks were performed on the 1.4.0.1 version of the game. 1.5.0.0 made a few performance fixes to particles
and adjusted the draw distances of some objects, so you may expect to see performance **slightly better than what I had**.

{% include figures/image.html thumbnail="/assets/img/posts/pmr-review/benchmark-1.webp" style="natural" %}
{% include figures/image.html thumbnail="/assets/img/posts/pmr-review/benchmark-2.webp" style="natural" %}

The results on the primary PC look... acceptable, but not mindblowing. It's not immediately evident on the benchmark,
but the lower presets were CPU-bound, as for some reason the game struggles to submit the render commands to the GPU efficiently,
and bottlenecks on a single CPU thread are commonplace. On higher detail levels, GPU usage rose drastically,
but so did the CPU load on the render thread, as draw distances also increased. I think only on Ultra I reached the point where
the GPU became the obvious bottleneck, hence the sharp decline in the frame rates.

Results on the secondary PC are abysmal, but this PC is under the minimum system requirements, both CPU and GPU-wise.
Those results don't surprise me.

In my subjective opinion, the GPU performance of the game satisfies me, but the CPU performance leaves plenty of room for improvement,
especially since you can't easily reduce the CPU bottleneck through the existing options in the game.
Even though Hadron is the main contributor to the game's overall CPU load, in my tests, the heaviest strain was always on the render thread,
and in some spots on specific tracks, I couldn't even maintain a stable 60 FPS on Ultra **in 1080p**:
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/ProjectMotorRacingGame_6PhTTLM6mp.jpg" thumbnail="auto" %}
On this shot, you can see that the GPU is hardly busy at all, yet the frame rate is poor, and a few CPU threads work overtime.
The in-game CPU profiler clearly shows the culprit -- rendering the scene takes **over 17.6 milliseconds**, with nearly half of this time
spent on generating the command buffers for the GPU to render!

# Steam Deck

This time, this section is going to be very brief! If you want to play PMR on a Steam Deck, my advice is: **don't**.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/20251125150800_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/20251125150849_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/20251125150957_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/pmr-review/screens/20251125151430_1.jpg" thumbnail="auto" %}
</figure>

The issue with the Steam Deck is that even though the game is very scalable on the GPU front, you can't do much to save yourself
if your CPU isn't up to scratch. In this case, Deck's CPU is way underpowered to deal with the game's physics engine,
so the game doesn't even run at a normal speed -- instead, if Hadron is unable to perform the calculations it wants,
the game slows down. On Deck, you're effectively stuck to driving in slow motion, even on the very lowest details, upscaling,
and when you're alone on the track. While it is possible to lower the physics processing rate through modding,
this most likely leaves you unable to play multiplayer, and I am not even convinced it would be enough if the game bottlenecks
on a render thread.

None of this is a surprise given the game's system requirements, but at least this test proves the game works fine on Proton.
I suspect it will be performing quite well on Steam Machines, or at least I hope so.

# What's next?

I won't lie -- I think that, in the current state, Project Motor Racing simply isn't good.
The developers already acknowledged the issues and promised fixes, but will it be enough, or will people simply move on to other games?
I want to believe they can turn this around, because nothing in the game is *fundamentally* broken and simply needs time.
This leads to my main point, though: PMR is currently simply unfinished, and I don't say that often.

Something clearly went wrong, and the game got hit by an immovable, rushed release date.
Looking at how many issues I reported over a single weekend of trying the review copy, I think it's a reasonable conclusion.
Over just a few days, I ended up with a direct line to the dev team, and stumbled upon multiple issues that likely haunted other,
less tech-oriented reviewers.

Personally, I have to give credit to PMR for recognizing the importance of letting different people
try the game early -- in this case, giving me a review copy evidently paid off 🙂
The main reason I reach out for early copies nowadays is to break them in a controlled environment,
and PMR proves it best so far that this is mutually beneficial for both my services and for the game.

That said, those reviews are not going to become a regular thing; after NASCAR 25, this is most likely my last review for 2025.
