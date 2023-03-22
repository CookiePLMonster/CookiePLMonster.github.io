---
layout: portfolio
title: "428: Shibuya Scramble"
image: "assets/img/portfolio/thumb/428.jpg"
feature-img: "assets/img/portfolio/428.jpg"
date: 2018-09-04
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2018-09-04" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC#PlayStation 4" %}

{% capture portfolio-contents %}
428: Shibuya Scramble is a visual novel adventure game where players take part in events from the perspectives of multiple protagonists,
all acting in parallel with no knowledge of each other. Set in the modern Japanese city of Shibuya, Tokyo, the characters are involved in a mystery that cannot be solved without their interactions,
and the plot is advanced by following clues found within the game's text and accompanying video sequences and making decisions on which path each protagonist should follow.
Depending on the player's choices, a number of new scenarios become available, which ultimately lead to different outcomes and endings

> I worked on this game during all stages of porting to PC and PlayStation 4, utilizing a SilverWare framework.
> Later I focused on fixing errors caused by translating the game to English and on tailoring the experience for English.
{% endcapture %}

{% include portfolio/template.html %}
