import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def browser():
    """Launch a Chromium browser for the test session."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Provide a fresh page with the SauceDemo base URL."""
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    yield page
    context.close()
