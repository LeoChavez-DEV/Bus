from cliente import Cliente
from bus import Bus
from billetes import Billete

menu = """
Menú:
1.- Crear bus
2.- Ver buses existentes
3.- Venta de billetes
4.- Devolución de billetes
5.- Estado de la venta
0.- Salir
"""
error_nombre = "Texto inválido.\nNo puede estar vacío.\nNo puede tener más de 20 caracteres.\nSolo caracteres alfabéticos.\nSin espacios."
buses = []

def añadir_bus(idBus, capacidad):
    nuevo_bus = Bus(idBus, capacidad)
    buses.append(nuevo_bus)
    print(f"Bus añadido: ID {idBus}, Capacidad {capacidad}")

def elegir_bus():
    if not buses:
        print("No hay buses creados.")
        return None
    print("\nSeleccione un bus:")
    for i, b in enumerate(buses):
        print(f"{i+1}. ID: {b.getIdBus()}, Capacidad: {b.getCapacidad()}, Libre: {b.capacidadLibre()}")
    while True:
        seleccion = input("Opción: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(buses):
            return buses[int(seleccion)-1]
        print("Opción inválida, intente de nuevo.")

while True:
    print(menu)
    opcion = input("Opción: ").strip()

    if opcion == "0":
        print("Saliendo del sistema")
        break

    elif opcion == "1":  
        idBus = input("ID del nuevo bus: ")
        if idBus.strip() == "":
            print("ID inválido. No puede estar vacío.")
            continue

        if idBus in [b.getIdBus() for b in buses]:
            print("ID ya existe. Elija otro.")
            continue

        if len(idBus) > 5:
            print("ID inválido. Máximo 5 caracteres.")
            continue

        if not idBus.isalnum():
            print("ID inválido. Solo caracteres alfanuméricos.")
            continue


        capacidad = input("Capacidad del nuevo bus: ")
        if capacidad.isdigit() and int(capacidad) >= 5 and int(capacidad) <= 100:
            añadir_bus(idBus, int(capacidad))
        else:
            print("Capacidad inválida. Debe ser un número positivo, mayor o igual a 5 y menor o igual a 100.") 

    elif opcion == "2":  
        if not buses:
            print("No hay buses creados.")
        else:
            print("\nBuses existentes:")
            for b in buses:
                 print(f"ID: {b.getIdBus()}, Capacidad: {b.getCapacidad()}, Libre: {b.capacidadLibre()}")
        
    elif opcion == "3":  
        bus_seleccionado = elegir_bus()

        if bus_seleccionado:
            nombre = input("Nombre cliente: ")
            if nombre.strip() == "":
                print(error_nombre)
                continue
            if len(nombre) > 20:
                print(error_nombre)
                continue
            if not nombre.isalpha():
                print(error_nombre)
                continue

            apellido = input("Apellido cliente: ")
            if apellido.strip() == "":
                print(error_nombre)
                continue
            if len(apellido) > 20:
                print(error_nombre)
                continue
            if not apellido.isalpha():
                print(error_nombre)
                continue

            cliente = Cliente(nombre, apellido)
            billete = Billete(cliente, bus_seleccionado)
            if billete.vender():
                print(f"Billete vendido: {cliente} en bus {bus_seleccionado.getIdBus()}")

    elif opcion == "4":
        bus_seleccionado = elegir_bus()
        if bus_seleccionado:
            nombre = input("Nombre cliente: ")
            apellido = input("Apellido cliente: ")
            cliente = Cliente(nombre, apellido)
            billete = Billete(cliente, bus_seleccionado)
            if billete.devolver():
                print(f"Billete devuelto: {cliente} del bus {bus_seleccionado.getIdBus()}")

    elif opcion == "5": 
        bus_seleccionado = elegir_bus()
        if bus_seleccionado:
            print(bus_seleccionado.estado())

# comentario prueba git
# comentario prueba git