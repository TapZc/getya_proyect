'''
Ejercicio 2: Edad para votar
Crea un programa que pregunte 
la edad del usuario y diga si 
puede votar (mayor o igual a 18 años) o no.
'''

edad = int(input("Ingrese su edad: "))

if edad<=0:
    print("Error: Dato no valido ")
elif edad>=18:
    print("Eres mayor de edad , puede votar. ")
else:
    print("Eres menor de edad, no puedes votar. ")