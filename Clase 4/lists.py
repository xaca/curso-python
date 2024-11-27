mi_lista = ["a", "b", "c", "d", "e"]
#mi_lista = [0,   1,   2,   3,   4]

print("-----", mi_lista)
print("-----", mi_lista[3])

# Cambiar un item de la lista
mi_lista[3] = "z"
print("-----", mi_lista)
print("-----", mi_lista[3])

# Añadir elemento
mi_lista.append(42)
print("-----", mi_lista)

# Quitar elemento de acuerdo al index
mi_lista.pop(0)
print("-----", mi_lista)

# Mirar tamaño de la lista
print(len(mi_lista))
