---
layout: default
title: "개발자 블로그"
description: "개발자 블로그"
cache-control: no-cache
expires: 0
pragma: no-cache
---

<div class="nav-bar">
    <a href="{{ site.baseurl }}/">🏠 홈</a>
    <a href="{{ site.baseurl }}/블로그/">🎨 블로그</a>
    <a href="{{ site.baseurl }}/회고/">📰 회고</a>
    <button id="theme-toggle" onclick="toggleTheme()">테마 전환</button>
</div>

<script>

// 폴더 정보 가져오기 함수
function getFolderInfo(folderName) {
    folderName = (folderName || '').toString().replace(/^\/+|\/+$/g, '');
    // 폴더명에 따른 아이콘과 설명 (중복 정리됨)
    const folderMappings = {
        '감성데이타': { icon: '📊', desc: 'AI HUB 감성 데이타셋' },
        '경구약제 이미지 데이터(데이터 설명서, 경구약제 리스트)': { icon: '📊', desc: '데이터 설명서' },
        '경구약제이미지데이터': { icon: '💊', desc: '약물 데이터' },
        '멘토': { icon: '👨‍🏫', desc: '멘토 관련 자료' },
        '백업': { icon: '💾', desc: '백업 파일들' },
        '발표자료': { icon: '📊', desc: '발표 자료' },
        '셈플': { icon: '📂', desc: '샘플 파일들' },
        '스터디': { icon: '📒', desc: '학습 자료' },
        '스프린트미션_완료': { icon: '✅', desc: '완료된 스프린트 미션들' },
        '스프린트미션_작업중': { icon: '🚧', desc: '진행 중인 미션들' },
        '실습': { icon: '🔬', desc: '실습 자료' },
        '위클리페이퍼': { icon: '📰', desc: '주간 학습 리포트' },
        '테스트': { icon: '🧪', desc: '테스트 파일들' },
        '협업일지': { icon: '📓', desc: '협업 일지' },
        '회의록': { icon: '📋', desc: '팀 회의록' },
        'AI 모델 환경 설치가이드': { icon: '⚙️', desc: '설치 가이드' },
        'assets': { icon: '🎨', desc: '정적 자원' },
        'image': { icon: '🖼️', desc: '이미지 파일들' },
        'Learning': { icon: '📚', desc: '학습 자료' },
        'Learning Daily': { icon: '📅', desc: '일일 학습 기록' },
        'md': { icon: '📝', desc: 'Markdown 문서' }
    };

    return folderMappings[folderName] || { icon: '📁', desc: '폴더' };
}

{%- comment -%} 트리에서 제외할 폴더명 목록 (쉼표로 구분해서 추가) {%- endcomment -%}
{% assign ignore_dir = "포트폴리오,시험중" %}

{% assign cur_dir = "/" %}
{% include cur_files.liquid %}
{% include page_values.html %}
{% include page_folders_tree.html %}

</script>

### 📚 개발자 블로그

##### 📁 폴더별 탐색

<div class="folder-grid">
  <!-- 폴더 목록이 JavaScript로 동적 생성됩니다 -->
</div>

<div class="navigation-footer">
  <a href="{{- site.baseurl -}}/" class="nav-button home">
    <span class="nav-icon">🏠</span> 홈으로
  </a>
</div>

<div class="footer-info">
<small>
<strong>AI/SW 엔지니어</strong> | 김명환<br>
마지막 업데이트: {{ site.time | date: "%Y년 %m월 %d일" }}
</small>
</div>
