# API-автотесты (Python + pytest)

Автоматизированные тесты для публичного API [Automation Exercise](https://automationexercise.com/api_list), написанные на Python с использованием библиотек `requests` и `pytest`.

Это автоматизированная версия ручной проверки API: те же эндпоинты и сценарии, что и в Postman-коллекции, реализованные кодом.

## Инструменты

- **Python**
- **requests** — отправка HTTP-запросов
- **pytest** — запуск тестов и формирование отчёта

## Покрытие

7 автотестов на 3 эндпоинта (позитивные и негативные сценарии):

| Тест | Эндпоинт | Сценарий |
|---|---|---|
| test_products_list_status | GET /api/productsList | Статус-код ответа 200 |
| test_products_list_not_empty | GET /api/productsList | Ответ содержит непустой список товаров |
| test_search_product | POST /api/searchProduct | Позитивный: поиск по валидному запросу |
| test_search_product_no_data | POST /api/searchProduct | Негативный: запрос без обязательного параметра |
| test_verify_login | POST /api/verifyLogin | Позитивный: вход с верными данными |
| test_verify_login_wrong_password | POST /api/verifyLogin | Негативный: неверный пароль |
| test_verify_login_no_params | POST /api/verifyLogin | Негативный: отсутствует обязательный параметр |

## Особенность API

API возвращает HTTP-статус 200 даже при ошибках, а фактический код результата передаётся в теле ответа в поле `responseCode`. Поэтому проверки выполняются по `responseCode` из тела, а не по HTTP-статусу (см. также BUG-003 в разделе bug-reports).

## Установка и запуск

1. Установить зависимости:
```
pip install -r requirements.txt
```

2. Запустить тесты:
```
pytest -v
```

Флаг `-v` выводит результат по каждому тесту отдельно (PASSED / FAILED).
