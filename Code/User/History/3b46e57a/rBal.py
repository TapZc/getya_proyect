'''Ejercicio 1: Número positivo, negativo o cero
Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.'''

numero = int(input("Ingrese un numero: "))

if numero > 0:
    print(f"\nEl numero {numero} es positivo ")
elif (numero < 0):
    print(f"\nEL numero {numero} es negativo")
else:
    print(f"\nEl numero {numero} es cero ")
    