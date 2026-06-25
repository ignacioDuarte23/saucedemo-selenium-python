# 🧪 Proyecto de Automatización - SauceDemo E-Commerce

Este repositorio contiene un caso de prueba automatizado para la plataforma de práctica de e-commerce **SauceDemo**, desarrollado con fines de práctica profesional y portafolio de QA Automation.

## 🚀 Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Herramienta de Automatización:** Selenium WebDriver
* **Estrategia de Localizadores:** SelectorsHub (ID, Class Name)
* **Control de Versiones:** Git & GitHub

## 📝 Caso de Prueba Automatizado
* **Test Case:** Login Exitoso
* **Flujo:** 
  1. Abrir el navegador Chrome e ingresar a la URL de SauceDemo.
  2. Localizar e ingresar las credenciales válidas (`standard_user` / `secret_sauce`).
  3. Ejecutar la acción de Login mediante un clic automatizado.
  4. **Validación (Assertion):** Verificar mediante aserción que el título de la página interna corresponda a "Products".
  5. Cierre seguro del WebDriver.

## 🔧 Requisitos e Instalación
Para ejecutar este script de forma local, necesitas clonar el repositorio e instalar las dependencias básicas:

```bash
# Clonar el proyecto
git clone https://github.com/ignacioDuarte23/saucedemo-selenium-python.git

# Instalar Selenium
pip install selenium
```
