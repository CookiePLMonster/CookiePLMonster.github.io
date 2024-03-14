---
title: "A Boy and His Blob"
image: "assets/img/portfolio/thumb/abahb.jpg"
feature-img: "assets/img/portfolio/abahb.jpg"
date: 2016-01-19
game-series: "a-boy-and-his-blob"
---

{% assign portfolio-client="Abstraction" %}
{% assign portfolio-engine="*Proprietary*#SilverWare" %}
{% capture portfolio-date %}{{ "2016-01-19" | date: page.date-format }}{% endcapture %}
{% assign portfolio-platform="PC#PlayStation 3#PlayStation 4#PlayStation Vita#Xbox One" %}

{% capture portfolio-contents %}
When Blobolonia is threatened by an evil Emperor, the blob comes to Earth looking for help.
Instead, he finds a young boy. Help the blob dethrone the evil Emperor that's terrorizing Blobolonia
and establish a friendship with the blob that will last a lifetime.

> I helped in the later stages of porting, mostly fixing issues introduced by migrating the game from
> a proprietary framework to SilverWare.
{% endcapture %}

{% include portfolio/template.html %}
