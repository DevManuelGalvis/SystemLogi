import json
import os
from utils import cargar_json, guardar_json

RUTA_ENVIOS = "datos/envios.json"

def seguimiento_paquete():
    # Funcion para hacerle seguimineto al envio
    if not os.path.isfile(RUTA_ENVIOS):
        print("❌ No hay envíos registrados.")
        return

    identificacion = input("Ingrese su número de identificación: ").strip()
    envios = cargar_json(RUTA_ENVIOS)

    # Buscar envíos cuyo destinatario tenga la identificación ingresada
    envios_destinatario = [
        envio for envio in envios
        if envio.get("remitente_id") == identificacion
    ]


    if not envios_destinatario:
        print("❌ No se encontraron envíos asociados a esa identificación.")
        return

    print(f"\n📦 Envíos encontrados para la identificación {identificacion}:\n")
    for envio in envios_destinatario:
        print(f"➡ Número de Guía: {envio['numero_guia']}")
        print(f"   Estado: {envio['estado']}")
        print(f"   Ciudad Destino: {envio['destinatario'].get('ciudad', 'N/A')}")
        print("")
