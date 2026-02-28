import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:
    """
    Класс для работы с страницей авторизации магазина.

    Содержит методы для перехода на страницу авторизации,
    ввода учётных данных и выполнения входа в систему.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        Разворачивает окно браузера и настраивает явное ожидание элементов.
        """
        self._driver = driver
        self._driver.maximize_window()
        self.wait = WebDriverWait(self._driver, 5)

    def authorization(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя на сайте.

        Переходит на страницу авторизации, ожидает доступности полей,
        заполняет логин и пароль, затем нажимает кнопку входа.
        """
        # Переход на страницу
        with allure.step("Перейти на страницу 'https://www.saucedemo.com/'"):
            self._driver.get("https://www.saucedemo.com/")

        # Переход на Авторизация

        print("Авторизация")

        # Ожидание доступности поля логин
        with allure.step("Подождать доступность поля для ввода Логина"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#user-name")))

        # Авторизация
        with allure.step("Авторизироваться {username}:{password}"):
            Login = self._driver.find_element(
                By.CSS_SELECTOR, "#user-name")
            Login.clear()
            Login.send_keys(username)

            Password = self._driver.find_element(
                By.CSS_SELECTOR, "#password")
            Password.clear()
            Password.send_keys(password)
        print("Поля заполненны, нажатие на кнопку Login")

        with allure.step("Нажать кнопку 'Login'"):
            Button = self._driver.find_element(
                By.CSS_SELECTOR, "#login-button")
            Button.click()
        print("Успешная авторизация")


class ProductPage:
    """
    Класс для работы с страницей товаров магазина.

    Содержит методы для добавления товаров в корзину покупок.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы товаров.

        Настраивает явное ожидание элементов для взаимодействия.
        """
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def add_product(self, *products: str) -> None:
        """
        Добавляет один или несколько товаров в корзину покупок.

        Для каждого переданного идентификатора товара находит соответствующую
        кнопку добавления, ожидает её доступности и выполняет клик.
        """
        # Добавляем Товар в корзину.
        with allure.step("Добавить товары в корзину {product}"):
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
    """
    Класс для работы с страницей корзины покупок.

    Содержит методы для перехода в корзину и оформления заказа.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        Настраивает явное ожидание элементов для взаимодействия.
        """
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Cart(self) -> None:
        """
        Выполняет переход в корзину покупок
                нажимает кнопку оформления заказа.

        Находит и кликает по иконке корзины, затем ожидает
        нажимает кнопку "Checkout" для перехода к оформлению.
        """
        print("Переходим в корзину")
        with allure.step("Нажать на кнопку корзины"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[class='shopping_cart_link']")))
            Basket = self._driver.find_element(
                By.CSS_SELECTOR, "[class='shopping_cart_link']")
            Basket.click()

        # Нажатие кнопки Checkout
        with allure.step("Нажать на кнопку 'Checkout'"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#checkout")))
            print("Открыта страница корзины")
            Checkout_button = self._driver.find_element(
                By.CSS_SELECTOR, "#checkout")
            Checkout_button.click()
            print("Ожидание открытия формы")


class FormPage:
    """
    Класс для работы с страницей оформления заказа (форма доставки).

    Содержит методы для заполнения полей формы с данными покупателя.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы формы оформления.

        Настраивает явное ожидание элементов для взаимодействия.
        """
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Form(self, name_first: str, name_last: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа данными покупателя.

        Заполняет поля: имя, фамилия и почтовый индекс, затем нажимает
        кнопку продолжения для перехода к итоговой странице.
        """
        with allure.step("Ожидать доспуность полей для ввода"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#first-name")))

        print("Форма открылась, заполнение полей")
        with allure.step("Заполнить поле First name {name_first}"):
            First_name = self._driver.find_element(
                By.CSS_SELECTOR, '#first-name')
            First_name.clear()
            First_name.send_keys(name_first)
        with allure.step("Заполнить поле Last name {name_last}"):
            Last_name = self._driver.find_element(
                By.CSS_SELECTOR, '#last-name')
            Last_name.clear()
            Last_name.send_keys(name_last)
        with allure.step("Заполнить поле Zip code {postal_code}"):
            Zip_code = self._driver.find_element(
                By.CSS_SELECTOR, '#postal-code')
            Zip_code.clear()
            Zip_code.send_keys(postal_code)
        with allure.step("Нажать кнопку 'continue'"):
            Continue_button = self._driver.find_element(
                By.CSS_SELECTOR, '#continue')
            Continue_button.click()

        print("Форма заполнена, ожидание перехода на страницу итога")


class SummaryPage:
    """
    Класс для работы с итоговой страницей оформления заказа.

    Содержит методы для получения и проверки финальной суммы заказа.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация итоговой страницы.

        Настраивает явное ожидание элементов для взаимодействия.
        """
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)

    def Summary(self) -> str:
        """
        Получает итоговую сумму заказа со страницы подтверждения.

        Ожидает появления элемента с итоговой стоимостью и возвращает
        его текстовое содержимое.
        """
        # Считывание итоговой стоимости с страницы
        with allure.step("Ожидать подсчёт итоговой суммы {Total_amount}"):
            self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
            print("Страница загружена")
        Amount = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        Total_amount = Amount.text
        print("Найдена итоговая сумма")
        return Total_amount
