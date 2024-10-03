#ACTUALIZACION EN LOTE
def mostrar_menu():
    print("Seleccione una opcion:")
    print("1. Actualizar productos")

def buscar_producto(productos, busqueda):
    for producto in productos:
        if producto["nombre"] == busqueda:
            return producto
    
    return False
    
def agregar_producto():
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
productos=[{"nombre":"JUGO TANG MANZANA X 15GR", "precio":200, "grupo":"JUGO TANG X 15GR"},
           {"nombre":"JUGO TANG NARANJA X 15GR", "precio":200, "grupo":"JUGO TANG X 15GR"},
           {"nombre":"JUGO TANG PERA X 15GR", "precio":200, "grupo":"JUGO TANG X 15GR"},
           {"nombre":"MAYONESA HELLMAN´S X 1KG", "precio":1000, "grupo": None},
           {"nombre":"SAL FINA CELUSAL X 500GR", "precio":500, "grupo": None},
           {"nombre":"AGUA MINERAL NESTLE X 500ML", "precio":400, "grupo": None},
           {"nombre":"PAN DE PANCHO BIMBO X 6UD", "precio":1500, "grupo": "PAN DE VIENA"},
           {"nombre":"PAN DE HAMBURGUESA BIMBO X 4UD", "precio":1500, "grupo": "PAN DE VIENA"}
           ]
while True:
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
        