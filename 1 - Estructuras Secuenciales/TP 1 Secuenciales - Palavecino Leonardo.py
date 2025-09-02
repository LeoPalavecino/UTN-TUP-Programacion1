#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

import math
radio = float(input("Ingrese el radio: "))  
area = math.pi * radio**2
perim = 2 * math.pi * radio
print(f"El área del círculo es: {area} y su perímetro es: {perim}") 

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = float(segundos / 3600)
print(f"El equivalente de {segundos} segundos en horas es: {horas}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num = int(input("Ingrese un número: "))
for i in range(1,11):
	multi = num * i 
	print(f"{num} x {i} = {multi}")
	
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1: int = int(input("inserta primer numero: "))
numero2: int = int(input("inserta segundo numero: "))

resultado: float = float(numero1 + numero2)
print(numero1, "+", numero2, "=", resultado)

resultado: float = float(numero1 - numero2)
print(numero1, "-", numero2, "=", resultado)

resultado: float = float(numero1 * numero2)
print(numero1, "x", numero2, "=", resultado)

resultado: float = float(numero1 / numero2)
print(numero1, "/", numero2, "=", resultado)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) al cuadrado

altura:float = float(input("Ingrese su altura en metros: "))
peso:float = float(input("Ingrese su peso en kilos: "))
imc:float = float(peso / (altura**2))
print(f"El IMC es de: {imc} kg/m")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temp_cels:float = float(input("Ingrese temperatura en grados Celsius: "))
temp_fahr:float = float((9/5)*temp_cels + 32)
print(f"El equivalente en grados Fahrenheit es: {temp_fahr}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1:float = float(input("Ingrese el primer número: "))
num2:float = float(input("Ingrese el segundo número: "))
num3:float = float(input("Ingrese el tercer número: "))
prom:float = float((num1 + num2 + num3) / 3)
print(f"El promedio de los 3 números es: {prom}")
