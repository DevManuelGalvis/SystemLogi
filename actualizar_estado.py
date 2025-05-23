import os
from datetime import datetime
from utils import cargar_json, guardar_json

RUTA_ENVIOS = "datos/envios.json"

ESTADOS = [
    "Recibido",
    "En Transito",
    "En Ciudad Destino",
    "En Bodega De La Transportadora",
    "En Reparto",
    "Entregado"
]

def actualizar_estado_envio():
    if not os.path.isfile(RUTA_ENVIOS):
        print("No hay envíos registrados.")
        return

    envios = cargar_json(RUTA_ENVIOS)

    # Mostrar todos los números de guía disponibles
    print("📦 Envíos disponibles:")
    for e in envios:
        print(f"- Guía: {e['numero_guia']} | Estado: {e['estado']}")

    numero_guia = input("\nIngrese el número de guía: ").strip().upper()
    for envio in envios:
        if envio["numero_guia"] == numero_guia:
            print(f"Estado actual: {envio['estado']}")
            for i, estado in enumerate(ESTADOS):
                print(f"{i + 1}. {estado}")
            opcion = input("Seleccione nuevo estado (1-6): ")

            try:
                nuevo_estado = ESTADOS[int(opcion) - 1]
                envio["estado"] = nuevo_estado

                if nuevo_estado == "Entregado":
                    envio["fecha_entrega"] = datetime.today().strftime("%Y-%m-%d")
                    print("📅 Fecha de entrega registrada.")

                # Guardar cambios en el archivo
                guardar_json(RUTA_ENVIOS, envios)
                print("✅ Estado actualizado.")
            except:
                print("❌ Opción inválida.")
            return
    print("❌ Número de guía no encontrado.")
