import os
import json

def inicializar_archivo():
    RUTA_CLIENTES = "datos/clientes.json"
    if not os.path.exists("datos"):
        os.makedirs("datos")

    if not os.path.isfile(RUTA_CLIENTES) or os.path.getsize(RUTA_CLIENTES) == 0:
        with open(RUTA_CLIENTES, "w") as archivo:
            json.dump([], archivo)


def cargar_json(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en: {ruta_archivo}")
        return None


def guardar_json(ruta_archivo, datos):
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar JSON: {e}")
