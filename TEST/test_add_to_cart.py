from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Diccionario de preferencias para silenciar el gestor de contraseñas y fugas
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False  # <--- Este desactiva el cartel
}

chrome_options.add_experimental_option("prefs", prefs)

# Inicializa el driver pasando las opciones
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")

#login
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()

#carrito
driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

titulo_carrito = driver.find_element(By.CLASS_NAME, "title").text
assert titulo_carrito == "Your Cart", f"Error: Se esperaba estar en el carrito, pero dice {titulo_carrito}"

boton_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button"))
)

boton_checkout.click()

#checkout
campo_nombre = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "first-name"))
)
campo_nombre.send_keys("Ignacio")

driver.find_element(By.ID,"last-name").send_keys("Duarte")
driver.find_element(By.ID,"postal-code").send_keys("2132")
driver.find_element(By.ID,"continue").click()

boton_finalizar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "finish"))
)
boton_finalizar.click()

mensaje_exito = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
).text

assert mensaje_exito == "Thank you for your order!", f"Error: La compra fallo, mensaje: {mensaje_exito}"

print("¡Prueba de flujo completo de checkout Exitoso y sincronizado!")
driver.quit()