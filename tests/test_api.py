# free_user_3L1XveNpvbuNHhrqpdVKLScodBF
import pytest
import requests 
import pytest_check as check

from utils.logger import logger

@pytest.mark.flaky(rerun=2,rerun_delay=5) # Hace que esta prueba en específico tenga 2 reintentos y una esperade 5 seg si falla
def test_obtener_usuario():
    url = "https://reqres.in/api/users/2"
    header = {"x-api-key":"free_user_3L1XveNpvbuNHhrqpdVKLScodBF"}
    response = requests.get(url, headers=header)
    logger.info("* Ingresando a la pag. https://reqres.in/api/users/2 para testeo de API")
    # Nivel 1: status code
    codigo = response.status_code
    assert codigo == 200
    
    # Nivel 2: headers
    assert response.headers["Content-Type"] == "application/json; charset=utf-8" # en esta linea se verifica que el Content-Type de la respuesta sea "application/json; charset=utf-8"
    assert "application/json" in response.headers["Content-Type"] # sería otra forma de verificar el Content-Type
    
    # Nivel 3: estructura
    data = response.json() # se obtiene la respuesta en formato JSON y se convierte a un diccionario de Python
    assert isinstance(data, dict) # si da verdadero, significa que la respuesta es un diccionario
    assert "data" in data # se verifica que la clave "data" esté presente en el diccionario
    # si se hubiera querido obtener el valor de la clave "data", se podría haber hecho así: data_usuario = data["data"]
    assert isinstance(data["data"], dict) # se verifica que el valor de la clave "data" sea un diccionario
    # luego se verifica que las claves "id", "email", "first_name", "last_name" y "avatar" estén presentes en el diccionario data["data"]
    # check sirve para realizar validaciones suaves, si falla alguna no se corta el test y sigue con la siguiente
    check.is_in("id",data["data"]) # assert "id" in data["data"]
    check.is_in("email",data["data"])# assert "email" in data["data"]
    check.is_in("first_name",data["data"])# assert "first_name" in data["data"]
    check.is_in("last_name",data["data"])# assert "last_name" in data["data"]
    check.is_in("avatar",data["data"])# assert "avatar" in data["data"]

    # Nivel 4: contenido: verificar que los datos del usuario sean correctos
    check.equal(data["data"]["id"],2)# assert data["data"]["id"] == 2
    check.equal(data["data"]["email"],"janet.weaver@reqres.in")# assert data["data"]["email"] == "janet.weaver@reqres.in"
    check.equal(data["data"]["first_name"],"Janet")# assert data["data"]["first_name"] == "Janet"
    check.equal(data["data"]["last_name"],"Weaver")# assert data["data"]["last_name"] == "Weaver"
    
    # Nivel 5: verificar tiempo de respuesta
    assert response.elapsed.total_seconds() < 2 # se verifica que el tiempo de respuesta sea menor a 2 segundos
    logger.info("Pasa test de obtener usuario")
    
def test_crear_usuario():
    url = "https://reqres.in/api/users"
    header = {
        "x-api-key":"free_user_3L1XveNpvbuNHhrqpdVKLScodBF"
    }
    usuario = {
        "email": "lm@reqres.in",
        "first_name": "Lio",
        "last_name": "Messi",
        "job": "QA  Engineer"
    }
    response = requests.post(url, headers=header, json=usuario)
    codigo = response.status_code
    logger.info("* Ingresando a la pag. https://reqres.in/api/users/2 para testeo de API")
    # Nivel 1: status code
    assert codigo == 201
    
    # Nivel 2: headers
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    
    # Nivel 3: estructura
    data = response.json()
    assert isinstance(data, dict)
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "job" in data
    
    # Nivel 4: contenido
    assert data["email"] == "lm@reqres.in"
    assert data["first_name"] == "Lio"
    assert data["last_name"] == "Messi"
    assert data["job"] == "QA  Engineer"
    
    # Nivel 5: verificar tiempo de respuesta
    assert response.elapsed.total_seconds() < 2
    logger.info("Pasa test de creación de usuario")
    
def test_eliminar_usuario():
    url = "https://reqres.in/api/users/2"
    header = {
        "x-api-key":"free_user_3L1XveNpvbuNHhrqpdVKLScodBF"
    }
    
    response = requests.delete(url, headers=header)
    codigo = response.status_code
    print(codigo)
    logger.info("* Ingresando a la pag. https://reqres.in/api/users/2 para testeo de API")
    assert codigo == 204
    assert response.text == ""  # se verifica que la respuesta sea vacía
    # assert "application/json" not in response.headers["Content-Type"]  # se verifica que el Content-Type de la respuesta no sea "application/json"
    assert response.elapsed.total_seconds() < 2  # se verifica que el tiempo de respuesta sea menor a 2 segundos
    logger.info("Pasa test de eliminación de usuario")
    
def test_obtener_usuario_inexistente():
    url = "https://reqres.in/api/users/23"
    header = {
        "x-api-key":"free_user_3L1XveNpvbuNHhrqpdVKLScodBF"
    }
    
    response = requests.get(url, headers=header)
    codigo = response.status_code
    print(codigo)
    data = response.json()
    print(data)
    logger.info("* Ingresando a la pag. https://reqres.in/api/users/2 para testeo de API")
    assert codigo == 404
    logger.info("Pasa test de obtención usuario inexistente")
