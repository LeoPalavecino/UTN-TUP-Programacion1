"""1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
Llamar a esta función desde el programa principal."""
print("---Ejercicio 01---\n")
def hola_mundo():
    print("Hola Mundo!")

hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva 
un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
Llamar a esta función desde el programa principal solicitando el nombre al usuario."""
print("\n---Ejercicio 02---\n")
def saludar_usuario(nom):
    print(f"Hola {nom}!")

nombre = input("Ingrese su nombre: ").strip()
saludar_usuario(nombre)

"""3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba 
cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""
print("\n---Ejercicio 03---\n")
def informacion_personal(nom, ape, ed, resid):
    print(f"Soy {nom} {ape}, tengo {ed} años y vivo en {resid}")
    
nombre = input("Ingrese su nombre: ").strip().capitalize()
apellido = input("Ingrese su apellido: ").strip().capitalize()
edad = input("Ingrese su edad: ").strip()
residencia = input("Ingrese su lugar de residencia: ").strip().capitalize()

informacion_personal(nombre, apellido, edad, residencia)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área
del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""
print("\n---Ejercicio 04---\n")
def calcular_area_circulo(rad):
    return pi * pow(rad,2)
def calcular_perimetro_circulo(rad):
    return 2 * pi * rad

from math import pi
radio:float = float(input("Ingrese el radio del círculo: ").strip())
area:float = round(calcular_area_circulo(radio),2)
perimetro:float = round(calcular_perimetro_circulo(radio),2)
print(f"\nEl área del círculo es: {area} y su perímetro: {perimetro}")

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando
esta función."""
print("\n---Ejercicio 05---\n")
def segundos_a_horas(seg):
    return (seg / 60) / 60

segundos = int(input("Ingrese una cantidad de segundos: ").strip())
print("Su equivalente en horas es: ", round(segundos_a_horas(segundos),2))

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima
la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función."""
print("\n---Ejercicio 06---\n")
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num} x {i} = ",num * i)

numero = int(input("Ingrese un número: ").strip())
tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una 
tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""
print("\n---Ejercicio 07---\n")
def operaciones_basicas(a,b):
    op_bas:list = []
    op_bas.append(a+b)
    op_bas.append(a-b)
    op_bas.append(a*b)
    op_bas.append(a/b)
    tup_op_bas = tuple(op_bas)
    return tup_op_bas

num1 = int(input("Ingrese un número: ").strip())
num2 = int(input("Ingrese otro número: ").strip())
tupla_operaciones_basicas:tuple = operaciones_basicas(num1,num2)
print(f"Tupla de operaciones básicas entre {num1} y {num2} (suma, resta, multiplicación, división) = {tupla_operaciones_basicas}")

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el 
resultado con dos decimales."""
print("\n---Ejercicio 08---\n")
def calcular_imc(peso, altura):
    return peso / pow(altura,2)

peso_en_kilos:float = float(input("Ingrese su peso en kilogramos: ").strip())
altura_en_metros:float = float(input("Ingrese su altura en metros: ").strip())
print(f"Su IMC es: {round(calcular_imc(peso_en_kilos,altura_en_metros),2)}")

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva
su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función."""
print("\n---Ejercicio 09---\n")
def celsius_a_fahrenheit(cel):
    return cel * 9/5 + 32
    
temp_en_celsius = float(input("Ingrese la temperatura en grados Celsius: ").strip())
temp_en_fahrenheit = celsius_a_fahrenheit(temp_en_celsius)
print(f"La temperatura en grados Fahrenheit es: {round(temp_en_fahrenheit,2)}")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva
el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando ésta función."""
print("\n---Ejercicio 10---\n")
def calcular_promedio(a, b, c):
    return (a+b+c) / 3

num1 = float(input("Ingrese el primer número: ").strip())
num2 = float(input("Ingrese el segundo número: ").strip())
num3 = float(input("Ingrese el tercer número: ").strip())
promedio = round(calcular_promedio(num1,num2,num3),2)
print(f"El promedio de los 3 números es: {promedio}")
