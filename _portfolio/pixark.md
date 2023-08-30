---
title: "PixARK"
image: "assets/img/portfolio/thumb/pixark.jpg"
feature-img: "assets/img/portfolio/pixark.jpg"
date: 2019-05-31
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="Unreal Engine 4" %}
{% capture portfolio-date %}{{ "2019-05-31" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PlayStation 4#Xbox One#Nintendo Switch" %}

{% capture portfolio-contents %}
Enter a world of mystery, danger, ancient dinosaurs, mythical beasts, and cubes!
Work by yourself or with a tribe of others to gather materials, craft useful items, tame wild creatures, and build huge bases to survive in PixARK!

> I briefly helped with the development of console ports, fixing miscellaneous cross-platform issues.
{% endcapture %}

{% include portfolio/template.html %}
