import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from Shop_page_object import AuthorizationPage
from Shop_page_object import ProductPage
from Shop_page_object import CartPage
from Shop_page_object import FormPage
from Shop_page_object import SummaryPage


@allure.epic("Магазин одежды")
@allure.feature("Покупка товаров")
@allure.story("Тест покупки товаров")
@allure.title("Проверка покупки товаров стандартным пользователем")
@allure.description("Тест проверяет полный цикл покупки товаров:"
                    "авторизация, добавление в корзину, оформление заказа")
@allure.severity("blocker")
@allure.id("SHOP-001")
def test_login_standard_user():

    with allure.step("Открыть браузер Firefox"):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
    try:
        with allure.step("Авторизация на сайте"):
            page = AuthorizationPage(driver)
            page.authorization("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            Product_Page = ProductPage(driver)
            Product_Page.add_product(
                'sauce-labs-backpack',
                'sauce-labs-onesie',
                'sauce-labs-bolt-t-shirt'
            )

        with allure.step("Переход в корзину и оформление"):
            Cart_Page = CartPage(driver)
            Cart_Page.Cart()

        with allure.step("Заполнение формы доставки"):
            Form_Page = FormPage(driver)
            Form_Page.Form('Daniil', 'Golikov', '163000')

        with allure.step("Получение итоговой суммы"):
            Summ_Page = SummaryPage(driver)
            Total_amount = Summ_Page.Summary()

        with allure.step("Проверка итоговой стоимости"):
            # Проверка итоговой стоимости с страницы
            expected_total_amount = "Total: $58.29"
            print(
                f"Сравнение итоговой {Total_amount} "
                f"и ожидаемой стоимости {expected_total_amount}"
            )
            expected_total_amount = "Total: $58.29"
            assert Total_amount == expected_total_amount, (
                f"Ожидалась сумма {expected_total_amount}, "
                f"но получили {Total_amount}")
            print("Тест успешно пройден!")

    except Exception as e:
        with allure.step("Обработка ошибки"):
            print(f"Произошла ошибка: {e}")
        raise
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
            print("Браузер закрыт")
