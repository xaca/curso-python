bandera = True

# Debemos tener precaución con los ciclos infinitos, estos se presentan cuando la condición siempre es verdadera, la clave para salir del ciclo, debe estar en el cuerpo del ciclo.
# No se debe tener miedo a un ciclo infinito, para detener el ciclo, se puede digitar la combinación de teclas en la consola de Python, Ctrl + C. O detener la terminal donde se esta ejecutando el código.

while bandera:
    print("Hola")
    bandera = False

