# Crear tres listas, la primera es una lista donde estan los precios de los productos, el codigo del producto, equivale al indice positivo de la lista.

# La segunda lista, contiene la cantidad de cada producto, ordenado por medio del indice positivo de la lista.

# La última lista, es factura que permite calcular el subtotal, teniendo presente que el producto se ingresa por codigo, para calcular el valor facturado por producto. Al finalizar se totaliza el consumo.

nombres = ["arroz","papa","carne","pollo","aceite","sal"]
precios = [1500,2000,50000,40000,12000,3000]
print("cantidad de productos",len(precios))
cantidad = [1,0,0,0,1,0]
factura = []
subtotal = 0

for i in range(len(precios)):
    if cantidad[i]>0:
        subtotal = subtotal + precios[i]*cantidad[i]
        print(nombres[i].capitalize(),precios[i],cantidad[i],precios[i]*cantidad[i])

print(str(subtotal).rjust(20,"-"))

#TODO: Mejorar la impresión de la factura, tenga en cuenta el espacio del ancho y un contenido proporcional que sea legible