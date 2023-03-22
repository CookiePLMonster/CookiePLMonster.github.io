---
layout: portfolio
title: "Industry Giant 2"
image: "assets/img/portfolio/thumb/industry-giant-2.jpg"
feature-img: "assets/img/portfolio/industry-giant-2.jpg"
date: 2022-02-14
---

{% assign portfolio-client="*Independent*, for Toplitz Productions" %}
{% assign portfolio-engine="*Proprietary*" %}
{% capture portfolio-date %}{{ "2022-02-14" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC (GOG)" %}

{% capture portfolio-contents %}
In Industry Giant 2 like its predecessor you start from humble beginnings to industry billionaire in this simulation, you will guide a company’s development,
right from its beginnings to – with any luck – an industrial giant. You control every aspect of an expanding business – building factories, developing products,
paying wages, pricing in retail outlets, even operating the transport network.

> I've been contracted with a task of preparing the game and its original Level Editor for a GOG release.
> I made the level editor functional again, as no digital releases thus far included it,
> updated it with several fixed and a slightly more modernized UI. I also prepared the game's GOG Galaxy integration for achievements and stats.
{% endcapture %}

{% include portfolio/template.html %}
