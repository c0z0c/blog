---
layout: default
title: 개발자 블로그
description: 기술 블로그와 학습 자료 모음
date: 2025-08-24
cache-control: no-cache
expires: 0
pragma: no-cache
---

# 📚 개발자 블로그

{% assign folder_set = "" | split: "" %}
{% for file in site.static_files %}
  {% assign path_parts = file.path | split: '/' %}
  {% if path_parts.size > 1 %}
    {% assign folder = path_parts[0] %}
    {% unless folder_set contains folder or folder == '' or folder contains '.' %}
      {% assign folder_set = folder_set | push: folder %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% for page in site.pages %}
  {% assign path_parts = page.path | split: '/' %}
  {% if path_parts.size > 1 %}
    {% assign folder = path_parts[0] %}
    {% unless folder_set contains folder or folder == '' or folder contains '.' %}
      {% assign folder_set = folder_set | push: folder %}
    {% endunless %}
  {% endif %}
{% endfor %}
<!-- 디버깅: 추출된 폴더 목록 -->
<!-- {{ folder_set | join: ', ' }} -->

<div class="nav-sections">
  <div class="section-card">
    <h2>📂 카테고리</h2>
    <div class="folder-links">
      {% assign folder_set = "" | split: "" %}
      {% for file in site.static_files %}
        {% assign path_parts = file.path | split: '/' %}
        {% if path_parts.size > 1 %}
          {% assign folder = path_parts[0] %}
          {% unless folder_set contains folder or folder == '' or folder contains '.' or folder == 'assets' %}
            <a href="{{ site.baseurl }}/{{ folder }}/" class="folder-link">
              <span class="folder-icon">📁</span>
              <span class="folder-name">{{ folder }}</span>
            </a>
            {% assign folder_set = folder_set | push: folder %}
          {% endunless %}
        {% endif %}
      {% endfor %}
      {% for page in site.pages %}
        {% assign path_parts = page.path | split: '/' %}
        {% if path_parts.size > 1 %}
          {% assign folder = path_parts[0] %}
          {% unless folder_set contains folder or folder == '' or folder contains '.' or folder == 'assets' %}
            <a href="{{ site.baseurl }}/{{ folder }}/" class="folder-link">
              <span class="folder-icon">📁</span>
              <span class="folder-name">{{ folder }}</span>
            </a>
            {% assign folder_set = folder_set | push: folder %}
          {% endunless %}
        {% endif %}
      {% endfor %}
    </div>
  </div>

  <div class="section-card">
    <h2>🔗 빠른 링크</h2>
    <div class="quick-links">
      <a href="https://c0z0c.github.io/" target="_blank">
        <span class="link-icon">🏠</span> 메인
      </a>
      <a href="https://github.com/c0z0c/blog" target="_blank">
        <span class="link-icon">📱</span> GitHub 프로필
      </a>
    </div>
  </div>
</div>

## �📋 최근 업데이트

{% assign all_posts = site.pages %}
{% assign filtered_posts = "" | split: "" %}
{% for page in all_posts %}
  {% if page.category and page.title != page.category %}
    {% assign filtered_posts = filtered_posts | push: page %}
  {% endif %}
{% endfor %}
{% assign sorted_posts = filtered_posts | sort: "date" | reverse %}

<div class="recent-posts">
  {% for post in sorted_posts limit: 5 %}
    <div class="recent-post-item">
      <span class="post-date">{{ post.date | date: "%Y년 %m월 %d일" | default: "최근" }}</span>
      <a href="{{ post.url | prepend: site.baseurl }}" class="post-title">{{ post.title }}</a>
      <span class="post-category">{{ post.category }}</span>
    </div>
  {% endfor %}
</div>

---

<div class="footer-info">
<small>
<strong>개발자 블로그</strong> | <a href="https://c0z0c.github.io/" target="_blank" style="color: #87ceeb;">🌐 메인</a><br>
마지막 업데이트: {{ site.time | date: "%Y년 %m월 %d일" }}
</small>
</div>
