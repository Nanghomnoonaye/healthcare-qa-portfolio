"""Base page object with shared navigation helpers.

All page objects inherit from BasePage so common behaviour (navigation,
waiting) lives in one place instead of being copy-pasted across tests.
"""
from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "") -> None:
        """Navigate to a path relative to the application base URL."""
        self.page.goto(f"{self.BASE_URL}{path}")

    @property
    def title(self) -> str:
        return self.page.title()
