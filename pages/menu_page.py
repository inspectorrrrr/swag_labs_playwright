from playwright.sync_api import Page

class MenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.locator('#react-burger-menu-btn')
        self.logout_link = page.locator('#logout_sidebar_link')

    def open_menu(self): # Открывает боковое меню
        self.menu_button.click()

    def logout(self): # Выполняет выход из учетной записи
        self.open_menu()
        self.logout_link.click()
        