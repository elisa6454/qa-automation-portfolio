# Test Plan — automationexercise.com

## 1. Overview

- **Target site**: [automationexercise.com](https://automationexercise.com) — an e-commerce demo site for practice
- **Automation tools**: Python, Selenium, pytest (Page Object Model)
- **Design techniques**: Equivalence Partitioning, Boundary Value Analysis, Decision Table

## 2. Test Scope and Results

| Feature        | TC Count | Passed | Main Design Techniques                            |
| -------------- | -------- | ------ | ------------------------------------------------- |
| Signup         | 4        | 4      | Equivalence Partitioning                          |
| Login / Logout | 8        | 8      | Equivalence Partitioning, Decision Table          |
| Product Search | 9        | 9      | Equivalence Partitioning, Boundary Value Analysis |
| **Total**      | **21**   | **21** |                                                   |

## 3. Detailed Test Cases

The full test cases (steps, test data, expected results, actual results) are available in the spreadsheet below.

👉 [test-cases.xlsx](./test-cases.xlsx)

## 4. Issues Found

Issues found during testing are documented separately.

👉 [bug-reports.md](./bug-reports.md)

## 5. Automation Code Structure

- `tests/ui/pages/` — Page Object classes (LoginPage, SignupPage, SearchPage)
- `tests/ui/test_*.py` — pytest test functions
- See [README.md](../README.md) for more details on the project structure
