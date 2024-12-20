import pytest

TEST_USERS = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "problem_user", "password": "secret_sauce"},
    {"username": "performance_glitch_user", "password": "secret_sauce"},
    {"username": "error_user", "password": "secret_sauce"},
    {"username": "visual_user", "password": "secret_sauce"}
]

@pytest.mark.parametrize("user", TEST_USERS)
def test_successful_login(login_page, user, browser): # Тест успешной аутентификации
    login_page.login(user["username"], user["password"])
    assert "/inventory.html" in browser.url, "Не удалось выполнить вход"

def test_invalid_user_login(login_page, browser): #Тест неудачной аутентификации(username)
    login_page.login("invalid_user", "secret_sauce")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message(), "/inventory.html" in browser.url

def test_invalid_pass_login(login_page, browser): # Тест неудачной аутентификации(password)
    login_page.login("standard_user", "invalid_pass")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message(), "/inventory.html" in browser.url

def test_failed_login(login_page, browser): # Тест неудачной аутентификации(user, pass)
    login_page.login("invalid_user", "invalid_pass")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message(), "/inventory.html" in browser.url

def test_locked_login(login_page, browser): # Тест 'пользователь заблокирован'
    login_page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_message(), "/inventory.html" in browser.url
    