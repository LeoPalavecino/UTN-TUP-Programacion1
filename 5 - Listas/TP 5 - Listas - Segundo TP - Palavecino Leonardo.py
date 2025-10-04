"""1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja."""
print("--- Ejercicio 01 ---\n")
import random
notas:list = []
suma:int = 0
mas_alta:int = 0
mas_baja:int = 0
for i in range (10):
  notas.append(random.randint(0,10))
  suma = suma + notas[i]
  if i == 0:
    mas_alta:int = notas[i]
    mas_baja:int = notas[i]
  if notas[i] >= mas_alta:
    mas_alta = notas[i]
  if notas[i] <= mas_baja:
    mas_baja = notas[i]  
print("Lista notas: ", notas)
print("Promedio notas: ",suma / 10)
print("Nota más baja: ", mas_baja)
print("Nota más alta: ", mas_alta)

"""2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista."""
print("\n--- Ejercicio 02 ---\n")
productos:list = []
for i in range(5):
  print("Ingrese un producto",i + 1,"/ 5: ")
  productos.append(input())

productos_ordenados:list = sorted(productos)
print(productos_ordenados)

eliminar = input("Qué producto desea eliminar?: ")
if eliminar in productos:
  productos.remove(eliminar)
  productos_ordenados:list = sorted(productos)
  print(f"Lista actualizada: {productos_ordenados}")
else:
  print(f"No se encontró el producto {eliminar}")  

"""3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista."""
print("\n--- Ejercicio 03 ---\n")
import random
lista:list = []
pares:list = []
impares:list = []
for i in range(15):
  lista.append(random.randint(1,100))
  if lista[i] % 2 == 0:
    pares.append(lista[i])
  else:
    impares.append(lista[i])  
print("Lista completa de números: ", lista)
print("Lista de números pares: ", pares)
print("Lista de números impares: ", impares)

"""4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado."""
print("\n--- Ejercicio 04 ---\n")
datos:list = [1,3,5,3,7,1,9,5,3]
datos_2:list = []
datos_original = [[1,3,5,3,7,1,9,5,3]] 
tam:int = len(datos)
repite:bool = False
cont:int = 0
while tam > 0:
  dato:int = datos[0]
  datos_2.append(dato)
  for i in range(tam):
    if dato in datos:
        datos.remove(dato)
  tam = len(datos)

print("Lista original: ", datos_original)
print("Lista sin repetidos: ",datos_2)

"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada"""
print("\n--- Ejercicio 05 ---\n")
nombres:list = ["GUSTAVO CORTES","FACUNDO FLORES","KEVIN PUCA","NAHUEL OLMOS","ENZO MARTINEZ","IGNACIO CARIAGA","GUILLERMO PINTO","MATIAS SOTO","FRANCO ROMERO"]
print("Lista nombres: ", nombres)
salir:bool = False
while salir == False:
  opcion = input("Elija Agregar estudiante, Eliminar estudiante o Salir A/E/S: ").strip().upper()
  if opcion == "S":
    salir = True
  elif opcion == "A":
    agregar = input("Escriba el nombre del alumno a Agregar: ").strip().upper()
    nombres.append(agregar)
    print("Lista nombres actualizada: ", nombres)
  elif opcion == "E":
    eliminar = input("Escriba el nombre del alumno a Eliminar: ").strip().upper()
    if eliminar in nombres:
      nombres.remove(eliminar)
      print("Lista nombres actualizada: ", nombres)
    else:
       print("No se encuentra el nombre...")  
  else:
    print("Dato mal ingresado...")
    
"""6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero)."""
print("\n--- Ejercicio 06 ---\n")
lista:list = [84,23,57,41,28,99,31] #lista inicial
print("Lista inicial: ",lista)
tam:int = len(lista)
#Se mueve el primer elemento de la lista hacia el final, luego se elimina el primer elemento
aux:int = lista[tam-1]
for i in range(tam-1,0,-1):
    lista[i] = lista[i-1]

lista[0] = aux     
#Se muestra la lista rotada
print("Lista rotada: ",lista)

"""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica."""
print("\n--- Ejercicio 07 ---\n")
#listas y variables iniciales:
temp_semanal:list = [[20,9],[22,11],[22,11],[24,13],[26,11],[21,12],[27,16]]
amplitudes:list = [[0,"LUNES"],[0,"MARTES"],[0,"MIERCOLES"],[0,"JUEVES"],[0,"VIERNES"],[0,"SABADO"],[0,"DOMINGO"]]
tam:int = len(temp_semanal)
suma_min:float = 0
suma_max:float = 0

#obtenemos la suma total de las temperaturas mínimas y máximas para luego obtener sus promedios
for i in range(tam):
  suma_min = suma_min + temp_semanal[i][1] 
  suma_max = suma_max + temp_semanal[i][0] 
  ampli:float = temp_semanal[i][0] - temp_semanal[i][1] 
  amplitudes[i][0] = ampli #obtenemos la amplitud de cada día y se guarda junto al día correspondiente en la lista "amplitudes"

#inicializamos variables de amplitud mayor y día correspondiente, para luego comparar y corregir de ser necesario
ampli_mayor:float = amplitudes[0][0]
dia_ampli_mayor = amplitudes[0][1]
for i in range(tam-1): #estructura de comparación
  muestra:float = amplitudes[i][0]
  if muestra > ampli_mayor:
    ampli_mayor = muestra
    dia_ampli_mayor = amplitudes[i][1]

#impresión por pantalla de consignas
print("Lista de temperaturas máximas y mínimas (semanal): ",temp_semanal)
print("El promedio de temperaturas mínimas es: ", round((suma_min / 7),2))
print("El promedio de temperaturas máximas es: ", round((suma_max / 7),2))
print(f"La mayor amplitud térmica es {ampli_mayor}º registrada el día {dia_ampli_mayor}")

"""8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia."""
print("\n--- Ejercicio 08 ---\n")
#listas y variables iniciales
notas:list = [[7,6,8],[4,8,7],[3,7,6],[9,10,7],[5,9,8]]
tam:int = len(notas)
suma_materia_1:float = 0
suma_materia_2:float = 0
suma_materia_3:float = 0
#cálculo de promedio general de notas y sumatorias de notas por materia
for i in range(tam):
  suma_estu:float = notas[i][0] + notas[i][1] + notas[i][2]
  prom_estu:float = round((suma_estu / 3),2)
  print("El promedio de notas para el estudiante nº",i+1,f" es: {prom_estu}")
  suma_materia_1:float = suma_materia_1 + notas[i][0]
  suma_materia_2:float = suma_materia_2 + notas[i][1]
  suma_materia_3:float = suma_materia_3 + notas[i][2]
print()
#cálculo y muestra por pantalla de los promedios de cada materia
print("El promedio para la materia nº1 es: ", round((suma_materia_1 / 5),2))
print("El promedio para la materia nº2 es: ", round((suma_materia_2 / 5),2))
print("El promedio para la materia nº3 es: ", round((suma_materia_3 / 5),2))

"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada."""
print("\n--- Ejercicio 09 ---\n")
tablero:list = [["-","-","-"],["-","-","-"],["-","-","-"]]
tam:int = len(tablero)
cont_de_turno:int = 0

#Estructura general de funcionamiento del juego
salir:bool = False
while not salir:
    if cont_de_turno == 0:
        #Bienvenida y elección de jugadores
        print("""-------------------------------------------
-----Bienvenido al juego del Ta-Te-Ti!-----
-------------------------------------------""")
        jugador_1 = input("Ingrese el nombre del Jugador 1, jugará con la X: ").strip()
        jugador_2 = input("Ingrese el nombre del Jugador 2, jugará con la O: ").strip()
        
        #Imprime Tablero vacío, la primera vez
        print("-------------Tablero Actual----------------")
        for i in range(tam):
            print(tablero[i])
        print("-------------------------------------------")

    #Marcador de turno actual
    cont_de_turno += 1
    if cont_de_turno % 2 != 0:
       print(f"Turno de {jugador_1} con la X")
       letra = "X"
    else:
       print(f"Turno de {jugador_2} con la O")
       letra = "O"

    #Ingreso de coordenadas
    coordenadas_ok = False
    while coordenadas_ok == False:
        print("Ingresar coordenadas (para SALIR del juego ingrese dato vacío)")
        fila = input("Ingrese fila (0-2): ").strip()
        columna = input("Ingrese columna (0-2): ").strip()
        if fila == "" or columna == "":
            print("Saliendo del juego...")
            coordenadas_ok = True
            salir = True
        else:
            if len(fila) == 1 and fila.isdigit():
                fila = int(fila)
                columna = int(columna)
                if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2:
                    print(f"Jugada realizada en fila: {fila} y columna: {columna}")
                    coordenadas_ok = True
                else:
                    print("Coordenadas mal ingresadas, intente nuevamente...")
        
        if salir != True:    
            #Asignamos la letra correspondiente a la coordenada indicada
            tablero[fila][columna] = letra

            #Imprime Tablero después de la jugada
            print("-------------Tablero Actual----------------")
            for i in range(tam):
                print(tablero[i])
            print("-------------------------------------------")
                    
            #Estructura de las 8 combinaciones ganadoras: 3 filas, 3 columnas, 2 diagonales
            hay_ganador:bool = False
            if tablero[0][0] == tablero[0][1] == tablero[0][2]:
                if tablero[0][0] == "X" or tablero[0][0] == "O":
                    hay_ganador = True
            elif tablero[1][0] == tablero[1][1] == tablero[1][2]:
                if tablero[1][0] == "X" or tablero[1][0] == "O":
                    hay_ganador = True
            elif tablero[2][0] == tablero[2][1] == tablero[2][2]:
                if tablero[2][0] == "X" or tablero[2][0] == "O":
                    hay_ganador = True

            if tablero[0][0] == tablero[1][0] == tablero[2][0]:
                if tablero[0][0] == "X" or tablero[0][0] == "O":
                    hay_ganador = True
            elif tablero[0][1] == tablero[1][1] == tablero[2][1]:
                if tablero[0][1] == "X" or tablero[0][1] == "O":
                    hay_ganador = True
            elif tablero[0][2] == tablero[1][2] == tablero[2][2]:
                if tablero[0][2] == "X" or tablero[0][2] == "O":
                    hay_ganador = True

            if tablero[0][0] == tablero[1][1] == tablero[2][2]:
                if tablero[0][0] == "X" or tablero[0][0] == "O":
                    hay_ganador = True
            elif tablero[2][0] == tablero[1][1] == tablero[0][2]:
                if tablero[2][0] == "X" or tablero[2][0] == "O":
                    hay_ganador = True
            

            #Si hay ganador se ejecuta el siguiente código sinó continúa el juego normalmente
            if hay_ganador == True:
                #Se indica al ganador
                if cont_de_turno % 2 != 0:
                    print(f"El jugador {jugador_1} es el ganador!")
                else:
                    print(f"El jugador {jugador_2} es el ganador!")

                #Condicional para seguir jugando o no
                seguir_ok = False
                while seguir_ok == False:
                    seguir = input("Juega nuevamente? s/n: ").strip().lower()
                    if seguir == "n":
                        print("Saliendo del juego...")
                        seguir_ok = True
                        salir = True
                    elif seguir == "s":
                        seguir_ok = True
                        tablero:list = [["-","-","-"],["-","-","-"],["-","-","-"]]
                        cont_de_turno = 0
                    else:
                        print("Dato mal ingresado, intente nuevamente...")

"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto. borrar: la suma de los 7 días
• Mostrar el día con mayores ventas totales. borrar: el día que más se vendió teniendo en cuenta los 4 productos
• Indicar cuál fue el producto más vendido en la semana. borrar: sumar para c/producto el total de la semana y comparar los 4 productos"""
print("\n--- Ejercicio 10 ---\n")
import random
ventas = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
total_semanal_por_producto = [0,0,0,0]
ventas_totales_por_dia = [0,0,0,0,0,0,0]
tam_ventas:int = len(ventas)
tam_semana:int = len(ventas[1])

#Llenamos la lista "ventas" con datos de venta aleatorios
for i in range(tam_ventas):
    for j in range(tam_semana):
        ventas[i][j] = random.randint(500,1000) 

#Mostramos los datos de la lista "ventas"
print("Semana de ventas por producto, Lunes a Domingo:\n")
for i in range(tam_ventas):
   print(f"Producto {i+1}: {ventas[i]}")
print("--------------------------------------")

#Cálculo y muestra del total semanal por producto
for i in range(tam_ventas):
    for j in range(tam_semana):
        total_semanal_por_producto[i] += ventas[i][j] 

for i in range(tam_ventas):
    print(f"Total semanal para producto {i+1}: {total_semanal_por_producto[i]}")
print("--------------------------------------")

#Cálculo de ventas totales por día (contemplando los 4 productos)
for i in range(tam_semana):
    for j in range(tam_ventas):
        ventas_totales_por_dia[i] += ventas[j][i]

print("Semana de ventas totales, Lunes a domingo: ", ventas_totales_por_dia)
print("--------------------------------------")

#Muestra del día con más ventas (contemplando los 4 productos)
dia_de_mas_ventas = max(ventas_totales_por_dia)
for i in range(tam_semana):
    if ventas_totales_por_dia[i] == dia_de_mas_ventas:
        indice:int = i
        
caso:int = indice + 1
match caso:
    case 1: dia = "Lunes"
    case 2: dia = "Martes"
    case 3: dia = "Miércoles"
    case 4: dia = "Jueves"
    case 5: dia = "Viernes"
    case 6: dia = "Sábado"
    case 7: dia = "Domingo"

print(f"El día con más ventas totales fue el {dia} con {dia_de_mas_ventas} en ventas")
print("--------------------------------------")
