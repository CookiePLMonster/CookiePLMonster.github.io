---
layout: portfolio
title: "The King of Fighters XIV"
image: "assets/img/portfolio/thumb/KOF14.jpg"
feature-img: "assets/img/portfolio/KOF-XIV.png"
date: 2017-06-15
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2017-06-15" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC" %}

{% capture portfolio-contents %}
The King of Fighters XIV is the newest entry in the King of Fighters series since 2010,
bringing the same iconic gameplay from earlier entries, with 50 characters in the base game each duking it out in multiplayer battles or through a single-player story mode.

> I worked on this game during all stages of porting from PlayStation 4 to PC, utilizing a SilverWare framework.
> I mostly worked on input, audio, voice chat implementation and bugfixing.
{% endcapture %}

{% include portfolio/template.html %}
