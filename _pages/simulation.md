---
layout: archive
title: "Simulation"
permalink: /simulation/
author_profile: true
---

{% include base_path %}

{% assign cell_automaton = site.simulation | where: "permalink", "/simulation/cell-automaton/" %}
{% for post in cell_automaton %}
  {% include archive-single.html %}
{% endfor %}

{% for post in site.simulation %}
  {% unless post.permalink == "/simulation/cell-automaton/" %}
    {% include archive-single.html %}
  {% endunless %}
{% endfor %}