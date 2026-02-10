from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
                "https://bonigarcia.dev/selenium-"
                "webdriver-java/slow-calculator.html")
        self._driver.maximize_window()
        self.wait = WebDriverWait(self._driver, 50)

# Ввод задержки

    def set_delay(self, second):
        Input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        Input_delay.clear()
        Input_delay.send_keys(second)

# Нажатие кнопок

    def click_button(self, button):

        button = self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button}']"
        )
        button.click()

# Ожидание необходтмого результата

    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result)
        )

# Запись необходимого результата

    def get_result_text(self):
        return self._driver.find_element(By.CLASS_NAME, "screen").text


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
