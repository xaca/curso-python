#Calcular la suma de n hasta m, donde n<m (Usar ciclos)
# Este ejercicio usa una bandera como control de los valores de entrada
n = 0
m = 0
suma = 0
error = True

while error:
    n = input("Ingrese el valor de n: ")
    m = input("Ingrese el valor de m: ")

    try:
        n = int(n)
        m = int(m)

        if n < m:
           error = False
        else:
            print("n debe ser menor que m")     
            error = True
    except:
        print("Valor incorrecto")
        error = True

# Si llegamos hasta esta parte, es porque los valores ingresados son correctos.
for i in range(n, m+1):
    suma = suma + i

print(f"La suma de los números de {n} hasta {m} es: {suma}")