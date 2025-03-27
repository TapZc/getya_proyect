'''
Ejercicio 5: Aprobado o reprobado
Un estudiante aprueba si su calificación 
es mayor o igual a 60. Escribe un programa 
que pida la calificación y muestre si está 
aprobado o reprobado.
'''
nombre = str(input("\nIngrese el nombre del estudiante: "))
nota = int(input(f"\nIngrese la nota de examen del estudiante {nombre}: "))

print("\nLa nota que has ingresado es: {nota}")

if nota < 0:
    print("\nError: Nota no existente")
elif nota >= 60: 
    print("\nLa nota es {nota}, ha sido aprobado en el examen. ")
else:
    print("\nLa nota es {nota}, ha sido reprobado en el examen. ")