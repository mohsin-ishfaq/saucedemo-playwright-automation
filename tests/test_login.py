from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_valid_login(page: Page):
    """TC01: Valid login with standard_user."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("/inventory.html")


def test_locked_out_user_error(page: Page):
    """TC03: Locked out user shows an error message."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Sorry, this user has been locked out."
    )
