#ACTUALIZACION EN LOTE
def cargar_productos_desde_csv():
    try:
        productos = []
        archivo_csv = open('lista_de_precios - Sheet1.csv', mode='r', encoding='UTF-8')
        archivo_csv.seek(1)

        for registro in archivo_csv:
            nombre, precio, grupo = registro.split(',')
            if not grupo:
                grupo = None
            productos.append({"nombre": nombre, "precio": float(precio), "grupo": grupo})
    
    except:

def mostrar_menu():
    print("Seleccione una opcion:")
    print("1. Actualizar productos")

def buscar_producto(productos, busqueda):
    for producto in productos:
        if producto["nombre"] == busqueda:
            return producto
    
    return False
    
def agregar_producto():
    try:
        archivo_csv = open('lista_de_precios - Sheet1.csv', mode w)
    nombre = input("Descripcion:")
    grupo = None
    grupo = input("grupo (No obligatorio):")
    precio = input("precio:")
    
    productos.append({"nombre": nombre, "precio": precio, "grupo": grupo})
    print("El producto ha sido agregado.")
    
def actualizar_precio_grupo(productos, grupo, nuevo_precio):
    for producto in productos:
        if producto["grupo"] == grupo:
            producto["precio"] = nuevo_precio
    print(f"Todos los productos del grupo '{grupo}' han sido actualizados a {nuevo_precio}.")
    
def actualizar_precio(productos, nombre, nuevo_precio):
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            
    print("El producto ha sido actualizado.")
#PP

while True:
    productos = cargar_productos_desde_csv()
    mostrar_menu()
    opcion = input("Ingrese su opcion: ")
    
    if opcion == "1":
        busqueda = input("Buscar:")
        agregado = buscar_producto(productos, busqueda)
        
        if agregado:
            for clave, valor in agregado.items():
                print(f"{clave}: {valor}")
                
            print("1. Actualizar precio")
            print("2. Actualizar precio en lote")
    
            rta = input("Ingrese su opcion:")
            
            if rta == "1":
                nuevo_precio = input("nuevo precio:")
                agregar_producto(productos, busqueda, nuevo_precio)
                
            elif rta == "2":
                nuevo_precio = input("nuevo precio:")
                actualizar_precio_grupo(productos, agregado["grupo"], nuevo_precio)
                
            else:
                print("Opcion no valida, intente nuevamente.")
        else:
            rta = input("El producto no se encuentra en la lista de productos. ¿Desea agregarlo?")
            if rta == "Si":
                agregar_producto()
                
    else:
        print("Opcion no valida, intente nuevamente.")
        