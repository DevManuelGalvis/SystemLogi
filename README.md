# Proyecto Logística - Gestión de Envíos

Este proyecto es un sistema de gestión de envíos y clientes para una empresa de logística, desarrollado en Python. Actualmente funciona como una aplicación de consola, pero su estructura modular permite escalarlo fácilmente para crear una aplicación de escritorio o web en el futuro.

## Características

- Registro y gestión de clientes.
- Registro y seguimiento de envíos.
- Actualización de estados de paquetes.
- Generación de reportes.
- Almacenamiento de datos en archivos JSON.

## Uso

El sistema se ejecuta desde la terminal y presenta un menú interactivo:

1. Registrar cliente
2. Registrar envío
3. Listar clientes
4. Seguimiento de paquete
5. Actualizar estado de paquete
6. Generar reporte de envíos
0. Salir

Solo necesitas seguir las instrucciones en pantalla para cada opción.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python 3.10 o superior instalado.
3. Ejecuta el sistema desde la terminal:

```sh
python main.py
```

## Escalabilidad y reutilización

El código está organizado en módulos independientes, lo que facilita su mantenimiento y ampliación. Puedes reutilizar las funciones y clases para integrarlas en otros proyectos o para desarrollar una interfaz gráfica o web en el futuro.

## Archivos de datos

Los datos se almacenan en la carpeta `datos/` en formato JSON:

- `datos/clientes.json`
- `datos/envios.json`

## Créditos

Desarrollado por DevManuelGalvis.

---
