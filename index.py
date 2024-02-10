""" Funcion Para Agregar productos """

def Agregar_Productos(inventario):
    nombre = input("Ingresa el nombre del producto : ")
    descripcion = input("Ingresa la descripcion del producto: ")
    precio = input("Ingresa el precio del producto")
    cantidad = input("Ingresa la cantidad disponible del producto")
    inventario[nombre] = {"descripcion":descripcion,"precio":precio,"cantidad":cantidad}
    print("Producto Agregado")

"""  Funcion para actualizar un producto  """

def Actualizar_Producto(inventario):
    nombre = input("Ingresa el nombre del producto a actualziar: ")
    if nombre in inventario:
        print("Actualice los detalles del producto")
        descripcion = input(f"Nueva descripción ({inventario[nombre]['descripcion']}): ") or inventario[nombre]['descripcion']
        precio = float(input(f"Nuevo precio  ({inventario[nombre]["desripcion"]}): ") or inventario[nombre["precio"]]) 
        cantidad = input(f"Nueva Cantidad ({inventario[nombre]["descripcion"]}):"   or inventario[nombre]["cantidad"])
        inventario[nombre] = {"descripcion":descripcion,"precio":precio,"cantidad":cantidad}
        print("el producto fue actualizado en el inventario")
    else:
        print("el producto no existe en el inventario")