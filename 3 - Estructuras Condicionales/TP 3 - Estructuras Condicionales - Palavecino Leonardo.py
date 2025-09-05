#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
edad = int(input("Ingrese su edad en años: "))
if edad >= 18:
  print("Es mayor de edad")
elif (edad < 18 and edad > 0):
    print("Es menor de edad")
else:
  print("Dato mal ingresado")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = float(input("Ingrese la nota: "))
if nota >= 6:
  print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
num:float = 1
while num != 0:
  num:float = float(input("Ingrese un número par ó 0 para terminar: "))
  if num != 0:
    if num % 2 == 0:
      print("Ha ingresado un número par")
    else:
      print("Por favor, ingrese un número par")
  else:
    print("Saliendo del programa...")



#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad = float(input("Ingrese su edad: "))
if edad < 12:
  print("Categoría Niño/a")
elif edad >= 12 and edad < 18:
  print("Categoría Adolescente")
elif edad >= 18 and edad < 30:
  print("Categoría Adulto/a joven")
elif edad >= 30:
  print("Categoría Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
frase:str = input("Ingrese la contraseña: ")
if len(frase) >= 8 and len(frase) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare
#para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda:float = float(mode(numeros_aleatorios))
mediana:float = float(median(numeros_aleatorios))
media:float = float(mean(numeros_aleatorios))
print(numeros_aleatorios)
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
if media > mediana and media > moda:
  print("Sesgo positivo")
elif media < mediana and mediana < moda:
  print("Sesgo negativo")
else:
  print("Sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
vocales = "aeiouAEIOU"
frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[-1]

if ultima_letra in vocales:
  print(f"La última letra es: {ultima_letra}, es vocal, agregaremos un signo de exclamación al final de la frase")
  frase = frase + "!"
  print("La frase es: ",frase)
else:
  print(f"La última letra es: {ultima_letra}, no es vocal...")
  print("La frase es: ",frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado
#por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: \n")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n")
op:int = int(input("Ingrese una opción 1-3: "))
match op:
  case 1:
    nuevo_nombre = nombre.upper()
    print(f"Su nombre: {nuevo_nombre}")
  case 2:
    nuevo_nombre = nombre.lower()
    print(f"Su nombre: {nuevo_nombre}")
  case 3:
    largo_nombre = len(nombre)
    nombre = nombre.lower()
    nuevo_nombre = (nombre[0]).upper()
    nombre = nombre[1:(largo_nombre)]
    nuevo_nombre = nuevo_nombre + nombre
    print(f"Su nombre: {nuevo_nombre}")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud
#en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud de su terremoto =): "))

if magnitud <= 0 or magnitud >=20:
  print("Fuera de clasificación...")
elif magnitud < 3:
  print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
  print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
  print("Extremo (puede causar graves daños a gran escala)")


#10) Utilizando la información aportada en la tabla sobre las estaciones del año:
#Periodo del año
#Desde el 21 de diciembre hasta el 20 de marzo(incluidos) Hem.Norte: Invierno Hem.Sur: Verano
#Desde el 21 de marzo hasta el 20 de junio(incluidos) Hem.Norte: Primavera Hem.Sur:Otoño
#Desde el 21 de junio hasta el 20 de septiembre(incluidos) Hem.Norte: Verano Hem.Sur: Invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) Hem.Norte: Otoño Hem.Sur: Primavera
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemi:str = str(input("En qué Hemisferio se encuentra? norte/sur: "))
mes:str = str(input("Qué mes del año es?: "))
dia:int = int(input("Qué día es? escriba el número correspondiente: "))
periodo_1 = ["enero", "febrero", "marzo"]
periodo_2 = ["abril", "mayo", "junio"]
periodo_3 = ["julio", "agosto", "septiembre"]
periodo_4 = ["octubre", "noviembre", "diciembre"]

if hemi == "sur":
  if mes in periodo_1:
    estacion = "Verano"
    if mes == "marzo" and dia > 20:
      estacion = "Otoño"
  elif mes in periodo_2:
    estacion = "Otoño"
    if mes == "junio" and dia > 20:
      estacion = "Invierno"
  elif mes in periodo_3:
    estacion = "Invierno"
    if mes == "septiembre" and dia > 20:
      estacion = "Primavera"
  elif mes in periodo_4:
    estacion = "Primavera"
    if mes == "diciembre" and dia > 20:
      estacion = "Verano"
else:

  if mes in periodo_1:
    estacion = "Invierno"
    if mes == "marzo" and dia > 20:
      estacion = "Primavera"
  elif mes in periodo_2:
    estacion = "Primavera"
    if mes == "junio" and dia > 20:
      estacion = "Verano"
  elif mes in periodo_3:
    estacion = "Verano"
    if mes == "septiembre" and dia > 20:
      estacion = "Otoño"
  elif mes in periodo_4:
    estacion = "Otoño"
    if mes == "diciembre" and dia > 20:
      estacion = "Invierno"

print(f"La estación es: {estacion}")
