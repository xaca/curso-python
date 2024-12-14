import os

def persona_mas_joven(datos):
    edad_menor = 99
    nombre_menor = ''
    temp = ""

    for dato in datos:
        temp = datos[dato]
        
        if temp['edad'] < edad_menor:
            edad_menor = temp["edad"]
            nombre_menor = temp["nombre"]

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
            resultado += f"{edades[i]};{nombres[i]}\n"
    return resultado

def cargar_datos():
    bandera = True
    resultado = {}
    ruta = os.path.join(os.path.dirname(__file__), "usuarios.csv")
    archivo = open(ruta, "r", encoding="utf-8")
    cont = 1
    for linea in archivo:
        if bandera:
            bandera = False
            continue
        datos = linea.split(";")
        resultado[f"usuario_{cont}"] = {"nombre":datos[0], "edad":int(datos[2]),"email":datos[3]}
        cont += 1
        #edades.append(int(datos[1]))
    
    archivo.close()

    return resultado
   

def main():
    
    datos = cargar_datos()
    
    persona_mas_joven(datos)
    """
    resultado = persona_mas_vieja(datos)

    print(f'La persona más vieja es {resultado[0]} con {resultado[1]} años.')
    
    promedio_edades(datos)
    resultado = mayores_50(datos)
    temp = []

    for i in range(len(resultado)):
        temp = resultado[i]
        print(f'La persona {temp[1]} tiene {temp[0]} años.')
    
    resultado = personas_menores_30(nombres, edades)
    print(resultado)
    """

if __name__ == '__main__':
    main()
