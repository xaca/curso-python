error = False

# Debemos tener precaución con los ciclos infinitos, estos se presentan cuando la condición siempre es verdadera, la clave para salir del ciclo, debe estar en el cuerpo del ciclo.

while not error:
    print("Ingresa al ciclo")
    error = True # La clave para salir del ciclo.