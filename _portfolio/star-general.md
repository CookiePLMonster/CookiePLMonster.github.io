---
layout: portfolio
title: "Star General"
image: "assets/img/portfolio/thumb/star-general.jpg"
feature-img: "assets/img/portfolio/star-general.jpg"
date: 2023-06-06
game-series: "star-general"
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2023-06-06" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam, GOG)" %}

{% capture portfolio-contents %}
Star General is light-years ahead of its proud ancestors from the award-winning 5-star strategy series.
It proposes a two-level combat system that accommodates space combat and surface combat. Resource management - conquer enemy planets and develop them for your needs.

> I've been contracted with consultation and bugfixing of the game in preparation for a digital release on Steam and GOG.
> I shipped appropriate DirectDraw and CD Audio wrappers and made the game work correctly in a digital form
> I also rolled out a stub DirectPlay wrapper to remove an invasive dependency on a legacy Windows component not installed in the OS by default,
> gracefully disabling the game's obsolete networking functionality, albeit with an option for the user to bring it back
> should they want to get it running at their own discretion.
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
