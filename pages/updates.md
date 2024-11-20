---
layout: page
title: Updates
subtitle: Mod updates, blog additions, new releases.
excerpt: Mod updates, blog additions, new releases.
permalink: /updates/
---

This list is also available as an RSS feed:
<a href="{{ site.baseurl }}/feed/updates.xml" title="{{ site.theme_settings.str_rss_follow }}"><i class="fas fa-rss"></i></a>

***

<div class="posts smaller-gaps">
  {% for entry in site.updates reversed %}
  <section>
    <h2 class="heading-big">
      <a href="{{ entry.url | relative_url }}">
        {{ entry.title | smartify }}
      </a>
    </h2>
    <p class="meta">
      {{ entry.date | date: "%B %-d, %Y" }}
      {% if entry.last_modified_at %}(edited {{ entry.last_modified_at | date: "%B %-d, %Y" }}){% endif %}
    </p>
    <div class="excerpt read-more">
        {{ entry.excerpt }}
        <a href="{{ entry.url | relative_url }}"><p>(Read more...)</p></a>
    </div>
  </section>
  {% endfor %}
</div>
