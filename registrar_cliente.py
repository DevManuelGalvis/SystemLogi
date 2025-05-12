import json
import os

RUTA_CLIENTES = "datos/clientes.json"

def inicializar_archivo():
    # Crea la carpeta datos si no existe.
    if not os.path.exists("datos"):
        os.makedirs("datos")

    if not os.path.isfile(RUTA_CLIENTES) or os.path.getsize(RUTA_CLIENTES) == 0:
        with open(RUTA_CLIENTES, "w") as archivo:
            json.dump([], archivo)

def cargar_clientes():
    with open(RUTA_CLIENTES, "r") as archivo:
        return json.load(archivo)

def guardar_clientes(clientes):
    with open(RUTA_CLIENTES, "w") as archivo:
        json.dump(clientes, archivo, indent=4)

def registrar_nuevo_cliente():
    clientes = cargar_clientes()

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
    guardar_clientes(clientes)
    print("✅ Cliente registrado correctamente.")

def actualizar_cliente_existente():
    clientes = cargar_clientes()

    identificacion = input("Ingrese el número de identificación del cliente a actualizar: ").strip()
    cliente = next((c for c in clientes if c["identificacion"] == identificacion), None)

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
    guardar_clientes(clientes)
    print("✅ Cliente actualizado correctamente.")

def menu_clientes():
    inicializar_archivo()
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Registrar nuevo cliente")
        print("2. Actualizar cliente existente")
        print("3. Volver al menú principal")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_nuevo_cliente()
        elif opcion == 2:
            actualizar_cliente_existente()
        elif opcion == 3:
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

def listar_clientes():
    inicializar_archivo()
    # with open(RUTA_CLIENTES, "r") as archivo:
    #     clientes = json.load(archivo)

    clientes = cargar_clientes()
    print("\nLista de Clientes Registrados:")
    for c in clientes:
        print(f"- {c['nombres']} {c['apellidos']} ({c['identificacion']})")
