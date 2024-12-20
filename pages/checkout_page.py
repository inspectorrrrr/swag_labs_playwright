from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('#first-name')
        self.last_name_input = page.locator('#last-name')
        self.postal_code_input = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.finish_button = page.locator('#finish')
        self.confirmation_message = page.locator('.complete-header')

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str): # Заполнение информации для оформления заказа
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def complete_order(self): # Завершение оформления заказа
        self.finish_button.click()

    def get_confirmation_message(self) -> str: # Получение сообщения о подтверждении заказа
        return self.confirmation_message.text_content() or ""
