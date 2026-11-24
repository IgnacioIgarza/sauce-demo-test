from selenium import webdriver
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage

from utils.reader import read_products_json
from utils.logger import logger

def test_cart(driver):
    try:
        login_page = LoginPage(driver)
        logger.info("* Iniciando prueba del carrito con el login")
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Ingreso exitoso")
        cart_page = CartPage(driver)
        inventory_page = InventoryPage(driver)
        
        producto = read_products_json()[0]
        inventory_page.agregar_producto_al_carrito(producto["nombre"])
        logger.info("Se agrega un producto al carrito")
        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Comprobación de agregado al carrito exitoso")
        inventory_page.ir_al_carrito()
        logger.info("Ingreso al carrito")
        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Obtención del nombre del producto agregado al carrito exitoso")
        assert cart_page.obtener_PRECIO_producto() == producto["precio"]
        logger.info("Obtención del precio del producto agregado al carrito exitoso")
    except Exception:
            logger.exception("Error durante la prueba del carrito")
            raise