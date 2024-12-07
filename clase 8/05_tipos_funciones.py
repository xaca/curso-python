"""
Función: Es un bloque de codigo, que se agrupa bajo un nombre descriptivo, para poder ser reutilizado en cualquier parte del programa. Por lo general, las funciones reciben parametros y devuelven un resultado.

Tipos de funciones:

1. Funciones sin parametros y sin retorno
2. Funciones sin parametros y con retorno
3. Funciones con parametros y sin retorno
4. Funciones con parametros y con retorno

¿Como se define una función en Python?

def nombre_funcion(parametros):
    # Cuerpo de la función
    return resultado # Opcional

Un parametro es una variable. Los parametros son los valores que recibe la función para realizar una operación.
    
Para llamar a una función se utiliza el nombre de la función seguido de parentesis y los argumentos que recibe la función. 

nombre_funcion(argumentos)

Nota: Si la función no recibe parametros, los parentesis se dejan vacios, sin argumentos.

"""
# Funciones sin parametros y sin retorno
def saludar():
    print("Hola mundo")

saludar() # Invocación o llamado de la función

# Funciones sin parametros y con retorno
def obtener_nombre():
    return "Juan"

nombre = obtener_nombre()
print(nombre) # Juan

# Funciones con parametros y sin retorno
def sumar(a, b):
    print(a + b)

sumar(5, 3) # 8
sumar(10, 20) # 30
sumar(23, 54) # 77

# Funciones con parametros y con retorno

def multiplicar(a, b):
    return a * b

resultado = multiplicar(5, 3)
print(resultado) # 15
