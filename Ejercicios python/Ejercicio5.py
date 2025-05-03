# Ejercicio 5: Descuento en compras
# Instrucciones:
# - Pedir al usuario el monto total de la compra.
# - Si el monto es mayor a $50.000, aplicar un 15% de descuento.
# - Mostrar el monto final a pagar y el descuento aplicado.

# Tu código aquí:
Descuento_porcentaje = float(input("Ingrese el monto total del descuento (X%): "))
Precio_original = float(input("Ingresa el valor del precio: "))

if Precio_original > 50000:
    Descuento_monto = (Precio_original * Descuento_porcentaje) / 100
    Precio_final = Precio_original - Descuento_monto
    print("Obtuviste un descuento de", Descuento_porcentaje, "% el precio original era de", Precio_original, "pero terminaste pagando", Precio_final)
else:
    Precio_final = Precio_original
    print("No obtuviste un descuento, tu precio final es", Precio_final)

print("El total a pagar es:", Precio_final)

# Pedir el monto total:
Precio_original = float(input("Ingresa el valor del precio: "))

# Verificar si corresponde descuento:
Descuento_porcentaje = float(input("Ingrese el monto total del descuento (X%): "))

# Calcular el monto final y el descuento si es necesario:

if Precio_original > 50000:
    Descuento_monto = (Precio_original * Descuento_porcentaje) / 100
    Precio_final = Precio_original - Descuento_monto
    print("Obtuviste un descuento de", Descuento_porcentaje, "% el precio original era de", Precio_original, "pero terminaste pagando", Precio_final)
else:
    Precio_final = Precio_original
    print("No obtuviste un descuento, tu precio final es", Precio_final)


# Mostrar el resultado:
# print("El total a pagar es:", ...)
print("El total a pagar es:", Precio_final)