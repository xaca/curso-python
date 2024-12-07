"""
Crear una función, que dependiendo de la hora militar, imprima un saludo. Si la hora es menor a 12, imprimir "Buenos días", si la hora es mayor o igual a 12 y menor a 19, imprimir "Buenas tardes", si la hora es mayor o igual a 19, imprimir "Buenas noches".

Modificar el siguiente código para que se ejecute dentro de una función llamada saludo_hora_militar.

hora = 20

if hora < 12:
    print("Buenos días")
elif hora < 19:
    print("Buenas tardes")
elif hora < 24:
    print("Buenas noches")
else:
    print("Hora no válida")

"""

def saludo_hora_militar(hora):
    if hora < 12:
        print("Buenos días")
    elif hora < 19:
        print("Buenas tardes")
    elif hora < 24:
        print("Buenas noches")
    else:
        print("Hora no válida")

#Invocación de la función
saludo_hora_militar(20) # Buenas noches
saludo_hora_militar(5) # Buenos días
saludo_hora_militar(14) # Buenas tardes
saludo_hora_militar(12) # Buenas tardes