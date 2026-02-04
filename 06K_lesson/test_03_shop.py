from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_store():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()))
    waiter = WebDriverWait(driver, 5)

    try:
        # Открываю страницу
        print("Открывается страница в браузере Firefox")
        driver.get(" https://www.saucedemo.com/")

        # Авторизуйтесь как пользователь standard_user
        print("Авторизация")
        # Ожидание доступности поля логин
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#user-name")))
        # Авторизация
        Login = driver.find_element(
            By.CSS_SELECTOR, "#user-name")
        Login.clear()
        Login.send_keys("standard_user")

        Password = driver.find_element(
            By.CSS_SELECTOR, "#password")
        Password.clear()
        Password.send_keys("secret_sauce")
        print("Поля заполненны, нажатие на кнопку Login")

        Button = driver.find_element(
            By.CSS_SELECTOR, "#login-button")
        Button.click()
        print("Успешная авторизация")
        # Добавление товаров в корзину

        # Добавляем Sauce Labs Backpack.
        print("Добавляем Sauce Labs Backpack")
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        Backpack = driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        Backpack.click()
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")))
        print("Добавлен Sauce Labs Backpack")

        # Добавляем Sauce Labs Bolt T-Shirt.

        print("Добавляем Sauce Labs Bolt T-Shirt")
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
        T_Shirt = driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        T_Shirt.click()
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")))
        print("Добавлен Sauce Labs Bolt T-Shirt")

        # Добавляем Sauce Labs Onesie.

        print("Добавляем Sauce Labs Onesie")
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
        Onesie = driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        Onesie.click()
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")))
        print("Добавлен Sauce Labs Onesie")

        # Переход в корзину
        print("Переходим в корзину")
        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[class='shopping_cart_link']")))
        Basket = driver.find_element(
            By.CSS_SELECTOR, "[class='shopping_cart_link']")
        Basket.click()

        # Нажатие кнопки Checkout

        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#checkout")))
        print("Открыта страница корзины")
        Checkout_button = driver.find_element(
            By.CSS_SELECTOR, "#checkout")
        Checkout_button.click()
        print("Ожидание открытия формы")

        # Заполнение формы

        waiter.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#first-name")))
        print("Форма открылась, заполнение полей")

        First_name = driver.find_element(
            By.CSS_SELECTOR, '#first-name')
        First_name.clear()
        First_name.send_keys('Daniil')

        Last_name = driver.find_element(
            By.CSS_SELECTOR, '#last-name')
        Last_name.clear()
        Last_name.send_keys('Golikov')

        Zip_code = driver.find_element(
            By.CSS_SELECTOR, '#postal-code')
        Zip_code.clear()
        Zip_code.send_keys('163000')

        Continue_button = driver.find_element(
            By.CSS_SELECTOR, '#continue')
        Continue_button.click()

        print("Форма заполнена, ожидание перехода на страницу итога")
        # Считывание итоговой стоимости с страницы

        waiter.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        print("Страница загружена")
        Amount = driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        Total_amount = Amount.text
        print("Найдена итоговая сумма")
        driver.quit()

        # Проверка итоговой стоимости с страницы
        print("Сравнение итоговой и ожидаемой стоимости")
        expected_total_amount = "Total: $58.29"
        assert Total_amount == expected_total_amount, (
            f"Ожидалась сумма {expected_total_amount}, "
            f"но получили {Total_amount}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise

    finally:
        driver.quit()
        print("Браузер закрыт")
        print("Тест успешно пройден!")


if __name__ == "__main__":
    test_store()
