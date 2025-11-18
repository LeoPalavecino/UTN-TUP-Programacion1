"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""
print("\n---Ejercicio 01---\n")
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

numero = int(input("Ingrese un número entero: "))
for i in range(1,numero + 1):
    print(f"El factorial de {i} es: ",factorial(i))

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique."""
print("\n---Ejercicio 02---\n")
def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

numero = int(input("Ingrese un número entero para indicar la posición en Fibonacci: "))
print(f"El número de Fibonacci en la posición {numero} es: {fibo(numero)}")

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛 ^ (𝑚−1)
. Prueba esta función en un algoritmo general."""
print("\n---Ejercicio 03---\n")
def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m - 1)

base = int(input("Ingrese un número entero para elevar a una potencia: "))
exponente = int(input("Ingrese un número entero que será usado como potencia: "))
print(f"El número {base} elevado a {exponente} es: {potencia(base,exponente)}")

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto."""
print("\n---Ejercicio 04---\n")
def binario(num):
    if num == 0:
        return ""
    else:
        return binario(num // 2) + str(num % 2)
    
numero = int(input("Ingrese un número decimal entero positivo para pasar a binario: "))
if numero != 0:
    print(f"El equivalente en binario es: {binario(numero)}")
else:
    print(f"El equivalente en binario es: 0")

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""
print("\n---Ejercicio 05---\n")
def es_palindromo(palabra):
    if len(palabra) <= 1: 
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1]) 

cadena = input("Ingrese una cadena de texto: ")
if es_palindromo(cadena):
    print("Es palíndromo")
else:
    print("No es palíndromo")

"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)"""
print("\n---Ejercicio 06---\n")
def suma_digitos(n):
    if n == 0:   
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)"""
print("\n---Ejercicio 07---\n")
def contar_bloques(n):
    if n == 1: 
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
print(f"El total de bloques necesarios es: {contar_bloques(bloques)}")

"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0"""
print("\n---Ejercicio 08---\n")
def contar_digito(numero, digito):
    if numero == 0: 
        return 0
    else:
        # Utilizamos un operador ternario (condicional)
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito a buscar, entre 0 y 9: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")
