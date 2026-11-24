# es la configuración de este tipo de pruebas con Gherkin

from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.quit()