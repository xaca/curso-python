lista = [1, 2, 3, 4, 5]
lista[2] = 10 # Modifica el valor de la posición 2, porque las listas son mutables
tupla = (1, 2, 3, 4, 5)
#tupla[2] = 10, no permite modificar
set_datos = {1, 2, 3, 4, 5}
set_datos.add(5)# No se agrega pero no hay error
set_datos.add(-3)
set_datos.add(18)
print(set_datos)

# Diccionarios
# Los diccionarios son una estructura de datos que permite almacenar datos de manera
# asociativa, es decir, cada elemento almacenado en un diccionario tiene una clave que
# lo identifica. La clave es única y no puede repetirse, pero el valor puede repetirse.
# Los diccionarios son mutables, es decir, se pueden modificar sus elementos.

diccionario = {
'nombre': 'Juan',
'apellido': 'Pérez',
'edad': 25,
}
print(diccionario['nombre'],diccionario['apellido'],diccionario['edad'])