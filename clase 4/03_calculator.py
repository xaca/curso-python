print("Bienvenido a la calculadora infinita. Elige una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Doble de un número")
print("7. Módulo")
print("8. Par o impar")
print("9. Salir")

while True:
  opcion = int(input("Selecciona una operación (1-9): "))

  if opcion == 9:
    print("Saliendo de la calculadora. ¡Hasta pronto!")
    break
  
  elif opcion == 1:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado:", num1 + num2)

  elif opcion == 2:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado:", num1 - num2)
    
  elif opcion == 3:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado:", num1 * num2)

  elif opcion == 4:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Resultado:", num1 / num2)

  elif opcion == 5:
    num1 = float(input("Introduce la base: "))
    num2 = float(input("Introduce el exponente: "))
    resultado = num1 ** num2
    print("Resultado:", resultado)
  
  elif opcion == 6:
    num = float(input("Introduce un número: "))
    print("El doble del número es:", num * 2)

  elif opcion == 7:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    print("Resultado:", num1 % num2)

  elif opcion == 8:
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
        
  else:
      print("Opción no válida. Intenta de nuevo.")