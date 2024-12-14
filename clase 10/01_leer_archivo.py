import os

#ruta = os.path.abspath("archivo.txt") # No se obtiene la ruta correcta, se obtiene la ruta del archivo que se está ejecutando
#ruta = os.getcwd() # Se obtiene la ruta del archivo que se está ejecutando

#print(__file__)
#print(os.path.dirname(__file__))
#print(os.path.join(os.path.dirname(__file__), "archivo.txt"))

ruta = os.path.join(os.path.dirname(__file__), "archivo.txt")
resultado = open(ruta, "r", encoding="utf-8")
print(resultado.read())
resultado.close()
