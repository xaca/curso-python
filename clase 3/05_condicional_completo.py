# Llamamos condicional completo, a una estructura de control que esta compuesta mínimo de dos partes, el bloque que se ejecuta si la instrucción es verdadera y el bloque que se ejecuta si la insttrucción es falsa.

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Los bloques pueden ser de una o múltiples sentencias, pero siempre deben estar identados.

# Ejercicio: Definir una variable, que contenga un valor de la hora en formato militar, y el programa debe imprimir un saludo dependiendo de la hora. Si la hora es menor a 12, imprimir "Buenos días", si la hora es mayor o igual a 12 y menor a 19, imprimir "Buenas tardes", si la hora es mayor o igual a 19, imprimir "Buenas noches".

hora = 20

if hora < 12:
    print("Buenos días")
elif hora < 19:
    print("Buenas tardes")
elif hora < 24:
    print("Buenas noches")
else:
    print("Hora no válida")

# elif es una opción que permite adicionarle más condiciones a un condicional, se pueden tener tantos elif como se necesiten.

# Dentro de un bloque, puedo anidar otras sentencias, incluso se pueden usar otros condicionales.

# Ejemplo: 

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    if edad >= 60:
        print("Eres un adulto mayor")
else:
    print("Eres menor de edad")

# Lo anterior es equivalente a tener

if edad >= 18 and edad >= 60:
    print("Eres mayor de edad")
    print("Eres un adulto mayor")
else:
    print("Eres menor de edad")

# Y otra opción usando elif sería

if edad >= 60:
    print("Eres un adulto mayor")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Se pueden tener diferentes niveles de anidación, sin embargo tenga presente, hacer un uso adecuado de la identación, para que el código sea más legible.

if True:
    print("Hola")
    if True:
        print("Mundo")
        if True:
            print("!!!")
            if True:
                print("!!!")
                if True:
                    print("!!!")
                    if True:
                        print("!!!")
                        if True:
                            print("!!!")
else:
    print("Mundo")
