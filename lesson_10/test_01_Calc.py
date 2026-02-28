import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calc_page_object import CalculatorPage


@allure.epic("Калькулятор")
@allure.feature("Расчёты")
@allure.story("Тест калькулятора")
@allure.title("Проверка сложения чисел")
@allure.description("Тест проверяет корректность сложения"
                    "двух чисел в калькуляторе")
@allure.severity("blocker")
@allure.id("CALC-001")
def test_calculator():
    with allure.step("Открыть браузер Chrome"):
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        Calculator = CalculatorPage(driver)

    with allure.step("Установка задержки 45 секунд"):
        Calculator.set_delay(45)

    with allure.step("Нажатие кнопки 7"):
        Calculator.click_button("7")

    with allure.step("Нажатие кнопки +"):
        Calculator.click_button("+")

    with allure.step("Нажатие кнопки 8"):
        Calculator.click_button("8")

    with allure.step("Нажатие кнопки ="):
        Calculator.click_button("=")

    with allure.step("Ожидание результата 15"):
        Calculator.wait_for_result("15")

    with allure.step("Получение фактического результата {actual_result}"):
        actual_result = Calculator.get_result_text()

    with allure.step("Проверка соответствия ожидаемого результата 15"):
        assert actual_result == "15", (
            f"Ожидался результат '15', но получили '{actual_result}'"
        )

    with allure.step("Закрытие браузера"):
        driver.quit()
