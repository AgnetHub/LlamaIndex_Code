# 📘 LlamaIndex 기반 RAG & AI Agent 실습 코드

이 저장소는 책에서 다루는 **RAG(Retrieval-Augmented Generation) 시스템과 AI Agent 구현** 예제 코드를 제공합니다.  
LlamaIndex를 중심으로 다양한 검색 기법, 멀티모달 처리, 에이전트 활용까지 단계별로 학습할 수 있도록 구성되어 있습니다.  

---

## 🚀 프로젝트 개요
- **목적**: LlamaIndex를 활용한 RAG 시스템 및 AI Agent 구축 학습  
- **특징**:
  - 단계별 학습 구조
  - 실습 위주 예제 코드 제공
  - 최신 LLM & Embedding 모델 활용(OpenAI, Claude, Gemini, Cohere 등)

---

## 📂 챕터별 구성
- **ch02**: LlamaIndex 기초 (파이프라인, 데이터 로드, 임베딩, 벡터DB, 쿼리)  
- **ch03**: Advanced RAG – 희소/밀집 검색, 리랭크, 멀티쿼리, 가상문서 임베딩  
- **ch04**: LLM 및 Embedding 모델 (OpenAI, Claude, Gemini, Cohere 등)  
- **ch05**: 멀티모달 RAG – 이미지, 표, 복잡한 PDF 문서 처리  
- **ch06**: 생각하고 판단하는 ReAct Agent 구현  
- **ch07**: Function Calling Agent – 즉시 함수 호출 기반 에이전트  

---

## 📥 설치 및 환경 설정

### 1. 저장소 클론
```bash
git clone https://github.com/AgnetHub/LlamaIndex_Code.git
cd LlamaIndex_Code
```

### 2. uv 활용 환경 세팅 (권장-최신 방법)
uv는 초고속 Python 패키지 관리 도구입니다.

```bash
# uv 설치 (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# uv 초기화
uv init
```

```bash
# uv 파이썬 버전 3.10.7으로 설정 (실습 시 의존성 이슈 해결)
uv python pin 3.10.7
(Get-Content pyproject.toml) -replace 'requires-python = ".*"', 'requires-python = ">=3.10.7"' | Set-Content pyproject.toml
```

```bash
# 가상환경 생성 및 활성화
uv venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
```

```bash
# 의존성 설치
uv pip install -r requirements.txt
```

```bash
# 이후 기존 코드의 pip 명령어를 실행시키기 위한 pip.exe 별도 설치
python.exe -m ensurepip --default-pip
# pip 최신 버전으로 업그레이드
python.exe -m pip install --upgrade pip
```

### 3. pip 활용 환경 세팅 (대안-책에서 소개한 내용)

```bash
# 가상환경 생성 및 활성화
python -m venv LlamaIndex_VENV
source LlamaIndex_VENV/bin/activate   # (Windows: LlamaIndex_VENV\Scripts\activate)
````

```bash
# 의존성 설치
pip install -r requirements.txt
````

* **환경 변수 설정**: `example.env` 파일을 `.env`로 수정 후 OpenAI API Key 등 필요한 설정 입력
* **예제 실행 방법**: 각 챕터 디렉토리 안의 Jupyter Notebook 또는 Python 스크립트 실행

---

## 🙌 기여 & 문의

* PR, Issue를 통한 피드백 환영
* 학습 중 발견한 개선점이나 버그는 자유롭게 남겨주세요!
