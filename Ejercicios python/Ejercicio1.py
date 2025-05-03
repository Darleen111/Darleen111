# Ejercicio 1: Calculadora simple

# Instrucciones:
# - Pedir al usuario el primer número.
# - Pedir al usuario el segundo número.
# - Preguntar qué operación desea realizar (+, -, *, /).
# - Mostrar el resultado con el mensaje: "El resultado es: "

# Tu código aquí:
Numero1 = float(input("Ingrese el valor de Numero1: "))
Numero2 = float(input("Ingrese el valor de Numero2: "))
Operación = input("Ingrese la operación que desea usar (+, -, *, /): ")


if Operación == "+":
    Solución = Numero1 + Numero2
elif Operación == "-":
    Solución = Numero1 - Numero2
elif Operación == "*":
    Solución = Numero1 * Numero2
elif Operación == "/":
    if Numero2 != 0:
        Solución = Numero1 / Numero2
    else:
        print("No se puede dividir entre cero")
else:
    print("Operación inválida")

Resultado = Solución
print("el resultado es:", Resultado)

# Solicitar el primer número:
Numero1 = float(input("Ingrese el valor de Numero1: "))

# Solicitar el segundo número:
Numero2 = float(input("Ingrese el valor de Numero2: "))

# Pedir la operación a realizar:
Operación = input("Ingrese la operación que desea usar (+, -, *, /): ")

# Calcular el resultado según la operación:

if Operación == "+":
    Solución = Numero1 + Numero2
elif Operación == "-":
    Solución = Numero1 - Numero2
elif Operación == "*":
    Solución = Numero1 * Numero2
elif Operación == "/":
    if Numero2 != 0:
        Solución = Numero1 / Numero2
    else:
        print("No se puede dividir entre cero")
else:
    print("Operación inválida")

# Mostrar el resultado:
# print("El resultado es:", ...)
Resultado = Solución
print("el resultado es:", Resultado)
