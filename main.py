def Get_bus_space():
    bus_space = input('Ingrese el número de asientos')
    correct_input = False
    while correct_input == False:
        if bus_space.isdigit():
            bus_space = int(bus_space)
            correct_input = True
        else:
            bus_space = input('Ingrese un numero válido.')
    return bus_space

def Buy_tickets(tickets, free_space, tickets_sold):
    status = ''
    if tickets <= free_space:
        free_space -= tickets
        tickets_sold += tickets
        status = f'Se vendieron {tickets} billetes'
    else:
        status = f'Error'
    return status, free_space, tickets_sold

def Return_tickets(tickets, free_space, tickets_sold):
    status= ''
    if tickets <= tickets_sold:
        status = f'Se devolvieron {tickets} billetes'
        free_space += tickets
        tickets_sold -= tickets
    else:
        status = 'Error'
    return status, free_space, tickets_sold

def Bus_status(bus_space, free_space, tickets_sold):
    status = (f'Total: {bus_space}\nLibre: {free_space}\nVendido: {tickets_sold}')
    return status

def Bus():
    bus_space = Get_bus_space()
    tickets_sold = 0
    free_space = bus_space - tickets_sold
    menu = '\n1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n0.- Salir.'
    
    print(menu)
    
    run_app = True
    while run_app == True:
        option = input()
        if option == '1':
            tickets_to_buy = int(input())
            message, free_space, tickets_sold = Buy_tickets(tickets_to_buy, free_space, tickets_sold)
            print(message)
        elif option == '2':
            tickets_to_return = int(input())
            message, free_space, tickets_sold = Return_tickets(tickets_to_return, free_space, tickets_sold)
            print(message)
        elif option == '3':
            print(Bus_status(bus_space, free_space, tickets_sold))
        elif option == '0':
            run_app = False
        else:
            print('Error. Introduce un numero del menu.')

Bus()