---
layout: page
title: SilentPatch
excerpt: About SilentPatch.
feature-img: "assets/img/mods/silentpatch/silentpatch-banner.png"
image: "assets/img/mods/silentpatch/silentpatch-banner.png"
permalink: /silentpatch/
last_modified_at: 2023-12-29
twitter: {card: "summary_large_image"}
hide: true
---

* TOC
{:toc}

# What is SilentPatch?

**SilentPatch** is a series of unofficial modifications led by me, Silent, aiming to fix bugs and improve compatibility with modern hardware in various PC games.
First released in 2013 as modifications for the classic Grand Theft Auto games (GTA III, Vice City, San Andreas),
**SilentPatch** has since expanded into over 25 games and gained a degree of recognition in the PC gaming space by players and developers alike.

What makes a **SilentPatch**? The released patches adhere to several core values that set it apart from the other, more broadly defined, unofficial patches:

{: .dl-no-indent }
"Be free for everyone"
: Downloads are never hidden behind a paywall.

"Stick to a silent installation"
: The setup is hassle-free. With very few exceptions, **SilentPatches** are installed by just extracting a few files in the game directory.

"Patch with surgical precision"
: Changes are as non-invasive as possible, and code changes are applied with utmost care. This ensures wide compatibility with different revisions of games,
  as well as with other modifications installed alongside the patch.

"Preserve the developers' vision"
: **SilentPatches** are designed to be used on either the first or subsequent playthroughs, providing an enhanced gaming experience
  while maintaining the original gameplay. To achieve this, games' original design choices are preserved as much as possible. **SilentPatch** never alters gameplay and/or balancing of the game,
  unless it is entirely provable that those are a result of a bug. In rare cases where **SilentPatch** makes changes that cannot be justified as fixes,
  they are always toggleable from the configuration file.

# Supported games

<ul class="tag-posts">
{% assign filter_conditions = "mod.warning-label != 'DEPRECATED',mod.warning-label == 'DEPRECATED'" | split: "," %}
{% for filter in filter_conditions %}
    {% assign items = site.games | sort_natural: "title" %}
    {% for item in items %}
        {% unless item.hide or item.hide-on-list %}
            {% assign silentpatches = site.mods | where: "game-series", item.game-series | where_exp: "mod", "mod.title contains 'SilentPatch'" | where_exp: "mod", filter %}
            {% if silentpatches.size > 0 %}
                <li>
                    {% assign mod = silentpatches | first %}
                    {% assign modid = mod.id | split: '/' | last %}
                    <a href="{{ item.url | relative_url }}#{{ modid }}"><i class="far fa-list-alt" aria-hidden="true"></i> {{ item.title | smartify }}</a>
                    {% include mod-label.html mod=mod %}
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
Last update: {{ page.last_modified_at | date: page.date-format }}
