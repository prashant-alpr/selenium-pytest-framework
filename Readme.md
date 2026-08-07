# Selenium-Pytest Event Booking Automation Framework

[![Selenium Pytest Event Booking Tests](https://github.com/prashant-alpr/selenium-pytest-framework/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/prashant-alpr/selenium-pytest-framework/actions/workflows/selenium-tests.yml)
![Python 3.12.0](https://img.shields.io/badge/python-3.12.0-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-v4.46.0-green.svg)
![Pytest](https://img.shields.io/badge/pytest-v9.1.1-green.svg)

An enterprise-grade cross browser End-to-End (E2E) automation framework built with **Python, Selenium and Pytest**, demonstrating advanced web automation patterns against a highly dynamic Event booking platform (https://eventhub.rahulshettyacademy.com/login). 

## 🏗️ Architecture & Technical Highlights

This project is structured using a strict **Page Object Model (POM)** and showcases solutions to common complex automation challenges:

* **Page Object Model (POM):** Clean separation of page locators, interactions, and test logic for high maintainability.
* **Robust Synchronization:** Zero hardcoded `time.sleep()` calls; utilizes custom `WebDriverWait` wrapper utilities to eliminate test flakiness.
* **Step-by-Step Execution Logging:** Automatically captures timestamped interaction logs (`click`, `type_text`, `navigation`) and attaches them directly into HTML test execution reports.
* **Failure Screenshots:** Automatically captures and attaches browser screenshots on test assertions/failures.
* **Cross-Browser & Headless Execution:** Configurable CLI flags for running on Chrome and Firefox in headed or headless modes.
* **Automated CI/CD:** Integrated GitHub Actions workflow running on pushes, pull requests, and scheduled nightly builds with HTML artifact deployment.

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.12.0+
* **Core Library:** Selenium WebDriver 4
* **Test Runner:** Pytest
* **Driver Management:** `webdriver-manager`
* **Reporting:** `pytest-html`
* **CI/CD:** GitHub Actions

## 📂 Project Structure

```text
amazon_automation/
├── conftest.py                        # Centralized environment configs & base URLs
├── data /
│   └── event_details.py               # Event details data
├── locators /
│   ├── login_page_locators.py         # Login page locators
│   ├── home_page_locators.py          # Home page locators
│   └── event_booked_page_locators.py  # Event booked page locators
├── pages/
│   ├── base_page.py                   # Robust Explicit Wait wrappers, step logging and common utilities.
│   ├── login_page.py                  # Login to the Events portal
│   ├── home_page.py                   # Search and book for event
│   └── event_booked_page.py           # Viewing the booked event details
├── tests/
│   └── test_events.py                 # E2E test execution flow
├── results                            # Test Results html report
├── pytest.ini                         # Pytest execution command, markers and logging config
└── README.md