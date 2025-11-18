---
layout: post
title: "NASCAR 25 PC review -- good game, basic port"
date: 2025-11-18 22:45:00 +0100
excerpt: Curse of the PC versions of annual sports games hits the oval track. Gameplay impressions, benchmarks, Steam Deck compatibility.
game-series: "nascar-25"
image: "assets/img/games/bg/nascar-25-alt.jpg"
thumbnail: "assets/img/games/bg/nascar-25.jpg"
feature-img: "assets/img/games/bg/nascar-25-alt.jpg"
twitter: {card: "summary_large_image"}
tags: [Reviews]
---

* TOC
{:toc}

# Introduction

It's been slightly over a month since NASCAR 25 released on consoles on {% include elements/time.html date="2025-10-14" text="October 14th" %}.
As announced a few months back, we had to wait one more month for the PC release, and it got released according to plan,
on {% include elements/time.html date="2025-11-11" text="November 11th" %}.

<div class="center-blocks">
<iframe src="https://store.steampowered.com/widget/3873970/" frameborder="0" width="646" height="190"></iframe>
</div>

Although I'm not big on NASCAR, I wanted to cover this game ever since I learned it's developed on Unreal Engine 5 by
the legendary Monster Games -- the same studio that gave us Viper Racing, NASCAR Dirt to Daytona,
and Test Drive: Eve of Destruction. In the 2010s, they've been busy working on the new NASCAR Heat games, and after a disastrous NASCAR 21: Ignition from Motorsport Games,
Monster Games got a chance to work on a NASCAR game again, this time under iRacing.

iRacing Motorsport Simulations supplied a review key for the purposes of this review, and so over the past several days,
I played through NASCAR 25 and documented my technical findings. As the game is locked down way more than a typical
UE5 game, it was more difficult than expected, but not impossible. While I can't give you an informed opinion on how accurately this game portrays
stock car racing, I will voice my thoughts on the technicalities, as I tend to do in my reviews.

# Gameplay impressions, aka car go left very well

NASCAR 25 features four racing series:
* ARCA Menards Series (replacing the fictional Xtreme Dirt Tour series, introduced in NASCAR Heat 3)
* Craftsman Truck Series
* Xfinity Series
* NASCAR Cup Series

It's no secret that I'm a tourist when it comes to NASCAR games -- after dabbling with the demos of excellent NASCAR Racing 3 and NASCAR Legends as a kid,
during my adult years I've only played NASCAR Heat 2002 on the PS2, and Heat 2, and Heat 3 on PC (NASCAR Rumble doesn't count in this context);
thus, I lack much insight on how the games have been progressing over the years,
and I have no interest in this sport IRL either, to the point that three-segment races featured in Heat 2 completely caught me off guard.

This is all to say that my opinion of the game's gameplay loop is that of an outsider's. For this piece, I've almost exclusively played the Career Mode
and have not advanced past the ARCA Series or touched the online mode. During that time in the Career Mode, I got to manage my own car, personnel, itinerary, and reputation.
None of those gameplay mechanics are particularly in-depth, and are usually limited to reacting to a message from a team member and making a hiring decision,
or selecting what event to attend. Managing the car has slightly more nuance, as the player needs to balance upgrading the car and keeping it in good shape,
and resources are quite limited. So far, I have always found myself with more than enough money to buy upgrades, but not enough time to get my car in good shape.
Maybe this means my driving is too reckless.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/NASCAR25_Steam-Win64-Shipping_gFb79WQc3b.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/NASCAR25_Steam-Win64-Shipping_vj7qlU0JCN.jpg" thumbnail="auto" %}
<figcaption markdown="span">Finally, I get to inspire someone.</figcaption>
</figure>

Initially skeptical about the prospect of turning left for 15 minutes at a time (as I played at a 25% race length and 4x the fuel usage/tire wear),
I *think* I now see the appeal. For the first few races, I was slightly too careless, punting AI along the way as I wrestled for better positions,
and burning through fuel way too fast. This not only led to me finishing very far down the pack due to me having to pit more often than the rest,
but also the in-game social media coverage of my driving was *dire*.

But then, I started figuring things out. Smoother lines, less aggression, and higher awareness of my car's dimensions, and coasting around the corners
-- each next race in the season was cleaner and more satisfying. I started seeing a shift in perception both in the social media coverage,
but also on the track, as I collided with AI much less -- I'm not sure if I simply got better at avoiding contact, or if the AI respected me more
and gave me space. As much as I'd like to believe it was the AI, it's probably all on me predicting the AI lines better.

Then, the very last race before I sat down to write this review, my pitting strategy and a lucky yellow flag from the AI crashing independently
of my actions, I won the race.

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/NASCAR25_Steam-Win64-Shipping_vkFuL17zcG11.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/NASCAR25_Steam-Win64-Shipping_vkFuL17zcG.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/3873970_20251116140308_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/3873970_20251116140205_1.jpg" thumbnail="auto" %}
<figcaption markdown="span">As I got better, I could see the perception in the in-game social media shift.</figcaption>
</figure>

Unfortunately, the game didn't give me a chance to celebrate my win by doing a victory lap or a burnout. This is still done in real-life races,
and the older NASCAR Heat games from Monster Games included that, so I'm not sure why NASCAR 25 completely omits it. Oh well.

Regardless, I'll keep playing NASCAR 25 more. I want to progress in the career *at least* far enough to enter the Craftsman Truck Series.
Career progression is reputation-based, so the better my driving is, the sooner I'll get invited.

# The technicalities

Now, for the main reason I'm looking into this game. All analysis and benchmarks were done on the launch PC version of the game,
dated **{% include elements/time.html date="2025-11-10" %}**. A small patch was released during the writing of this review,
but it didn't contain any performance changes or fixes to issues I outline here. Since the time I
[published my previous game review]({% post_url 2025-05-23-jdm-japanese-drift-master-review %}), I upgraded my main PC and retired
my aging graphics card to a secondary PC. This makes my benchmarks more meaningful and "true to life", and I can try the game on both setups!

Does it work fine? Does it scale? Does the PC port go above and beyond, since it was released a month after the consoles? Let's find out.

## Game engine, graphics, system requirements

NASCAR 25 runs on **Unreal Engine 5.5**, although unlike the other games I've covered, it's been heavily UE4-ified.
You won't find any signs of Nanite or Lumen in here; they've been permanently disabled at the project level, and no amount
of INI tweaks will get you any ray-tracing. For this game, I am going to completely ignore the minimum requirements,
as they've been copy-pasted straight from iRacing, and I don't trust them to be meaningful. I threw NASCAR 25 at two setups:

* **Intel Core i9-12900K** with an **NVIDIA GeForce RTX 5070 Ti**.
* **Intel Core i7-6700K** with an **NVIDIA GeForce GTX 1070**.

For my impressions, I've been using exclusively the primary PC. However, for benchmarking, I used both.
All screenshots in this article were taken on the Highest quality levels, unless stated otherwise.

***

Graphically, I feel like NASCAR 25 caught the bug of a typical annual sports game -- it doesn't look "bad", but it's far from impressive.
To my knowledge, tracks come straight from iRacing, and they certainly show their age. Lighting is basic and relatively dull, and effects like
the lens flare appear to be similar to stock Unreal Engine 5 effects.

This decision makes sense to me, though -- in the absence of ray-tracing and heavy upscaling, the game looks reasonably sharp, and doesn't require a top-end PC.
Additionally, since it's obviously not open world, in my experience, it's free of any Unreal hitches: I don't think I have seen a shader compilation stutter even once.
The game doesn't seem to be shader-heavy in the first place -- even though it doesn't ship any precompiled PSOs,
at the time of writing this review, my gathered PSO cache file sits at around 760KB, which is not a lot for Unreal standards.

That said, even before I started inspecting the graphics options, I couldn't help but notice how blurry the cinematics are:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/3873970_20251113122630_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/3873970_20251115185802_1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/NASCAR25_Steam-Win64-Shipping_Al7Rt9co7p.jpg" thumbnail="auto" %}
</figure>

These aren't temporal artifacts or anything like this -- these cinematics are simply out of focus! I have no idea if this is a bug
or if cinematics neglect to set the focus points correctly, but I reported it to the developers with an assumption that it's an oversight,
as I can't imagine the camera focusing on a random cameraman is intentional.

## The port's disappointments

With this PC port arriving a month after the console releases, I was hoping the game would be well-adapted for PCs and offer
a wider range of options. Unfortunately, the reality couldn't be further away from the truth, and we instead were given a simple,
straightforward PC port that works, but doesn't offer anything of note either.

On the first boot, the game defaults to disabled VSync, so first-time players see the intro FMV with frame tearing and maxing 100% of their GPU.
The system mouse cursor doesn't ever hide, and the mouse can't be used to navigate menus, so it's on you to tuck it away somewhere.
Keyboard prompts are nonexistent, so it's up to you to figure out the keyboard menu controls.
Even then, you'll soon find out that some actions, like opening the driver name text input field, **require** using the gamepad
(and then you need to use the keyboard to type the name, of course).

On the upside, all input controls are customizable. Unfortunately, they are presented in such a disorganized way that I initially suspected
some of the mappings were listed by mistake, as the game's enormous Input Mapping list includes game actions, followed by... remappable gamepad buttons.

{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/20251118185653_1.jpg" thumbnail="auto"
    caption="\"Toggle mirror\" and radio controls, followed by DPad and gamepad buttons? Sure, whatever." %}


Later, I realized that those are mappings for **menus**, and so they correspond to the legends of the UI actions.[^menu-actions]
While this does make some sense, I feel like they should have been at least separated into a distinct sub-list, just like the axes (throttle/brake/steering) are.
To top it off, there is no way to reset bindings back to the defaults! The only way to do that is by deleting the input configuration file.

[^menu-actions]: My reaction to this realization was approximately like [THIS]({% link assets/img/posts/nascar25-review/i-guess.jpg %}){:target="_blank"}.

The game also lacks any sort of customizable FOV. It's not as much of a port issue, but it would have been welcome to see, especially since ultra-wide
monitors are supported. However, the biggest indicator of this port's simplistic nature is the Display menu.

## In-game graphics options

If you were like me and expected this port to have reasonably extensive graphical options, I have bad news. NASCAR 25 features only the most fundamental
options typical of UE games:

{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/nascar25-graphics-options.png" thumbnail="auto" %}

Missing something? Yes, a lot:
* Instead of an option to select and/or toggle upscalers, or at least a fixed Render Scale option, Dynamic Resolution is listed,
  reminiscent of typical scaling mechanisms in the console games.
* Multi-monitor is not a thing at all, so you're out of luck if you want to play on anything else but your primary monitor.
  You can, of course, move the game window, but the game fails to list resolutions appropriate for the other screens and doesn't play nice with high DPI scaling.
* For Anti-Aliasing, only a typical UE5 scalability option is exposed, adjusting the AA quality. Otherwise, the game always uses TSR and doesn't give the player any alternatives.
  On the upside, when Dynamic Resolution is disabled, TSR seems to work with a 100% screen scaling, effectively becoming a slightly better TAA.
  You can't, however, use FXAA or disable AA entirely.
* While omitting some UE scalability options (like Foliage Quality) makes sense, Reflection Quality would make sense in a game like this, yet it's not exposed in menus.

Let me demonstrate: with a simple `Engine.ini` change, I can make the game look better than the default max details, by disabling forced TSR, and setting the resolution scale to 200%:

```ini
[/Script/Engine.RendererSettings]
r.AntiAliasingMethod=0
r.ScreenPercentage=200
```

The result maxes out my GPU, but looks far better than the default anti-aliasing:
<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/supersample-1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/supersample-2.jpg" thumbnail="auto" %}
</figure>

If users were given an option to use DLAA and/or FXAA, or an option to disable AA entirely, they could rely on DSR configured externally,
without the need for any INI tweaks like this.

## Graphics presets

The game comes with a set of 5 presets that correspond directly to the scalability levels in Unreal: **Low**, **Medium**, **High**, **Very High** (renamed Epic),
**Highest** (renamed Cinematic). Interestingly enough, Epic discourages developers from exposing Cinematic in games as it's only meant for offline rendering (e.g. movies or FMVs),
and yet NASCAR 25 uses it. From what I can tell, those scalability options are *mostly* left untouched from Epic's defaults, although since Lumen is globally disabled,
higher Global Illumination options have barely any noticeable differences.

The presets look as follows. The differences are very subtle, so you'll likely want to click on the images to open them full screen:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/low-1.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/medium-1.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/high-1.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/veryhigh-1.jpg" thumbnail="auto" caption="Very High" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/highest-1.jpg" thumbnail="auto" caption="Highest" %}
</figure>

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/low-2.jpg" thumbnail="auto" caption="Low" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/medium-2.jpg" thumbnail="auto" caption="Medium" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/high-2.jpg" thumbnail="auto" caption="High" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/veryhigh-2.jpg" thumbnail="auto" caption="Very High" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/highest-2.jpg" thumbnail="auto" caption="Highest" %}
</figure>

I'll be honest: with the game not letting me change options in-race (so the comparison screens are not identical), and with differences this small,
pointing out the differences is difficult. Perhaps presets affect more under different circumstances, for example, during the night races,
but during the day, there isn't much to talk about.

* On **Low**, shadows are grainy and have a short draw distance, and textures are low resolution.
* On **Medium**, a vignette effect appears, and textures get a quality bump. Shadows look smoother and more detailed.
* **High** and **Very High** further increase the quality of shadows and draw distance, but I'm not sure if they do anything meaningful in the main menu.
* On **Highest**, shadows draw from afar, and props appear to have "infinite" draw distance.

Overall, the differences seem quite miniscule, other than shadows and the texture resolution. Not sure if they warrant 5 distinct presets,
but my guess is that it was done so they "automatically" benefit from the overkill settings of the Cinematic detail setting.

# Benchmarks

As mentioned before, I benchmarked the game on two PCs, on all graphics presets. For the benchmark, I selected a night race setup
and tried my best to drive as consistently as possible. I selected:
* NASCAR Cup Series.
* Bristol, Bass Pro Shops Night Race.
* Started at the back of the pack and stayed there for the duration of the benchmark.
* Raced in the chase camera.
* Kept the rear-view mirror enabled.
* Started the benchmark directly after taking control of the car, and sampled 30 seconds of data.

For the **RTX 5070 Ti** machine, I performed the benchmark at 1440p, as otherwise all presets had nearly identical readings due to a CPU bottleneck.
On the **GTX 1070** machine, 1080p was enough.

{% include figures/image.html thumbnail="/assets/img/posts/nascar25-review/benchmark-1.webp" style="natural" %}
{% include figures/image.html thumbnail="/assets/img/posts/nascar25-review/benchmark-2.webp" style="natural" %}

The results look somewhat acceptable: similar Low 1%'s and Low 0.1%'s show that the game's performance is stable and consistent.
Both machines started by being CPU-bound, before becoming GPU-bound on the higher details. The claim of a CPU bottleneck on an **i9-12900K** might sound strange,
but it's a bottleneck on a single thread performance: it doesn't show up in Practice or Qualify sessions, so I suspect it's caused by the AI and physics simulation
happening on one or just a few threads for all 40 cars. A game of this type being more CPU-heavy than GPU-heavy makes perfect sense.

With those results, I could draw those conclusions about my hardware:
* Not even an **i9-12900K** has single-thread performance good enough to achieve 120 FPS.
* **RTX 5070 Ti** blasts through the game with ease.
* **i7-6700K** is slightly too slow for stable 60 FPS.
* **GTX 1070** should be fine at Low and Medium details, but it needs to be paired with a more powerful CPU.
* **GTX 1070** may benefit from disabling TSR.

# Steam Deck

When I started this review, this section was intended to be very short -- at launch, the game instantly crashed on the Deck (and on Wine/Proton) in general,
and a rather sparse official disclaimer was published shortly after launch:

> ### Steam Deck Compatibility Information
> {:.no_toc}
> NASCAR 25 does not support Steam Deck.

The game crashed instantly while attempting to execute an illegal processor instruction. I investigated it and found that it was due to the block of code being... encrypted.
On Windows, this same block of code was not encrypted in-memory, yet it was encrypted on-disk, so it looked like under Proton, decryption was either failing
or deliberately not running at all. Just to be sure, I [reported this incompatibility in the Proton repository](https://github.com/ValveSoftware/Proton/issues/9216){:target="_blank"},
and just before this review was finalized, I heard back -- **the game crashed as it exposed an API implementation bug in Wine!** Proton Bleeding Edge has since been updated with a few fixes,
and suddenly, encryption was no longer an issue, and the game boots!

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck1.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck2.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck3.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck4.jpg" thumbnail="auto" %}
</figure>

As the game has anti-debug measures, I was not able to troubleshoot the exact cause properly, and thus my conclusion was incorrect -- encryption was not the root cause of this issue,
and instead, a failure to create a resource executed code that was not decrypted **yet**. If, for any reason, this resource fails to be created on Windows, the same crash would occur -- and
maybe it does, as some people report that the game crashes on launch instantly even on Windows.

***

That said, you probably can tell that the performance on Deck leaves a lot to be desired. Similar to my desktop benchmarks, a severe CPU bottleneck appears in races, while big,
open courses (like Chicago) are GPU-bound. With a full grid of cars on a small oval track, the CPU bottleneck is so significant that it leaves the GPU starving for power, downclocked
to **less than half** of its maximum frequency!

I wasn't able to get the game to maintain a stable 30 FPS no matter what, so I wouldn't consider it Deck playable. However, those findings benefit all users of Wine/Proton,
and are good news for the future owners of a Steam Machine -- the game will probably run great on it. I was able to squeeze a few more frames per second by disabling the rear view mirror
and TSR (via the INI tweak), but it's still underwhelming:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck1-notaa.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/nascar25-review/screens/deck2-notaa.jpg" thumbnail="auto" %}
</figure>

iRacing, please let us disable TSR and mirrors in the cockpit cameras!

# Conclusion

Overall, I'm content with the state of NASCAR 25 as it is now. Sure, I would have preferred if the game scaled better, offered better graphics,
and more PC customization. However, none of those were ever a priority for NASCAR games, and I need to acknowledge that it's treated more like an annual sports game
than a beefed up racing game -- with games of this kind, their absolute priority is to capture a wide range of fans of a particular sport or motorsport,
and those folks don't necessarily have to be gamers.

In the long run, a decision to aim lower might be a better one, as it means more "casual gamers" can enjoy the game.

***
