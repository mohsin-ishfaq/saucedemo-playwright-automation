# SauceDemo Automation

Simple Playwright + Pytest automation framework for [SauceDemo](https://www.saucedemo.com) using the Page Object Model.

## Tech stack

- Python
- pytest
- Playwright (sync API)
- pytest-html

## Project structure

```
saucedemo-automation/
├── pages/                  # Page Object Model classes
├── tests/                  # Test cases
├── conftest.py             # Browser and page fixtures
├── pytest.ini              # Pytest config and HTML report settings
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest -v --html=reports/report.html
```

The HTML report is generated at `reports/report.html`.

## Test cases

| ID   | Test                                      |
|------|-------------------------------------------|
| TC01 | Valid login with standard_user            |
| TC03 | Locked out user error                     |
| TC09 | Add single item to cart (Backpack)        |
| TC11 | Remove item from products page            |
| TC15 | Checkout with missing first name          |
| TC17 | Complete happy path checkout              |

## Credentials

- Valid user: `standard_user` / `secret_sauce`
- Locked out user: `locked_out_user` / `secret_sauce`
