'''
Ejercicio 4: Descuento en una tienda
Una tienda ofrece 10% de descuento si la compra 
es mayor a $100. Escribe un programa que pida el
total de la compra y muestre el precio final con 
descuento si aplica.
'''

compra=float(input("\nPorfavor ingrese el total de la compra en dolares: "))
    
print(f"\nEl precio total de la compra es de un total de ${compra:.2f} dolares")

if compra >= 100:
    descuento=compra * 0.10
    precioFinal= compra - descuento

    print(f"\nEl descuento que estaria aplicando es de {descuento:.2f} ")
    print(f"\nEl precio final con el descuento es de un total de: ${precioFinal:.2f} dolares")
elif compra< 100:
    print("\nNo obtiene descuento")