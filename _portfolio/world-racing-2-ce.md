---
title: "World Racing 2: Champion Edition"
image: "assets/img/portfolio/thumb/world-racing-2-ce.jpg"
feature-img: "assets/img/portfolio/world-racing-2-ce.jpg"
date: 2022-12-08
game-series: "world-racing-2-ce"
---

{% assign portfolio-client="*Independent*, for UniqueGames" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2022-12-08" | date: page.date-format }} (Steam)#{{ "2023-10-26" | date: page.date-format }} (ZOOM Platform)#{{ "2023-11-27" | date: page.date-format }} (GOG){% endcapture %}
{% assign portfolio-platform="PC (Steam, ZOOM Platform, GOG)" %}

{% capture portfolio-contents %}
World Racing 2 Champion Edition offers the full experience and the classic gameplay of the original 2005 game, plus:

* Custom unlicensed cars created by modifying the original 2005 game's licensed ones, fitting in an unified "Synetic lore" of N.I.C.E., World Racing, and Crash Time
* Revised environment art, placing the game's sceneries in an unified "Synetic lore" of N.I.C.E., World Racing, and Crash Time
* Numerous technical improvements that ensure smooth experience on both older and modern PCs
* Support for ultrawide displays and modern controllers
* Raised stock game limits and a 64-bit build, allowing for more extreme modding
* Expanded Photo Mode
* 52 achievements
* Full Steam Workshop support, building upon the original game's modding capabilities and expanding them further
* Steam Remote Play Together, allowing players to play split-screen online
* Steam Cloud

> I've been contracted as a sole programmer for this re-release. I outlined the scope of technical changes
> the game is set to receive, upgraded the codebase to work with modern compilers and to support targetting 64-bit,
> upgraded the rendering API from Direct3D 8 to Direct3D 9Ex, implemented Steam Workshop and the corresponding uploader application,
> and worked on countless bugfixes and smaller changes.
>
> Later in development I also took upon managing production more, being responsible for identifying the project requirements
> and looping in the right people.
{% endcapture %}

{% include portfolio/template.html %}
