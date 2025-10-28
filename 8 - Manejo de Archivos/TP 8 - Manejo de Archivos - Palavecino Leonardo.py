"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""
print("\n---Ejercicio 01---\n")
with open("productos.txt","w") as archivo:
    archivo.write("lapicera,120.5,30\n")
    archivo.write("regla,200.0,25\n")
    archivo.write("goma,100.5,40\n")

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""
print("\n---Ejercicio 02---\n")
with open("productos.txt","r") as archivo:
    
    for linea in archivo:
            linea = linea.strip()
            partes = linea.split(",")
            print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")

"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente."""
print("\n---Ejercicio 03---\n")
salir:bool = False
while not salir:
    with open("productos.txt","r") as archivo:
        print("======= Catálogo de productos =======")
        for linea in archivo:
                linea = linea.strip()
                partes = linea.split(",")
                print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
        print("=====================================")
        agregar:str = input("Desea Agregar un nuevo producto? Presione ´s´ para Agregar o cualquier otra tecla para Salir: ")
        if agregar != "s":
            print("Saliendo...")
            salir = True
        else:
            nombre:str = input("Ingrese el nombre: ")
            precio:str = input("Ingrese el precio: ")
            cantidad:str = input("Ingrese la cantidad: ")        
            with open("productos.txt","a") as archivo:
                nueva_fila:str = nombre + "," + precio + "," + cantidad + "\n"
                archivo.write(nueva_fila)           
                               
"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad"""
print("\n---Ejercicio 04---\n")
with open("productos.txt","r") as archivo:
    productos:list = []
    for linea in archivo:
            linea = linea.strip()
            partes = linea.split(",")
            productos.append({"nombre": partes[0], "precio": partes[1], "cantidad": partes[2]})
    
    print(productos)        

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error."""
print("\n---Ejercicio 05---\n")
salir:bool = False
while not salir:
    encontrado:bool = False
    producto_buscado:str = input("Ingrese el producto a buscar o ´s´para Salir: ")
    if producto_buscado != "s":
        for i in range(len(productos)):
            if productos[i]["nombre"] == producto_buscado:
                print(f"""
                    ========================================
                    Producto encontrado, datos del producto:
                    Nombre: {productos[i]["nombre"]}
                    Precio: ${productos[i]["precio"]}
                    Cantidad: {productos[i]["cantidad"]}
                    ========================================
                    """)
                encontrado = True
        if encontrado == False:
            print("Producto no encontrado...")        
    else:
         print("Saliendo...")
         salir = True                
    
"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista."""
print("\n---Ejercicio 06---\n")
with open("productos.txt", "w") as archivo:
     for i in range(len(productos)):
          linea:str = productos[i]["nombre"] + "," + productos[i]["precio"] + "," + productos[i]["cantidad"] + "\n"
          archivo.write(linea)

print("Archivo ´productos.txt´:")
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
