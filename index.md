---
layout: default
title: 개발자 블로그
description: 기술 블로그와 학습 자료 모음
cache-control: no-cache
expires: 0
pragma: no-cache
---

# 📚 개발자 블로그

기술적 학습과 경험을 정리하는 공간입니다.

<div class="nav-sections">
  <div class="section-card">
    <h2>📂 카테고리별 탐색</h2>
    <div class="folder-links">
      <a href="{{ site.baseurl }}/블로그/" class="folder-link">
        <span class="folder-icon">💭</span>
        <span class="folder-name">블로그</span>
        <span class="folder-desc">일반 블로그 포스트</span>
      </a>
      
      <a href="{{ site.baseurl }}/Tech%20Retrospective/" class="folder-link">
        <span class="folder-icon">🔍</span>
        <span class="folder-name">Tech Retrospective</span>
        <span class="folder-desc">기술 회고 및 경험담</span>
      </a>
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
      <!--
      <a href="{{ site.baseurl }}/about">
        <span class="link-icon">📖</span> About
      </a>
      -->
    </div>
  </div>
</div>

## � 파일 목록

<div class="file-grid">
  {% assign current_path = "/blog/" %}
  {% assign static_files = site.static_files | where_exp: "item", "item.path contains current_path" %}
  {% assign markdown_pages = site.pages | where_exp: "page", "page.path contains 'blog'" %}
  
  {% assign all_files = "" | split: "" %}
  
  <!-- Add static files -->
  {% for file in static_files %}
    {% assign relative_path = file.path | remove: current_path %}
    {% unless relative_path contains "/" or file.name == "index.md" or file.name contains "_config" or file.name contains "Gemfile" %}
      {% assign all_files = all_files | push: file %}
    {% endunless %}
  {% endfor %}
  
  <!-- Add markdown pages -->
  {% for page in markdown_pages %}
    {% assign relative_path = page.path | remove_first: "blog" | remove_first: "/" %}
    {% unless relative_path contains "/" or page.name == "index.md" %}
      {% assign all_files = all_files | push: page %}
    {% endunless %}
  {% endfor %}
  
  {% assign sorted_files = all_files | sort: "name" %}
  
  {% if sorted_files.size > 0 %}
    {% for file in sorted_files %}
      {% assign file_ext = file.extname | downcase %}
      {% if file_ext == "" and file.path %}
        {% assign file_name = file.path | split: "/" | last %}
        {% assign file_ext = file_name | split: "." | last | downcase %}
        {% assign file_ext = "." | append: file_ext %}
      {% endif %}
      {% assign file_icon = "📄" %}
      {% assign file_type = "파일" %}
      
      {% if file_ext == ".md" %}
        {% assign file_icon = "📝" %}
        {% assign file_type = "Markdown 문서" %}
      {% elsif file_ext == ".py" %}
        {% assign file_icon = "🐍" %}
        {% assign file_type = "Python 스크립트" %}
      {% elsif file_ext == ".json" %}
        {% assign file_icon = "⚙️" %}
        {% assign file_type = "JSON 설정" %}
      {% elsif file_ext == ".yml" or file_ext == ".yaml" %}
        {% assign file_icon = "⚙️" %}
        {% assign file_type = "YAML 설정" %}
      {% elsif file_ext == ".html" %}
        {% assign file_icon = "🌐" %}
        {% assign file_type = "HTML 파일" %}
      {% elsif file_ext == ".css" %}
        {% assign file_icon = "🎨" %}
        {% assign file_type = "CSS 스타일" %}
      {% elsif file_ext == ".js" %}
        {% assign file_icon = "⚡" %}
        {% assign file_type = "JavaScript" %}
      {% elsif file_ext == ".lock" %}
        {% assign file_icon = "🔒" %}
        {% assign file_type = "Lock 파일" %}
      {% endif %}
      
      <div class="file-item">
        <div class="file-icon">{{ file_icon }}</div>
        <div class="file-info">
          <h4 class="file-name">{% if file.name %}{{ file.name }}{% else %}{{ file.path | split: "/" | last }}{% endif %}</h4>
          <p class="file-type">{{ file_type }}</p>
          <p class="file-size">{% if file.modified_time %}{{ file.modified_time | date: "%Y-%m-%d" }}{% else %}{{ file.date | date: "%Y-%m-%d" }}{% endif %}</p>
        </div>
        <div class="file-actions">
          {% if file_ext == ".md" and file.name != "index.md" %}
            {% assign file_name_clean = file.name %}
            {% if file_name_clean == nil %}
              {% assign file_name_clean = file.path | split: "/" | last %}
            {% endif %}
            {% assign md_name_clean = file_name_clean | remove: '.md' %}
            <a href="https://c0z0c.github.io/blog/{{ md_name_clean }}" class="file-action" title="렌더링된 페이지 보기" target="_blank">🌐</a>
            <a href="https://github.com/c0z0c/c0z0c.github.io/blob/main/blog/{{ file_name_clean }}" class="file-action" title="GitHub에서 원본 보기" target="_blank">📖</a>
          {% elsif file_ext == ".html" %}
            {% assign file_name_clean = file.name %}
            {% if file_name_clean == nil %}
              {% assign file_name_clean = file.path | split: "/" | last %}
            {% endif %}
            <a href="https://c0z0c.github.io/blog/{{ file_name_clean }}" class="file-action" title="렌더링된 페이지 보기" target="_blank">🌐</a>
            <a href="https://github.com/c0z0c/c0z0c.github.io/blob/main/blog/{{ file_name_clean }}" class="file-action" title="GitHub에서 원본 보기" target="_blank">📖</a>
          {% elsif file_ext == ".py" %}
            {% assign file_name_clean = file.name %}
            {% if file_name_clean == nil %}
              {% assign file_name_clean = file.path | split: "/" | last %}
            {% endif %}
            <a href="https://github.com/c0z0c/c0z0c.github.io/blob/main/blog/{{ file_name_clean }}" class="file-action" title="GitHub에서 보기" target="_blank">📖</a>
            <a href="https://github.com/c0z0c/c0z0c.github.io/raw/main/blog/{{ file_name_clean }}" class="file-action" title="원본 다운로드" target="_blank">⬇️</a>
          {% else %}
            {% assign file_name_clean = file.name %}
            {% if file_name_clean == nil %}
              {% assign file_name_clean = file.path | split: "/" | last %}
            {% endif %}
            <a href="https://github.com/c0z0c/c0z0c.github.io/blob/main/blog/{{ file_name_clean }}" class="file-action" title="GitHub에서 보기" target="_blank">📖</a>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  {% else %}
    <div class="empty-message">
      <span class="empty-icon">📄</span>
      <h3>파일이 없습니다</h3>
      <p>현재 이 위치에는 파일이 없습니다.</p>
    </div>
  {% endif %}
</div>

<!-- Debugging Section -->
<details style="margin: 20px 0; padding: 10px; background: #f8f9fa; border-radius: 5px;">
<summary style="cursor: pointer; font-weight: bold;">🔍 디버깅 정보 (파일 감지 상태)</summary>
<h4>Static Files in /blog/:</h4>
<ul>
{% for file in site.static_files %}
  {% if file.path contains '/blog/' %}
    <li>{{ file.path }} ({{ file.name }}) - {{ file.extname }}</li>
  {% endif %}
{% endfor %}
</ul>
<h4>Pages in blog:</h4>
<ul>
{% for page in site.pages %}
  {% if page.path contains 'blog' %}
    <li>{{ page.path }} ({{ page.name }}) - {{ page.url }}</li>
  {% endif %}
{% endfor %}
</ul>
</details>

## �📋 최근 업데이트

{% assign all_posts = site.pages %}
{% assign filtered_posts = "" | split: "" %}
{% for page in all_posts %}
  {% if page.category and page.title != page.category %}
    {% assign filtered_posts = filtered_posts | push: page %}
  {% endif %}
{% endfor %}
{% assign sorted_posts = filtered_posts | sort: "date" %}

<div class="recent-posts">
  {% for post in sorted_posts limit: 5 %}
    <div class="recent-post-item">
      <span class="post-date">{{ post.date | date: "%Y년 %m월 %d일" | default: "최근" }}</span>
      <a href="{{ post.url | prepend: site.baseurl }}" class="post-title">{{ post.title }}</a>
      <span class="post-category">{{ post.category }}</span>
    </div>
  {% endfor %}
</div>

- **2025년 8월**: GitHub Pages 웹호스팅 설정 완료
- **블로그 시스템**: 동적 폴더 인식 및 마크다운 렌더링 구현
- **UI 개선**: 테이블 형태의 파일 목록 표시 (날짜순 정렬)

---

<div class="footer-info">
<small>
<strong>개발자 블로그</strong> | <a href="https://c0z0c.github.io/" target="_blank" style="color: #87ceeb;">🌐 메인</a><br>
마지막 업데이트: {{ site.time | date: "%Y년 %m월 %d일" }}
</small>
</div>
