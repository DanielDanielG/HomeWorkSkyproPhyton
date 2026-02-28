# Проект автотестов с Allure Report

> Автоматизированное тестирование веб-приложений «Калькулятор» и «Магазин одежды» с использованием Python, Selenium и Allure.

## О проекте

Проект содержит UI-автотесты для двух веб-приложений:

| Приложение | Описание | Файл теста |
|------------|----------|------------|
| Калькулятор | Проверка арифметических операций с задержкой | `test_01_Calc.py` |
| Магазин одежды | Полный цикл покупки: авторизация → корзина → оплата | `test_02_Shop.py` |

## Используемые расширения
- Python 3.8+
- pytest
- Selenium WebDriver
- Allure Report
- webdriver-manager

## Запуск тестов
Запуск конкретного файла

## Тест калькулятора
python -m pytest test_01_Calc.py --alluredir allure-result

## Тест магазина
python -m pytest test_02_Shop.py --alluredir allure-result

# Формирование и просмотр отчёта

### Команда для запуска отчёта

allure serve allure-result

allure serve Запускает временный сервер с отчётом
allure-result Папка с результатами тестов

## Запуск через run.bat (Windows)

Проект включает скрипт run.bat для автоматизации полного цикла на Windows.

Как запустить:
cmd
cd C:\путь\к\проекту
run.bat

Скрипт:

echo off
:: ============================================
:: СКРИПТ ЗАПУСКА АВТОТЕСТОВ С ALLURE
:: ============================================
:: Автоматическая очистка, запуск тестов,
:: сохранение истории и открытие отчёта
:: ============================================

:: Настройка путей (относительные)
set results=allure-result
set report=allure-report
set history=%report%\history

:: Шаг 1: Очистка папки с предыдущими результатами тестов
echo [1/4] Clean allure-result
rmdir /S /Q %results% 2>nul

:: Шаг 2: Запуск тестов pytest с сохранением результатов
echo [2/4] Start test on pytest...
python -m pytest --alluredir=%results%

:: Шаг 3: Генерация нового HTML-отчёта Allure
echo [3/4] Generate Allure...
allure serve %results%

:: Шаг 4: Открытие отчёта в браузере по умолчанию
echo [4/4] Open Allure on browser
allure serve %report%

echo.
echo ============================================
echo Allure open on browser
echo ============================================
pause

Настройка путей в run.bat:

set results=allure-result               :: Папка результатов
set report=allure-report                :: Папка отчёта
set history=%report%\history            :: Папка истории

# Структура проекта
project/
├── Calc_page_object.py       # Page Object: калькулятор
├── Shop_page_object.py       # Page Object: магазин
├── test_01_Calc.py           # Тесты калькулятора
├── test_02_Shop.py           # Тесты магазина
├── run.bat                   # Скрипт запуска для Windows
├── README.md                 # Документация
├── allure-result/            # Результаты тестов (генерируется)
└── allure-report/            # Готовый отчёт (генерируется)

# Allure-аннотации

@allure.epic("Название эпика")           # Крупный функциональный блок
@allure.feature("Название фичи")         # Конкретная возможность системы
@allure.story("Пользовательская история") # Сценарий использования
@allure.title("Заголовок теста")         # Человекочитаемое имя теста
@allure.description("Описание")          # Детальное описание теста
@allure.severity("blocker")              # Критичность 
@allure.id("TEST-001")                   # Уникальный ID теста
Шаги в отчёте:
with allure.step(""):

#  Проверка работоспособности:

        Шаг                     Ожидаемый результат
Запуск тестов           Браузер открывается и выполняет действия
После завершения        В консоли отображается результат тестов
Запуск allure serve     Отчёт Allure открывается в браузере
В отчёте                Видны эпик, фичи, шаги тестов