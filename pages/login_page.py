from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('.error-message-container')

    def login(self, username: str, password: str): # Выполняет вход в систему с указанными credentials
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str: # Получает текст сообщения об ошибке
        return self.error_message.text_content() or ""
    