"""Authentication test cases.

Represents access control for a secure clinical/financial portal: a valid
clinician logs in successfully, while invalid credentials must be rejected.
"""
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.auth
def test_valid_login_reaches_secure_area(login_page):
    """A valid user lands in the secure area with a success message."""
    login_page.login_as_valid_user()
    expect(login_page.flash).to_contain_text("You logged into a secure area!")
    expect(login_page.logout_button).to_be_visible()


@pytest.mark.auth
def test_invalid_password_is_rejected(login_page):
    """A valid username with a wrong password must not authenticate."""
    login_page.login(login_page.VALID_USER, "wrong-password")
    expect(login_page.flash).to_contain_text("Your password is invalid!")
    expect(login_page.logout_button).to_have_count(0)


@pytest.mark.auth
def test_unknown_username_is_rejected(login_page):
    """An unknown username must not authenticate."""
    login_page.login("not_a_real_user", login_page.VALID_PASSWORD)
    expect(login_page.flash).to_contain_text("Your username is invalid!")


@pytest.mark.auth
@pytest.mark.parametrize(
    "username, password",
    [
        ("", ""),                       # both blank
        ("tomsmith", ""),               # missing password
        ("", "SuperSecretPassword!"),   # missing username
    ],
)
def test_empty_credentials_are_rejected(login_page, username, password):
    """Blank/partial credentials must never reach the secure area."""
    login_page.login(username, password)
    expect(login_page.flash).to_contain_text("invalid")
    expect(login_page.logout_button).to_have_count(0)


@pytest.mark.auth
def test_logout_ends_session(login_page):
    """After logout the user is returned to the login screen."""
    login_page.login_as_valid_user()
    login_page.logout_button.click()
    expect(login_page.flash).to_contain_text("You logged out of the secure area!")
    expect(login_page.submit_button).to_be_visible()
