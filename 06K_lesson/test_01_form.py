from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"C:\Users\Daniel\Edgedriver\msedgedriver.exe"


def test_form():
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    waiter = WebDriverWait(driver, 40)

    try:
        print("Открывается страница в браузере Edge")
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        driver.maximize_window()

        #  Заполнение формы
        print("Заполняется форма")
        First_name = driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]')
        First_name.clear()
        First_name.send_keys('Иван')

        Last_name = driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]')
        Last_name.clear()
        Last_name.send_keys('Петров')

        Address = driver.find_element(
            By.CSS_SELECTOR, '[name="address"]')
        Address.clear()
        Address.send_keys('Ленина, 55-3')

        Email = driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]')
        Email.clear()
        Email.send_keys('test@skypro.com')

        Phone = driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]')
        Phone.clear()
        Phone.send_keys('+7985899998787')

        Zip_code = driver.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]')
        Zip_code.clear()

        City = driver.find_element(
            By.CSS_SELECTOR, '[name="city"]')
        City.clear()
        City.send_keys('Москва')

        Country = driver.find_element(
            By.CSS_SELECTOR, '[name="country"]')
        Country.clear()
        Country.send_keys('Россия')

        Job_position = driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]')
        Job_position.clear()
        Job_position.send_keys('QA')

        Company = driver.find_element(
            By.CSS_SELECTOR, '[name="company"]')
        Company.clear()
        Company.send_keys('SkyPro')

        # Нажатие на кнопку
        print("Нажатие на кнопку Submit")
        Button = driver.find_element(
            By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]')
        Button.click()

        # Ожидание видимости Zip поля
        print("Ожидание подсветки поля Zip code")
        waiter.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#zip-code")))

        # Проверьте (assert), что поле Zip code подсвечено красным.
        print("Проверка поля Zip code")
        fields_zip = driver.find_element(
            By.CSS_SELECTOR, "#zip-code")
        class_fields_zip = fields_zip.get_attribute("class")
        assert "alert-danger" in class_fields_zip, (
            'Zip code не подсвечено красным!')
        print("Поле Zip code подсвечено красным")

        # Проверить, что остальные поля подсвечены зеленым
        print("Проверка остальные поля зелёные")
        all_fields = driver.find_elements(
            By.CSS_SELECTOR, "div.alert")
        for field in all_fields:
            field_id = field.get_attribute("id")
            field_class = field.get_attribute("class")
            if field_id == "zip-code":
                continue
            assert (
                "alert-success" in field_class
            ), f"Поле '{field_id}' подсвечено красным!"

        print("Остальные поля подсвечены зелёным")

        driver.quit()
        print("Тест успешно пройден!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form()
