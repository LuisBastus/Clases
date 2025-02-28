lista=[]
continuar = True 

while continuar: 
    print("\n--Lista de la compra--")
    print("============================")
    print("1. Agrega un elemento: ")
    print("2. Buscar elemento: ")
    print("3. Eleiminar elemento: ")
    print("4. Mostrar lista.")
    print("5. Vaciar lista.")
    print("6. Salir.")

    eleccion = input("Elige Una opción del 1 al 6: ")
    
    if eleccion == "1":
        print("has escogido la opcion 1!")
        elemento = input("Escribe el elemento: ")
        if elemento in lista:
            print("El elemento ya se encuentra en la lista")
        else:
            lista.append(elemento)
            print("El elemento ha sido guardado con exito!")
            
    elif eleccion == "2":
        print("has escogido la opcion 2!")
        elementobuscar = input("Escribe el elemento a buscar: ")
        if elementobuscar in lista:
            print("El elemento se encuentra en la lista")
        else:
            print("El elemento no se encuentra en la lista")
    
    elif eleccion == "3":
        print("has escogido la opcion 3!")
        elementoeliminar = input("Escribe el elemento a eliminar: ")
        if elementoeliminar in lista:
            lista.remove(elementoeliminar)
            print("El elemento ha sido eliminado con exito!")
        else:
            print("El elemento no se encuentra en la lista")
         
    elif eleccion == "4":
        print("has escogido la opcion 4!")
        print(lista)
        
    elif eleccion == "5":
        print ("has escogido la opcion 5!")
        lista.clear()
        print("La lista ha sido vaciada con exito!")
        
    elif eleccion == "6":
        print("has escogido la opcion 6!")
        print("Saliendo del programa...")
        continuar = False        
        
        
