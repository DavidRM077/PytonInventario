""" Funcion Para Agregar productos """

def Agregar_Productos(inventario):
    nombre = input("Ingresa el nombre del producto : ")
    descripcion = input("Ingresa la descripcion del producto: ")
    precio = input("Ingresa el precio del producto")
    cantidad = input("Ingresa la cantidad disponible del producto")
    inventario[nombre] = {"descripcion":descripcion,"precio":precio,"cantidad":cantidad}
    print("Producto Agregado")

 