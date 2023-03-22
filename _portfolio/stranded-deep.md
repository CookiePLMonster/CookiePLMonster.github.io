---
layout: portfolio
title: "Stranded Deep"
image: "assets/img/portfolio/thumb/stranded-deep.jpg"
feature-img: "assets/img/portfolio/stranded-deep.jpg"
date: 2021-08-31
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="Unity" %}
{% capture portfolio-date %}{{ "2021-08-31" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="Nintendo Switch" %}

{% capture portfolio-contents %}
Experience terrifying encounters both above and below an endless environment with a different experience each time you play.
In the aftermath of a mysterious plane crash, you are stranded in the vast expanse of the Pacific Ocean. Alone, without any means to call for help, you must do what you can to survive.

> I briefly joined the project late in development and was tasked with fixing several minor gameplay tailoring and leaderboard integration issues.
{% endcapture %}

{% include portfolio/template.html %}
