"""
Por defecto cuando imprimimos usando print, se imprime un salto de línea al final de la impresión. Pero no siempre se imprime de esta manera, para cambiar la forma de impresión, se puede hacer por medio del parametro end, que indica como se finaliza la secuenciencia de impresión.

 Por defecto es lo mismo imprimir estas dos sentencias:
    print("Hola")
    print("Hola",end="\n")

  Si cambiamos el valor de end, podemos cambiar la forma de impresión:
    print("Hola",end="") 
    print("Mundo",end="")

    Salida: HolaMundo

    print("Hola",end=" ")
    print("Mundo",end="")

    Salida: Hola Mundo

    print("Hola",end="-")
    print("Mundo",end="")

    Salida: Hola-Mundo

    print("Hola",end=" ")
    print("Mundo",end="\n")
    print("Feliz)

    Salida: Hola Mundo
            Feliz

"""