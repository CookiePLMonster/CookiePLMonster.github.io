---
layout: portfolio
title: "DeathKeep "
image: "assets/img/portfolio/thumb/deathkeep.jpg"
feature-img: "assets/img/portfolio/deathkeep.jpg"
date: 2023-03-27
game-series: "deathkeep"
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2023-03-27" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam, GOG)" %}

{% capture portfolio-contents %}
DeathKeep is D&D dungeon delving the way you like it -- fast, furious and fun! An evil Necromancer has escaped from his icy prison
and is wreaking havoc upon the surrounding lands. Journey to this frozen wasteland and destroy the forces of evil -- if you dare.

> I've been contracted with consultation and bugfixing of the game in preparation for a digital release on Steam and GOG.
> I shipped an appropriate DirectDraw wrapper, and additionally patched the game's binary with several compatibility and QoL bugfixes.
> I also fixed multiple instances of the game acting invasively and generally being unlike what people expect from software
> nowadays (e.g. forcibly hiding the Taskbar).
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
