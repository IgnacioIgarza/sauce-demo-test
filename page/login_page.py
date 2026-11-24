# se usará POM 
# aquí va todo lo relacionado con la interacción con la página de login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, usuario = "standard_user"):
        campo_usuario = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

    def ingresar_contraseña(self, contraseña):
        campo_contraseña = self.driver.find_element(By.ID, "password")
        campo_contraseña.clear()
        campo_contraseña.send_keys(contraseña)

    def click_boton_login(self):
        boton_login = self.driver.find_element(By.ID, "login-button")
        boton_login.click()

    def login(self, usuario, contraseña):
        self.ingresar_usuario(usuario)
        self.ingresar_contraseña(contraseña)
        self.click_boton_login()
        
    def obtener_mensaje_error(self):
        mensaje_error = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
        return mensaje_error.text