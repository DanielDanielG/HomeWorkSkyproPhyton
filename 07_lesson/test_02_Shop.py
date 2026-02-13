from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from Shop_page_object import AuthorizationPage
from Shop_page_object import ProductPage
from Shop_page_object import CartPage
from Shop_page_object import FormPage
from Shop_page_object import SummaryPage


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
