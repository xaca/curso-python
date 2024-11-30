# Invertir una cadena de texto
cadena = "Hola Mundo"
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end="")
print()

cont = len(cadena) - 1
salida = ""
for i in cadena:
    salida += cadena[cont]  
    cont -= 1  
print(salida)

cont = len(cadena) - 1
while cont >= 0:
    print(cadena[cont], end="")
    cont -=1

# Pasar una cadena a minusculas y mayusculas, por ejemplo:
# "Hola Mundo" -> "HoLa MuNdO"
print()
cadena = "Hola Mundo"
salida = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        salida += cadena[i].upper()
    else:
        salida += cadena[i].lower()
print(salida)

# Calcular si una cadena es palindroma, por ejemplo:
# "Anita lava la tina" -> True
# "Hola Mundo" -> False
# "Reconocer" -> True
