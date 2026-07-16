---
title: "Shell Growth Simulator"
permalink: /simulation/shell-growth-simulator/
excerpt: "Interactive parametric shell growth simulator."
layout: single
author_profile: false
classes: wide
---

An interactive shell generator with parameter controls, cross-section editing, and texture mapping.

<div class="shell-growth-embed">
  <iframe
    src="{{ '/assets/webgl/shell-growth-simulator/' | relative_url }}"
    title="Shell Growth Simulator"
    allowfullscreen>
  </iframe>
</div>

<style>
.shell-growth-embed {
  width: 100%;
  min-height: 640px;
  height: clamp(640px, 56.25vw, 1080px);
  border: 1px solid #ddd;
}

.shell-growth-embed iframe {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
}

/* Academic Pages normally limits a single-page layout to 1280px. This page
   is an application workspace, so allow its embedded player to use the full
   browser width while retaining a small responsive gutter. */
@media (min-width: 925px) {
  #main {
    width: 100%;
    max-width: none;
    box-sizing: border-box;
    padding-right: clamp(1rem, 3vw, 4rem);
    padding-left: clamp(1rem, 3vw, 4rem);
  }

  #main .page {
    float: none;
    width: 100%;
    margin: 0;
    padding: 0;
  }
}
</style>
