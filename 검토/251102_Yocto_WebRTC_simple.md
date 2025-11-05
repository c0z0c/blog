---
layout: default
title: "Yocto ARM32 WebRTC 오디오 테스트 환경 구축 가이드 (검토)"
description: "Yocto ARM32 WebRTC 오디오 테스트 환경 구축 가이드 (검토)"
author: "김명환"
date: 2025-11-05
category: "검토"
cache-control: no-cache
expires: 0
pragma: no-cache
---

# Yocto ARM32 WebRTC 오디오 테스트 환경 구축 가이드 (검토)

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [Yocto 이미지 빌드](#yocto-이미지-빌드)
3. [WebRTC 환경 구성](#webrtc-환경-구성)
4. [GStreamer + WebRTC 테스트](#gstreamer--webrtc-테스트)
5. [MVP 테스트 (코딩 없이)](#mvp-테스트-코딩-없이)
6. [오디오 테스트 시나리오](#오디오-테스트-시나리오)

---

## 프로젝트 개요

### 목표
동일 IP 망에서 ARM32 Yocto 장치 간 WebRTC를 통한 양방향 오디오 통신 테스트

### 테스트 구성
```
[장치 A]                              [장치 B]
mp3 재생 → PulseAudio → WebRTC ═══════> WebRTC → PulseAudio → 스피커
스피커 ← PulseAudio ← WebRTC <═══════ WebRTC ← PulseAudio ← mp3 재생
```

### 필요 구성요소
- Yocto Project (ARM32 타겟)
- GStreamer (1.20+)
- GStreamer WebRTC 플러그인
- PulseAudio
- 간단한 WebRTC 시그널링 서버

---

## Yocto 이미지 빌드

### 1단계: 빌드 환경 준비

#### 호스트 시스템 요구사항
```bash
# Ubuntu 22.04 LTS 권장
# 최소 100GB 여유 디스크 공간
# 최소 8GB RAM (16GB 권장)
```

#### 필수 패키지 설치
```bash
sudo apt update
sudo apt install -y \
    gawk wget git diffstat unzip texinfo gcc build-essential \
    chrpath socat cpio python3 python3-pip python3-pexpect \
    xz-utils debianutils iputils-ping python3-git python3-jinja2 \
    libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit \
    mesa-common-dev zstd liblz4-tool
```

### 2단계: Yocto 프로젝트 다운로드

```bash
# 작업 디렉토리 생성
mkdir -p ~/yocto-webrtc
cd ~/yocto-webrtc

# Yocto Kirkstone (LTS) 다운로드
git clone -b kirkstone git://git.yoctoproject.org/poky.git
cd poky

# 추가 레이어 다운로드
git clone -b kirkstone git://git.openembedded.org/meta-openembedded
git clone -b kirkstone https://github.com/meta-qt5/meta-qt5.git
```

### 3단계: 빌드 환경 초기화

```bash
# ARM32 타겟으로 빌드 환경 설정
source oe-init-build-env build-arm32
```

### 4단계: local.conf 설정

`conf/local.conf` 파일을 편집합니다:

```bash
# 타겟 머신 설정 (예: Raspberry Pi 3)
MACHINE = "raspberrypi3"

# 또는 일반 ARM32 QEMU 테스트용
# MACHINE = "qemuarm"

# 병렬 빌드 설정 (CPU 코어 수에 맞게 조정)
BB_NUMBER_THREADS = "8"
PARALLEL_MAKE = "-j 8"

# 디스크 공간 모니터링
BB_DISKMON_DIRS = "\
    STOPTASKS,${TMPDIR},1G,100K \
    STOPTASKS,${DL_DIR},1G,100K \
    STOPTASKS,${SSTATE_DIR},1G,100K \
    STOPTASKS,/tmp,100M,100K \
    ABORT,${TMPDIR},100M,1K \
    ABORT,${DL_DIR},100M,1K \
    ABORT,${SSTATE_DIR},100M,1K \
    ABORT,/tmp,10M,1K"

# 패키지 관리자
PACKAGE_CLASSES = "package_ipk"

# 추가 이미지 기능
EXTRA_IMAGE_FEATURES += "debug-tweaks ssh-server-openssh tools-debug"

# 네트워크 설정
DISTRO_FEATURES:append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""
```

### 5단계: bblayers.conf 설정

`conf/bblayers.conf` 파일에 필요한 레이어 추가:

```bash
BBLAYERS ?= " \
  /home/user/yocto-webrtc/poky/meta \
  /home/user/yocto-webrtc/poky/meta-poky \
  /home/user/yocto-webrtc/poky/meta-yocto-bsp \
  /home/user/yocto-webrtc/poky/meta-openembedded/meta-oe \
  /home/user/yocto-webrtc/poky/meta-openembedded/meta-multimedia \
  /home/user/yocto-webrtc/poky/meta-openembedded/meta-networking \
  /home/user/yocto-webrtc/poky/meta-openembedded/meta-python \
  "
```

### 6단계: 커스텀 이미지 레시피 생성

`meta-custom` 레이어 생성:

```bash
cd ~/yocto-webrtc/poky
bitbake-layers create-layer meta-custom
bitbake-layers add-layer meta-custom
```

`meta-custom/recipes-core/images/webrtc-test-image.bb` 생성:

```bash
SUMMARY = "WebRTC Audio Test Image"
LICENSE = "MIT"

inherit core-image

IMAGE_INSTALL:append = " \
    packagegroup-core-boot \
    packagegroup-core-full-cmdline \
    packagegroup-base-wifi \
    gstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-plugins-base-playback \
    gstreamer1.0-plugins-base-audiotestsrc \
    gstreamer1.0-plugins-good-pulse \
    gstreamer1.0-plugins-good-autodetect \
    pulseaudio \
    pulseaudio-server \
    pulseaudio-module-loopback \
    alsa-utils \
    alsa-plugins \
    mpg123 \
    curl \
    wget \
    nano \
    vim \
    openssh \
    python3 \
    python3-pip \
    python3-websockets \
    python3-aiohttp \
    kernel-modules \
    linux-firmware \
    "

# WebRTC 플러그인 추가 (GStreamer 1.20+에서 기본 포함)
IMAGE_INSTALL:append = " gstreamer1.0-plugins-bad-webrtc "

# 네트워크 도구
IMAGE_INSTALL:append = " \
    iproute2 \
    iputils \
    net-tools \
    avahi-daemon \
    "

# 개발 도구 (선택사항)
IMAGE_INSTALL:append = " \
    gdb \
    strace \
    tcpdump \
    "

IMAGE_FEATURES += "package-management"

# 루트 파일시스템 크기 (MB)
IMAGE_ROOTFS_EXTRA_SPACE = "2048"
```

### 7단계: 이미지 빌드

```bash
# 빌드 시작 (첫 빌드는 수 시간 소요)
bitbake webrtc-test-image

# 빌드 완료 후 이미지 위치
# tmp/deploy/images/${MACHINE}/webrtc-test-image-${MACHINE}.wic.gz
```

### 8단계: 이미지 플래싱

#### SD 카드에 쓰기 (Raspberry Pi 예시)
```bash
cd tmp/deploy/images/raspberrypi3

# SD 카드 확인 (예: /dev/sdX)
lsblk

# 압축 해제 및 쓰기
gunzip -c webrtc-test-image-raspberrypi3.wic.gz | sudo dd of=/dev/sdX bs=4M status=progress
sync
```

#### QEMU 테스트용
```bash
# QEMU로 직접 부팅
runqemu qemuarm nographic slirp

# 또는
runqemu qemuarm
```

---

## WebRTC 환경 구성

### 1단계: 장치 네트워크 설정

각 장치에서 고정 IP 설정:

```bash
# 장치 A: 192.168.1.100
sudo nmcli con mod eth0 ipv4.addresses 192.168.1.100/24
sudo nmcli con mod eth0 ipv4.gateway 192.168.1.1
sudo nmcli con mod eth0 ipv4.dns 8.8.8.8
sudo nmcli con mod eth0 ipv4.method manual
sudo nmcli con up eth0

# 장치 B: 192.168.1.101
sudo nmcli con mod eth0 ipv4.addresses 192.168.1.101/24
sudo nmcli con mod eth0 ipv4.gateway 192.168.1.1
sudo nmcli con mod eth0 ipv4.dns 8.8.8.8
sudo nmcli con mod eth0 ipv4.method manual
sudo nmcli con up eth0
```

또는 systemd-networkd 사용:

```bash
# /etc/systemd/network/10-eth0.network
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
```

### 2단계: PulseAudio 설정

```bash
# PulseAudio 설정 파일 확인
cat /etc/pulse/default.pa

# 자동 시작 설정
systemctl --user enable pulseaudio
systemctl --user start pulseaudio

# 오디오 장치 확인
pactl list sources short
pactl list sinks short
```

PulseAudio 네트워크 설정 (`/etc/pulse/default.pa`):

```bash
# TCP를 통한 네트워크 오디오 (선택사항)
load-module module-native-protocol-tcp auth-anonymous=1

# 모니터 소스 활성화
load-module module-loopback latency_msec=1
```

### 3단계: 오디오 장치 테스트

```bash
# 녹음 테스트
arecord -d 5 -f cd test.wav
aplay test.wav

# PulseAudio 테스트
parecord -d 5 test-pulse.wav
paplay test-pulse.wav

# GStreamer 오디오 테스트
gst-launch-1.0 audiotestsrc ! autoaudiosink
```

---

## GStreamer + WebRTC 테스트

### 1단계: GStreamer WebRTC 플러그인 확인

```bash
# WebRTC 플러그인 확인
gst-inspect-1.0 webrtcbin

# 사용 가능한 모든 플러그인 확인
gst-inspect-1.0 | grep -i webrtc
gst-inspect-1.0 | grep -i rtp
```

### 2단계: 간단한 시그널링 서버 준비

Python 기반 간단한 WebSocket 시그널링 서버 (`signaling-server.py`):

```python
#!/usr/bin/env python3
import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 연결된 클라이언트 저장
clients = {}

async def signaling_handler(websocket, path):
    client_id = None
    try:
        # 클라이언트 등록
        async for message in websocket:
            data = json.loads(message)
            msg_type = data.get('type')
            
            if msg_type == 'register':
                client_id = data.get('id')
                clients[client_id] = websocket
                logger.info(f"Client {client_id} registered. Total clients: {len(clients)}")
                await websocket.send(json.dumps({
                    'type': 'registered',
                    'id': client_id
                }))
            
            elif msg_type == 'offer' or msg_type == 'answer' or msg_type == 'ice':
                # 다른 클라이언트에게 전달
                target_id = data.get('target')
                if target_id in clients:
                    await clients[target_id].send(message)
                    logger.info(f"Forwarded {msg_type} from {client_id} to {target_id}")
    
    except websockets.exceptions.ConnectionClosed:
        logger.info(f"Client {client_id} disconnected")
    
    finally:
        if client_id and client_id in clients:
            del clients[client_id]

async def main():
    server = await websockets.serve(signaling_handler, "0.0.0.0", 8443)
    logger.info("Signaling server started on ws://0.0.0.0:8443")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
```

호스트 PC에서 실행:

```bash
# Python websockets 설치
pip3 install websockets

# 서버 실행
python3 signaling-server.py
```

### 3단계: GStreamer WebRTC 송신 파이프라인

장치 A (송신자):

```bash
#!/bin/bash
# webrtc-sender.sh

SIGNALING_SERVER="ws://192.168.1.1:8443"
CLIENT_ID="device_a"

gst-launch-1.0 -v \
    webrtcbin name=sendrecv bundle-policy=max-bundle \
    stun-server=stun://stun.l.google.com:19302 \
    ! queue ! rtpopusdepay ! opusdec ! audioconvert ! pulsesink \
    pulsesrc ! audioconvert ! audioresample ! opusenc ! rtpopuspay ! \
    queue ! application/x-rtp,media=audio,encoding-name=OPUS,payload=96 ! sendrecv.
```

### 4단계: GStreamer WebRTC 수신 파이프라인

장치 B (수신자):

```bash
#!/bin/bash
# webrtc-receiver.sh

SIGNALING_SERVER="ws://192.168.1.1:8443"
CLIENT_ID="device_b"

gst-launch-1.0 -v \
    webrtcbin name=sendrecv bundle-policy=max-bundle \
    stun-server=stun://stun.l.google.com:19302 \
    ! queue ! rtpopusdepay ! opusdec ! audioconvert ! pulsesink \
    pulsesrc ! audioconvert ! audioresample ! opusenc ! rtpopuspay ! \
    queue ! application/x-rtp,media=audio,encoding-name=OPUS,payload=96 ! sendrecv.
```

---

## MVP 테스트 (코딩 없이)

### 방법 1: GStreamer 직접 RTP 스트리밍 (WebRTC 없이)

이 방법은 시그널링 없이 간단하게 테스트할 수 있습니다.

#### 장치 A (송신):
```bash
# MP3 파일을 RTP로 전송
gst-launch-1.0 -v \
    filesrc location=/path/to/test.mp3 ! \
    mpegaudioparse ! mpg123audiodec ! \
    audioconvert ! audioresample ! \
    opusenc ! rtpopuspay ! \
    udpsink host=192.168.1.101 port=5000
```

#### 장치 B (수신):
```bash
# RTP 수신 및 재생
gst-launch-1.0 -v \
    udpsrc port=5000 caps="application/x-rtp,media=audio,encoding-name=OPUS,payload=96" ! \
    rtpopusdepay ! opusdec ! \
    audioconvert ! pulsesink
```

### 방법 2: PulseAudio 네트워크 스트리밍

더욱 간단한 방법:

#### 장치 A (서버):
```bash
# PulseAudio를 네트워크 서버로 설정
pactl load-module module-native-protocol-tcp auth-anonymous=1

# MP3 재생
mpg123 -a pulse /path/to/test.mp3
```

#### 장치 B (클라이언트):
```bash
# 원격 PulseAudio 서버 연결
export PULSE_SERVER=192.168.1.100

# 원격 오디오 듣기
paplay --server=192.168.1.100 /path/to/test.mp3

# 또는 모든 오디오 자동 전달
pactl load-module module-tunnel-sink server=192.168.1.100
```

### 방법 3: GStreamer WebRTC 기존 예제 사용

GStreamer에 포함된 WebRTC 예제 활용:

```bash
# GStreamer 예제 다운로드
git clone https://gitlab.freedesktop.org/gstreamer/gst-examples.git
cd gst-examples/webrtc/sendrecv/gst

# Python 종속성 설치
pip3 install websockets

# 송신 측 (장치 A)
python3 webrtc_sendrecv.py --peer-id=1 --server=ws://192.168.1.1:8443

# 수신 측 (장치 B)
python3 webrtc_sendrecv.py --peer-id=2 --server=ws://192.168.1.1:8443
```

---

## 오디오 테스트 시나리오

### 시나리오 1: MP3 파일 → WebRTC → 스피커

#### 장치 A:
```bash
# MP3를 PulseAudio로 재생 (백그라운드)
mpg123 -a pulse /path/to/test.mp3 &

# PulseAudio 출력을 WebRTC로 전송
gst-launch-1.0 -v \
    pulsesrc ! audioconvert ! audioresample ! \
    opusenc ! rtpopuspay ! \
    udpsink host=192.168.1.101 port=5000
```

#### 장치 B:
```bash
# WebRTC 수신 및 스피커 출력
gst-launch-1.0 -v \
    udpsrc port=5000 caps="application/x-rtp,media=audio,encoding-name=OPUS,payload=96" ! \
    rtpopusdepay ! opusdec ! \
    audioconvert ! pulsesink
```

### 시나리오 2: 양방향 오디오 (Full Duplex)

#### 장치 A:
```bash
# 송신
gst-launch-1.0 -v \
    pulsesrc device="default" ! \
    audioconvert ! audioresample ! \
    opusenc ! rtpopuspay ! \
    udpsink host=192.168.1.101 port=5000 &

# 수신
gst-launch-1.0 -v \
    udpsrc port=5001 caps="application/x-rtp,media=audio,encoding-name=OPUS,payload=96" ! \
    rtpopusdepay ! opusdec ! \
    audioconvert ! pulsesink
```

#### 장치 B:
```bash
# 송신
gst-launch-1.0 -v \
    pulsesrc device="default" ! \
    audioconvert ! audioresample ! \
    opusenc ! rtpopuspay ! \
    udpsink host=192.168.1.100 port=5001 &

# 수신
gst-launch-1.0 -v \
    udpsrc port=5000 caps="application/x-rtp,media=audio,encoding-name=OPUS,payload=96" ! \
    rtpopusdepay ! opusdec ! \
    audioconvert ! pulsesink
```

### 시나리오 3: PulseAudio Monitor 캡처

스피커 출력을 다시 캡처하여 전송:

```bash
# 사용 가능한 소스 확인
pactl list sources short

# 모니터 소스 찾기 (예: alsa_output.platform-bcm2835_audio.analog-stereo.monitor)

# 스피커 출력(모니터)을 WebRTC로 전송
gst-launch-1.0 -v \
    pulsesrc device="alsa_output.platform-bcm2835_audio.analog-stereo.monitor" ! \
    audioconvert ! audioresample ! \
    opusenc ! rtpopuspay ! \
    udpsink host=192.168.1.101 port=5000
```

### 시나리오 4: 루프백 테스트 (단일 장치)

```bash
# 마이크 → 스피커 루프백
gst-launch-1.0 -v \
    pulsesrc ! audioconvert ! pulsesink

# 지연 시간 측정
gst-launch-1.0 -v \
    audiotestsrc wave=sine freq=1000 ! \
    audioconvert ! pulsesink
```

---

## 문제 해결 가이드

### 오디오 장치가 인식되지 않는 경우

```bash
# ALSA 장치 확인
aplay -l
arecord -l

# PulseAudio 재시작
systemctl --user restart pulseaudio

# 커널 모듈 확인
lsmod | grep snd

# 오디오 그룹 권한 확인
groups
sudo usermod -aG audio $USER
```

### GStreamer 파이프라인 디버깅

```bash
# 디버그 레벨 설정
export GST_DEBUG=3

# WebRTC 상세 로그
export GST_DEBUG=webrtc:5,dtls:5

# 파이프라인 그래프 생성
export GST_DEBUG_DUMP_DOT_DIR=/tmp
gst-launch-1.0 ... (your pipeline)
dot -Tpng /tmp/*.dot -o pipeline.png
```

### 네트워크 연결 테스트

```bash
# ping 테스트
ping 192.168.1.101

# UDP 포트 테스트
nc -u -l 5000  # 수신 측
echo "test" | nc -u 192.168.1.101 5000  # 송신 측

# 방화벽 확인
sudo iptables -L
sudo iptables -A INPUT -p udp --dport 5000:5010 -j ACCEPT
```

### PulseAudio 오디오 품질 설정

`/etc/pulse/daemon.conf`:

```conf
default-sample-format = s16le
default-sample-rate = 48000
default-sample-channels = 2
default-fragments = 4
default-fragment-size-msec = 10
```

---

## 성능 최적화

### 1. 지연 시간 최소화

```bash
# 낮은 지연 시간 설정
gst-launch-1.0 -v \
    pulsesrc buffer-time=20000 latency-time=10000 ! \
    audioconvert ! audioresample ! \
    opusenc bitrate=128000 frame-size=10 ! \
    rtpopuspay ! udpsink host=192.168.1.101 port=5000 sync=false
```

### 2. CPU 사용률 모니터링

```bash
# GStreamer 통계
gst-launch-1.0 ... --gst-debug-level=0 -v 2>&1 | grep -i "cpu\|buffer"

# 시스템 모니터링
top -p $(pgrep gst-launch)
```

### 3. 버퍼 크기 조정

```bash
# 버퍼 크기 증가 (안정성 우선)
gst-launch-1.0 -v \
    pulsesrc buffer-time=200000 ! \
    queue max-size-buffers=10 ! \
    audioconvert ! pulsesink buffer-time=200000

# 버퍼 크기 감소 (지연 시간 우선)
gst-launch-1.0 -v \
    pulsesrc buffer-time=10000 latency-time=5000 ! \
    queue max-size-buffers=2 ! \
    audioconvert ! pulsesink buffer-time=10000
```

---

## 다음 단계

### 프로덕션 환경으로 전환

1. **보안 강화**
   - DTLS/SRTP 활성화
   - 인증 시스템 구현
   - 방화벽 규칙 설정

2. **안정성 향상**
   - 자동 재연결 로직
   - 에러 핸들링
   - 로깅 시스템

3. **기능 확장**
   - 다중 피어 지원
   - 비디오 스트리밍 추가
   - 녹음/녹화 기능

4. **모니터링**
   - 네트워크 품질 측정
   - 패킷 손실률 추적
   - 지연 시간 모니터링

---

## 참고 자료

- [GStreamer 공식 문서](https://gstreamer.freedesktop.org/documentation/)
- [GStreamer WebRTC 플러그인](https://gstreamer.freedesktop.org/documentation/webrtc/index.html)
- [Yocto Project 공식 문서](https://docs.yoctoproject.org/)
- [PulseAudio 문서](https://www.freedesktop.org/wiki/Software/PulseAudio/)
- [WebRTC 표준](https://webrtc.org/)
