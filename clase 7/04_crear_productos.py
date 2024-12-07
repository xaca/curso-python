productos = []

while True:
    print("Ingrese un producto o escriba 'salir' para terminar")
    producto = input("Ingrese un producto: ")
    if producto == "salir":
        break
    productos.append(producto)

for i in productos:
    print(i)