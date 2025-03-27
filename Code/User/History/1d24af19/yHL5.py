'''
Ejercicio 2: Edad para votar
Crea un programa que pregunte 
la edad del usuario y diga si 
puede votar (mayor o igual a 18 años) o no.
'''

edad = int(input("Ingrese su edad: "))

if edad>=18:
    print("Eres mayor de edad, Se permite votar. ")
elif edad <18:
    print("Eres menor de edad, No esta permitido para votar.")
else:
    print("Cero no valido")