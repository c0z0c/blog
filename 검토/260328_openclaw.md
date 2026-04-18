---
layout: default
title: "OpenClaw 배포 및 텔레그램 봇 설정 가이드"
description: "OpenClaw 배포 및 텔레그램 봇 설정 가이드"
author: "김명환"
date: 2026-03-28
category: "검토"
cache-control: no-cache
expires: 0
pragma: no-cache
---


# 🦞 OpenClaw 배포 및 텔레그램 봇 설정 가이드

본 가이드는 Docker를 활용하여 OpenClaw 기반의 AI 어시스턴트(학습 도우미/팀 비서)를 구축하고 텔레그램 그룹방에 연동하는 표준 절차를 설명합니다.

## 1. 사전 준비
- **Docker & Docker Compose** 설치 완료
- 텔레그램 **@BotFather**를 통해 봇 생성 및 Token 확보
- 텔레그램 봇의 **Privacy Mode를 `Disable`**로 설정 (그룹방 모든 메시지 수신용)

## 2. 디렉토리 구조 및 시스템 설정

작업할 최상위 디렉토리(예: `~/openclaw`)를 생성하고 이동합니다.

```bash
mkdir -p ~/openclaw/{config,data,company_docs}
cd ~/openclaw
```

### 2.1. `docker-compose.yml` 작성
`~/openclaw/docker-compose.yml` 파일을 생성하고 아래 내용을 입력합니다. (RAG 파일 자동 정리를 위해 `company_docs`는 `rw` 권한으로 마운트합니다.)

```yaml
services:
  openclaw:
    image: ghcr.io/openclaw/openclaw:latest
    container_name: openclaw-bot
    restart: always
    network_mode: "host"
    volumes:
      - ./config:/home/node/.openclaw
      - ./data:/home/node/.openclaw/data
      - ./company_docs:/app/user_docs:rw
      - /etc/localtime:/etc/localtime:ro
    env_file: .env
    deploy:
      resources:
        limits:
          memory: 4G
```

### 2.2. `.env` 파일 작성
`~/openclaw/.env` 파일에 필요한 환경 변수(API 키 등)를 구성합니다.

```env
# 필요한 환경 변수 예시
GEMINI_API_KEY=your_api_key_here
```

## 3. 에이전트 초기화 (Workspace 생성)

Docker 컨테이너를 임시로 실행하여 `main` 에이전트의 기본 구조와 설정 파일을 생성합니다.

```bash
sudo docker compose run --rm openclaw openclaw agents add main
```
> **결과:** `config/` 폴더 하위에 `openclaw.json` 및 `workspace/` 디렉토리가 자동 생성됩니다.

## 4. 텔레그램 연동 및 그룹방 설정

봇이 특정 그룹방에서 멘션 없이도 대화를 읽고 반응하도록 `config/openclaw.json`을 수정합니다.

```json
"channels": {
  "telegram": {
    "enabled": true,
    "dmPolicy": "pairing",
    "groupPolicy": "allowlist",
    "groups": {
      "-100XXXXXXXXXX": { 
        "requireMention": false
      }
    },
    "streaming": "partial"
  }
}
```
* `-100XXXXXXXXXX` 부분을 실제 텔레그램 슈퍼그룹 ID로 변경합니다.

## 5. 봇 페르소나 및 운영 규칙 설정 (한국어 패치)

`config/workspace/` 내의 주요 마크다운 파일들을 수정하여 봇의 성격과 동작 방식을 제어합니다.

### 5.1. `SOUL.md` (응답 규칙)
```markdown
# 핵심 응답 규칙 (CRITICAL)
1. **관찰 및 기록**: 그룹 대화의 모든 내용을 경청하고 맥락을 기억에 저장하십시오. 
2. **응답 조건**: 메시지에 반드시 **"xxxAI"**라는 호출어가 포함된 경우에만 응답하십시오.
3. **파일 관리**: 업로드된 문서는 내용에 따라 `/app/user_docs/` 하위의 적절한 폴더로 자동 이동 및 정리하십시오.
```

### 5.2. `AGENTS.md` (재시작 및 초기화 규칙)
```markdown
## 세션 시작 절차
시스템이 재시작되거나 새로운 세션이 활성화되면 즉시 다음 메시지를 전송하십시오:
**"xxxAI 안녕하세요. 현재 시간은 [현재 시간] 입니다. 시스템이 가동되었습니다."**
```

### 5.3. 에이전트 식별자 설정 (`config/agents/main/agent/identity.json`)
봇이 자신을 부르는 이름을 명확히 인지하도록 설정합니다.
```json
{
  "names": ["xxxAI"],
  "description": "학습 도우미 및 팀 비서"
}
```

## 6. 서비스 실행 및 일일 자동 요약(Cron) 설정

### 6.1. 서비스 백그라운드 실행
```bash
sudo docker compose up -d
```

### 6.2. crontab을 이용한 자동 요약 스케줄링
매일 밤 23시 50분에 봇에게 하루 대화 요약을 지시하는 명령을 호스트 OS의 crontab에 등록합니다.

```bash
# crontab -e 명령어로 아래 내용 추가
50 23 * * * /usr/bin/docker exec openclaw-bot openclaw message send --channel telegram --target -100XXXXXXXXXX --message "xxxAI 오늘 대화 내용을 요약해서 메모리에 저장해줘."
```

## 7. RAG (지식 베이스) 문서 추가 방법
호스트 서버의 `~/openclaw/company_docs/` 디렉토리 내에 하위 폴더를 만들고 텍스트(`.txt`, `.md`) 또는 PDF 파일을 넣으면 봇이 이를 참조하여 답변합니다.

---

이 문서를 바탕으로 다른 서버에 세팅하시거나 팀원에게 공유하시면 동일한 환경을 10분 내에 구성하실 수 있습니다. 

추가로 문서에 포함하고 싶은 보안 관련 설정이나 네트워크 격리 등 세부 항목이 있으신가요?