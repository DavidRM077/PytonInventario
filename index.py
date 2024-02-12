""" Funcion Para Agregar productos """

def Agregar_Productos(inventario):
    nombre = input("Ingresa el nombre del producto : ")
    descripcion = input("Ingresa la descripcion del producto: ")
    precio = input("Ingresa el precio del producto")
    cantidad = input("Ingresa la cantidad disponible del producto")
    inventario[nombre] = {"descripcion":descripcion,"precio":precio,"cantidad":cantidad}
    print("Producto Agregado")

"""  Funcion para actualizar un producto  """

def Actualizar_Productos(inventario):
    nombre = input("Ingresa el nombre del producto a actualziar: ")
    if nombre in inventario:
        print("Actualice los detalles del producto")
        descripcion = input(f"Nueva descripción ({inventario[nombre]['descripcion']}): ") or inventario[nombre]['descripcion']
        precio = float(input(f"Nuevo precio ({inventario[nombre]['precio']}): ")) or inventario[nombre]['precio']
        cantidad = input(f"Nueva Cantidad ({inventario[nombre]['cantidad']}): ") or inventario[nombre]["cantidad"]
        inventario[nombre] = {"descripcion":descripcion,"precio":precio,"cantidad":cantidad}
        print("el producto fue actualizado en el inventario")
    else:
        print("el producto no existe en el inventario")


 

        """ Funcion para eliminar producto del inventario  """

def Eliminar_Productos(inventario):
    nombre = input("Ingresa el nombre del producto para eliminar")
    if nombre in inventario:
        del inventario[nombre]
        print("El producto fue eliminado con exito")
    else:
        print("El producto no existe o no fue encontrado")


""" Funcion para mostrar los productos del inventario  """

def Mostrar_Inventario(inventario):
    print("Inventario:")
    for nombre,detalles, in inventario.items():
        print(f"Nombre: {nombre}, Descripcion: {detalles['descripcion']}, Precio:{detalles['precio']},Cantidad: {detalles['cantidad']}")



""" Funcion Principal        """

def Principal():
    inventario = {}
    while True:
        print("\n1 Agregar Producto \n2 Actualizar Producto \n3 Eliminar Producto \n4 Mostrar Inventario \n5 Salir")
        opcion = input("Selecione una opcion : ")
        if opcion == "1":
            Agregar_Productos(inventario)
        elif opcion == "2":
            Actualizar_Productos(inventario)
        elif opcion == "3":
            Eliminar_Productos(inventario)
        elif opcion == "4":
            Mostrar_Inventario(inventario)
        elif opcion == "5":
            print("Saliendo del sistema")
            break
        else:
            print("opcion invalida , intentelo denuevo")


if __name__  == "__main__":
    Principal()