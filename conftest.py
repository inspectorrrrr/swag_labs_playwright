import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(params=["chromium", "firefox"]) # Фикстура для параметризации браузеров
def browser(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(browser): # Фикстура для создания страницы логина
    browser.goto("https://www.saucedemo.com/")
    return LoginPage(browser)
