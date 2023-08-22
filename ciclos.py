print("***Departamento de confeccion***")
print("1. Ingresar producto a fabrica")
print("2. Mostrar inventario en fabrica")
print("0. Salir")
opcion=100

listaProductos=[]
while opcion!=0:
    opcion=int(input("Digita una opcion: "))
    if opcion==1:
        print("*Ingresa nuevo producto**")
        producto=input("Ingresa el producto: ")
        #Agregar un producto a la lista de productos
        listaProductos.append(producto)
    elif opcion==2:
        print("**Mostrando inventario**")
        print(listaProductos)
    elif opcion==0:
        print("Gracias, hasta pronto.")
    else:
        print("Opcion invalida..")