# Crear un menu con una decoracion usando ASCII, donde el usuario por medio de una seleccion, acceda a un submenu.
# El ejemplo de la clase, será un menú para cambiar entre calculadora básica y calculadora científica.

# Primera parte validar la interfaz gráfica personalizada, que no contenga warnings.
# Segunda parte, validar la funcionalidad del menú, que permita al usuario seleccionar calculadora cientifica y acceder al submenu.
# Tercera parte, validar la funcionalidad del submenu, regresar al menú principal.

# Primera parte
opcion = 0
error = False

while opcion != 5:

    print("  ______________________________")
    print(" // \\                            \\.")
    print("|   |                            |.")
    print(" \\_ |    Bienvenidos a la        |.")
    print("    |     Calculadora            |.")
    print("    |                            |.")
    print("    |      1. Sumar              |.")
    print("    |      2. Restar             |.")
    print("    |      3. Dividir            |.")
    print("    |      4. Cientifica         |.")
    print("    |      5. Salir              |.")
    print("    |   _________________________|___")
    print("    |  //                            //.")
    print("    \\_//dc__________________________//.")

    opcion = input("Seleccione una opción: ")

    try:
        opcion = int(opcion)
    except:
        print("Valor incorrecto")
        error = True

    if error:
        continue
        error = False

    if opcion == 1:
        print("Sumar")
    elif opcion == 2:
        print("Restar")
    elif opcion == 3:
        a = input("Ingrese el numerador:")
        b = input("Ingrese el denominador:")
        try:
            a = float(a)
            b = float(b)
            if b == 0:
                print("No se puede dividir por cero")
                continue
            else:
                print(a/b)
        except:
            print("Valor incorrecto")
            continue
    elif opcion == 4:
        print("  ____________________________")
        print(" |  ________________________  |")
        print(" | |                        | |")
        print(" | |                        | |")
        print(" | |     Calculadora        | |")
        print(" | |     Cientifica         | |")
        print(" | |      1. Seno           | |")
        print(" | |      2. Coseno         | |")
        print(" | |      3. Raíz           | |")
        print(" | |      4. Regresar       | |")
        print(" | |________________________dc|")
        print(" |____________________________|")

    input("Presione enter para continuar")
    