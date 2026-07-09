"""Page object for the secure-area login flow.

Models the login form used to represent an authenticated clinical/financial
portal. Keeping locators here means a UI change is fixed in one file, not in
every test.
"""
from playwright.sync_api import Page
from .base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    # Valid demo credentials published by the practice application.
    VALID_USER = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")

    def load(self) -> "LoginPage":
        self.open(self.PATH)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        return self

    def login_as_valid_user(self) -> "LoginPage":
        return self.login(self.VALID_USER, self.VALID_PASSWORD)

    @property
    def flash_message(self) -> str:
        return self.flash.inner_text()
