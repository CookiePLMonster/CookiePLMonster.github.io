---
title: "Frostpunk"
image: "assets/img/portfolio/thumb/frostpunk.jpg"
feature-img: "assets/img/portfolio/frostpunk.jpg"
date: 2021-02-24
game-series: "frostpunk"
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="Liquid Engine" %}
{% capture portfolio-date %}{{ "2021-02-24" | date: page.date-format }} (macOS)#{{ "2021-07-21" | date: page.date-format }} (PlayStation 4, Xbox One){% endcapture %}
{% assign portfolio-platform="macOS#PlayStation 4 (DLC)#Xbox One (DLC)" %}

{% capture portfolio-contents %}
Frostpunk is the first society survival game. As the ruler of the last city on Earth,
it is your duty to manage both its citizens and its infrastructure. What decisions will you make to ensure your society's survival?
What will you do when pushed to breaking point? Who will you become in the process?

> On macOS, I was involved in general porting and bugfixing. On consoles, we were tasked with porting the DLCs into the console
> version of Frostpunk. I was involved in that process, as well as in fixing whatever issues that arised and tailoring the DLC experience
> for consoles.
{% endcapture %}

{% include portfolio/template.html %}
