#ACTUALIZACION EN LOTE
def cargar_productos_desde_csv():
    #Crea una lista con los productos del archivo csv donde se encuentran y la devuelve.

    try:
        productos = []
        archivo_csv = open('lista_de_precios - Sheet1.csv', mode='r', encoding='UTF-8')

        for i, registro in enumerate(archivo_csv):
            if i == 0:
                continue
            nombre, precio, grupo = registro.strip().split(',')
            if not grupo:
                grupo = None
            productos.append({"nombre": nombre, "precio": precio, "grupo": grupo})
    
    except FileNotFoundError as m:
        print(f"El archivo {archivo_csv} no existe. Para mas detalle: {m}")
    except OSError as m:
        print(f"Hubo un error relacionado con el sistema operativo. Para mas detalle: {m}")
    finally:
        try:
            archivo_csv.close()
        except Exception:
            print("Se ha producido un error a la hora de cerrar el archivo.")
    return productos
def guardar_productos_en_csv(productos):
    #Guarda cualquier cambio hecho a la lista y sobreescribe el archivo csv.
    try:
        archivo_csv = open('lista_de_precios - Sheet1.csv', mode = 'w', encoding='UTF-8')
        archivo_csv.write("PRODUCTO,PRECIO,GRUPO\n")
        for producto in productos:
            archivo_csv.write(f'{producto["nombre"]},{producto["precio"]},{producto["grupo"]}\n')

        print("Los cambios se han guardado con exito.")
    
    except FileNotFoundError as m:
        print(f"El archivo {archivo_csv} no existe. Para mas detalle: {m}")
    except OSError as m:
        print(f"Hubo un error relacionado con el sistema operativo. Para mas detalle: {m}")
    
    finally:
        try:
            archivo_csv.close()
        except Exception:
            print("Se ha producido un error a la hora de cerrar el archivo csv.")
            
def mostrar_menu():
    #Muesta el menu con todas las funcionalidades que tiene el programa.

    print("MENU\n")
    print("Seleccione una opcion:")
    print("1. Actualizar productos")
    print("2. Agregar productos")
    print("3. Guardar cambios")
    print("4. Salir\n")

def solicitar_opcion_valida(opciones_validas): 
    #Solicita, valida y devuelve la opcion que se va a elegir en un intervalo determinado.
    
    while True:
        try:            
            opcion = int(input("Ingrese su opción: "))
            if opcion in opciones_validas:
                return opcion
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def solicitar_precio():
    while True:
        try:
            precio = float(input("Ingrese el nuevo precio: "))
            return precio
        except ValueError:
            print("Por favor, ingrese un valor numérico.")

def buscar_producto(productos, busqueda):
    #Busca y devuelve un producto de la lista de productos. Si no lo encuentra, devuelve False.

    for producto in productos:
        if producto["nombre"] == busqueda:
            return producto
    
    return False
    
def agregar_producto(productos):
    #Solicita los datos correspondientes, agrega el nuevo producto a la lista y devuelve la nueva lista.

    print("DATOS DEL PRODUCTO")
    nombre = input("Descripcion:")
    grupo = None
    grupo = input("grupo (No obligatorio):")
    precio = solicitar_precio()
    
    productos.append({"nombre": nombre, "precio": precio, "grupo": grupo})
    print("El producto ha sido agregado.")

    return productos
    
def actualizar_precio(productos, nombre, nuevo_precio):
    #Actualiza el precio de un solo producto y devuelve la nueva lista.

    for producto in productos:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            break
            
    print("El producto ha sido actualizado.")
    return productos

def actualizar_precio_grupo(productos, grupo, nuevo_precio):
    #Actualiza los precios de los productos de un grupo y devuelve la nueva lista.

    for producto in productos:
        if producto["grupo"] == grupo:
            producto["precio"] = nuevo_precio
    print(f"Todos los productos del grupo '{grupo}' han sido actualizados a {nuevo_precio}.")

    return productos

#PP
productos = cargar_productos_desde_csv() 

while True:
    mostrar_menu() 
    opcion = solicitar_opcion_valida([1,2,3,4]) 
    
    if opcion == 1:
        busqueda = input("\nBuscar:")
        agregado = buscar_producto(productos, busqueda) 
        
        if agregado:
            for clave, valor in agregado.items():
                print(f"{clave}: {valor}")
                
            print("1. Actualizar precio")
            print("2. Actualizar precio en lote")
    
            opcion = solicitar_opcion_valida([1,2]) 
            
            if opcion == 1:
                nuevo_precio = solicitar_precio()
                productos = actualizar_precio(productos, busqueda, nuevo_precio) 
                
            elif opcion == 2:
                nuevo_precio = solicitar_precio()
                productos = actualizar_precio_grupo(productos, agregado["grupo"], nuevo_precio) 
                
        else:
            print("El producto no se encuentra en la lista de productos. ¿Desea agregarlo?")
            opcion = solicitar_opcion_valida([0,1])
            if opcion == 1:
                productos = agregar_producto(productos) 
    elif opcion == 2:
        productos = agregar_producto(productos)
    
    elif opcion == 3:
        guardar_productos_en_csv(productos)
    elif opcion == 4:
        guardar_productos_en_csv(productos)
        print("Saliendo del programa...")
        break 