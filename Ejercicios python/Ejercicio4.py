# Ejercicio 4: Mayor de tres números
# Instrucciones:
# - Pedir tres números al usuario.
# - Determinar cuál es el mayor utilizando condicionales (if, elif, else).
# - Mostrar el número mayor con el mensaje: "El número mayor es: ".

# Tu código aquí:
Numero1 = int(input("Ingrese el valor de Numero1: "))
Numero2 = int(input("Ingrese el valor de Numero2: "))
Numero3 = int(input("Ingrese el valor de Numero3: "))

if Numero1 > Numero2 and Numero1 > Numero3:
    Mayor = Numero1
    print("El número", Mayor, "es mayor que", Numero2, "y", Numero3)
elif Numero2 > Numero1 and Numero2 > Numero3:
    Mayor = Numero2
    print("El número", Mayor, "es mayor que", Numero1, "y", Numero3)
elif Numero3 > Numero1 and Numero3 > Numero2:
    Mayor = Numero3
    print("El número", Mayor, "es mayor que", Numero1, "y", Numero2)
else:
    print("Hay números iguales o no se pudo determinar un único mayor.")

Resultado = Mayor
print("El numero mayor es: " , Mayor)

# Pedir el primer número:
Numero1 = int(input("Ingrese el valor de Numero1: "))

# Pedir el segundo número:
Numero2 = int(input("Ingrese el valor de Numero2: "))

# Pedir el tercer número:
Numero3 = int(input("Ingrese el valor de Numero3: "))

# Comparar los números para saber cuál es el mayor:
if Numero1 > Numero2 and Numero1 > Numero3:
    Mayor = Numero1
    print("El número", Mayor, "es mayor que", Numero2, "y", Numero3)
elif Numero2 > Numero1 and Numero2 > Numero3:
    Mayor = Numero2
    print("El número", Mayor, "es mayor que", Numero1, "y", Numero3)
elif Numero3 > Numero1 and Numero3 > Numero2:
    Mayor = Numero3
    print("El número", Mayor, "es mayor que", Numero1, "y", Numero2)
else:
    print("Hay números iguales o no se pudo determinar un único mayor.")

# Mostrar el resultado:
# print("El número mayor es:", ...)
Resultado = Mayor
print("El numero mayor es: " , Mayor)
