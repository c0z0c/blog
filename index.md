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
      <a href="https://github.com/c0z0c" target="_blank">
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

## 📋 최근 업데이트

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

- **2025년 8월**: GitHub Pages 웹호스팅 설정 완료
- **블로그 시스템**: 동적 폴더 인식 및 마크다운 렌더링 구현
- **UI 개선**: 테이블 형태의 파일 목록 표시 (날짜순 정렬)

---

<div class="footer-info">
<small>
<strong>개발자 블로그</strong> | <a href="https://c0z0c.github.io/" target="_blank" style="color: #3498db;">🌐 메인</a><br>
마지막 업데이트: {{ site.time | date: "%Y년 %m월 %d일" }}
</small>
</div>

<style>
.nav-sections {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
  margin: 30px 0;
}

.section-card {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 25px;
  border: 2px solid #e9ecef;
}

.section-card h2 {
  margin-top: 0;
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
}

.folder-links {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.folder-link {
  display: flex;
  align-items: center;
  padding: 15px;
  background: white;
  border-radius: 8px;
  text-decoration: none;
  border: 1px solid #dee2e6;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.folder-link:hover {
  background: #e3f2fd;
  border-color: #3498db;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  text-decoration: none;
}

.folder-icon {
  font-size: 24px;
  margin-right: 15px;
  width: 30px;
  text-align: center;
}

.folder-name {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 10px;
  flex: 1;
}

.folder-desc {
  color: #666;
  font-size: 0.9em;
  font-style: italic;
}

.quick-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.quick-links a {
  display: flex;
  align-items: center;
  padding: 12px;
  background: white;
  border-radius: 6px;
  text-decoration: none;
  border: 1px solid #dee2e6;
  transition: all 0.3s ease;
}

.quick-links a:hover {
  background: #e8f5e8;
  border-color: #27ae60;
  text-decoration: none;
}

.link-icon {
  margin-right: 10px;
  font-size: 16px;
}

.footer-info {
  text-align: center;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #eee;
  color: #666;
}

/* 최근 포스트 스타일 */
.recent-posts {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  border-left: 4px solid #3498db;
}

.recent-post-item {
  display: flex;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid #e9ecef;
  gap: 15px;
}

.recent-post-item:last-child {
  border-bottom: none;
}

.post-date {
  color: #666;
  font-size: 0.9em;
  min-width: 100px;
}

.post-title {
  flex: 1;
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
}

.post-title:hover {
  color: #3498db;
  text-decoration: underline;
}

.post-category {
  background: #3498db;
  color: white;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  font-weight: 500;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .nav-sections {
    grid-template-columns: 1fr;
  }
  
  .folder-link {
    flex-direction: column;
    text-align: center;
    gap: 5px;
  }
  
  .folder-name, .folder-desc {
    margin: 0;
  }
  
  .recent-post-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 5px;
  }
  
  .post-date {
    min-width: auto;
  }
}
</style>
