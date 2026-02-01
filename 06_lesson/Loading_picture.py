from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40)
# Перейдите на сайт
Url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(Url)
# Дождитесь загрузки всех картинок.
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".lead"), "Done!")
)
# Получите значение атрибута src у 3-й картинки.
images = driver.find_elements(By.CSS_SELECTOR, "img")
third_image = images[3]
third_image_src = third_image.get_attribute("src")
# Выведите значение в консоль.
print(third_image_src)
driver.quit()
