from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self.wait = WebDriverWait(self._driver, 5)

    def authorization(self, username, password):

        # Переход на страницу

        self._driver.get("https://www.saucedemo.com/")

        # Переход на Авторизация

        print("Авторизация")

        # Ожидание доступности поля логин

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#user-name")))

        # Авторизация

        Login = self._driver.find_element(
            By.CSS_SELECTOR, "#user-name")
        Login.clear()
        Login.send_keys(username)

        Password = self._driver.find_element(
            By.CSS_SELECTOR, "#password")
        Password.clear()
        Password.send_keys(password)
        print("Поля заполненны, нажатие на кнопку Login")

        Button = self._driver.find_element(
            By.CSS_SELECTOR, "#login-button")
        Button.click()
        print("Успешная авторизация")


class ProductPage:

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def add_product(self, *products):

        # Добавляем Товар в корзину.

        for product in products:
            print(f"Добавляем {product}")
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"#add-to-cart-{product}")))
            product_button = self._driver.find_element(
                By.CSS_SELECTOR, f"#add-to-cart-{product}")
            product_button.click()
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"#remove-{product}")))
            print(f"Добавлен {product}")


class CartPage:

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Cart(self):

        print("Переходим в корзину")
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[class='shopping_cart_link']")))
        Basket = self._driver.find_element(
            By.CSS_SELECTOR, "[class='shopping_cart_link']")
        Basket.click()

        # Нажатие кнопки Checkout

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#checkout")))
        print("Открыта страница корзины")
        Checkout_button = self._driver.find_element(
            By.CSS_SELECTOR, "#checkout")
        Checkout_button.click()
        print("Ожидание открытия формы")


class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Form(self, name_first, name_last, postal_code):

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#first-name")))

        print("Форма открылась, заполнение полей")

        First_name = self._driver.find_element(
            By.CSS_SELECTOR, '#first-name')
        First_name.clear()
        First_name.send_keys(name_first)

        Last_name = self._driver.find_element(
            By.CSS_SELECTOR, '#last-name')
        Last_name.clear()
        Last_name.send_keys(name_last)

        Zip_code = self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code')
        Zip_code.clear()
        Zip_code.send_keys(postal_code)

        Continue_button = self._driver.find_element(
            By.CSS_SELECTOR, '#continue')
        Continue_button.click()

        print("Форма заполнена, ожидание перехода на страницу итога")


class SummaryPage:

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Summary(self):
        # Считывание итоговой стоимости с страницы

        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        print("Страница загружена")
        Amount = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        Total_amount = Amount.text
        print("Найдена итоговая сумма")
        return Total_amount


def test_login_standard_user():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    try:
        page = AuthorizationPage(driver)
        page.authorization("standard_user", "secret_sauce")
        Product_Page = ProductPage(driver)
        Product_Page.add_product(
            'sauce-labs-backpack',
            'sauce-labs-onesie',
            'sauce-labs-bolt-t-shirt'
        )
        Cart_Page = CartPage(driver)
        Cart_Page.Cart()

        Form_Page = FormPage(driver)
        Form_Page.Form('Daniil', 'Golikov', '163000')

        Summ_Page = SummaryPage(driver)
        Total_amount = Summ_Page.Summary()

        # Проверка итоговой стоимости с страницы
        print("Сравнение итоговой и ожидаемой стоимости")
        expected_total_amount = "Total: $58.29"
        assert Total_amount == expected_total_amount, (
            f"Ожидалась сумма {expected_total_amount}, "
            f"но получили {Total_amount}")
        print("Тест успешно пройден!")

    except Exception as e:

        print(f"Произошла ошибка: {e}")
        raise
    finally:
        driver.quit()
        print("Браузер закрыт")
