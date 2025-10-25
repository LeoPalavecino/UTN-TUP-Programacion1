"""1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450
}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""
print("\n---Ejercicio 01---\n")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Precios frutas: {precios_frutas}")

precios_frutas["Naranja"] = 1200 #método para agregar un elemento 
nuevos_elementos = {"Manzana": 1500, "Pera": 2300} #creamos un diccionario con los nuevos elementos
precios_frutas.update(nuevos_elementos) #método para agregar usando otro diccionario
print(f"Precios frutas actualizado: {precios_frutas}")

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""
print("\n---Ejercicio 02---\n")
print(f"Precios frutas: {precios_frutas}")
precios_frutas["Banana"] = 1330
precios_frutas.update({"Manzana": 1700, "Melón": 2800})
print(f"Precios frutas actualizado: {precios_frutas}")

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios."""
print("\n---Ejercicio 03---\n")
print(f"Precios frutas: {precios_frutas}")
lista_frutas:list = []
for clave in precios_frutas:
    lista_frutas.append(clave)
print(f"Lista frutas: {lista_frutas}")

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo: 
contactos = {"Juan": "123456", "Ana": "987654"}
#Consultar: "Juan" -> muestra "123456" """
print("\n---Ejercicio 04---\n")
#contactos : dict = {}
contactos = dict()
for i in range(5):
    nombre = input(f"Ingrese nombre {i+1}/5: ")
    numero = int(input("Ingrese número telefónico: "))
    contactos[nombre] = numero
print(f"Contactos: {contactos}")
nombre = input("Ingrese un nombre: ")
print(f"El número asociado al nombre {nombre} es: {contactos[nombre]}")

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
#Entrada -> "hola mundo hola"
#Salida:
Palabras_unicas: {"hola", "mundo"}
Recuento: {"hola": 2, "mundo": 1} """
print("\n---Ejercicio 05---\n")
lista_frase = list()
recuento_palabras = dict()
cont:int = 0
frase = input("Ingrese una frase: ").strip()
print(f"La frase es: {frase}")
lista_frase = frase.split()
#print(f"Lista de frase: {lista_frase}") check de lista creada
palabras_unicas = set(lista_frase)
print(f"Palabras únicas en la frase: {palabras_unicas}")
for i in range(len(lista_frase)):
    cont = lista_frase.count(lista_frase[i])
    recuento_palabras[lista_frase[i]] = cont 
print(f"Recuento de palabras en la frase: {recuento_palabras}")

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = {
        "Sofia": (10,9,8),
        "Luis": (6,7,7)
} """
print("\n---Ejercicio 06---\n")
notas_alumno:dict = {}
notas = tuple()
for i in range(3):
    nombre = input(f"Ingresar nombre de alumno {i+1}/3: ")
    notas_alumno[nombre] = ""
    lista_notas:list = []
    for j in range(3):
        nota = input(f"Ingresar nota nº{j+1}: ")
        lista_notas.append(nota)
        notas = tuple(lista_notas)
    notas_alumno[nombre] = notas
print(f"Diccionario notas alumno: {notas_alumno}")
lista_nombres:list = []
for nom in notas_alumno:
    lista_nombres.append(nom)

for i in range(len(lista_nombres)):
    alumno = lista_nombres[i]
    notas_a_promediar = notas_alumno[alumno]
    tam = len(notas_a_promediar)
    promedio:int = 0
    for j in range(tam):
        promedio = promedio + int(notas_a_promediar[j])
    print(f"El promedio de notas para el alumno {alumno} es: {promedio/tam:.2f}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""
print("\n---Ejercicio 07---\n")
aprobados_parcial_1 = {1, 2, 3, 4, 5, 6, 7, 8}
aprobados_parcial_2 = {4, 5, 7, 8, 9}
print(f"Aprobados Parcial 1: {aprobados_parcial_1}")
print(f"Aprobados Parcial 2: {aprobados_parcial_2}")

aprobados_ambos_parciales = aprobados_parcial_1 & aprobados_parcial_2 #Intersección
print(f"\nAprobaron ambos parciales: {aprobados_ambos_parciales}")

aprobaron_solo_un_parcial = aprobados_parcial_1 ^ aprobados_parcial_2 #Diferencia simétrica
print(f"\nAprobaron sólo uno de los dos parciales: {aprobaron_solo_un_parcial}")

aprobaron_al_menos_un_parcial = aprobados_parcial_1 | aprobados_parcial_2 #Unión
print(f"\nAprobaron al menos un parcial: {aprobaron_al_menos_un_parcial}")

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""
print("\n---Ejercicio 08---\n")
stock:dict = {"mouse": 5, "teclado": 4, "auricular": 10}
salir:bool = False
while not salir:
  lista_articulos = list(stock.keys())
  print(f"Listado de artículos: {lista_articulos}")
  print("=======================")
  art_buscado = input("Ingrese el artículo para ver su stock: ")
  if art_buscado in lista_articulos:
    print(f"Stock del artículo {art_buscado}: ", stock[art_buscado], "unidades")
    agregar:str = input("Desea modificar el stock del artículo? Presione ´s´ para modificar o cualquier otra tecla para Salir: ")
    if agregar == "s":
      stock_nuevo:int = input("Ingrese el nuevo stock: ")
      stock[art_buscado] = stock_nuevo
      print(f"Stock actualizado a {stock_nuevo} unidades")
  else:
      print("Artículo no existente...")
      agregar_art:str = input(f"Desea agregar el artículo {art_buscado} al Listado? Presione ´s´ para agregar o cualquier otra tecla para Salir: ")
      if agregar_art == "s":
        stock_nuevo:int = input(f"Ingrese el stock para el nuevo artículo: ")
        stock[art_buscado] = stock_nuevo
        print(f"Stock actualizado a {stock_nuevo} unidades")
      else: 
        print("Saliendo...")
        salir = True
  opcion_salir:str = input("Presiones ´c´ para continuar o cualquier tecla para salir: ")
  if opcion_salir != "c":
    salir = True
    
"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:
agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
}
Permití consultar qué actividad hay en cierto día y hora."""
print("\n---Ejercicio 09---\n")
agenda = {
    ("LUNES", "10:00"): "Reunión",
    ("MARTES", "15:00"): "Clase de inglés",
    ("MIERCOLES", "12:00"): "Almuerzo familiar",
    ("JUEVES", "18:00"): "Bicicleta fija",
    ("VIERNES", "19:00"): "Paddle"
    }

salir:bool = False
while not salir:
        print("================")
        print(f"Agenda semanal")
        print("================")
        lista_agenda = list(agenda)
        for i in range(len(lista_agenda)):
                evento:str = agenda[lista_agenda[i]]
                print(f"{lista_agenda[i]}: ",evento)
        
        print("================")
        consultar:str = input("Consultar Agenda? Presione ´s´ para Consultar o cualquier otra tecla para salir: ")
        if consultar != "s":
                print("SALIENDO...")
                salir = True
        else:
                dia:str = input("Ingrese el día de la semana: ").upper()
                horario:str = input("Ingrese el horario (formato 12:00): ")
                buscar_evento = (dia, horario)
                if buscar_evento in agenda:
                        print(f"Día y horario: {buscar_evento} ")
                        print(f"Evento: {agenda[buscar_evento]}")
                else:
                        print(f"No hay eventos agendados para {buscar_evento}")
                        agendar:str = input(f"Desea agendar un evento en {buscar_evento}? Presione ´s´ para agendar o cualquier otra tecla para salir: ")
                        if agendar == "s":
                                nuevo_evento:str = input("Ingrese el nuevo evento: ")
                                agenda[buscar_evento] = nuevo_evento
                        else:
                                print("NO AGENDAMOS NUEVO EVENTO...")
                
"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
Ejemplo:
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}"""
print("\n---Ejercicio 10---\n")
original:dict = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago"}
invertido:dict = {}
print("Diccionario original:")
print(original)
lista_claves_original:list = list(original)
lista_valores_original:list = []

for i in range(len(lista_claves_original)):
    clave_original:str = lista_claves_original[i]
    valor_original:str = original[clave_original]
    lista_valores_original.append(valor_original)

print("\nLista claves original:")
print(lista_claves_original)
print("Lista valores original:")
print(lista_valores_original)

for i in range(len(lista_valores_original)):
    nueva_clave:str = lista_valores_original[i]
    nuevo_valor:str = lista_claves_original[i]
    invertido[nueva_clave] = nuevo_valor

print("\nDiccionario invertido:")
print(invertido)
