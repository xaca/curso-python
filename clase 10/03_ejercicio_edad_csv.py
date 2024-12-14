import os

def leer_csv():
    bandera = True
    ruta = os.path.join(os.path.dirname(__file__), "usuarios.csv")
    resultado = open(ruta, 'r', encoding='utf-8')
    
    print(f'{"Nombre".ljust(10)}{"Apellido".ljust(10)} Edad')
    print('-'*27)
    for linea in resultado:
        temp = linea.split(';')
        if bandera:
            bandera = False
            continue
        print(f'{temp[0].ljust(10)} {temp[1].ljust(10)} {temp[2]}')

def main():
    leer_csv()

if __name__ == "__main__":
    main()
    