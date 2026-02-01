from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
# Перейдите на сайт http://uitestingplayground.com/textinput.
driver.get("http://uitestingplayground.com/textinput")
# Укажите в поле ввода текст SkyPro.
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys('SkyPro')
# Нажмите на синюю кнопку.
Blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
Blue_button.click()
# Получите текст кнопки и выведите в консоль
print(Blue_button.text)
# ("SkyPro")
driver.quit
