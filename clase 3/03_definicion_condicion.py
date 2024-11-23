# Una condición en programación es una pregunta, que solo se responde con dos posibilidades respuestas: Verdadero o Falso.

# Ejemplo de condición
# Pregunta: ¿Es 5 mayor que 3?
# Respuesta: Verdadero

# Pregunta: ¿Es 5 menor que 3?
# Respuesta: Falso

# Pregunta: ¿Es 5 igual a 3?
# Respuesta: Falso

# Las preguntas anteriores son preguntas que usan los operadores de relación.

# Ejemplo de condiciones con operadores lógicos:

# Pregunta: ¿Es 5 mayor que 3 y 5 es menor que 10?

# Respuesta: Verdadero

# Ejemplos de condiciones en codigo

condicion1 = 5 > 3
print(condicion1) # Salida: True
edad = 12
condicion2 = edad >= 18
print(condicion2) # Salida: False
edad = 25
condicion3 = edad >= 18 and edad <= 35
print(condicion3) # Salida: True

nacionalidad = "estadounidense"
condicion4 = (edad > 15 and edad < 18) and (nacionalidad == "colombiana")