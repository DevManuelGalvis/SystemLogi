import json
import os
import random
import string
from datetime import datetime


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
    inicializar_archivos()

    with open(RUTA_CLIENTES, "r") as f:
        clientes = json.load(f)
    with open(RUTA_ENVIOS, "r") as f:
        envios = json.load(f)

    remitente_id = input("Identificación del remitente: ").strip()
    # remitente = next((c for c in clientes if c["identificacion"] == remitente_id), None)
    remitente = list(filter(lambda c: c["identificacion"] == remitente_id, clientes))
    remitente = remitente[0] if remitente else None
    # print('remitente', type(remitente))
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
    with open(RUTA_ENVIOS, "w") as f:
        json.dump(envios, f, indent=4)
    print(f"✅ Envío registrado correctamente. Número de guía: {envio['numero_guia']}")
