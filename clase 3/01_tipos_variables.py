# Contador, variable que permite incrementar un valor, en este caso se inicializa en 0
# Se usan números enteros, para contar de uno en uno

contador = 0

contador = contador + 1 # Incremento de la variable en una unidad

print(contador) # Se imprime el valor de la variable contador

contador = contador + 1 # Incremento de la variable en una unidad

print(contador) # Se imprime el valor de la variable contador

contador += 1 # Equivalente a contador = contador + 1

# contador++  No es posible usar el operador ++ en Python 

# contador--  No es posible usar el operador -- en Python

# El contador puede incrementar o decrementar en una unidad

# Un contador puede ser las vidas de un jugador, normalmente estas se obtienen o se pierden de una en una. El código de una factura, también puede ser un ejemplo de un contador, que lleva una secuencia numérica, que se incrementa en una unidad cada vez que se emite una factura.

# Acumulador, variable que permite sumar valores, en este caso se inicializa en 0

acumulador = 0

acumulador = acumulador + 5 # Suma de 5 al acumulador
acumulador += 5 # Equivalente a acumulador = acumulador + 5

# Un incremento puede ser una multiplicación o una división
acumulador *= 2 # Equivalente a acumulador = acumulador * 2
acumulador /= 2 # Equivalente a acumulador = acumulador / 2

print(acumulador) # Se imprime el valor del acumulador

# Otro ejemplo de acumulador, seria el puntaje de un juego, ya que este cambia sin un patrón fijo, y se va acumulando a lo largo de la partida.

# Centinela, es una variable de control, esta vigilando la ocurrencia de un cambio especifico en la variable

centinela = 0

# El valor centinela, lo define el programador y es un valor que significa algo en el contexto del programa, por ejemplo que el programa debe terminar si el usuario digita el -1.

# El centinela por lo general es un número entero, pero puede ser cualquier tipo de dato, que indique un cambio en un umbral esperado, por ejemplo la temperatura de un sensor, la presión de un tanque, la velocidad de un vehículo, etc.

# Estos datos son los resultados en el tiempo de un sensor de temperatura (El reporte llega cada delta de tiempo), el centinela es el valor 9, que indica que el sensor ha dejado de funcionar.

centinela = 4
centinela = 5
centinela = 9 # El sensor ha dejado de funcionar

# En este caso el programa se detiene, y espera una decisión o dispara una alarma, para que un técnico revise el sensor.

# Bandera, es una variable que indica si se ha cumplido una condición, en este caso se inicializa en False

bandera = False

# Cuando la variable esta en false, significa que por ejemplo no hay correo en el buzón. Cuando la variable esta en True, significa que hay correo en el buzón.

bandera = True

# Por ejemplo, la bandera nos permite controlar cuando hay un error en una operación. Si consultamos una fuente de datos, podemos obtener dos resultados, que la operación se hizo correctamente, entonces el error es False. Pero si se cae la conexión o si hay un problema con la transacción, entonces la bandera es True.







