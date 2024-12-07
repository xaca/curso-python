""" 
Ejercicios:

1. Leer una lista de números e imprimir la lista con el siguiente formato de salida:

    Entrada: [2, 4, 6, 8, 10]
    Salida: |2-4-6-8-10| o |2 - 4 - 6 - 8 - 10|

2. Realizar un programa que pida n valores númericos, y calcule el promedio de los valores ingresados.

    Entrada: [2, 4, 6, 8, 10]
    Salida: 6.0

"""
lista = []
while True:
    try:
        print("Ingrese salir para terminar")
        n = input("Ingrese un número: ")
        if n != "salir":
            n = float(n)
            lista.append(n)
        else:
            break
    except:
        print("Ingrese un número válido")

print(lista)

print("|", end="")

for i in lista:
    if i == lista[-1]:
        print(i, end="") # Impresion en la misma linea
    else:
        print(i, end=" - ")# Impresion en la misma linea pero con un guión

print("|")

print(f"El promedio es {sum(lista)/len(lista)}")