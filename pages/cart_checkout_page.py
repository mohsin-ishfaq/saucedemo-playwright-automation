from playwright.sync_api import Page


class CartCheckoutPage:
    """Page object for cart and checkout flows."""

    def __init__(self, page: Page):
        self.page = page

    def go_to_cart(self):
        """Open the shopping cart."""
        self.page.click('[data-test="shopping-cart-link"]')

    def checkout(self, first: str, last: str, zip_code: str):
        """Start checkout and fill customer information."""
        self.page.click('[data-test="checkout"]')
        self.page.fill('[data-test="firstName"]', first)
        self.page.fill('[data-test="lastName"]', last)
        self.page.fill('[data-test="postalCode"]', zip_code)
        self.page.click('[data-test="continue"]')

    def finish_checkout(self):
        """Complete the checkout on the overview page."""
        self.page.click('[data-test="finish"]')

    def get_thankyou_message(self) -> str:
        """Return the order confirmation header text."""
        return self.page.locator('[data-test="complete-header"]').inner_text()

    def get_checkout_error(self) -> str:
        """Return validation error shown on the checkout info step."""
        return self.page.locator('[data-test="error"]').inner_text()
