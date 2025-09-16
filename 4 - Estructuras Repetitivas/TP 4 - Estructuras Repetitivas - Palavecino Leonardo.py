"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
for i in range (101):
  print(f"Número: {i}")


"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
bandera:bool = True
while bandera:
  numero = input("Ingrese un número entero: ")
  if not numero.isalpha(): #verifica que no sea una letra del alfabeto
    contador:int = 0
    for i in numero: #para recorrer el número
      if i != "-" and i != " ": #controla si ingresan espacios, para no contarlos
        contador+=1

    print(f"La cantidad de dígitos es: {contador}")
    bandera = False
  else:
    print("Ingrese un valor valido")


"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
num1:int = int(input("Ingrese el primer número: "))
num2:int = int(input("Ingrese el segundo número: "))
sum:int = 0
if num1 < num2:
  for i in range(num1 + 1,num2):
    sum = sum + i
elif num2 < num1:
  for i in range(num2 + 1,num1):
    sum = sum + i

print("La suma es:",sum)


"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
bandera:bool = True
suma:int = 0
while bandera:
  numero:int = int(input("Ingrese un numero entero o 0 para finalizar: "))
  suma += numero
  if numero == 0:
    bandera = False

print("La suma es: ", suma)


"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random
adivinar:int = int(random.randint(0,9))
bandera:bool = True
intentos:int = 0
while bandera:
  numero:int = int(input("Ingrese un número entero entre el 0 y el 9: "))
  intentos += 1
  if numero == adivinar:
    print(f"Adivinaste! el número {adivinar}, luego de {intentos} intentos")
    bandera = False
  elif numero > adivinar:
    print("Te pasaste, intenta nuevamente")
  elif numero < adivinar:
    print("No llegaste, intenta nuevamente")


"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
for i in range(100,0-1,-1): #el código incluye a los extremos 0 y 100 como pares
  if i % 2 == 0:
    print (i)


"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
suma:int = 0
band:bool = True
while band:
  num:int = int(input("Ingrese un número entero positivo: "))
  if num >= 0:
    band = False
  else:
    print("Dato no válido")

for i in range(0,num):
  suma += i

print(f"La suma de los números entre 0 y {num} es: {suma}")


"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
cant_num:int = 10 #variable para indicar la cantidad de números a ingresar
cont_par:int = 0
cont_impar:int = 0
cont_pos:int = 0
cont_neg:int = 0

for i in range(0,cant_num):
  numero:int = int(input("Ingrese un número por favor: "))
  if numero % 2 == 0:
    cont_par += 1
  else:
      cont_impar += 1
  if numero >= 0:
    cont_pos += 1
  else:
    cont_neg += 1

print(f"Cantidad de números pares: {cont_par}")
print(f"Cantidad de números impares: {cont_impar}")
print(f"Cantidad de números positivos: {cont_pos}")
print(f"Cantidad de números negativos: {cont_neg}")


"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""
cant_num:int = 10 #variable para indicar la cantidad de números a ingresar
suma:int = 0
media:float = 0

for i in range(0,cant_num):
  numero:int = int(input("Ingrese un número por favor: "))
  suma += i

media:float = suma / cant_num
print(f"La media es: {media}")


"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""
bandera:bool = True
while bandera:
  numero = input("Ingrese un número entero: ")
  
  if not numero.isalpha(): #validamos si el dato ingresado no son letras
    numero:int = int(numero)
    if numero < 0: #si es un número negativo, lo hacemos positivo para poder procesarlo
      numero = numero * -1
      es_negativo:bool = True
    else:
      es_negativo:bool = False  
    numero_invertido:int = 0
    numero_convertido:int = int(numero)
    while numero_convertido != 0: #proceso de inversión
      digito = numero_convertido % 10
      numero_invertido = numero_invertido * 10 + digito
      numero_convertido = numero_convertido // 10
    
    if es_negativo == True: #de ser necesario, convertimos el número a negativo nuevamente
      numero_invertido = numero_invertido * -1
    print(numero_invertido)
    bandera = False
  else:
      print("Ingrese un número válido")
