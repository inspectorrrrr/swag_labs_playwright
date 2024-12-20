from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator('#checkout')
        self.cart_items = page.locator('.cart_item')

    def proceed_to_checkout(self): #Переход к оформлению заказа
        self.checkout_button.click()
        