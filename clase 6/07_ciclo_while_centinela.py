intentos = 3
clave = "1234"
temp = ""

while intentos > 0:
    temp = input("Ingrese la clave: ")
    if temp == clave:
        print("Clave correcta")
        intentos = 0
        continue
    else:
        print("Clave incorrecta")
        intentos -= 1
        print("Intentos restantes:", intentos)
    
    print("Este mensaje no siempre se imprime")
    if intentos == 0:
        print("Se acabaron los intentos")
        print("Bloquear cuenta")