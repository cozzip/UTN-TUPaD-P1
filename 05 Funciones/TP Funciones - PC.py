# 1:

# def hola_mundo():
#     print("Hola Mundo!")
# hola_mundo()

# 2:

# def saludar(nombre):
#     return f"Hola {nombre}!"
# nombre = input("Ingrese su nombre: ")
# saludo = saludar(nombre)
# print(saludo)

# 3:

# def datos(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su lugar de residencia: ")
# datos(nombre, apellido, edad, residencia)

# 4:

# from math import pi
# def area(radio):
#     return pi*radio ** 2
# def perimetro(radio):
#     return 2 * pi * radio
# radio = float(input("Ingrese el radio del círculo: "))
# area = area(radio)
# perimetro = perimetro(radio)
# print(f"El área es: {area:.2f}")
# print(f"El perímetro es: {perimetro:.2f}")

# 5:

# def seg_hs(segundos):
#     return segundos / 3600
# segundos = float(input("Ingrese los seg: "))
# horas = seg_hs(segundos)
# print(f"{segundos} seg equivalen a {horas:.2f} hs.")

# 6:

# def tabla(numero):
#     print(f"Tabla de multiplicar de {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")
# numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
# tabla(numero)

# 7:

# def operaciones(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     if b != 0:
#         division = a / b
#     else:
#         division = None
#     return (suma, resta, multiplicacion, division)
# a = float(input("Ingrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))
# suma, resta, multiplicacion, division = operaciones(a, b)
# print("Suma:", suma)
# print("Resta:", resta)
# print("Multiplicación:", multiplicacion)
# if division is not None:
#     print("División:", division)
# else:
#     print("No se puede dividir por cero.")

# 8:

# def imc(peso, altura):
#     return peso / (altura ** 2)
# peso = float(input("Peso en kg: "))
# altura = float(input("Altura en m: "))
# imc = imc(peso, altura)
# print(f"Tu imc es: {imc:.2f}")

# 9:

# def celsius_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
# celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# fahrenheit = celsius_fahrenheit(celsius)
# print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10:

# def promedio(a, b, c):
#     return (a + b + c) / 3
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))
# promedio = promedio(num1, num2, num3)
# print(f"El promedio es: {promedio:.2f}")
