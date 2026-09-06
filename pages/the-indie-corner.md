---
layout: page
title: The Indie Games Corner
description: A curated list of 60+ indie games, mostly racing, including released, upcoming, and unannounced titles worth keeping an eye on.
feature-img: "/assets/img/the-indie-corner/the-indie-corner.webp"
image: "/assets/img/the-indie-corner/the-indie-corner.webp"
permalink: /the-indie-corner/
date: 2026-03-19 13:30:00 +0100
last_modified_at: 2026-09-06 16:50:00 +0200
twitter: {card: "summary_large_image"}
hide: true
extra_scss: |
  dd {
    margin-inline-start: 1.5em;

    > p:last-of-type {
      display: contents;
    }

    > .fig-entry {
      margin-block-start: 1em;
    }
  }
  .unannounced {
    font-style: italic;
    &::before {
      content: '[';
    }
    &::after {
      content: ']';
    }
  }
  .review {
    display: block;
  }
seo:
  type: CollectionPage
---

{% include schema/indie-corner.html items=site.indies page=page %}

* TOC
{:toc}

As time goes on, there are increasingly many interesting indie racers that I follow and talk about. As I started losing track of some individual games
and people started asking me for recommendations, my own list of noteworthy games can help everyone!

I wish to highlight any kinds of games: released, in development, even unnamed and unannounced projects that show promise. I played most of the games on those lists
(the ones that have a full or a demo release), and if I have not, I make it clear in the description. I think all games on this list deserve a shout-out,
because even if I don't love the goal of each and every one of them, I think they are all done well and will inevitably interest someone looking for something to play.

"Released" and "Demo & Early Access" games are sorted by their release dates, with the most recent games on top. "Upcoming" games are sorted alphabetically.

{:.sidenote}
Last update: {% include elements/time.html date=page.last_modified_at %}

{:.disclaimer.info}
This page contains affiliate links (marked with an asterisk*), meaning I get a commission for every purchase made through them.

# Racing games

{%- assign racing_games = site.indies | where: "genre", "Racing" %}

Strictly racing/rally games, nothing else.

## Released {#released-racing-games}

{%- assign released_racing_games = racing_games | where: "state", "released" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=released_racing_games %}

## Demo & Early Access {#demo-racing-games}

{%- assign demo_racing_games = racing_games | where: "state", "demo" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=demo_racing_games %}

## Upcoming {#upcoming-racing-games}

{%- assign upcoming_racing_games = racing_games | where: "state", "upcoming" | sort_natural: "title" %}
{%- assign upcoming_named_racing_games = upcoming_racing_games | where_exp: "item", "item.title != ''" %}
{% include indie-corner/list.html items=upcoming_named_racing_games %}

{%- assign upcoming_unnamed_racing_games = upcoming_racing_games | where: "title", empty %}
{% include indie-corner/list.html items=upcoming_unnamed_racing_games %}

## On hold & Cancelled {#cancelled-racing-games}

{%- assign suspended_racing_games = racing_games | where: "state", "suspended" | sort_natural: "title" %}
{% include indie-corner/list.html items=suspended_racing_games %}

# Other car games {#car-games}

{%- assign vehicular_games = site.indies | where: "genre", "Vehicular" %}

Any other games involving vehicles, but not necessarily racing. Trucking, vehicular combat, exploration, etc.

## Released {#released-car-games}

{%- assign released_vehicular_games = vehicular_games | where: "state", "released" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=released_vehicular_games %}

## Demo & Early Access {#demo-car-games}

{%- assign demo_vehicular_games = vehicular_games | where: "state", "demo" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=demo_vehicular_games %}

## Upcoming {#upcoming-car-games}

{%- assign upcoming_vehicular_games = vehicular_games | where: "state", "upcoming" | sort_natural: "title" %}
{% include indie-corner/list.html items=upcoming_vehicular_games %}

# Other games

{%- assign other_games = site.indies | where_exp: "item", "item.genre != 'Racing' and item.genre != 'Vehicular'" %}

Anything else.

## Released {#released-other-games}

{%- assign released_other_games = other_games | where: "state", "released" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=released_other_games %}

## Demo & Early Access {#demo-other-games}

{%- assign demo_other_games = other_games | where: "state", "demo" | sort: "release_date" | reverse %}
{% include indie-corner/list.html items=demo_other_games %}

## Upcoming {#upcoming-other-games}

{%- assign upcoming_other_games = other_games | where: "state", "upcoming" | sort_natural: "title" %}
{% include indie-corner/list.html items=upcoming_other_games %}

# Changelog

* {% include elements/time.html date="2026-09-06 16:50:00 +0200" %}:
  * New entries: [**Nitrania**](#nitrania), [**The Henchmen**](#the-henchmen), [**Rogue Stradale**](#rogue-stradale), [**Plentiful**](#plentiful),
    [**Driving Rogue**](#driving-rogue), [**Super Woden GP 3**](#super-woden-gp3), [**Throttle Trace**](#throttle-trace), [**Heatwarped**](#heatwarped).
  * [**iRacing Arcade**](#iracing-arcade) got new content and a console release.
  * [**Easy Delivery Co.**](#easy-delivery-co) got a free **EasyCo EasyRally** expansion.
  * [**Race Jam**](#race-jam) is out of Early Access.
  * [**Exo Rally Championship**](#exo-rally-championship), [**Denshattack!**](#denshattack) and [**Agent 64: Spies Never Die**](#agent-64) are out.
  * [**Formula Circus**](#formula-circus) and [**REV UP**](#rev-up) suspended development.
  * [**ASUKA x Redline Reverie**](#asuka-redline-reverie), [**Kaido Genkai**](#kaido-genkai) and [**4x4 in a Furniture Store**](#4x4-in-a-furniture-store) now have demos.
  * [**RREV: Racing Revolution**](#rrev-racing-revolution) announced a "remix" demo.
  * **Super Woden** and **Highway Warriors** entries split from series to separate entries.
  * Turned the changelog titles into clickable links.
* {% include elements/time.html date="2026-04-07 21:15:00 +0200" %}:
  * [**Formula Circus**](#formula-circus) got a demo available on Patreon, moved it to an appropriate section.
* {% include elements/time.html date="2026-03-22 12:55:00 +0100" %}:
  * New entry: [**The Driver Syndicate**](#the-driver-syndicate).
  * Ordered released games by release date.
  * Added screenshots.
* {% include elements/time.html date=page.date %}:
  * Initial version.
