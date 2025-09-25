from cliente import Cliente
from bus import Bus
from billetes import Billete

menu = "\n1. - Crear bus\n2.- Venta de billetes\n3.- Devolución de billetes\n4.- Estado de la venta\n0.- Salir"

buses = []

while True:
    bus_id = str(input("ID bus: "))
    capacidad = int(input("Número total de plazas del bus: "))
   
    bus = Bus(bus_id, capacidad)
    
    print(menu)
    opcion = input("Opción: ")

    if opcion == "1":
        bus_id = input("Bus ID: ")
        capacidad = int(input("Número plazas: "))
        bus = Bus(bus_id, capacidad)
        buses.append(bus)
        print(f"Bus {bus_id} con capacidad {capacidad}.")
    
    elif opcion == "2":
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")
        cliente = Cliente(nombre, apellido)
        billete = Billete(cliente, bus)
        print(billete.vender())

    elif opcion == "3":
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")
        cliente = Cliente(nombre, apellido)
        billete = Billete(cliente, bus)
        print(billete.devolver())

    elif opcion == "4":
        print(bus.estado_bus())

    elif opcion == "0":
        break

    else:
        print("Opción no válida")