# Healthcare QA Automation Suite

A robust, automated end-to-end (E2E) testing framework built with **Python**, **Playwright**, and **Pytest**. This suite simulates real-world clinical workflows and critical data integrity checks to demonstrate enterprise-grade quality assurance practices in the healthcare technology domain.

---

## 🧪 Core Test Scenarios Covered

* **Clinical Portal Authentication:** Validates secure session initiation, user boundary limits, and successful landing on encrypted medical dashboards.
* **Continuous Glucose Monitor (CGM) Data Integrity:** Implements boundary value analysis (BVA) on number fields to ensure the UI layer successfully intercepts or flags invalid negative clinical data inputs (preventing dangerous calculation errors).
* **UI Responsiveness & Layout Stability:** Verifies core diagnostic visual frames render consistently without strict-mode locator ambiguities.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.9+
* **Automation Engine:** Playwright (Chromium)
* **Test Runner:** Pytest
* **Design Paradigm:** Core Functional Verification & Hierarchy-Based Locators

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3 installed on your machine.

### Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Nanghomnoonaye/healthcare-qa-portfolio.git](https://github.com/Nanghomnoonaye/healthcare-qa-portfolio.git)
   cd healthcare-qa-portfolio
