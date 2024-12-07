import random

frutas = ['manzana', 'pera', 'uva', 'sandía', 'mango']
numero_aleatorio = random.randint(0, len(frutas)-1)
print(f'La fruta es: {frutas[numero_aleatorio]}')