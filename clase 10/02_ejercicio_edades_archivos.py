import os

def persona_mas_joven(nombres, edades):
    edad_menor = 0
    nombre_menor = ''

    edad_menor = edades[0]
    nombre_menor = nombres[0]

    for i in range(1,len(edades)):

        if edades[i] < edad_menor:
            edad_menor = edades[i]
            nombre_menor = nombres[i]
    
    if edad_menor == 0:
        print('No hay personas registradas.')
    else:
        print(f'La persona más joven es {nombre_menor} con {edad_menor} años.')

def persona_mas_vieja(nombres, edades):

    nombre_mayor = nombres[0]
    edad_mayor = edades[0]
    resultado = []
    
    for i in range(1,len(nombres)): 
        if edades[i] > edad_mayor:
            edad_mayor = edades[i]
            nombre_mayor = nombres[i]
    
    resultado.append(nombre_mayor)
    resultado.append(edad_mayor)

    return resultado
    #print(f'La persona más vieja es {nombre_mayor} con {edad_mayor} años.')

def promedio_edades(edades):
    print(f"El promedio de edades es {sum(edades)/len(edades)}")

def mayores_50(nombres, edades):
    resultado = []
    temp = []
    for i in range(len(edades)):
        if edades[i] > 50:
            temp = []
            temp.append(edades[i])
            temp.append(nombres[i])
            resultado.append(temp)
    return resultado

def personas_menores_30(nombres, edades):
    resultado = ""
    for i in range(len(edades)):
        if edades[i] < 30:
            resultado += f"{edades[i]}#{nombres[i]};"
    return resultado

def cargar_datos():
    nombres = []
    edades = []
    ruta = os.path.join(os.path.dirname(__file__), "usuarios.txt")
    archivo = open(ruta, "r", encoding="utf-8")
    for linea in archivo:
        datos = linea.split("#")
        nombres.append(datos[0])
        edades.append(int(datos[1]))
    archivo.close()
    print(nombres)
    print(edades)

def main():
    resultado = ""
    
    cargar_datos()
    
    return
    persona_mas_joven(nombres, edades)
    resultado = persona_mas_vieja(nombres, edades)

    print(f'La persona más vieja es {resultado[0]} con {resultado[1]} años.')
    
    promedio_edades(edades)
    resultado = mayores_50(nombres, edades)
    temp = []

    for i in range(len(resultado)):
        temp = resultado[i]
        print(f'La persona {temp[1]} tiene {temp[0]} años.')
    
    resultado = personas_menores_30(nombres, edades)
    print(resultado)


if __name__ == '__main__':
    main()
