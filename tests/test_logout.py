from pages.menu_page import MenuPage

def test_login_before_logout(browser, login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in browser.url, "Не удалось войти в систему"

def test_menu_opening(browser, login_page):
    login_page.login("standard_user", "secret_sauce")
    menu_page = MenuPage(browser)
    menu_page.open_menu()
    assert menu_page.logout_link.is_visible(), "Кнопка logout не отображается"

def test_logout_process(browser, login_page):
    login_page.login("standard_user", "secret_sauce")
    menu_page = MenuPage(browser)
    menu_page.logout()
    assert "https://www.saucedemo.com/" in browser.url, "После logout не произошло возврата на страницу входа"

def test_protected_routes_after_logout(browser, login_page):
    login_page.login("standard_user", "secret_sauce")
    menu_page = MenuPage(browser)
    menu_page.logout()
    
    browser.goto("https://www.saucedemo.com/inventory.html")
    assert "Epic sadface: You can only access '/inventory.html' when you are logged in." in login_page.get_error_message(), "/inventory.html" in browser.url