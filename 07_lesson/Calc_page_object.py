from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
