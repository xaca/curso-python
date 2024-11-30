# Este es un programa que calcula el pago de un producto, permitiendo al usuario seleccionar el método de pago, el programa se ejecuta hasta que el usuario seleccione un método de pago válido.

pago = False
tipo_pago = 0

#Al evaluar un ciclo, debemos validar que se ingrese al menos una vez al ciclo y que podamos salir de él, por medio de una actualización del estado de la bandera.

while not pago:
    print("Seleccione el método de pago")
    print("1. Efectivo")
    print("2. Transferencia")
    print("Un valor diferente es incorrecto y se termina el programa")
    tipo_pago = input("Ingrese el método de pago: ")
    
    try:
        tipo_pago = int(tipo_pago)

        if tipo_pago == 1:
            print("pago con efectivo")
            pago = True
        elif tipo_pago == 2:
            print("pago con transferencia")
            pago = True
        else:
            print("El programa se termina")

        if pago:
            print("Gracias por su compra")
        
        pago = True

    except:
        print("Valor incorrecto")
        pago = False
