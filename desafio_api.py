# Desafío - API
# Patricio Cortés
# G18
# 20-09-2021

# importar la librería para llamar a la API
import requests
import json

# crea funcion que llama una url con una determinada accion
def llamar_api(url, accion, datos):
    headers = {}
    payload = json.dumps(datos)
    # obtiene respuesta del servidor
    respuesta = requests.request(accion, url, data=payload, headers = headers)
    print("Acción: {}\nCódigo: {}".format(accion,respuesta))
    return json.loads(respuesta.text)

# *** Desafío 1 ***
url_get = "https://reqres.in/api/users"
user_get = {
    "name": "Ignacio",
    "job": "profesor"
}
print("Desafío 1:")
users_data = llamar_api(url_get, "GET", user_get)
print(users_data)

# *** Desafío 2 ***
url_post = "https://reqres.in/api/users"
user_post = {
    "name": "Ignacio",
    "job": "profesor"
}
print("Desafío 2:")
created_user = llamar_api(url_post, "POST", user_post)
print(created_user)

# *** Desafío 3 ***
url_put = "https://reqres.in/api/users/2"
user_put = {
    "name": "Morpheus",
    "residence": "Zion"
}
print("Desafío 3:")
updated_user = llamar_api(url_put, "PUT", user_put)
print(updated_user)

# *** Desafío 4 ***
url_delete = "https://reqres.in/api/users/2"
user_delete = {
    "name": "Pepe"
}
print("Desafío 4:")
deleted_user = llamar_api(url_delete, "DELETE", user_delete)
print(deleted_user)

# nota: no pude sacar el error en la accion DELETE, como que el VSC no lo reconoce.

# Fin del Programa