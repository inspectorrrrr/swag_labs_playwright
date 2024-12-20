# Автоматизация тестирования интернет-магазина Swag Labs с использованием Playwright и pytest

## 📝 Описание проекта

Этот проект реализует автоматизированное тестирование функциональности интернет-магазина **Swag Labs** (https://www.saucedemo.com/) с использованием Python, Playwright и pytest. Тесты покрывают следующие сценарии:

1. Аутентификация пользователя.  
2. Добавление товаров в корзину.  
3. Оформление заказа.  
4. Выход из учетной записи и проверка недоступности защищённых страниц.  

---

## 🗝️ Основные возможности

- **Аутентификация:**
  - Успешный вход с валидными учетными данными.
  - Проверка отображения ошибок при неверном вводе имени пользователя или пароля.
  - Проверка ошибки для заблокированного пользователя.

- **Корзина:**
  - Добавление товаров в корзину.
  - Проверка количества товаров и суммарной стоимости.

- **Оформление заказа:**
  - Заполнение данных и подтверждение заказа.
  - Проверка сообщения об успешном заказе.

- **Выход из учетной записи:**
  - Проверка корректности процесса выхода.
  - Проверка недоступности защищенных страниц после выхода.

---

## 📚 Технические требования

- Python 3.11+
- Playwright 1.49+
- pytest 8.3+
- pytest-html 4.1+ (для генерации отчетов)

---
## 📂 Структура проекта

```plaintext
swag_labs_playwright/
│
├── tests/
│   ├── test_authentication.py    # Тесты для аутентификации
│   ├── test_cart.py              # Тесты корзины
│   ├── test_checkout.py          # Тесты оформления заказа
│   ├── test_logout.py            # Тесты выхода из системы
│
├── pages/
│   ├── login_page.py             # Страница логина
│   ├── inventory_page.py         # Страница инвентаря
│   ├── cart_page.py              # Страница корзины
│   ├── checkout_page.py          # Страница оформления заказа
│   ├── menu_page.py              # Меню
│     
├── conftest.py                   # Конфигурация и фикстуры
├── pytest.ini                    # Файл конфигурации
├── requirements.txt              # Управление зависимостями
└── README.md                     # Документация проекта
```

---
## 📦 Установка

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/inspectorrrrr/swag_labs_playwright.git
   cd swag_labs_playwright
   ```

2. **Создание виртуального окружения**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/MacOS
   venv\Scripts\activate       # Windows
   ```

3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Установка Playwright**:
    ```bash
    playwright install
    ```

## 🚀 Запуск тестов

### Запуск всех тестов:
```bash
pytest
```

### Запуск конкретного теста:
```bash
pytest tests/test_authentication.py
pytest tests/test_cart.py
pytest tests/test_checkout.py
pytest tests/test_logout.py
```


## 📑 Тестовые данные
В проекте используются следующие тестовые аккаунты:
- standard_user
- locked_out_user
- problem_user
- performance_glitch_user
- error_user
- visual_user

Пароль для всех аккаунтов: `secret_sauce`

---

## 📊 Отчеты о тестах

Проект генерирует HTML-отчеты, содержащие:
- Сводку выполнения тестов
- Подробные результаты тестов
- Время выполнения
- Сообщения об ошибках

После выполнения команды отчет будет доступен в файле `report.html`. Отчет включает информацию о всех тестах, их статусе, продолжительности и ошибках (если они были).

---
