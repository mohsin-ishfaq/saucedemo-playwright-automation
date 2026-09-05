from playwright.sync_api import Page


class LoginPage:
    """Page object for the SauceDemo login screen."""

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """Navigate to the login page."""
        self.page.goto("/")

    def login(self, username: str, password: str):
        """Fill credentials and submit the login form."""
        self.page.fill('[data-test="username"]', username)
        self.page.fill('[data-test="password"]', password)
        self.page.click('[data-test="login-button"]')

    def get_error_message(self) -> str:
        """Return the login error message text."""
        return self.page.locator('[data-test="error"]').inner_text()
