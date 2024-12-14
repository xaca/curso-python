"""
 1. Leer el salario de todos los empleados de una empresa, y guardarlos en una lista. La entrada de datos finaliza cuando el usuario escriba el número cero (0) en el salario. Al finalizar se deben mostrar los siguientes resultados:

    - Promedio del salario de todos los empleados.
    - Salario más alto y salario más bajo.
    - Número de empleados con salarios inferiores a $10.000.000.
    - Promedio del salario de los empleados que ganan más de $10.000.000.
"""

def leer_salarios():
    # Lectura de salarios
    salarios = []
    salario = 0
    while True:
        try:
            salario = float(input("Ingrese el salario del empleado: "))
            if salario != 0:
                if salario > 0:
                    if salario >= 1300000 and salario <= 15000000:
                        salarios.append(salario)
                    else:
                        print("El salario debe estar entre $1.300.000 y $15.000.000")
                else:
                    print("Ingrese un salario válido")
            else:
                return salarios
        except:
            print("Ingrese un salario válido")

def promedio_salarios(lista_salarios):
    # Promedio de salarios
    cantidad_empleados = len(lista_salarios)
    if cantidad_empleados > 0:
        return sum(lista_salarios)/cantidad_empleados
    else:
        return 0

def salario_mayor(lista_salarios):
    # Salario mayor
    num_max = 0

    for i in lista_salarios:
        if i > num_max:
            num_max = i

    return num_max

def salario_menor(lista_salarios):
    # Salario menor
    print("Salario menor")

def empleados_salario_inferior(lista_salarios):
    # Empleados con salario inferior a 10.000.000
    print("Empleados con salario inferior a 10.000.000")

def promedio_salario_mayor_10m(lista_salarios):
    # Promedio de salario de empleados con salario mayor a 10.000.000
    print("Promedio de salario de empleados con salario mayor a 10.000.000")

def main():
    promedio = 0
    lista_salarios = leer_salarios()
    promedio = promedio_salarios(lista_salarios)

    if promedio > 0:
        print(f"El promedio de salarios es: {promedio}")
        input("Presione una tecla para continuar...")

    salario_max = salario_mayor(lista_salarios)

    if salario_max > 0:
        print(f"El salario mayor es: {salario_max}")
        input("Presione una tecla para continuar...")


if __name__ == "__main__":
    main()