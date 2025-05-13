from registrar_cliente import menu_clientes, listar_clientes
from registrar_envio import registrar_envio
from seguimiento import seguimiento_paquete
from actualizar_estado import actualizar_estado_envio
from reportes import generar_reporte

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar cliente")
        print("2. Registrar envío")
        print("3. Listar clientes")
        print("4. Seguimiento de paquete")
        print("5. Actualizar estado de paquete")
        print("6. Generar reporte de envíos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1": 
            menu_clientes()
        elif opcion == "2":
            registrar_envio()
        elif opcion == "3":
            listar_clientes()
        elif opcion == "4":
            seguimiento_paquete()
        elif opcion == "5":
            actualizar_estado_envio()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Gracias por usar la plataforma!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
 