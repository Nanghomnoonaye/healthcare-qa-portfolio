# Healthcare / Fintech UI QA Automation Portfolio

![Tests](https://github.com/Nanghomnoonaye/healthcare-qa-portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Pytest-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal QA automation portfolio demonstrating end-to-end UI testing with
**Python, Playwright, and Pytest**, using the Page Object Model, CI, HTML
reporting, and a written defect log.

> **Honest scope:** tests run against
> [`the-internet.herokuapp.com`](https://the-internet.herokuapp.com), a public
> practice application. The scenarios are *framed* around health-tech / fintech
> workflows (secure login, clinical numeric-data validation, layout stability)
> to show how I would approach testing in a regulated product — not to imply
> access to a real medical system.

---

## What this project demonstrates

- **Test design:** positive, negative, and edge/boundary cases — not just happy paths.
- **Page Object Model:** locators and page behaviour live in `pages/`, so a UI change is fixed once.
- **Fixtures & hooks:** shared setup in `conftest.py`, with an automatic screenshot on any failure.
- **Boundary Value Analysis (BVA):** systematic checks on a numeric clinical field.
- **Defect reporting:** findings written up as proper bug tickets in [`docs/BUG_REPORTS.md`](docs/BUG_REPORTS.md).
- **CI:** every push runs the suite via GitHub Actions and publishes an HTML report artifact.

---

## Test coverage

| Area | File | What it checks |
|------|------|----------------|
| Authentication | `tests/test_authentication.py` | Valid login, invalid password, unknown user, blank/partial credentials (parametrized), logout |
| Data integrity (BVA) | `tests/test_data_integrity.py` | Negative values, out-of-range max, decimals, step increments, non-numeric rejection |
| UI stability | `tests/test_ui_stability.py` | Content renders, expected rows, scoped locator avoids strict-mode conflict, correct page title |

Run a subset by marker, e.g. `pytest -m auth` or `pytest -m data_integrity`.

---

## Getting started

```bash
# 1. Clone
git clone https://github.com/Nanghomnoonaye/healthcare-qa-portfolio.git
cd healthcare-qa-portfolio

# 2. Install dependencies
pip install -r requirements.txt
python -m playwright install chromium

# 3. Run the suite
pytest

# 4. Run with an HTML report
pytest --html=report.html --self-contained-html
```

---

## Project structure

```
healthcare-qa-portfolio/
├── .github/workflows/tests.yml   # CI: runs the suite on every push
├── pages/                        # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inputs_page.py
│   └── dynamic_content_page.py
├── tests/                        # Test suite (grouped by feature)
│   ├── test_authentication.py
│   ├── test_data_integrity.py
│   └── test_ui_stability.py
├── docs/BUG_REPORTS.md           # Sample defect tickets
├── conftest.py                   # Fixtures + screenshot-on-failure hook
├── pytest.ini                    # Markers and default options
└── requirements.txt
```

---

## Roadmap

- Add a parallel JavaScript/Playwright example to show cross-language coverage.
- Add visual-regression snapshots.
- Add cross-browser runs (Firefox + WebKit) in the CI matrix.
