a = 5
b = 8

# El corto circuit para un and, significa que si el primer operando es falso, no se evalua el segundo operando.
if a > b and True:
    print('a es mayor que b')

# El corto circuit para un or, significa que si el primer operando es verdadero, no se evalua el segundo operando.

if a < b or False:
    print('a es menor que b')

# En una condición no se puede realizar una asignación de una variable, ni siquiera si la asignación es un valor booleano.

# TODO: Realizar pruebas con los operadores de corto circuito en otra clase
