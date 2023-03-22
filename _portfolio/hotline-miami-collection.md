---
layout: portfolio
title: "Hotline Miami Collection"
image: "assets/img/portfolio/thumb/hm-collection.jpg"
feature-img: "assets/img/portfolio/hm-collection.jpg"
date: 2019-08-19
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="GameBaker#SilverWare" %}
{% capture portfolio-date %}{{ "2019-08-19" | date: page.date-format }} (Switch)#{{ "2020-04-07" | date: page.date-format }} (X1)#{{ "2020-09-22" | date: page.date-format }} (Stadia){% endcapture %}
{% assign portfolio-platform="Nintendo Switch#Xbox One#Google Stadia" %}

{% capture portfolio-contents %}
Hotline Miami Collection contains both legendary games in the neon-soaked, brutally-challenging Hotline Miami series from Dennaton Games.

> I worked on ports to the aforementioned platforms as a generalist engine programmer, being responsible for porting
> general systems as well as bugfixing.
{% endcapture %}

{% include portfolio/template.html %}
