---
title: "SNK Heroines: Tag Team Frenzy"
image: "assets/img/portfolio/thumb/snk-heroines.jpg"
feature-img: "assets/img/portfolio/snk-heroines.png"
date: 2018-09-07
game-series: "snk-heroines"
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2018-09-07" | date: page.date-format }} (Switch)#{{ "2019-02-21" | date: page.date-format }} (PC){% endcapture %}
{% assign portfolio-platform="Nintendo Switch#PC" %}

{% capture portfolio-contents %}
Take control of SNK's most iconic female characters and battle it out in this crazy tag fighting game featuring a plethora of cute costumes and accessories!
With one button special moves and a deep but simplified combo system this is a great game for fighting game fans and newcomers alike!
A brand new style of fighting action has arrived!

> I worked on this game during all stages of porting from PlayStation 4 to our target platforms, utilizing a SilverWare framework.
> On PC, I worked on fixing several vendor-specific issues and hard to track threading bugs.
{% endcapture %}

{% include portfolio/template.html %}
