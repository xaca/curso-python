# Crear una función que lea n números y retorne una lista
# Crear una función que calcule el promedio de una lista de números 

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

def promedio(lista):
    return sum(lista)/len(lista)

lista = leer_numeros()
print(lista)
print(promedio(lista))