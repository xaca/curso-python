lista = [True, 3.5,23,-2,"hola"]

"""
print(lista)
lista.clear()
print(lista)
"""
print(lista)
try:
    lista.remove(-2)
except:
    print("El valor no existe en la lista")
print(lista)

lista.pop()
print(lista)

print(len(lista))