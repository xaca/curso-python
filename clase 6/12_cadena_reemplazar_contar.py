# Eliminar las vocales de una cadena
cadena = "Hola MUndo Alegre"
cadena = cadena.lower()
#cadena = cadena.replace("a", "")
#cadena = cadena.replace("e", "")
#cadena = cadena.replace("i", "")
#cadena = cadena.replace("o", "")
#cadena = cadena.replace("u", "")
#print(cadena)

for temp in cadena:
    if temp in "aeiou":
        cadena = cadena.replace(temp, "") 
print(cadena)

# Eliminar las consonantes de una cadena
cadena = "Hola MUndo Alegre"
cadena = cadena.lower()
for temp in cadena:
    #print(not (temp in "aeiou"))
    if not (temp in "aeiou"):
        cadena = cadena.replace(temp, "") 
print(cadena)

# Reemplazar las vocales de una cadena por un guion

cadena = "Hola MUndo Alegre"
for temp in cadena:
    if temp in "aeiou":
        cadena = cadena.replace(temp, "-") 
print(cadena)

# Buscar la primera ocurrencia de una subcadena en una cadena y eliminarla
# Si la cadena es: "hola mundo, hola soledad"
# Pedimos las ocurrencia de hola: 2, cantidad de apariciones de hola en la cadena

cadena = "Hola Mundo Alegre"
subcadena = "Mundo"
ocurrencias = cadena.count(subcadena)

if ocurrencias > 0:
    cadena = cadena.replace(subcadena, "")
print(cadena)

# A la salida del programa anterior, dejar solo como separador un espacio

# Contar las ocurrencias de una subcadena en una cadena

cadena = "hola mundo hola soledad hola"
subcadena = "hola"
print(cadena.count(subcadena))

