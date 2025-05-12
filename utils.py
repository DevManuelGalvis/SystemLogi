import json

def mostrar_json(RUTA_ENVIOS):
    with open(RUTA_ENVIOS, "r") as archivo:
        return json.load(archivo)