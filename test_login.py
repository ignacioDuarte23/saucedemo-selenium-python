from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

titulo_productos = driver.find_element(By.CLASS_NAME, "title").text

assert titulo_productos == "Products", f"Error: El login fallo, se obtuvo {titulo_productos}"

print("Prueba de login Exitosa")

driver.quit()