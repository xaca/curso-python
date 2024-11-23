# Normalmente las variables pueden contener diferentes tipos, pero cuando estos datos los ingresa el usuario, normalmente son datos alfanúmericos, es decir una combinación, de números, letras y símbolos. Con los datos alfanúmericos no se puede relizar operaciones matemáticas, por lo que es necesario convertir estos datos a un tipo numérico. Para esto se utilizan los comandos int() y float().

dato = "2346" # Aunque es un número, esto es un dato alfanúmerico porque esta escrito entre comillas. El dato alfanúmerico se llama en inglés string (str) o candena de texto.

# En esta línea hay un error porque no podemos sumar o concatenar cadenas con números, por lo que es necesario convertir el dato alfanúmerico a un dato numérico.
# dato = dato + 1

dato = int(dato) # Esta operación, no siempre es posible, porque depende del valor del dato, si el valor es posible de convertirse, se hacer la operación, si no es posible, se generará un error.

dato = dato + 1 # Ahora si se puede realizar la operación porque el dato es numérico.

print(dato) # El resultado de la operación es 2347.

#dato = "345!"
#dato = int(dato) # Esta operación generará un error en tiempo de ejecución que detiene el programa porque el dato alfanúmerico no es posible convertirlo a numérico.

dato = "345.5"

dato = float(dato) # Esta operación convierte el dato alfanúmerico a un dato numérico, en este caso a un número decimal.

print(dato)

# Es posible, realizar conversiones, teniendo en cuenta la precisión de los datos, por ejemplo, si se convierte un número decimal a un número entero, se pierde la parte decimal.

dato = 345.5
dato = int(dato)
print(dato) # El resultado es 345, se pierde la parte decimal.

# La otra opción de conversión es usar el comando round(), el cual redondea el valor, teniendo presente la configuración del programador.

dato = 345.52345
dato = round(dato, 2) # Redondea el valor a dos decimales.
print(dato) # El resultado es 345.52.

# Conversion de valores booleanos
print("---- Valores booleanos ----")
print(bool("hola"))# Verdadero a una cadena diferente de vacio
print(bool("0"))# Verdadero a una cadena diferente de vacio
print(bool("0.0"))# Verdadero a una cadena diferente de vacio
print(bool("False"))# Verdadero a una cadena diferente de vacio
print(bool("None"))# Verdadero a una cadena diferente de vacio
print(bool(""))# Falso a una cadena vacia
print(bool(0)) # Falso a un número entero igual a 0
print(bool(0.0)) # Falso a un número decimal igual a 0
print(bool(False)) # Falso a un valor booleano igual a False
print(bool(None)) # Falso a un valor nulo
print(bool(35)) # Verdadero a un número entero diferente de 0

# Todos los símbolos o caracteres del teclado tienen un valor numérico, por lo que se pueden convertir a un número entero. Eso se conocer como el código ASCII. Para convertir un carácter a un número entero se utiliza el comando ord().

#ord convierte de un caracter a un número entero
print(ord("@"))

#chr convierte de un número entero a un caracter
print(chr(64))

