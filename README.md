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
