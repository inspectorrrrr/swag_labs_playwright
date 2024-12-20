from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_order(browser, login_page): # Тест оформления заказа
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(browser)
    inventory_page.add_items_to_cart(3)
    inventory_page.cart_link.click()
    
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_info("Qwerty", "Asdfgh", "123456")
    checkout_page.complete_order()
    
    assert "Thank you for your order!" in checkout_page.get_confirmation_message(), "Не удалось выполнить заказ"