#biblioteca 

catalogo = {}
continuar = True

#lista de opciones 
while continuar:
    print("\nCatalogo de libros")
    print("1. Agregar libro (libro, autor, año de publicacion)")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Mostrar catalogo")
    print("5. Vaciar catalogo")
    print("6. Editar libro")
    print("7. Salir")

    eleccion = input("elige una opcion (1 a 6): ")

    if eleccion == "1":
        print(" has escogido la opcion 1")
        libro = input("Escribe el libreo que deseas agregar:")
        autor = input("Escribe el autor del libro: ")
        año = input("Escribe el año de publicacion: ")
        catalogo[libro] = [autor, año]
        print("El libro ha sido guardado con exito!")
    
    if eleccion == "2": 
        print("has escogido la opcion 2")
        buscado = input("Escribe el libro que deseas buscar: ")
        if buscado in catalogo:
            print("EL libro se encuentra en el catalogo")
        else : 
            print("el libro no se encuentra en el catalogo")
    
    if eleccion == "3":
        print("opcion 3")
        eliminar = input("Escribe el nunero que deseas eliminar:")
        if eliminar in catalogo:
            catalogo.pop(eliminar)
            print("El elemento se ha borrado con exito")
        else:
            print("el elemento no existe o tiene un error en la escritura")
    
    if eleccion == "4":
        print ("opcion 4")
        print(catalogo)
    
    if eleccion == "5":
        print("has escogido la opcion 5")
        catalogo.clear()
        print("El catalogo se ha borrado con exito")
        
    if eleccion == 6:
        print("HAs escogido la opcion 6")
        
        
    if eleccion =="7":
        print("has escogido la opcion 7")
        continuar = False