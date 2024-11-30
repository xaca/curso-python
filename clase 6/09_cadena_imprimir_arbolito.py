# Crear un programa que reciba un valor n, que representa la altura de un pino, y el programa debe imprimir un arbolito de navidad de esa altura.

# Ejemplo:
# n = 5
#
#     *     1
#    ***    3
#   *****   5
#  *******  7
# ********* 9
#     *

n = 5
for i in range(n):
    #print(i,n,(n-i-1),(2*i+1))
    print(" "*(n-i-1) + "*"*(2*i+1))
print(" "*(n-1) + "*")

print()
n = 20
salida = ""
for i in range(n):
    salida += ("*"*(2*i+1)).center(n*2-1) + "\n"
salida += "*".center(n*2-1)
print(salida)

# Imprimir el arbol, pero con un fondo de un caracter
# 0000*0000
# 000***000
# 00*****00
# 0*******0
# *********
# 0000*0000
print()
n = 10
fondo = "-"
relleno = "1"
for i in range(n):
    print(fondo*(n-i-1) + relleno*(2*i+1) + fondo*(n-i-1))
print(fondo*(n-1) + relleno + fondo*(n-1))
