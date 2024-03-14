---
title: "Danganronpa: Trigger Happy Havoc"
image: "assets/img/portfolio/thumb/danganronpa1.jpg"
feature-img: "assets/img/portfolio/danganronpa.jpg"
date: 2016-02-18
game-series: "danganronpa"
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2016-02-18" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC" %}

{% capture portfolio-contents %}
In "Danganronpa" you’ll dive into a series of class trials and expose the lies and contradictions of your classmates in order to find out who’s behind each grisly murder.
In each trial, you’ll have to use the evidence and testimony collected during your investigation to literally shoot down your opponent’s assertions.
By combining logic and motion, "Danganronpa" offers an exciting and unprecedented gaming experience.

> I worked on this game during all stages of porting from PlayStation Vita to PC, utilizing a SilverWare framework.
> I played a major role in shipping the game with a 60FPS upgrade, researching it and fixing some FPS-related issues.
{% endcapture %}

{% include portfolio/template.html %}
