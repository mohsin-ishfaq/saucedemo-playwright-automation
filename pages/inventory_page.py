from playwright.sync_api import Page


class InventoryPage:
    """Page object for the SauceDemo products / inventory page."""

    BACKPACK_ADD_BUTTON = '[data-test="add-to-cart-sauce-labs-backpack"]'
    BACKPACK_REMOVE_BUTTON = '[data-test="remove-sauce-labs-backpack"]'

    def __init__(self, page: Page):
        self.page = page

    def add_backpack_to_cart(self):
        """Add Sauce Labs Backpack to the cart."""
        self.page.click(self.BACKPACK_ADD_BUTTON)

    def remove_backpack(self):
        """Remove Sauce Labs Backpack from the cart on the products page."""
        self.page.click(self.BACKPACK_REMOVE_BUTTON)

    def get_cart_count(self) -> str:
        """Return the cart badge count as a string."""
        return self.page.locator(".shopping_cart_badge").inner_text()

    def sort_by_price_low_to_high(self):
        """Sort products by price from low to high."""
        self.page.select_option('[data-test="product-sort-container"]', "lohi")
