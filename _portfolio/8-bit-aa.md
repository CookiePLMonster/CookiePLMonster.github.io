---
title: "8-bit Adventure Anthology: Volume I"
image: "assets/img/portfolio/thumb/8baa.jpg"
feature-img: "assets/img/portfolio/8-bit-anthology-hero.jpg"
date: 2017-10-31
game-series: "8-bit-adventure-anthology"
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="Unity" %}
{% capture portfolio-date %}{{ "2017-10-31" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC#PlayStation 4#Xbox One" %}

{% capture portfolio-contents %}
8-bit Adventure Anthology is a compilation featuring faithful remakes of three of the best 8-bit point & click adventure games ever made.
Originally released between 1987-1991, each stand-alone adventure features the same mind-blowing puzzles, graphics and music that mesmerized generations of console gamers!

> I briefly worked on the proprietary Unity-based NES emulator used by the game, fixing a few emulation issues.
{% endcapture %}

{% include portfolio/template.html %}
