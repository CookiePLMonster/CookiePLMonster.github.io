---
layout: portfolio
title: "Sid Meier's Civilization VI"
image: "assets/img/portfolio/thumb/civ6.jpg"
feature-img: "assets/img/portfolio/civ6.jpg"
date: 2019-11-21
---
{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2019-11-11" | date: page.date-format }} (X1)#{{ "2020-08-13" | date: page.date-format }} (Android){% endcapture %}
{% assign portfolio-platform="Xbox One#Android" %}

{% capture portfolio-contents %}
Originally created by legendary game designer Sid Meier, Civilization is a turn-based strategy game in which you attempt to build an empire to stand the test of time.
Explore a new land, research technology, conquer your enemies, and go head-to-head with history’s most renowned leaders as you attempt to build the greatest civilization the world has ever known.

> On both target platforms, I was involved in general porting and bugfixing. On Android, I was additionally responsible for setting up the turn-limited demo functionality.
{% endcapture %}

{% include portfolio/template.html %}
