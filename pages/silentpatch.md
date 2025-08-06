---
layout: page
title: SilentPatch
excerpt: About SilentPatch.
feature-img: "assets/img/mods/silentpatch/silentpatch-banner.png"
image: "assets/img/mods/silentpatch/silentpatch-banner.png"
permalink: /silentpatch/
last_modified_at: 2025-03-09
twitter: {card: "summary_large_image"}
hide: true
---

* TOC
{:toc}

# What is SilentPatch?

**SilentPatch** is a series of unofficial modifications led by me, Silent, aimed at fixing bugs and improving compatibility with modern hardware in various PC games.
Originally released in 2013 for the classic Grand Theft Auto titles (GTA III, Vice City, San Andreas),
**SilentPatch** has since expanded to over 25 games and gained recognition from both players and developers in the PC gaming space.

What makes a **SilentPatch**? The released patches adhere to several core values that set them apart from other, more broadly defined, unofficial patches:

"Be free for everyone"
: **SilentPatch** downloads are never hidden behind a paywall.

"Stick to a silent installation"
: Installation is hassle-free. With very few exceptions, **SilentPatches** require nothing more than extracting a few files into the game directory.

"Patch with surgical precision"
: Changes are as non-invasive as possible, and code changes are applied with utmost care. This ensures wide compatibility across different game versions
  and allows **SilentPatch** to work seamlessly with other installed modifications.

"Preserve the developers' vision"
: **SilentPatches** are designed to enhance the gaming experience while maintaining the original gameplay, making them suitable for both first-time and returning players.
  Original design choices are preserved as much as possible -- **SilentPatch** never alters gameplay or balancing unless it is provably the result of a bug.
  In rare cases where changes extend beyond pure bug fixes, they are always toggleable via the configuration file.

# Supported games

<ul class="list-icons">
{% assign filter_conditions = "mod.warning-label != 'DEPRECATED',mod.warning-label == 'DEPRECATED'" | split: "," %}
{% for filter in filter_conditions %}
    {% assign items = site.games | sort_natural: "title" %}
    {% for item in items %}
        {% unless item.hide %}
            {% assign silentpatches = site.mods | where: "game-series", item.game-series | where_exp: "mod", "mod.title contains 'SilentPatch'" | where_exp: "mod", filter %}
            {% if silentpatches.size > 0 %}
                <li>
                    <span class="fa-li"><i class="far fa-list-alt"></i></span>
                    {%- assign mod = silentpatches | first -%}
                    {%- assign modid = mod.id | split: '/' | last -%}
                    <a href="{{ item.url | relative_url }}#{{ modid }}">{{ item.title | smartify }}</a>
                    {% include elements/mod-label.html mod=mod -%}
                </li>
            {% endif %}
        {% endunless %}
    {% endfor %}
{% endfor %}
</ul>

# More resources

## Development timeline

To celebrate a decade of patching, I have created an updated timeline of the SilentPatch history.
I highlighted the most important events related to those, mostly focusing on the GTA patches due to their historical significance,
but also listing all the other supported games, as well as some other events that directly led to the creation of, or influenced the shape of SilentPatch.

The legend for colours is as follows:
* Blue -- SilentPatch events
* Green -- miscellaneous events directly related to SilentPatch
* Pink -- events related to other modifications, which were relevant for SilentPatch development nonetheless
* Orange -- 'community spotlight' events

I recommend viewing the timeline fullscreen!
<iframe width="100%" height="450" src="https://time.graphics/embed?v=1&id=202189" frameborder="0" allowfullscreen></iframe>

## SilentPatch in media

{% assign media_items = site.data.media | where: 'game-series', 'silentpatch' | sort: 'date' %}
{% include related-reads-list.html related_items=media_items %}

{:.sidenote}
Last update: {% include elements/time.html date=page.last_modified_at %}
