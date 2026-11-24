# Configuraciones y fixtures para usar en las pruebas
# Tiene que estar en la raíz del proyecto para que pytest lo reconozca automáticamente

import pytest
from selenium import webdriver
import pathlib
import base64
import pytest_html


# Función que inicializa el driver de Selenium con Chrome, el implicit wait y lo cierra al finalizar la prueba
@pytest.fixture
def driver():
    # primero todo lo que vaya al inicio de la prueba
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    # con el yield se indica que lo que está antes es lo que se ejecuta al inicio de la prueba y lo que está después es lo que se ejecuta al final de la prueba
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)    
def pytest_runtest_makereport(item, call): # item es la prueba que se está ejecutando y call es la información sobre la ejecución de la prueba en alguna de sus etapas
    # Esta función se ejecuta después de cada prueba y permite acceder al resultado de la prueba
    # Se puede usar para hacer cosas como tomar capturas de pantalla en caso de fallo
    outcome = yield # yield es el último momento donde se quedó la prueba cuando falló, y se puede usar para acceder al resultado de la prueba
    report = outcome.get_result() # se obtiene el resultado de la prueba
    
    if report.when == "call" and report.failed: # si la prueba falló en la etapa de ejecución (call)
        driver = item.funcargs.get("driver") # se obtiene el driver de la prueba que falló
        carpeta = pathlib.Path("reports/screenshots") # se define la carpeta donde se guardarán las capturas de pantalla
        carpeta.mkdir(parents=True, exist_ok=True) # se crea la carpeta si no existe
        nombre_archivo = carpeta / f"{item.name}.png" # se define el nombre del archivo de la captura de pantalla
        driver.save_screenshot(str(nombre_archivo)) # se guarda la captura de pantalla
        
        imagen = base64.b64encode(nombre_archivo.read_bytes()).decode("utf-8") # se codifica la imagen en base64 para poder incrustarla en el reporte HTML
        report.extra = [
            pytest_html.extras.image(imagen, name="Screenshot", mime_type="image/png", extension="png") # se agrega la imagen al reporte HTML
        ]
        


