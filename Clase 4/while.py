
"""
contador = 1  # Inicializamos el contador

while contador <= 5:  # Mientras el contador sea menor o igual a 5
    print("Número:", contador)
    contador += 1  # Incrementamos el contador

print("Fin del bucle while")

#////////////////////// while else /////////////////////

contador = 0

while contador <= 5:
    print(contador)
    contador = contador + 1

else:
    print("No se cumple la condición")

    
#/////////////// Break /////////////////////
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
    if contador == 3:
        break
print("finalizó el ciclo")

#/////////////// Continue /////////////////////


count = 0
while count < 5: # Mientras se cumpla la condición
    if count == 3:
        count += 1
        print("Debería imprimir 3")
        continue

    print("count:", count)
    count += 1



count = 2
while count <= 32: # Mientras se cumpla la condición
    if count == 16:
        count = count * 2
        print("Para la ejecución actual, deber imprimir 16")
        continue # Ignora lo que sigue y continua con la siguiente iteración

    print("count:", count)
    count = count * 2
"""

while True:  # Condición siempre verdadera
    print("Obedece")
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        break

print("Bucle terminado")