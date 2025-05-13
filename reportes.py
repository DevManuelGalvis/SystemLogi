import os
from collections import Counter, defaultdict
from datetime import datetime
from utils import cargar_json

RUTA_ENVIOS = "datos/envios.json"

def generar_reporte():
    # Funcion para generar un reporte de envíos
    if not os.path.isfile(RUTA_ENVIOS):
        print("No hay datos para generar reporte.")
        return

    envios = cargar_json(RUTA_ENVIOS)

    if not envios:
        print("No hay envíos registrados.")
        return

    print("\n📊 Reporte general de envíos:")
    print(f"Total de envíos: {len(envios)}")

    # 1. Conteo de estados
    estados = [e["estado"] for e in envios]
    conteo_estados = Counter(estados)
    print("\n📦 Estados actuales de los paquetes:")
    for estado, cantidad in conteo_estados.items():
        print(f"{estado}: {cantidad}")

    # 2.Envíos por mes
    envios_por_mes = defaultdict(int)
    for e in envios:
        fecha = e.get("fecha_envio")
        if fecha:
            try:
                mes = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m")
                envios_por_mes[mes] += 1
            except:
                continue

    print("\n📅 Número de envíos por mes:")
    for mes, cantidad in sorted(envios_por_mes.items()):
        print(f"{mes}: {cantidad} envíos")

    opcion = input("\n¿Desea ver envíos por fecha específica? (s/n): ").strip().lower()
    if opcion == "s":
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        filtrados = [e for e in envios if e["fecha_envio"] == fecha]
        print(f"\n📦 Envíos en {fecha}: {len(filtrados)}")
        for e in filtrados:
            print(f"- Guía {e['numero_guia']}, Estado: {e['estado']}")
