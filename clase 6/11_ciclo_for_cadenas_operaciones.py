# Cadena: Conjunto de caracteres o valores alfanuméricos, que se encuentran entre comillas simples o dobles. También se conoce como string.

temp = "Hola"
#Convertir el texto a mayúsculas
print(temp.upper())
temp = "HOLA"

#Convertir el texto a minúsculas
print(temp.lower())

# Recorrido con for
for i in temp:
    print(i)

# Recorrido con while
i = len(temp) # Número de caracteres en la cadena
cont = 0 # Las cadenas son zero-based porque el indice empieza en 0

#print(temp[2]) Los corchetes se utilizan para acceder a un elemento de la cadena
while cont < i:
    #print(temp[cont])
    print(cont)
    cont += 1