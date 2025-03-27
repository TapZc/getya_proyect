'''
Ejercicio 3: Número par o impar
Haz un programa que solicite un 
número y determine si es par o impar.
'''

numero = int(input("Ingrese un numero: "))
if numero ==0:
    print(input("El numero es cero"))
elif numero % 2==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")