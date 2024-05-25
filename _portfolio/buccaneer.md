---
title: "Buccaneer"
image: "assets/img/portfolio/thumb/buccaneer.jpg"
feature-img: "assets/img/portfolio/buccaneer.jpg"
date: 2024-07-01
game-series: "buccaneer"
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2024-07-01" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam, GOG)" %}

{% capture portfolio-contents %}
Buccaneer is a 17th-century Caribbean 3D adventure that blends high-seas combat with resource management.
Opt for combat-only, engage in ship-to-ship battles or lead crew boardings.
Dive into the buccaneer world through campaigns. Plunder, negotiate, survive, and live to tell the tale!

> I've been contracted with consultation and bugfixing of the game in preparation for a digital release on Steam and GOG.
> I shipped appropriate DirectDraw and CD Audio wrappers and rolled out a stub DirectPlay wrapper to remove an invasive dependency
> on a legacy Windows component not installed in the OS by default,
> gracefully disabling the game's obsolete networking functionality.
>
> The original game was released in a terrible state and barely worked even back in 1997.
> Although many problems were addressed by bundling [DDrawCompat](https://github.com/narzoul/DDrawCompat),
> I also had to fix numerous original game issues ranging from crashes, memory leaks, and lack of error checking,
> to unimplemented basic features -- like the SFX volume option not loading from the settings, or the game crashing
> when attempting to select empty save slots.
> Although the game's mediocre quality is still evident, with my fixes it can be played without major blockers.
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
