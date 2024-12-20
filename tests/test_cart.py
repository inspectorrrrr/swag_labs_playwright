from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_add_to_cart(browser, login_page): # Тест добавления товаров в корзину
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.add_items_to_cart(3)
    assert inventory_page.get_cart_items_count() == 3

def test_add_to_cart_with_price_validation(browser, login_page): # тест добавления товаров в корзину с проверкой количества и суммы
    # Вход в систему
    login_page.login("standard_user", "secret_sauce")
    
    # Создаем страницу инвентаря
    inventory_page = InventoryPage(browser)
    
    # Получаем список товаров перед добавлением
    item_names = browser.locator('.inventory_item_name').all()
    item_prices = browser.locator('.inventory_item_price').all()
    
    # Массивы для хранения данных о добавленных товарах
    added_names = []
    added_prices = []
    
    # Добавляем первые 3 товара
    for i in range(3):
        # Запоминаем название и цену
        added_names.append(item_names[i].text_content())
        added_prices.append(float(item_prices[i].text_content().replace('$', '')))
        
        # Добавляем в корзину
        inventory_page.add_to_cart_buttons.nth(i).click()
    
    # Проверяем количество товаров в корзине
    assert inventory_page.get_cart_items_count() == 3, "Неверное количество товаров в корзине"
    
    # Переходим в корзину
    inventory_page.cart_link.click()

    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_info("Qwerty", "Asdfgh", "123456")
    
    # Проверяем товары в корзине
    cart_items = browser.locator('.cart_item')
    
    # Проверяем, что добавленные товары совпадают
    for i in range(3):
        # Проверяем название
        assert added_names[i] in cart_items.nth(i).locator('.inventory_item_name').text_content(), \
            f"Название товара {i+1} не совпадает"
        
        # Проверяем цену
        item_price = float(cart_items.nth(i).locator('.inventory_item_price').text_content().replace('$', ''))
        assert item_price == added_prices[i], f"Цена товара {i+1} не совпадает"
    
    # Проверка общей суммы
    total_prices = sum(added_prices)
    cart_total = float(browser.locator('[data-test=\"total-label\"]').text_content().replace('Total: $', ''))
    tax_total = float(browser.locator('[data-test=\"tax-label\"]').text_content().replace('Tax: $', ''))
    assert abs(total_prices + tax_total - cart_total) < 0.01, "Общая сумма товаров не совпадает"