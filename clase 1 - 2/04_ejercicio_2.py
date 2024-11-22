#2. Calcular la suma de n hasta m, donde n<m (No usar ciclos)

# Esta aproximación no funcionaria, no es practica la solución
suma = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(suma)

# Esta es la solución correcta, usando una formula
n = 5000
suma = (n * (n+1))/2 # Reasignación de la variable suma
print(suma)