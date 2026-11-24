# lee y devuelve los datos de un archivo CSV y json
import csv
import json

def read_users_csv():
    with open("data/users.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
    
data = read_users_csv() # data es una lista de diccionarios con los datos del CSV

"""
La información dentro de data es la siguiente: una lista de diccionarios
[
    {'usuario': 'standard_user', 'contrasena': 'secret_sauce'},
    {'usuario': 'Nacho', 'contrasena': 'secret_sauce'},
    {'usuario': 'standard_user', 'contrasena': '123456'},
    {'usuario': 'Nacho', 'contrasena': '123456'}
]
"""

def read_products_json():
    with open("data/products.json") as jsonfile:
        data = json.load(jsonfile)
        return data