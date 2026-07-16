---
title: "Shell Growth Simulator"
permalink: /simulation/shell-growth-simulator/
excerpt: "Interactive parametric shell growth simulator."
layout: single
author_profile: false
classes: wide
---

パラメータ操作、断面編集、テクスチャ適用ができるインタラクティブな貝殻生成アプリです。

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
  height: min(82vh, 960px);
  border: 1px solid #ddd;
}

.shell-growth-embed iframe {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
}
</style>