# Usamos POM
# Aquí van las pruebas relacionadas con la página de inventario

from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import pytest

from utils.logger import logger

def test_inventory_page(driver):
    try:
        logger.info("* Iniciando la prueba del inventario")
        login_page = LoginPage(driver)
        logger.info("Ingresando a la página web")
        driver.get("https://www.saucedemo.com/")
        logger.info("Ingresando  credenciales para iniciar sesión")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Sesión iniciada correctamente")
        inventory_page = InventoryPage(driver)
        
        # Verificar que el título de la página es "Products"
        assert inventory_page.obtener_titulo() == "Products"
        logger.info("Se verificó que el título del inventario sea Products")
        # Verificar que hay productos en la página
        assert len(inventory_page.obtener_productos()) > 0
        logger.info("Se verificó que hay productos en el inventario")
        # Verificar que el primer producto tiene un nombre
        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        logger.info("Se verificó que el primer producto en el inventario tenga el nombre correcto")
        # Verificar que el primer producto tiene un precio
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Se verificó que el primer producto en el inventario tenga el precio correcto")
        # Verificar que el menú está presente
        assert inventory_page.verificar_existencia_menu() # == True
        logger.info("Se verificó que el inventario tenga un menu")
        # Verificar que el carrito está presente
        assert inventory_page.verificar_existencia_carrito() # == True
        logger.info("Se verificó que el inventario tenga un carrito")
        # Verificar que los filtros están presentes
        assert inventory_page.verificar_existencia_filtros() # == True
        logger.info("Se verificó que el inventario tenga un filtro")
    except Exception:
        logger.exception("Error durante la prueba del inventario")
        raise