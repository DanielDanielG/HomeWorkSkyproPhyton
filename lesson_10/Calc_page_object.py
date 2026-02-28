import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы с страницей калькулятора.

    Содержит методы для взаимодействия с элементами страницы калькулятора
    в автоматизированных тестовых сценариях с использованием Selenium.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        Открывает страницу калькулятора в браузере, разворачивает окно
        и настраивает явное ожидание элементов.

        :param driver: Экземпляр WebDriver Selenium для управления браузером
        :type driver: webdriver
        :return: None
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-"
            "webdriver-java/slow-calculator.html"
        )
        self._driver.maximize_window()
        self.wait = WebDriverWait(self._driver, 50)

    def set_delay(self, second: str) -> None:
        """
        Устанавливает задержку получения ответа от калькулятора.

        Находит поле ввода задержки по CSS-селектору, очищает его
        и вводит новое значение задержки.
        """
        with allure.step("Найти элемент (кнопку)"):
            input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
            with allure.step("Очистить строку ввода ожидания"):
                input_delay.clear()
                with allure.step(f"Ввести ожидание {second}"):
                    input_delay.send_keys(second)

    def click_button(self, button: str) -> None:
        """
        Выполняет нажатие на кнопку калькулятора по её тексту.

        Находит элемент кнопки по XPath, используя переданный текст,
        и выполняет клик по нему.

        """
        with allure.step(f"Найти элемент (кнопку {button})"):
            button_element = self._driver.find_element(
                By.XPATH,
                f"//span[contains(@class, 'btn') and text()='{button}']"
            )
        with allure.step(f"Нажать на найденный элемент (кнопку {button})"):
            button_element.click()

    def wait_for_result(self, expected_result: str) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Использует WebDriverWait для ожидания, пока текст элемента
        с классом 'screen' не будет содержать ожидаемое значение.

        :param expected_result: Ожидаемый текст результата
                                на экране калькулятора
        """
        with allure.step(f"Ожидание необходимого результата {expected_result}"
                         ):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), expected_result
                )
            )

    def get_result_text(self) -> str:
        """
        Получает текущий текст результата с экрана калькулятора.

        Находит элемент экрана калькулятора по классу 'screen'
        и возвращает его текстовое содержимое.
        """
        return self._driver.find_element(By.CLASS_NAME, "screen").text
