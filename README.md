# SauceDemo E2E Automation – Playwright Python + PyTest | POM Framework

Automated end-to-end testing for **SauceDemo** e-commerce demo – built with Playwright Python (Sync API) + PyTest + Page Object Model.

> **Live Site:** https://www.saucedemo.com | **Author:** Mohsin Ishfaq – Senior QA Engineer

### 🟢 Execution Results
- **6 Tests Automated | 6 Passed | 0 Failed**
- **Framework:** POM + Fixtures + pytest-html Reports + Video Recording

---

### 📁 Project Structure
saucedemo-playwright-automation/
├── pages/               # Page Object Model
├── tests/               # Test Cases (6 tests)
├── reports/             # HTML Reports
├── Screenshots/         # Execution Proof
├── Videos/              # Test Run Recording
├── conftest.py
├── pytest.ini
└── requirements.txt

### 🧪 Test Coverage – 6 Test Cases

| ID | Test |
|----|------|
| TC01 | Valid login with standard_user |
| TC03 | Locked out user error |
| TC09 | Add single item to cart (Backpack) |
| TC11 | Remove item from products page |
| TC15 | Checkout with missing first name |
| TC17 | Complete happy path checkout |

### 🛠️ Tech Stack
- Python 3.11, Playwright Sync API, PyTest, pytest-html, Page Object Model

### ⚙️ Setup & Run
pip install -r requirements.txt
playwright install
pytest -v --html=reports/report.html --self-contained-html --video=on

### 📸 Screenshots & Video Proof
Check /Screenshots and /Videos folders

### 🔑 Credentials
- Valid: standard_user / secret_sauce
- Locked: locked_out_user / secret_sauce

### 👨‍💻 Author
Mohsin Ishfaq - Senior QA Engineer | Manual, Automation, API, DB, Performance, Security
GitHub: github.com/mohsin-ishfaq
