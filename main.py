from cliente import Cliente
from bus import Bus
from billetes import Billete

menu = "\n1. - Escoge bus\n2.- Venta de billetes\n3.- Devolución de billetes\n4.- Estado de la venta\n0.- Salir"

buses = [
    Bus("V23", 30),
    Bus("H10", 20),
    Bus("39", 25),
    Bus("D40", 15)
]

def elegir_bus():
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

    if opcion == "1":  
        bus_seleccionado = elegir_bus()
        nombre = input("Nombre cliente: ")
        apellido = input("Apellido cliente: ")
        cliente = Cliente(nombre, apellido)
        billete = Billete(cliente, bus_seleccionado)
        resultado = billete.vender()
        if resultado:
            print(f"Billete vendido: {cliente} en bus {bus_seleccionado.getIdBus()}")
        else:
            print("No se pudo vender el billete.")
    
    elif opcion == "2":  
        bus_seleccionado = elegir_bus()
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")
        cliente = Cliente(nombre, apellido)
        billete = Billete(cliente, bus_seleccionado)
        exito = billete.devolver()
        if exito:
            print(f"Billete devuelto: {cliente} del bus {bus_seleccionado.getIdBus()}")
        else:
            print("No se encontró billete para devolver.")

    elif opcion == "3":  
        bus_seleccionado = elegir_bus()
        print(bus_seleccionado.estado())

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")