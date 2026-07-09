"""Shared pytest fixtures and hooks.

Provides page objects to tests and captures a screenshot automatically when a
test fails, so failures are easy to triage from the artifacts folder / CI run.
"""
import os
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inputs_page import InputsPage
from pages.dynamic_content_page import DynamicContentPage

SCREENSHOT_DIR = "screenshots"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page).load()


@pytest.fixture
def inputs_page(page: Page) -> InputsPage:
    return InputsPage(page).load()


@pytest.fixture
def dynamic_content_page(page: Page) -> DynamicContentPage:
    return DynamicContentPage(page).load()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach a screenshot to the report when a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            try:
                page.screenshot(path=path, full_page=True)
                print(f"\n[QA] Failure screenshot saved: {path}")
            except Exception as exc:  # pragma: no cover - best effort only
                print(f"\n[QA] Could not capture screenshot: {exc}")
