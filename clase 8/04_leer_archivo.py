import os

#print(os.path.abspath("archivo.txt"))
ruta = os.path.abspath("archivo.txt")
ruta = ruta.replace("\\","/")
resultado = open(ruta, "r")
print(resultado.readline())