from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_buttons = page.locator('.btn_inventory')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.cart_link = page.locator('.shopping_cart_link')

    def add_items_to_cart(self, num_items: int = 3): # Добавляет указанное количество товаров(num_items) в корзину
        for i in range(min(num_items, len(self.add_to_cart_buttons.all()))):
            self.add_to_cart_buttons.nth(i).click()

    def get_cart_items_count(self) -> int: # Получает количество товаров в корзине
        return int(self.cart_badge.text_content() or 0)
    