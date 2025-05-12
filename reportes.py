import json
import os
from collections import Counter, defaultdict
from datetime import datetime

RUTA_ENVIOS = "datos/envios.json"

def generar_reporte():
    if not os.path.isfile(RUTA_ENVIOS):
        print("No hay datos para generar reporte.")
        return

    with open(RUTA_ENVIOS, "r") as archivo:
        envios = json.load(archivo)

    

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

    # 2. Envíos por mes
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

    # 3. Tiempos promedio de entrega
    # total_tiempo = 0
    # entregados = 0
    # for e in envios:
    #     if e["estado"] == "Entregado" and "fecha_envio" in e and "fecha_entrega" in e:
    #         try:
    #             f_envio = datetime.strptime(e["fecha_envio"], "%Y-%m-%d")
    #             f_entrega = datetime.strptime(e["fecha_entrega"], "%Y-%m-%d")
    #             dias = (f_entrega - f_envio).days
    #             total_tiempo += dias
    #             entregados += 1
    #         except:
    #             continue

    # if entregados > 0:
    #     promedio = total_tiempo / entregados
    #     print(f"\n⏱️ Tiempo promedio de entrega: {promedio:.2f} días")
    # else:
    #     print("\n⏱️ No hay datos suficientes para calcular el tiempo promedio de entrega.")

    # 4. Envíos por fecha específica (opcional)
    opcion = input("\n¿Desea ver envíos por fecha específica? (s/n): ").strip().lower()
    if opcion == "s":
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        filtrados = [e for e in envios if e["fecha_envio"] == fecha]
        print(f"\n📦 Envíos en {fecha}: {len(filtrados)}")
        for e in filtrados:
            print(f"- Guía {e['numero_guia']}, Estado: {e['estado']}")
