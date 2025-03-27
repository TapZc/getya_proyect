'''
Ejercicio 5: Aprobado o reprobado
Un estudiante aprueba si su calificación 
es mayor o igual a 60. Escribe un programa 
que pida la calificación y muestre si está 
aprobado o reprobado.
'''
nombre = str(input("\nIngrese el nombre del estudiante: "))
nota = float(input(f"\nIngrese la nota de examen del estudiante {nombre}: "))

print(f"\nLa nota que has ingresado es: {nota}")

if nota < 0 or nota> 100:
    print("\nError: La nota ingresada no es válida. Debe estar entre 0 y 100.")
elif nota >= 60: 
    print(f"\nLa nota es {nota}, ha sido aprobado en el examen. \n")
else:
    print(f"\nLa nota es {nota}, ha sido reprobado en el examen. \n")