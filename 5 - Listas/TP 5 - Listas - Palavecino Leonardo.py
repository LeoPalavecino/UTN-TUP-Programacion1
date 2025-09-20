"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""
print("--- Ejercicio 01 ---\n")
lista = list(range(4,101,4))
print(lista)


"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!"""
print("\n--- Ejercicio 02 ---\n")
lista:list = ["comida",1,3.5,"hola",23]
print(lista[-2])



"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo: lista_vacia = []"""
print("\n--- Ejercicio 03 ---\n")
lista:list = []
lista.append("hola")
lista.append("cómo")
lista.append("estás")
print(lista)


"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]"""
print("\n--- Ejercicio 04 ---\n")
animales:list = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)"""
print("\n--- Ejercicio 05 ---\n")
print("Respuesta: La función max nos devuelve el valor más grande de un iterable.")
print("En éste caso se utiliza para remover el valor más grande de la lista ´numeros´, sería")
print("el valor ´22´, luego se muestra por pantalla la lista sin el valor removido.")


"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""
print("\n--- Ejercicio 06 ---\n")
lista = list(range(10,31,5))
print(lista)
print(f"Primer número: {lista[0]}")
print(f"Segundo número: {lista[1]}")


"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera. autos = ["sedan", "polo", "suran", "gol"]"""
print("\n--- Ejercicio 07 ---\n")
autos:list = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "polito"
autos[2] = "sauron"
print(autos)


"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""
print("\n--- Ejercicio 08 ---\n")
dobles:list = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)


"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""
print("\n--- Ejercicio 09 ---\n")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print(compras)
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""
print("\n--- Ejercicio 10 ---\n")
lista_anidada:list = []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([])
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)
print(lista_anidada)
