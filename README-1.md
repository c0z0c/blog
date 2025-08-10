# 개발자 블로그

GitHub Pages로 호스팅되는 Jekyll 기반 기술 블로그입니다.

## 🌐 라이브 사이트

[https://c0z0c.github.io/blog/](https://c0z0c.github.io/blog/)

## 📁 폴더 구조

```
├── _config.yml          # Jekyll 설정 파일
├── _layouts/            # 레이아웃 템플릿
│   ├── default.html     # 기본 레이아웃
│   └── folder.html      # 폴더 목록 레이아웃
├── 블로그/              # 일반 블로그 포스트
├── Tech Retrospective/  # 기술 회고 및 경험담
└── .github/workflows/   # GitHub Actions 워크플로우
```

## ✨ 주요 기능

1. **동적 폴더 인식**: 새로운 폴더를 추가하면 자동으로 인식됩니다
2. **테이블 형태 파일 목록**: 각 폴더의 파일들이 깔끔한 테이블로 표시됩니다
3. **마크다운 렌더링**: `.md` 파일들이 자동으로 HTML로 변환됩니다
4. **반응형 디자인**: 모바일과 데스크톱에서 모두 최적화된 UI

## 🚀 사용 방법

### 새 포스트 추가

1. 적절한 카테고리 폴더에 `.md` 파일을 생성합니다
2. 파일 상단에 Front Matter를 추가합니다:

```yaml
---
layout: default
title: "포스트 제목"
date: 2025-08-09
category: "블로그"
description: "포스트 설명"
cache-control: no-cache
expires: 0
pragma: no-cache
---
```

3. 마크다운 내용을 작성합니다

### 새 카테고리 추가

1. 새 폴더를 생성합니다
2. 폴더 내에 `index.md` 파일을 생성합니다:

```yaml
---
layout: folder
title: "카테고리 이름"
description: "카테고리 설명"
---
```

3. 메인 `index.md`에서 새 카테고리 링크를 추가합니다

## 🛠️ 로컬 개발

```bash
# Jekyll 설치 (Ruby 필요)
gem install bundler jekyll

# 의존성 설치
bundle install

# 로컬 서버 실행
bundle exec jekyll serve

# 브라우저에서 http://localhost:4000/blog/ 접속
```

## 📝 설정 자동화

`setup_blog.py` 스크립트를 사용하여 마크다운 파일들에 자동으로 Front Matter를 추가할 수 있습니다:

```bash
python setup_blog.py
```

## 🔧 커스터마이징

- `_config.yml`: 사이트 전역 설정
- `_layouts/default.html`: 기본 페이지 레이아웃
- `_layouts/folder.html`: 폴더 목록 페이지 레이아웃
- CSS는 각 레이아웃 파일 내에 인라인으로 포함되어 있습니다

## 📄 라이선스

이 프로젝트는 개인 블로그용으로 제작되었습니다.
