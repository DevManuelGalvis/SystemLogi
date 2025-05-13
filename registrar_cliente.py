import json
import os
from utils import inicializar_archivo, cargar_json, guardar_json

RUTA_CLIENTES = "datos/clientes.json"

def registrar_nuevo_cliente():
    # Funcion para registrar clientes
    clientes = cargar_json(RUTA_CLIENTES)

    identificacion = input("Número de identificación: ").strip()
    if any(cliente["identificacion"] == identificacion for cliente in clientes):
        print("⚠️ Ya existe un cliente con ese número de identificación.")
        return

    cliente = {
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "identificacion": identificacion,
        "tipo_identificacion": input("Tipo de identificación (CC, TI, CE): ").upper(),
        "direccion": input("Dirección: "),
        "telefono_fijo": input("Teléfono fijo: "),
        "numero_celular": input("Número celular: "),
        "barrio": input("Barrio de residencia: ")
    }

    clientes.append(cliente)
    guardar_json(RUTA_CLIENTES, clientes)

    print("✅ Cliente registrado correctamente.")

def actualizar_cliente_existente():
    # Funcion para actualizar datos del cliente registrado.
    clientes = cargar_json(RUTA_CLIENTES)

    identificacion = input("Ingrese el número de identificación del cliente a actualizar: ").strip()
    # cliente = next((c for c in clientes if c["identificacion"] == identificacion), None)
    clientes_dict = {c["identificacion"]: c for c in clientes}
    cliente = clientes_dict.get(identificacion)


    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    print("Ingrese los nuevos datos del cliente (deje en blanco si no desea cambiar un campo):")

    nuevos_datos = {
        "nombres": input(f"Nombres [{cliente['nombres']}]: ") or cliente["nombres"],
        "apellidos": input(f"Apellidos [{cliente['apellidos']}]: ") or cliente["apellidos"],
        "tipo_identificacion": input(f"Tipo de identificación [{cliente['tipo_identificacion']}]: ").upper() or cliente["tipo_identificacion"],
        "direccion": input(f"Dirección [{cliente['direccion']}]: ") or cliente["direccion"],
        "telefono_fijo": input(f"Teléfono fijo [{cliente['telefono_fijo']}]: ") or cliente["telefono_fijo"],
        "numero_celular": input(f"Número celular [{cliente['numero_celular']}]: ") or cliente["numero_celular"],
        "barrio": input(f"Barrio de residencia [{cliente['barrio']}]: ") or cliente["barrio"]
    }

    cliente.update(nuevos_datos)
    guardar_json(RUTA_CLIENTES, clientes)
    print("✅ Cliente actualizado correctamente.")

def menu_clientes():
    # Menu de opciones
    inicializar_archivo()
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Registrar nuevo cliente")
        print("2. Actualizar cliente existente")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_nuevo_cliente()
        elif opcion == "2":
            actualizar_cliente_existente()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

def listar_clientes():
    # Mostrar todos los clientes registrados
    inicializar_archivo()
    clientes = cargar_json(RUTA_CLIENTES)
    print("\nLista de Clientes Registrados:")
    for c in clientes:
        print(f"- {c['nombres']} {c['apellidos']} ({c['identificacion']})")
