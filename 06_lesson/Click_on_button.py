from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.implicitly_wait(16)

# Перейдите на страницу http://uitestingplayground.com/ajax.
driver.get("http://uitestingplayground.com/ajax")
# Нажмите на синюю кнопку.
Button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
# Получите текст из зеленой плашки.
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
# Выведите его в консоль
print(txt)
# ("Data loaded with AJAX get request.")
driver.quit()
