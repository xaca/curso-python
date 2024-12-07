# Lista, es un conjunto de datos relacionados entre sí, bajo un mismo nombre de variable y que se pueden acceder por medio de un índice. El indice, permite acceder a las posiciones donde estan los valores almacenados.

# Crear una lista
# Una lista se crea con corchetes [] y los valores separados por comas.
# Ejemplo
# Crear una lista de números
numeros = [] # Lista vacía
print(numeros)
numeros.append(23)# Agregar un valor a la lista
print(numeros)
numeros.append(12)
print(numeros)
numeros.append(5)
numeros.append(5)
print(numeros)
numeros.append(8)
print(numeros)

# Acceso a los elementos de la lista
print(numeros[2])
print(numeros[-2])

# Modificar un elemento de la lista, se debe pasar un valor de posición que este dentro del rango de la lista.
numeros[4] = 88
print(numeros)

# Agregar un elemento en una posición específica
numeros.insert(2, 100)
numeros.insert(1, 5)

# Para conocer el total de elementos en una lista, se usa len()

print(numeros)
print("Total de elementos:",len(numeros))

# Eliminar un elemento de la lista
# Se puede eliminar un elemento por su valor o por su posición
# Eliminar por valor
print(numeros)
numeros.remove(5)
print(numeros)

# Eliminar por posición
print(numeros)
numeros.pop(2)
print(numeros)

# Es posible eliminar un elemento por su posición
del numeros[2]

""" Ejemplo al borrar la variable
x = 4
print(x)
del x
print(x)
"""

for i in numeros:
    print(i)
