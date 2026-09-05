from playwright.sync_api import Page, expect

from pages.cart_checkout_page import CartCheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def _login_and_add_backpack(page: Page):
    """Log in and add one item to the cart."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("/inventory.html")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()


def test_checkout_missing_first_name(page: Page):
    """TC15: Checkout fails when first name is missing."""
    _login_and_add_backpack(page)

    checkout_page = CartCheckoutPage(page)
    checkout_page.go_to_cart()
    checkout_page.checkout("", "Doe", "12345")

    expect(page.locator('[data-test="error"]')).to_contain_text("First Name is required")


def test_complete_happy_path_checkout(page: Page):
    """TC17: Complete checkout from cart to confirmation."""
    _login_and_add_backpack(page)

    checkout_page = CartCheckoutPage(page)
    checkout_page.go_to_cart()
    checkout_page.checkout("John", "Doe", "12345")
    checkout_page.finish_checkout()

    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")
