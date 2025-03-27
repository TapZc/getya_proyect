'''
Ejercicio 5: Aprobado o reprobado
Un estudiante aprueba si su calificación 
es mayor o igual a 60. Escribe un programa 
que pida la calificación y muestre si está 
aprobado o reprobado.
'''
nombre = " "
nota = float(input(f"Ingrese la nota de examen {nombre}"))

print("La nota que has ingresado es: {nota}")

if nota < 0:
    print("Error: Nota no existente")
elif nota >= 60: 
    print("La nota es {nota}, ha sido aprobado en el examen. ")
else:
    print("La nota es {nota}, ha sido reprobado en el examen. ")