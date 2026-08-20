# 🧪 QA Automation Portfolio — automationexercise.com

## 📌 Overview
I'm a junior QA with zero professional experience, learning by doing.
This project is my first attempt at building the full QA workflow from scratch —
designing test cases, automating them, finding real bugs, and writing it all down —
using a public e-commerce demo site as the target.

Everything here was built and tested in about 10 days, hands-on, with a lot of
trial and error along the way (see "What I Learned" below for the honest version).

## 🛠️ Tech Stack
Python 3.12 · Selenium · pytest · requests

## 🌐 Target Site
[automationexercise.com](https://automationexercise.com) — a demo e-commerce site
made for automation practice, with both UI and API endpoints.

## 📊 Test Coverage

### 🖥️ UI Automation (Selenium + POM)
| Feature | TC Count | Passed |
|---|---:|---:|
| Signup | 4 | 4 |
| Login / Logout | 8 | 8 |
| Product Search | 9 | 9 |
| **Total** | **21** | **21** |

### 🔌 API Automation (requests)
| Endpoint | TC Count | Passed |
|---|---:|---:|
| Products List | 2 | 2 |
| Search Product | 2 | 2 |
| Verify Login | 3 | 3 |
| **Total** | **7** | **7** |

## 📁 Project Structure
```text
qa-automation-portfolio/
├── docs/
│   ├── test-plan.md
│   ├── test-cases.xlsx
│   └── bug-reports.md
├── tests/
│   ├── ui/
│   │   ├── pages/
│   │   │   ├── login_page.py
│   │   │   ├── signup_page.py
│   │   │   └── search_page.py
│   │   ├── test_login.py
│   │   ├── test_signup.py
│   │   └── test_search.py
│   └── api/
│       ├── test_products_api.py
│       ├── test_search_api.py
│       └── test_login_api.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# UI tests
pytest tests/ui/

# API tests
pytest tests/api/
```

## 🧩 Design Techniques Used
- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table

## 🐛 Key Findings
While testing, I found a few real issues — mostly around weak input validation
(no password length limit, loose email format check, etc.) and a mismatch between
the official API docs and how the server actually responds.
Full list here: [docs/bug-reports.md](./docs/bug-reports.md)

## 📚 What I Learned
This was my first real automation project, so I ran into (and fixed) a lot of things:
- How to structure UI tests with Page Object Model instead of copy-pasting code everywhere
- Why "it works when I watch it but fails in pytest" usually means a timing issue,
  not a broken locator
- Ad overlays and duplicate `name` attributes can silently break your tests —
  learned to debug both the hard way
- Writing API tests with `requests` and checking real server behavior instead of
  trusting the docs blindly
- Designing test cases with EP / BVA instead of just guessing random inputs

## 🚀 Next Steps
- Add test cases for cart and checkout
- Set up GitHub Actions to run tests automatically on push

==============================================================================================

# 🧪 QA 자동화 포트폴리오 — automationexercise.com

## 📌 개요
실무 경험은 없지만, 직접 해보며 배우고 있는 신입 QA 엔지니어 정윤희입니다.
본 프로젝트는 공개 이커머스 데모 사이트를 대상으로 테스트 케이스 설계, 자동화 스크립트 구현, 실제 결함 발굴 및 문서화까지 전체 QA 워크플로우를 처음부터 끝까지 구축해 본 첫 결과물입니다.

약 10일 동안 직접 코드를 작성하고 테스트를 수행하였으며, 그 과정에서 겪은 수많은 시행착오와 해결 과정은 아래 "배운 점" 항목에 사실대로 기록해 두었습니다.

## 🛠️ 기술 스택
Python 3.12 · Selenium · pytest · requests

## 🌐 테스트 대상 사이트
[automationexercise.com](https://automationexercise.com) — UI 및 API 엔드포인트를 제공하며, 테스트 자동화 실습을 위해 구축된 이커머스 데모 사이트입니다.

## 📊 테스트 커버리지 (Coverage)

### 🖥️ UI 자동화 (Selenium + POM 적용)
| 기능 | TC 수 | 합격 (Passed) |
|---|---:|---:|
| 회원가입 (Signup) | 4 | 4 |
| 로그인 / 로그아웃 | 8 | 8 |
| 상품 검색 (Product Search) | 9 | 9 |
| **합계** | **21** | **21** |

### 🔌 API 자동화 (requests 활용)
| 엔드포인트 | TC 수 | 합격 (Passed) |
|---|---:|---:|
| 상품 목록 (Products List) | 2 | 2 |
| 상품 검색 (Search Product) | 2 | 2 |
| 로그인 검증 (Verify Login) | 3 | 3 |
| **합계** | **7** | **7** |

## 📁 프로젝트 구조
```text
qa-automation-portfolio/
├── docs/
│   ├── test-plan.md         # 테스트 계획서
│   ├── test-cases.xlsx      # 테스트 케이스 명세서
│   └── bug-reports.md       # 결함 리포트
├── tests/
│   ├── ui/                  # UI 테스트 코어
│   │   ├── pages/           # Page Object Model 패턴 적용
│   │   │   ├── login_page.py
│   │   │   ├── signup_page.py
│   │   │   └── search_page.py
│   │   ├── test_login.py
│   │   ├── test_signup.py
│   │   └── test_search.py
│   └── api/                 # API 테스트 스크립트
│       ├── test_products_api.py
│       ├── test_search_api.py
│       └── test_login_api.py
├── requirements.txt         # 의존성 패키지 목록
└── README.md

## ▶️ 실행방법
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# UI tests
pytest tests/ui/

# API tests
pytest tests/api/
```

## 🧩 적용한 테스트 설계 기법
- 동등 분할 (Equivalence Partitioning)
- 경계값 분석 (Boundary Value Analysis)
- 결정 테이블 (Decision Table)

## 🐛 주요 결함 발굴 성과 (Key Findings)
테스팅을 진행하며 **입력값 검증 미흡(비밀번호 길이 제한 부재, 느슨한 이메일 형식을 허용하는 문제 등)**에 관한 실제 이슈와 **공식 API 문서와 실제 서버 응답 간의 불일치 현상**을 발굴했습니다.
- 상세 내역은 다음 문서에서 확인하실 수 있습니다: [docs/bug-reports.md](./docs/bug-reports.md)

## 📚 배운 점 및 트러블슈팅 (What I Learned)
첫 자동화 프로젝트를 진행하며 직접 직면하고 해결한 기술적 경험들입니다:
- 코드를 일일이 복사/붙여넣기하는 대신 **Page Object Model(POM)** 디자인 패턴을 적용하여 UI 테스트의 재사용성과 유지보수성을 높이는 방법을 체득했습니다.
- "눈으로 볼 땐 잘 작동하는데 pytest 실행 시 실패하는 문제"는 요소 위치의 문제가 아니라 **페이지 로딩 타이밍 이슈**라는 점을 깨닫고 명시적 대기(Explicit Wait) 처리법을 익혔습니다.
- **광고 팝업 오버레이 및 중복된 `name` 속성**으로 인해 테스트가 실패하는 현상을 디버깅하며 프론트엔드 DOM 구조 분석 역량을 키웠습니다.
- API 문서 내용을 맹신하지 않고 `requests` 라이브러리를 사용해 **실제 서버의 데이터 응답 및 상태 코드를 검증하는 습관**을 길렀습니다.
- 단순 추측에 의존하지 않고 **동등분할(EP) 및 경계값 분석(BVA)** 기법을 적용하여 체계적으로 예외 테스트 케이스를 설계했습니다.

## 🚀 향후 개선 계획 (Next Steps)
- 장바구니 및 결제 기능에 대한 테스트 케이스 추가 확장
- GitHub Actions를 연동하여 코드 푸시 시 자동으로 테스트가 실행되는 CI/CD 파이프라인 구축
