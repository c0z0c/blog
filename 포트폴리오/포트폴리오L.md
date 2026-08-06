---
layout: default
title: "포트폴리오"
description: "포트폴리오"
date: 2026-01-30
cache-control: no-cache
expires: 0
pragma: no-cache
---

# 안녕하세요, 엔지니어 김명환입니다
> **수석 시스템 소프트웨어 엔지니어 & AI 스페셜리스트**
>
> *"복잡한 로직을 신뢰할 수 있는 시스템으로. 20년의 엔지니어링 경험을 AI에 담았습니다."*

[![Email](https://img.shields.io/badge/Email-c0z0c%40outlook.com-0078D4?style=flat-square&logo=microsoft-outlook&logoColor=white)](mailto:c0z0c@outlook.com)
[![GitHub](https://img.shields.io/badge/GitHub-c0z0c-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/c0z0c)
[![PyPI](https://img.shields.io/badge/PyPI-Projects-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/c0z0c)
[![Patents](https://img.shields.io/badge/Patents-10_Registered-FFD700?style=flat-square)](http://kipris.or.kr)

---

## Professional Summary

**"실험실의 AI를 현장의 시스템으로 구현하는 엔지니어"**

저는 지난 20년간 철도 및 전력 제어 시스템 분야에서 고신뢰성 시스템을 설계하고 개발해왔습니다. IEC 62443 보안 표준을 준수하는 고신뢰성 소프트웨어를 개발하며 다수의 특허를 등록했습니다.

이러한 **'시스템 엔지니어링(System Engineering)'** 역량을 바탕으로, 현재는 **'AI 엔지니어링(AI Engineering)'** 분야에서 LLM 서빙 최적화, RAG 파이프라인 구축, On-device AI 경량화에 주력하고 있습니다. 단순히 모델을 돌려보는 것을 넘어, 실제 비즈니스 환경에서 **가용성(Availability)과 확장성(Scalability)**을 보장하는 AI 서비스를 만듭니다.

---

## Technical Skills

| Domain | Skills | Proficiency |
|:---:|:---|:---|
| **AI & LLM** | **PyTorch, LangChain, OpenAI API**, FAISS, HuggingFace, Prompt Engineering | **** |
| **Backend & Cloud** | **FastAPI, Docker**, Google Cloud Platform (Cloud Run, Compute Engine), Streamlit | **** |
| **System & Embedded** | **C/C++, Qt, Linux System Programming**, IPC, Multi-threading, Yocto | ***** |
| **DevOps & Tools** | Git, GitHub Actions, Jira, Confluence | **** |

---

## Key Projects (AI Engineering)

#### 1. [팀] 나노코코아 - SaaS 광고 콘텐츠 생성 플랫폼
> **Role:** 시스템 아키텍트 & 백엔드 리드 | **Period:** 2025.12 - 2026.01
* **개요:** 소상공인을 위해 광고 문구(LLM)와 이미지(Diffusion)를 원스톱으로 생성하는 SaaS
* **Tech Stack:** FastAPI, MSA, Docker, FLUX.1-dev, Qwen-2.5-32b

#### Technical Challenges & Solutions
* **Challenge 1: GPU 메모리 한계와 속도 저하 (Latency)**
    * **문제:** 초기 고성능 모델(FLUX.1-dev)이 L4 GPU VRAM을 초과하여, 요청 시마다 모델을 올리고 내리는 **Load/Unload 방식**을 적용했으나 생성에 **600초**가 소요되는 성능 이슈 발생.
    * **해결:** 프로젝트 종료 후 독자적인 고도화를 수행. 파라미터 수가 적으면서도 동등 성능을 내는 **최신 경량화 모델을 발굴 및 검증**하여, 모델을 메모리에 상주시키는 **In-Memory Serving 아키텍처**로 전환.
    * **성과:** 모델 로딩 오버헤드를 완전히 제거하여 생성 시간 **600초 → 60초 (90% 단축)** 달성.
* **Challenge 2: 한글 텍스트 렌더링 깨짐 현상**
    * **문제:** 확산 모델(Diffusion)이 이미지 내 한글 텍스트를 제대로 생성하지 못하는 고질적 문제.
    * **해결:** 텍스트 영역을 HTML/CSS로 렌더링한 후 이미지로 변환하여 합성하는 **Hybrid Rendering** 파이프라인 구축.
    * **성과:** 텍스트 **오타율 0%** 달성.

 [GitHub 저장소](https://github.com/c0z0c/codeit-ai-3team-ad-content) | [데모 영상](https://youtu.be/YG-xEIOPDD8)
---

### 2. [팀] RAG 기반 나라장터 입찰 문서 검색 시스템
> **Role:** 임베딩 엔지니어 (PM) | **Period:** 2025.11 - 2025.12
* **개요:** 공공조달 문서(PDF, HWP)의 복잡한 표와 데이터를 LLM이 이해할 수 있도록 구조화하여 검색
* **Tech Stack:** LangChain, FAISS, OpenAI Embeddings, Streamlit

#### Technical Challenges & Solutions
* **Challenge 1: 임베딩 비용 과다 및 검색 정확도 저하**
    * **문제:** 수천 장의 문서 전체를 임베딩할 경우 비용이 높고, 불필요한 헤더/푸터가 검색 품질 저하.
    * **해결:** 문서의 의미론적 청킹(Semantic Chunking) 및 메타데이터 필터링 적용. **파일 해시(SHA-256)** 기반 중복 문서 제거 로직 구현.
    * **성과:** 원본 대비 토큰 사용량 **21.5% 절감**, 검색 정확도 향상.
* **Challenge 2: HWP(한글) 문서의 표 데이터 손실**
    * **문제:** 기존 라이브러리가 HWP 표 구조를 텍스트로만 추출하여 LLM이 맥락을 이해하지 못함.
    * **해결:** HWP 표 구조를 유지하며 Markdown 형식으로 변환하는 전처리 도구 **`helper-hwp`** 자체 개발 및 배포.

 [GitHub 저장소](https://github.com/c0z0c/codeit_ai_g2b_search) | [데모 영상](https://youtu.be/rFoyNxsR5cE)

---

### 3. [개인] H2 Map - 실시간 수소충전소 지도 서비스
> **Tech:** Google Cloud Run, Flask, Kakao Map API
* **서버리스 아키텍처:** 트래픽이 간헐적인 서비스 특성을 고려해 **Google Cloud Run (Scale-to-Zero)** 도입, 유지 비용 최소화.
* **실시간 데이터 파이프라인:** 공공데이터 포털 API를 5분 단위로 폴링(Polling)하여 캐싱, 사용자 대기 시간 제거.
* [서비스 바로가기](https://h2map-p4wpy5hxaa-du.a.run.app)

---

## Open Source Contributions (PyPI)
개발자들의 생산성을 높이기 위해, 반복되는 문제를 해결하는 도구를 라이브러리화하여 배포했습니다.

* **[helper-dev-utils](https://pypi.org/project/helper-dev-utils/)**: `pip install helper-dev-utils`
    * 복잡한 로깅 설정과 디버깅 유틸리티를 한 줄로 초기화할 수 있는 래퍼(Wrapper).
* **[helper-plot-hangul](https://pypi.org/project/helper-plot-hangul/)**: `pip install helper-plot-hangul`
    * Matplotlib 사용 시 OS(Windows/Linux/Mac)를 자동 감지하여 한글 폰트를 적용해주는 라이브러리.
* **[helper-md-doc](https://pypi.org/project/helper-md-doc/)**: Python Docstring을 파싱하여 Markdown 기술 문서를 자동 생성.
* **[helper-hwp](https://pypi.org/project/helper-hwp/)**: RAG 시스템 구축을 위해 HWP 문서를 텍스트/마크다운으로 변환.

---

## System Engineering Experience (2005 ~ 2025)
**"극한의 환경에서도 멈추지 않는 시스템을 만들었습니다."**

### 주요 성과 (Key Achievements)
* **Virtual Simulation (Digital Twin)**
    * **상황:** 지하철 신호 시스템 테스트를 위해 실제 차량을 운행해야 하는 물리적/비용적 제약 발생.
    * **해결:** 실제 차량의 통신 프로토콜과 동작을 100% 모사하는 **가상 시뮬레이터(TCMS Simulator)**를 C++/Qt로 독자 개발.
    * **결과:** 현장 테스트 기간 6개월 단축 및 디버깅 효율 향상 (특허 등록).

* **Cyber Security & Integrity**
    * **상황:** 외부 인터넷 연결이 차단된 폐쇄망 환경(전력 제어 시스템)에서의 무결성 검증 요구.
    * **해결:** 블록체인 원리를 응용한 **경량 해시체인(Hash-Chain)** 기술을 임베디드 장비에 적용.
    * **결과:** 국제 보안 표준 **IEC 62443-4-1** 인증 획득 및 시스템 무결성 보장.

---

## Patents & Education

### Patents (10 Registered)
* **AI & Data:** JSONL 포맷 압축 및 복원 방법 (출원 중, 10-2025-XXXXXXX)
* **Simulation:** 열차방송 시뮬레이션 장치 (등록 제 10-XXXXXXX호)
* **Network:** PLC 네트워크 신호 간섭 판단 시스템 (등록 제 10-XXXXXXX호)

### Education
* **Codeit AI Engineering Track 4기** (2025.07 - 2026.01)
    * 딥러닝 이론(CNN/RNN/Transformer) 및 MLOps 실무 과정 수료

---

© 2026 MyungHwan Kim.