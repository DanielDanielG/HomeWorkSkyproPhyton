
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys("tomsmith")
time.sleep(1)
password_field.send_keys("SuperSecretPassword!")
time.sleep(1)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
time.sleep(2)
success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)
driver.quit()
