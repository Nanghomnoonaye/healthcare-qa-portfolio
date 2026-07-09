# Healthcare & Fintech UI QA Automation Suite

A robust, automated end-to-end (E2E) testing framework built with **Python**, **Playwright**, and **Pytest**. This suite simulates real-world clinical and fintech workflows, implementing strict edge-case validation and resolving strict-mode visual regressions to demonstrate production-grade quality assurance.

---

## 🧪 Core Test Scenarios Covered

* **Secure Portal Authentication:** Validates session initiation, secure boundaries, and successful landing on encrypted medical/financial dashboards.
* **Data Integrity & Boundary Value Analysis (BVA):** Implements BVA on numeric form fields (e.g., medical device/CGM data logs) to guarantee that the UI layer correctly catches or flags invalid negative values before data processing.
* **Layout Stability & Locator Ambiguity Fixes:** Targets dynamic, fast-moving layouts by utilizing explicit CSS hierarchy constraints (`.example #content`) to eliminate strict-mode locator conflicts and ensure reliable, visual-ready rendering.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.9+
* **Automation Engine:** Playwright (Chromium)
* **Test Runner:** Pytest
* **Design Paradigm:** Hierarchy-Based Locators & Functional Boundary Testing

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3 installed on your machine.

### Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Nanghomnoonaye/healthcare-qa-portfolio.git](https://github.com/Nanghomnoonaye/healthcare-qa-portfolio.git)
   cd healthcare-qa-portfolio
