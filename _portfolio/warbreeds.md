---
title: "WarBreeds"
image: "assets/img/portfolio/thumb/warbreeds.jpg"
feature-img: "assets/img/portfolio/warbreeds.jpg"
date: 2023-12-19
game-series: "warbreeds"
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2023-12-19" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam, GOG)" %}

{% capture portfolio-contents %}
WarBreeds is a strategy game where the objective is to become the ruler of the fallen Empire.
Defeat your enemies and steal their genetic material to expand your clan’s skills and firepower.
Engineer and customize your army with a vast mixture of advanced bio-technological weaponry.

> I've been contracted with consultation and bugfixing of the game in preparation for a digital release on Steam and GOG.
> I shipped appropriate DirectDraw and CD Audio wrappers and rolled out a stub DirectPlay wrapper to remove an invasive dependency
> on a legacy Windows component not installed in the OS by default,
> gracefully disabling the game's obsolete networking functionality, albeit with an option for the user to bring it back
> should they want to get it running at their own discretion.
>
> I also fixed several original bugs in the game that could render the Explorer unusable if the game didn't shut down gracefully,
> effectively performing a Denial of Service "attack" on the Explorer.
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
