'''
Ejercicio 4: Descuento en una tienda
Una tienda ofrece 10% de descuento si la compra 
es mayor a $100. Escribe un programa que pida el
total de la compra y muestre el precio final con 
descuento si aplica.
'''

compra=(input("Porfavor ingrese el total de la compra: "))
    
print(f"El precio total de la compra es de un total de {compra}")

if compra >= 100:
    descuento=compra * 0.10
    precioFinal= compra - descuento
    
    print(f"El descuento que estaria aplicando es de {descuento}")
    print(f"La precio final con el descuento es de un total de: ",precioFinal)
elif compra< 100:
    print("No obtiene descuento")