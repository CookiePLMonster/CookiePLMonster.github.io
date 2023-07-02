---
layout: portfolio
title: "Take No Prisoners"
image: "assets/img/portfolio/thumb/take-no-prisoners.jpg"
feature-img: "assets/img/portfolio/take-no-prisoners.jpg"
date: 2023-06-28
game-series: "take-on-prisoners"
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2023-06-28" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam, GOG)" %}

{% capture portfolio-contents %}
Take No Prisoners is a hard-core top-down 3D shooter that allows you to blow away enemies.
As Slade, a mercenary surviving on the fringes of a post-nuclear world, you'll fight through 20 non-linear territories populated by hordes of twisted mutants and refugees.

> I've been contracted with consultation and bugfixing of the game in preparation for a digital release on Steam and GOG.
> I shipped appropriate DirectDraw and CD Audio wrappers and rolled out a stub DirectPlay wrapper to remove an invasive dependency
> on a legacy Windows component not installed in the OS by default,
> gracefully disabling the game's obsolete networking functionality, albeit with an option for the user to bring it back
> should they want to get it running at their own discretion.
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
