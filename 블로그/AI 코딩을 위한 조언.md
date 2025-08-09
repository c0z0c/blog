---
layout: default
title: "AI 코딩을 위한 조언"
date: 2025-08-09
category: "블로그"
description: ""
---

# AI 코딩을 위한 조언

## 1. 💡 기본 틀(Basic Scaffolding) 작성하기

- 📝 초안 작성에 집중하기
    - 코드가 당장 동작하지 않아도 괜찮습니다.
    - 오타나 불완전한 논리가 있어도 AI와 함께 다듬으면 됩니다.
- 🚀 빠른 1차 완성 예제
    
    python
    
    `# main.py
    
    def fetch_data(source):
        # TODO: 데이터 소스에 맞게 요청 로직 구현
        pass
    
    def process_data(data):
        # TODO: 데이터 전처리 로직 작성
        pass
    
    def save_results(results, filepath):
        # TODO: 결과를 파일로 저장하는 코드 작성
        pass
    
    if __name__ == "__main__":
        raw = fetch_data("https://api.example.com/data")
        processed = process_data(raw)
        save_results(processed, "output.json")`
    
    1차적으로 함수 시그니처와 전체 흐름을 잡아두고, 자세한 로직은 TODO로 남깁니다.
    

## 2. 🐛 오류 수정(Debugging)은 AI에게 맡기기

- 📩 오류 메시지 전송
    - 발생한 에러 전체를 복사·붙여넣기 하세요.
- 🔎 원인 분석 & 해결책 제시 예제
    
    python
    
    `# 에러 발생 코드
    nums = [1, 2, 3]
    print(nums[5])`
    
    `IndexError: list index out of range`
    
    → AI에 “위 IndexError를 해결하려면 어떻게 수정해야 하나요?”라고 요청
    
- 🎯 수정 후 예시
    
    python
    
    `nums = [1, 2, 3]
    index = 5
    
    if index < len(nums):
        print(nums[index])
    else:
        print(f"Index {index} is out of range.")`
    

## 3. 🎨 세부 조정 & 최적화

- ✏️ TODO 주석 활용
    - “# TODO: 짝수만 필터링”과 같이 원하는 변경 사항을 명확히 남깁니다.
- 🤝 AI에게 TODO 검토 요청
“이 TODO를 반영해 코드 수정해줘”라고 하면, AI가 아래처럼 완성해 줍니다.
- ⚙️ 수정 전/후 비교 예시
    
    python
    
    `# 수정 전
    def filter_even(numbers):
        # TODO: 짝수만 필터링
        return numbers`
    
    python
    
    `# AI가 수정해준 코드
    def filter_even(numbers):
        return [n for n in numbers if n % 2 == 0]`
    

## AI 활용 시 주의사항

- ⚠️ "이렇게 해줘"만으로는 부족할 수 있음
    - AI가 맥락 없이 단순 요청만으로 정확한 결과를 내기란 어렵습니다.
    - 특히 복잡하거나 다단계 로직일 경우, 요청 내용이 구체적이지 않으면 잘못된 코드가 생성될 가능성이 높습니다.
- 📌 API나 함수 목록을 제공하세요
    - 예를 들어, 아래처럼 필요한 API나 사용하고자 하는 클래스 이름을 명확하게 전달하면 훨씬 정확한 결과가 나옵니다.
    
    python
    
    `# 사용할 주요 API 목록
    # - requests.get
    # - json.loads
    # - pandas.DataFrame`
    
    그런 다음 AI에게 “위 API를 참고해서 XXX 기능을 구현하는 방법을 알려줘” 요청합니다:
    
    가끔 개발 언어를 혼용할 경우 언어를 이야기 해줘야 하는 경우도 있습니다.
    
- 🧠 AI를 ‘설계자’가 아닌 ‘코딩 비서’처럼 활용하세요
    - 로직을 설계하는 주체는 개발자이고, AI는 이를 코드로 구현하는 도구입니다.
    - 따라서 요구사항과 사용 기술 스택(API, 라이브러리 등)을 명확히 전달하는 것이 핵심입니다.