n = 0
intentos = 3
clave = "1234"

for i in range(1,4):
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


"""
    for i in range(1,11):
        print(i)

    print("----")

    for i in range(1,21):
        if i > 10:
            break
        print(i)
"""