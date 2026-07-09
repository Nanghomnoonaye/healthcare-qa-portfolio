"""Page object for the dynamic-content layout.

Used for UI-stability checks: verifying the main content container renders and
that scoped locators avoid Playwright strict-mode ambiguity on repeated rows.
"""
from playwright.sync_api import Page
from .base_page import BasePage


class DynamicContentPage(BasePage):
    PATH = "/dynamic_content"

    def __init__(self, page: Page):
        super().__init__(page)
        # Scoped to `.example` to avoid strict-mode conflicts with other #content.
        self.content = page.locator(".example #content")
        self.rows = page.locator(".example .row")

    def load(self) -> "DynamicContentPage":
        self.open(self.PATH)
        return self

    def row_count(self) -> int:
        return self.rows.count()
