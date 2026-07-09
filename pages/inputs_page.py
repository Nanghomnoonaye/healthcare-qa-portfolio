"""Page object for the numeric input field.

Used to model data-integrity / boundary-value checks on a clinical numeric
field (e.g. a CGM blood-glucose reading entered by a user).
"""
from playwright.sync_api import Page
from .base_page import BasePage


class InputsPage(BasePage):
    PATH = "/inputs"

    def __init__(self, page: Page):
        super().__init__(page)
        self.number_input = page.locator("input[type='number']")

    def load(self) -> "InputsPage":
        self.open(self.PATH)
        return self

    def enter_value(self, value: str) -> "InputsPage":
        self.number_input.fill(str(value))
        return self

    def press_up_arrow(self, times: int = 1) -> "InputsPage":
        for _ in range(times):
            self.number_input.press("ArrowUp")
        return self

    @property
    def current_value(self) -> str:
        return self.number_input.input_value()
