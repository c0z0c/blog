---
layout: default
title: 포트폴리오 - 보관함
description: 포트폴리오 자료들
date: 2025-08-20
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


# 🎨 포트폴리오

<script>

// 폴더 정보 가져오기 함수
function getFolderInfo(folderName) {
    folderName = (folderName || '').toString().replace(/^\/+|\/+$/g, '');
    // 폴더명에 따른 아이콘과 설명 (가나다순 정렬)
    const folderMappings = {
        '감성데이타': { icon: '📊', desc: 'AI HUB 감성 데이타셋' },
        '경구약제 이미지 데이터(데이터 설명서, 경구약제 리스트)': { icon: '📊', desc: '데이터 설명서' },
        '경구약제이미지데이터': { icon: '💊', desc: '약물 데이터' },
        '멘토': { icon: '👨‍🏫', desc: '멘토 관련 자료' },
        '백업': { icon: '💾', desc: '백업 파일들' },
        '발표자료': { icon: '📊', desc: '발표 자료' },
        '셈플': { icon: '📂', desc: '샘플 파일들' },
        '스터디': { icon: '📒', desc: '학습 자료' },
        '포트폴리오': { icon: '✅', desc: '완료된 스프린트 미션들' },
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

function getFileInfo(extname) {
  switch(extname.toLowerCase()) {
    case '.ipynb':
      return { icon: '📓', type: 'Colab' };
    case '.py':
      return { icon: '🐍', type: 'Python' };
    case '.md':
      return { icon: '📝', type: 'Markdown' };
    case '.json':
      return { icon: '⚙️', type: 'JSON' };
    case '.zip':
      return { icon: '📦', type: '압축' };
    case '.png':
    case '.jpg':
    case '.jpeg':
      return { icon: '🖼️', type: '이미지' };
    case '.csv':
      return { icon: '📊', type: '데이터' };
    case '.pdf':
      return { icon: '📄', type: 'PDF' };
    case '.docx':
      return { icon: '�', type: 'Word' };
    case '.pptx':
      return { icon: '📊', type: 'PowerPoint' };
    case '.xlsx':
      return { icon: '📈', type: 'Excel' };
    case '.hwp':
      return { icon: '📄', type: 'HWP' };
    case '.txt':
      return { icon: '📄', type: 'Text' };
    case '.html':
      return { icon: '🌐', type: 'HTML' };
    default:
      return { icon: '📄', type: '파일' };
  }
}

{% assign cur_dir = "/포트폴리오/" %}
{% include cur_files.liquid %}
{% include page_values.html %}
{% include page_files_table.html %}

// DOM이 로드되고 테이블이 렌더링된 후 자동으로 title 컬럼(1번 인덱스) 정렬
window.addEventListener('load', function() {
  // 테이블이 완전히 렌더링되기를 잠시 기다림
  setTimeout(function() {
    const table = document.querySelector('.file-table');
    if (table) {
      // title 컬럼(인덱스 1)을 오름차순으로 정렬
      // sortTable(2, 'Asc'); // 0 날짜 1 제목 2 파일명
      sortTable(0, 'Desc'); // 0 날짜 1 제목 2 파일명
    }
  }, 100); // 100ms 딜레이로 테이블 렌더링 완료 대기
});

</script>

<div class="file-grid">
  <!-- 파일 목록이 JavaScript로 동적 생성됩니다 -->
</div>

---

<div class="navigation-footer">
  <a href="{{- site.baseurl -}}/" class="nav-button home">
    <span class="nav-icon">🏠</span> 홈으로
  </a>
</div>
