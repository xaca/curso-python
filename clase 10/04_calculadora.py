# Crear un menu con una decoracion usando ASCII, donde el usuario por medio de una seleccion, acceda a un submenu.
# El ejemplo de la clase, será un menú para cambiar entre calculadora básica y calculadora científica.

# Primera parte validar la interfaz gráfica personalizada, que no contenga warnings.
# Segunda parte, validar la funcionalidad del menú, que permita al usuario seleccionar calculadora cientifica y acceder al submenu.
# Tercera parte, validar la funcionalidad del submenu, regresar al menú principal.

# TODO: Terminar la calculadora científica y el resto de operaciones pendientes

# Nueva versión calculadora científica
import math

def menu(tipo):
    opcion = -1
    error = False

    txt_submenu = """ 
      ____________________________
     |  ________________________  |
     | |                        | |
     | |                        | |
     | |     Calculadora        | |
     | |     Cientifica         | |
     | |      1. Seno           | |
     | |      2. Coseno         | |
     | |      3. Raíz           | |
     | |      0. Regresar       | |
     | |________________________dc|
     |____________________________|
     """

    txt_menu = """
         ______________________________
     // \\                            \\.
    |   |                            |.
     \\_ |    Bienvenidos a la        |.
        |     Calculadora            |.
        |                            |.
        |      1. Sumar              |.
        |      2. Restar             |.
        |      3. Dividir            |.
        |      4. Cientifica         |.
        |      5. Salir              |.
        |   _________________________|___
        |  //                            //.
        \\_//dc__________________________//.

        """

    if tipo == 1:
        print(txt_menu)
    
    if tipo == 2:
        print(txt_submenu)

    opcion = input("Seleccione una opción: ")

    try:
        opcion = int(opcion)
    except:
        print("Valor incorrecto")

    return opcion

def leer_numero():
    while True:
        a = input("Ingrese el número: ")
        try:
            a = float(a)
            return a
        except:
            print("Valor incorrecto")
            continue

def sumar():
    print("Ingrese los números a sumar")
    a = leer_numero()
    b = leer_numero()
    print(f"La suma es {a+b}")

def restar():
    print("Ingrese los números a restar")
    a = leer_numero()
    b = leer_numero()
    print(f"La resta es {a-b}")

def dividir():
    print("Ingrese los números a dividir")
    while True:
        a = leer_numero()
        b = leer_numero()
    
        if b == 0:
            print("No se puede dividir por cero")
            continue
        else:
            print(f"La división es {a/b}")
            break

def raiz():
    print("Ingrese el número al que se le calculará la raíz")
    while True:
        a = leer_numero()
        if a < 0:
            print("No se puede calcular la raíz de un número negativo")
            continue
        else:
            print(f"La raíz es: {a**(1/2)}")
            break

def seno():
    print("Ingrese el número al que se le calculará el seno")
    a = leer_numero()
    print(f"El seno es {math.sin(a)}")

def coseno():
    print("Ingrese el número al que se le calculará el coseno")
    a = leer_numero()
    print(f"El coseno es {math.cos(a)}")

def main():
    opcion = -1
    while opcion != 5:
        opcion = menu(1)
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            dividir()
        elif opcion == 4:
            while opcion != 0:
                opcion = menu(2)                
                if opcion == 1:
                    seno()
                elif opcion == 2:
                    coseno()
                elif opcion == 3:
                    raiz()
                elif opcion == 4:
                    break 

        input("Presione enter para continuar")

if __name__ == "__main__":
    main()
    