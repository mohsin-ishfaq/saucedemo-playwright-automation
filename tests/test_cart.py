from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def _login_as_standard_user(page: Page):
    """Helper to log in before cart tests."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("/inventory.html")


def test_add_single_item_to_cart(page: Page):
    """TC09: Add Sauce Labs Backpack to the cart."""
    _login_as_standard_user(page)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_remove_item_from_products_page(page: Page):
    """TC11: Remove item from the products page."""
    _login_as_standard_user(page)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    inventory_page.remove_backpack()
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
