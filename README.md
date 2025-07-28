# Mock API Server

FastAPI 기반의 Mock 서버입니다. 간단한 테스트를 위한 목적으로 제작되었습니다.

---

## 🚀 실행 방법

### 1. 가상환경 설정 (Windows 기준)

```bash
python -m venv venv # 가상환경 생성하기
venv\Scripts\activate #가상환경 실행
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt 
```

### 3. 서버 실행

```bash
uvicorn run:app --reload # 방법1
python run.py # 방법2 
```

## 🔐 인증 토큰
모든 API 요청에는 아래의 인증 헤더가 필요합니다:

```
Authorization: Bearer mock_app_key
```
## 📂 디렉토리 구조

```
app/
├── api/
│   └── v1/
│       ├── endpoints/
│       │   └── user.py
│       └── router.py
├── exceptions/
│   └── error_responses.py
├── mock_data/
│   └── mock_users.py
├── schemas/
│   └── user.py
└── main.py

clean.sh # 캐시 파일 삭제
run.py
requirements.txt
.gitignore
README.md

```
