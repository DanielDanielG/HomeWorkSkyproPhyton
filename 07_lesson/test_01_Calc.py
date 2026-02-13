from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calc_page_object import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    Calculator = CalculatorPage(driver)
    Calculator.set_delay(45)
    Calculator.click_button("7")
    Calculator.click_button("+")
    Calculator.click_button("8")
    Calculator.click_button("=")
    Calculator.wait_for_result("15")
    actual_result = Calculator.get_result_text()
    assert actual_result == "15", "Ожидался результат '15'"
    ", но получили '{actual_result}'"
    driver.quit()
