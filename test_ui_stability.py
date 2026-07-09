"""UI-stability tests.

Verifies that key layout containers render reliably and that locators are
scoped to avoid Playwright strict-mode ambiguity on pages with repeated
elements (a common source of flaky UI tests).
"""
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_main_content_container_is_visible(dynamic_content_page):
    """The primary content region renders on load."""
    expect(dynamic_content_page.content).to_be_visible()


@pytest.mark.ui
def test_content_has_expected_rows(dynamic_content_page):
    """The dynamic content area renders its expected set of rows."""
    assert dynamic_content_page.row_count() >= 1


@pytest.mark.ui
def test_scoped_locator_avoids_strict_mode_conflict(dynamic_content_page):
    """A scoped locator resolves to exactly one element (no strict-mode error)."""
    expect(dynamic_content_page.content).to_have_count(1)


@pytest.mark.ui
def test_page_title_is_correct(dynamic_content_page):
    """The page loads the expected document, guarding against bad redirects."""
    assert "The Internet" in dynamic_content_page.title
