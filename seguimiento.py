import json
import os

RUTA_ENVIOS = "datos/envios.json"

def seguimiento_paquete():
    if not os.path.isfile(RUTA_ENVIOS):
        print("❌ No hay envíos registrados.")
        return

    identificacion = input("Ingrese su número de identificación: ").strip()
    
    with open(RUTA_ENVIOS, "r") as archivo:
        envios = json.load(archivo)

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
