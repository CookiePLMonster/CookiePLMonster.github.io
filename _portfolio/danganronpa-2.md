---
title: "Danganronpa 2: Goodbye Despair"
image: "assets/img/portfolio/thumb/danganronpa2.jpg"
feature-img: "assets/img/portfolio/danganronpa-2.png"
date: 2016-04-18
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2016-04-18" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC" %}

{% capture portfolio-contents %}
Jabberwock Island – once a popular tourist destination, this now uninhabited island remains oddly pristine.
You and your classmates at the elite Hope’s Peak Academy have been brought to this island by your super-cute teacher for a "lovey-dovey, heart-throbbing school trip."
Everyone seems to be having fun in the sun... until Monokuma returns to restart his murderous game! Trapped on this island of mutual killing, your only hope of escape rests in solving the island’s mysteries.
But be warned—sometimes the truth can be its own despair...

> I worked on this game during all stages of porting from PlayStation Vita to PC, utilizing a SilverWare framework.
> I played a major role in shipping the game with a 60FPS upgrade, researching it and fixing some FPS-related issues.
{% endcapture %}

{% include portfolio/template.html %}
