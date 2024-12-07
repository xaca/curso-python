"""
 Dado el formato de fecha siguiente:
    2021-05-30 o 2021/05/30

 ¿Cómo extraemos el año, el mes y el día por separado de una fecha?

"""
fecha = "2021-05-30"
fecha = fecha.split("-")

a = int(fecha[0])
m = int(fecha[1])
d = int(fecha[2])

print(f"El año es {a}, el mes es {m} y el día es {d}")

"""
    Extraer la información del siguiente formato, teniendo en cuenta que dependiendo del separador podemor representar información asociada a unos productos, así:

    Entrada del registro:
        2,2-3,3-12,6-34,12;2300#530#1200#3000;Huevo|Leche|Pan|Queso

    Significado de cada parte:
        Codigos y cantidad: 2,1-3,3-12,6-34,12
        Precios: 2300#530#1200#3000
        Nombre: Huevo|Leche|Pan|Queso

    Crear un programa que imprima la información de la siguiente forma:

        Huevo x 2  a $2300  ... $4600
        Leche x 3  a $530   ... $1590
        Pan   x 6  a $1200  ... $7200
        Queso x 12 a $3000  ... $36000    
"""

registro = "2,2-3,3-12,6-34,12;2300#530#1200#3000;Torta de carne|Leche|Pan|Queso"
print(registro)
datos = registro.split(";")
codigos = datos[0]
precios = datos[1]
nombres = datos[2]

codigos = codigos.split("-")
precios = precios.split("#")
nombres = nombres.split("|")

cantidades = []
cod_temp = []
temp = ""

for i in range(len(codigos)):
    temp = codigos[i].split(",")
    cod_temp.append(temp[0])
    cantidades.append(temp[1])

codigos = cod_temp

print(codigos)
print(precios)
print(nombres)
print(cantidades)

#str = "texto largo muy largo"
#print(str[0:10]) # Recortar un pedazo de la cadena
total = 0

for i in range(len(codigos)):
    #Huevo x 2  a $2300  ... $4600
    nombre = nombres[i]
    nombre = nombre[0:10]
    nombre = nombre.ljust(10," ")

    print(f"{nombre} x",end=" ")

    cantidad = cantidades[i]
    if len(cantidad)<2:
        cantidad = cantidad.rjust(2,"0")
    
    print(f"{cantidad}",end=" ")

    precio = precios[i].rjust(7," ")
    print(f"a ${precio}",end=" ")

    subtotal = int(cantidad)*int(precios[i])
    total += subtotal
    print(f"... ${subtotal}")

total = str(total)
print(f"Total: ${total.rjust(29,' ')}")

    # TODO: En la salida de impresion, pegar el caracter de dinero, del valor del precio del producto. Es decir que quede $2300 en lugar de $    2300

    # TODO: Ajustar la palabra total para que se alinee con el valor total de la compra.