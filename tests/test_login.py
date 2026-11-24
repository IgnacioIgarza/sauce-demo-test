# Usamos POM
# Aquí van las pruebas relacionadas con la página de login

import pytest
from page.login_page import LoginPage
from utils.reader import read_users_csv
from utils.logger import logger

# @pytest.fixture
@pytest.mark.parametrize("data", read_users_csv())
def test_login_page(driver, data):
    try:
        logger.info("* Iniciando prueba de login")
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        logger.info("Página www.saucedemo.com abierta correctamente")
        login_page.login(data['usuario'], data['contrasena'])
        logger.info("Ingreso de credenciales")
        if data['tipo_usuario'] == 'correcto':
            assert "/inventory.html" in driver.current_url
            logger.info("Ingreso exitoso")
        else:
            assert "Epic sadface: Username and password do not match any user in this service" in login_page.obtener_mensaje_error()
            logger.info("Prueba de mensaje de error válida")
    except Exception:
        logger.exception("Error durante la prueba de login")
        raise
        
        
    
    
