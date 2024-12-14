import os

#print(os.path.abspath("archivo.txt"))
#ruta = os.getcwd()#os.path.abspath()
#ruta = ruta.replace("\\","/")
#print(ruta)
#print(os.path.dirname(__file__))
ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")#os.path.dirname(__file__)
ruta.replace("\\","/")
resultado = open(ruta, "r")
"""while True:
    linea = resultado.readline()
    if not linea:
        break
    print(linea)
resultado.close()"""

for linea in resultado:
    print(linea)

resultado.close()