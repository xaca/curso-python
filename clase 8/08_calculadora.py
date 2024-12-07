# Crear las funciones suma, resta, multiplicación y división, que reciban dos números y retornen el resultado de la operación. E invocarla desde una función llamada menu. 

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def menu():
    while True:
        try:
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Salir")
            opcion = int(input("Ingrese una opción: "))
            if opcion == 5:
                break
            else:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                if opcion == 1:
                    print(suma(a, b))
                elif opcion == 2:
                    print(resta(a, b))
                elif opcion == 3:
                    print(multiplicacion(a, b))
                elif opcion == 4:
                    if b == 0:
                        print("No se puede dividir por cero")
                    else:
                        print(division(a, b))
                else:
                    print("Opción no válida")
        except:
            print("Ingrese un número válido")