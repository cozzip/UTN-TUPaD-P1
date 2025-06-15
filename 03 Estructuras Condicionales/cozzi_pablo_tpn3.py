# 1: 
# edad = int(input("ingrese su edad: "))
# if edad >= 18:
#     print ("es mayor de edad")
# else:
#     print ("es menor de edad")

# 2: 
# nota = int(input("ingrese su nota: "))
# if nota >= 6:
#     print ("Aprobo la asignatura!")
# else:
#     print ("NO aprobo la asignatura!")

# 3: 
# numero = int(input("ingrese un numero: "))
# if numero % 2 == 0:
#     print ("número par!")
# else:
#     numero = int(input("ingrese un número par "))

# 4: 
# edad = int(input("ingrese su edad: "))
# if edad < 12:
#     print("Usted es un niño/a!")
# elif edad == 12 or edad < 18:
#     print("Usted es un adolescente!")
# elif edad >= 18 and edad < 30:
#     print("Usted es un adulto/a joven!")
# else:
#     print("Usted es un adulto!")

# 5:
# clave = input("ingrese una contaseña entre 8 y 14 caracteres!: ")
# digitos = len(clave)
# if digitos >= 8 and digitos <= 14:
#     print ("contraseña correcta")
# else:
#     print("ingrese una contraseña de entre 8 y 14 caracteres")

# 6: 
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# from statistics import mode,median,mean
# moda = mode (numeros_aleatorios)
# mediana = median (numeros_aleatorios)
# media = mean (numeros_aleatorios)
# print ("La media es: ",media," La mediana es: ",mediana," La moda es: ",moda)
# if media > mediana and mediana > moda:
#     print ("sesgo positivo hacia la derecha")
# elif media < mediana and mediana < moda:
#     print ("sesgo negativo hacia la izquierda")
# elif media == moda == mediana:
#     print ("No hay sesgo")
# else: 
#     print("Los valores no entran dentro de ninguna clasificacion")

# 7: 
# palabra = input ("ingrese una palabra: ")
# ultima_letra = palabra[-1]
# if ultima_letra in "aeiou":
#     print(f"{palabra}!")
# else:
#     print (palabra)

# 8:
# nombre = input("ingrese su nombre: ")
# print ("1: Nombre en mayuscula")
# print ("2: Nombre en minuscula")
# print ("3: Primera letra en mayuscula y el resto en minuscula")
# opcion = input("opcion elegida: ")
# if opcion == "1":
#     print (nombre.upper())
# elif opcion == "2":
#     print (nombre.lower())
# elif opcion == "3":
#     print (nombre.title())

# 9: 
# magnitud = float(input("magnitud del terremoto: "))
# if magnitud < 3:
#     print ("El terremoto fue muy leve")
# elif magnitud >= 3 and magnitud < 4:
#     print ("El terremoto fue leve")
# elif magnitud >= 4 and magnitud < 5:
#     print ("El terremoto fue moderado")
# elif magnitud >= 5 and magnitud < 6:
#     print ("El terremoto fue fuerte (puede causar daños en estructuras débiles)")
# elif magnitud >= 6 and magnitud < 7:
#     print ("El terremoto fue muy fuerte")
# elif magnitud >= 7:
#     print ("El terremoto fue extremo ")

# 10: 
# hemisferio = input("ingrese S si se encuentra en el hemisferio Sur, o N si se encuentra en el hemisferio Norte: ").upper()
# mes = int(input("ingrese el número del mes (1 al 12): "))
# dia = int(input("ingrese el día: "))
# if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#     estacion = "Verano" if hemisferio == "S" else "Invierno"
# elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#     estacion = "Otoño" if hemisferio == "S" else "Primavera"
# elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#     estacion = "Invierno" if hemisferio == "S" else "Verano"
# elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
#     estacion = "Primavera" if hemisferio == "S" else "Otoño"
# else:
#     estacion = "Fecha inválida"
# print(f"La estación en el hemisferio {hemisferio} es: {estacion}")



