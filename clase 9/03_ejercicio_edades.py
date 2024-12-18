"""
    Escriba un programa que lea el nombre y la edad de cualquier cantidad de personas y escriba algunos resultados.

    Se deben definir las siguientes funciones:

    - Función que lea los datos de cada persona (nombre, edad) y los almacente en listas, cero (0) para terminar. Realizar validación de edad entre 18 y 65 años. El nombre debe tener seis (6) o más caracteres, y no puede tener más de 30.

    - Función que reciba las listas de nombres y edades y que escriba los siguientes resultados: 

        - Nombre y edad de la persona más joven del grupo
        - Nombre y edad de la persona más vieja del grupo

    - Función que reciba las listas de nombres y edades y que escriba los siguientes resultados:

        - Promedio de edades
        - Número de personas mayores de 50 años
        - Promedio edad de las personas menores de 30 años

    Se puede usar len, append, pop, insert.

"""

def leer_nombres():
    nombres = []

    while True:
        nombre = input('Nombre: ')
        if nombre == '0':
            break
        if len(nombre) < 6 or len(nombre) > 30:
            print('El nombre debe tener entre 6 y 30 caracteres.')
            continue

        nombres.append(nombre)
    
    return nombres

def leer_edades(nombres):
    edades = []

    for nombre in nombres:
        while True:
            try:
                edad = int(input(f'Edad de {nombre}: '))
                if edad == 0:
                    break
                if edad < 18 or edad > 65:
                    print('La edad debe estar entre 18 y 65 años.')
                    continue

                edades.append(edad)
                break
            except:
                print('Edad inválida.')
    return edades

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

def main():
    resultado = ""
    nombres = leer_nombres()
    edades = leer_edades(nombres)
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
