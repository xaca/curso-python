# Crear una función que lea n números y retorne una lista
# Crear una función que calcule el promedio de una lista de números 

"""
Tener precaución con el contexto de una función, es decir el inventario interno de una función solo puede ser accedida por ella misma, no por funciones o código que este en el exterior.
"""

def leer_numeros():
    lista = []
    while True:
        try:
            print("Ingrese salir para terminar")
            n = input("Ingrese un número: ")
            if n != "salir":
                n = float(n)
                lista.append(n)
            else:
                return lista
        except:
            print("Ingrese un número válido")

def promedio(numeros):
    return sum(numeros)/len(numeros)

datos = leer_numeros() #Invocación de la función leer_numeros
print(datos)
print(promedio(datos))