---
layout: portfolio
title: "Pacific General"
image: "assets/img/portfolio/thumb/pacific-general.jpg"
feature-img: "assets/img/portfolio/pacific-general.jpg"
date: 2021-09-16
---

{% assign portfolio-client="*Independent*, for SNEG" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2021-09-16" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (Steam)" %}

{% capture portfolio-contents %}
Pacific General explores the Pacific front of the Second World War. Taking control of Axis or Allied forces,
you must strategically battle your way through the Eastern and Western front of the Pacific war, using a wide array of land, air and naval forces.

> I've been contracted with consultation and bugfixing of the game in preparation for the Steam release.
> I troubleshooted the existing compatibility issues and shipped an appropriate DirectDraw wrapper,
> and additionally patched the game's binary with several compatibility and QoL bugfixes.
>
> The game's source code has been lost, so all work was done via reverse engineering.
{% endcapture %}

{% include portfolio/template.html %}
