---
layout: default
title: "YOLO 모델 검토 보고서"
description: "YOLO 모델 검토 보고서"
author: "김명환"
date: 2025-08-12
category: "검토"
cache-control: no-cache
expires: 0
pragma: no-cache
---


> **작성자:** 김명환  
> **작성일:** 2025-08-12

# YOLO 모델 검토 보고서

## 1. YOLO(You Only Look Once) 개요

YOLO는 실시간 객체 탐지를 위한 딥러닝 모델로, 2015년 Joseph Redmon이 처음 제안했습니다. "You Only Look Once"라는 이름처럼 이미지를 한 번만 보고 객체의 위치와 클래스를 동시에 예측하는 것이 특징입니다.

## 2. YOLO의 주요 특징

### 2.1 실시간 처리 성능
- **단일 신경망 구조**: 전체 이미지를 한 번에 처리하여 빠른 추론 속도 제공
- **End-to-End 학습**: 객체 탐지와 분류를 동시에 수행
- **실시간 처리**: YOLOv8 기준 RTX 3080에서 약 100+ FPS 달성 가능

### 2.2 통합된 탐지 방식
- **Grid-based 접근**: 이미지를 그리드로 나누어 각 셀에서 객체 탐지
- **Bounding Box + Confidence**: 객체의 위치와 신뢰도를 동시에 예측
- **Non-Maximum Suppression**: 중복 탐지 제거로 정확도 향상

### 2.3 버전별 발전사항
- **YOLOv1-v3**: 초기 개념 정립 및 성능 개선
- **YOLOv4-v5**: 정확도와 속도의 균형점 향상
- **YOLOv8-v11**: 최신 버전으로 사용성과 성능 대폭 개선

## 3. YOLO 학습을 위한 필수 라이브러리 및 도구

### 3.1 Python 환경 구성
```bash
# 기본 환경
Python 3.8+ (권장: 3.9-3.11)
pip install ultralytics  # YOLOv8+ 통합 패키지
```

### 3.2 필수 라이브러리
```bash
# 딥러닝 프레임워크
torch>=1.8.0
torchvision>=0.9.0

# 데이터 처리
opencv-python>=4.5.0
pillow>=8.0.0
numpy>=1.21.0
pandas>=1.3.0

# 시각화 및 모니터링
matplotlib>=3.3.0
seaborn>=0.11.0
wandb  # 선택사항: 학습 모니터링

# 데이터 어노테이션 (선택사항)
labelImg  # 수동 라벨링 도구
roboflow  # 자동 데이터 증강 및 관리
```

### 3.3 개발 환경 추천
- **Jupyter Notebook** 또는 **Google Colab**: 초기 실험용
- **PyCharm** 또는 **VSCode**: 본격적인 개발용
- **Docker**: 환경 일관성 확보

## 4. 학습을 위한 하드웨어 요구사항

### 4.1 최소 사양 (학습 가능)
- **GPU**: GTX 1660 Ti (6GB VRAM) 이상
- **CPU**: Intel i5-8400 / AMD Ryzen 5 2600 이상
- **RAM**: 16GB 이상
- **저장공간**: SSD 100GB 이상 여유공간

### 4.2 권장 사양 (효율적 학습)
- **GPU**: RTX 3060 (12GB VRAM) 이상
- **CPU**: Intel i7-10700 / AMD Ryzen 7 3700X 이상
- **RAM**: 32GB
- **저장공간**: NVMe SSD 200GB 이상

## 5. 실시간 CCTV 추론을 위한 하드웨어 요구사항

### 5.1 4대 1920×1080 CCTV 동시 처리 사양

#### 최소 사양 (15-20 FPS)
- **GPU**: RTX 3070 (8GB VRAM) 이상
- **CPU**: Intel i7-10700K / AMD Ryzen 7 3700X
- **RAM**: 32GB DDR4
- **저장공간**: NVMe SSD 500GB (녹화 시)

#### 권장 사양 (30 FPS 안정)
- **GPU**: RTX 4070 (12GB VRAM) 이상
- **CPU**: Intel i7-12700K / AMD Ryzen 7 5800X
- **RAM**: 64GB DDR4
- **저장공간**: NVMe SSD 1TB 이상

#### 고성능 사양 (60 FPS)
- **GPU**: RTX 4080 (16GB VRAM) 이상
- **CPU**: Intel i9-12900K / AMD Ryzen 9 5900X
- **RAM**: 64GB DDR4
- **네트워크**: 기가비트 이더넷

### 5.2 성능 최적화 고려사항
- **배치 처리**: 4개 스트림을 배치로 묶어 GPU 효율성 향상
- **멀티스레딩**: CPU 코어 활용한 전후처리 병렬화
- **메모리 관리**: VRAM 부족 시 모델 크기 조정 (YOLOv8n → YOLOv8s)

## 6. 구현 단계별 가이드

### 6.1 데이터 준비
1. **데이터 수집**: 200장 이상 이미지 확보
2. **라벨링**: YOLO 형식 (클래스 x_center y_center width height)
3. **데이터 분할**: Train(70%), Validation(20%), Test(10%)
4. **데이터 증강**: 회전, 크기 조정, 밝기 변경 등

### 6.2 학습 과정
```python
# 기본 학습 코드 예시
from ultralytics import YOLO

# 모델 로드 (전이 학습)
model = YOLO('yolov8n.pt')  # nano 모델로 시작

# 학습 수행
results = model.train(
    data='path/to/dataset.yaml',  # 데이터셋 설정 파일
    epochs=100,                   # 학습 횟수
    imgsz=640,                   # 입력 이미지 크기
    batch=16,                    # 배치 크기 (GPU 메모리에 따라 조정)
    device=0                     # GPU 사용
)
```

### 6.3 실시간 추론
```python
# CCTV 다중 스트림 처리 예시
import cv2
from ultralytics import YOLO
import threading

model = YOLO('best.pt')  # 학습된 모델

def process_stream(stream_url, stream_id):
    cap = cv2.VideoCapture(stream_url)
    while True:
        ret, frame = cap.read()
        if ret:
            results = model(frame, verbose=False)
            # 결과 처리 및 표시
            annotated_frame = results[0].plot()
            cv2.imshow(f'Stream {stream_id}', annotated_frame)
```

## 7. 추가 고려사항

### 7.1 성능 최적화
- **TensorRT**: NVIDIA GPU에서 추론 속도 2-3배 향상
- **ONNX 변환**: 다양한 플랫폼 호환성
- **양자화**: 모델 크기 및 추론 시간 단축
- **모델 경량화**: YOLOv8n(nano) 버전 사용 고려

### 7.2 운영 환경 고려사항
- **네트워크 대역폭**: 4개 스트림 처리 시 충분한 네트워크 용량 확보
- **전력 소비**: 24시간 운영 시 전력 효율성 고려
- **온도 관리**: 연속 운영 시 적절한 냉각 시스템 필요
- **백업 및 복구**: 시스템 장애 대비 이중화 구성


### 7.3 정확도 향상 방안
- **데이터 품질**: 다양한 조건(조명, 각도, 날씨)의 이미지 수집
- **하이퍼파라미터 튜닝**: Learning rate, batch size 등 최적화
- **오차 보정 및 튜닝**: 학습 후 Validation/Test 결과를 바탕으로 오차가 큰 클래스나 상황에 대해 추가 데이터 확보, 하이퍼파라미터 재조정, 모델 구조 변경 등 반복적인 튜닝 과정 필요
- **앙상블**: 여러 모델 결과 조합으로 정확도 향상
- **Active Learning**: 성능이 떨어지는 케이스를 점진적으로 학습

