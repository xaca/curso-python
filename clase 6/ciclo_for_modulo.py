# Calcular el promedio de los número pares de n hasta m, donde n<m (Usar ciclos)
# Pista: Usar el operador módulo
# Un número par es aquel que es divisible por 2, es decir, el residuo de la división entre 2 es 0.

suma = 0
total = 0
for i in range(1,21):
    if i % 2 == 0:
        suma = suma + i
        total += 1

print("El promedio de los números pares de 1 hasta 20 es", suma/total)