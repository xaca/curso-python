#Calcular el promedio los números enteros de n hasta m, donde n<m (Usar ciclos)

n = 0
m = 0
suma = 0
total = 0

while True:
    n = input("Ingrese el valor de n: ")
    m = input("Ingrese el valor de m: ")

    try:
        n = int(n)
        m = int(m)

        if n < m:
           break
        else:
            print("n debe ser menor que m") 
            # continue, no es necesario porque el ciclo se termina en la siguiente línea    
    except:
        print("Valor incorrecto")
        # continue, no es necesario porque el ciclo se termina en la siguiente línea 

# Si llegamos hasta esta parte, es porque los valores ingresados son correctos.
for i in range(n, m+1):
    suma = suma + i
    total += 1

print("El promedio de los números enteros de", n, "hasta", m, "es", suma/total)