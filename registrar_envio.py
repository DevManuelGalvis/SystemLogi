import json
import os
import random
import string
from datetime import datetime
from utils import cargar_json, guardar_json  

RUTA_CLIENTES = "datos/clientes.json"
RUTA_ENVIOS = "datos/envios.json"

def generar_numero_guia():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# def generar_numero_guia():
#     return str(random.randint(100000, 999999))

def inicializar_archivos():
    if not os.path.exists("datos"):
        os.makedirs("datos")
    for ruta in [RUTA_CLIENTES, RUTA_ENVIOS]:
        if not os.path.isfile(ruta):
            with open(ruta, "w") as f:
                json.dump([], f)

def registrar_envio():
    # Funcion para registrar un nuevo envío
    inicializar_archivos()

    clientes = cargar_json(RUTA_CLIENTES)
    envios = cargar_json(RUTA_ENVIOS)

    remitente_id = input("Identificación del remitente: ").strip()
    # remitente = next((c for c in clientes if c["identificacion"] == remitente_id), None)
    remitente = list(filter(lambda c: c["identificacion"] == remitente_id, clientes))
    remitente = remitente[0] if remitente else None
 
    if not remitente:
        print("❌ El remitente no está registrado.")
        return

    envio = {
        "fecha_envio": datetime.now().strftime("%Y-%m-%d"),
        "hora_envio": datetime.now().strftime("%H:%M:%S"),
        "numero_guia": generar_numero_guia(),
        "estado": "Recibido",
        "remitente_id": remitente_id,
        "destinatario": {
            "nombre": input("Nombre del destinatario: "),
            "direccion": input("Dirección del destinatario: "),
            "telefono": input("Teléfono de contacto: "),
            "ciudad": input("Ciudad: "),
            "barrio": input("Barrio: ")
        }
    }

    envios.append(envio)
    guardar_json(RUTA_ENVIOS, envios)
    print(f"✅ Envío registrado correctamente. Número de guía: {envio['numero_guia']}")
