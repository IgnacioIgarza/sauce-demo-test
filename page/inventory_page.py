# se usará POM 
# aquí va todo lo relacionado con la interacción con la página de inventario

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        titulo = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        return titulo.text
    
    def obtener_productos(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    def obtener_nombre_primer_producto(self):
        primer_producto = self.obtener_productos()[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name")
        return nombre_producto.text
    
    def obtener_precio_primer_producto(self):
        primer_producto = self.obtener_productos()[0]
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price")
        return precio_producto.text
    
    def verificar_existencia_menu(self):
        menu = self.wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
        return menu.is_displayed()
    
    def verificar_existencia_carrito(self):
        carrito = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
        return carrito.is_displayed()
    
    def verificar_existencia_filtros(self):
        filtros = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
        return filtros.is_displayed()
    
    def agregar_producto_al_carrito(self,nombre):
        productos = self.obtener_productos()
        for producto in productos:
            nombre_producto = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
            if nombre_producto == nombre:
                producto.find_element(By.TAG_NAME,"button").click()
                return
        raise AssertionError(f"No se encontró el producto: {nombre}")
    
    def obtener_contador_carrito(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text
    
    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()
    