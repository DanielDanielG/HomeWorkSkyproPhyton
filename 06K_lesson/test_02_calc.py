from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

URL = ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    # Ожидание 45 + 1 сек запас
    wait = WebDriverWait(driver, 46)

    try:

        # Открываю страницу
        print("Открывается страница в браузере Chrome")
        driver.get(URL)

        # Поиск локатора delay и ввод 45
        Input_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
        Input_delay.clear()
        Input_delay.send_keys('45')
        print("Установлен таймер на 45 секунд ")

        # Кнопка 7
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()
        print("Нажата кнопка '7'")

        # Кнопка +
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()
        print("Нажата кнопка '+'")

        # Кнопка 8
        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        print("Нажата кнопка '8'")

        # Кнопка =
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()
        print("Нажата кнопка '='")

        # Ждем пока результат станет равным 15
        print("Ожидание рузультата")
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        # Получаем фактический результат для проверки
        Result = driver.find_element(By.CLASS_NAME, "screen").text
        print("Получен результат для проверки")
        assert Result == "15", "Ожидался результат 15, но получили {Result}"
        print(f"Фактический результат: {Result}")
        driver.quit()
        print("Тест успешно пройден!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
