n = 0
intentos = 3
clave = "1234"

while True:
    n = input("Ingrese su clave: ")

    if n == clave:
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print("Clave incorrecta, le quedan", intentos, "intentos")

    if intentos == 0:
        print("Acceso denegado")
        break

