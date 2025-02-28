#lista de la compra

lista = []
lista2 = []
lista2 = lista[0:1]
continuar = True
while continuar:
    print("\nLa lista de la compra: ")
    print("1. agrega un elemento")
    print("2. Sustituir un elemento")
    print("3. Buscar un elemento")
    print("4. Eliminar elemento")
    print("5. Eliminar repetidos")
    print("6. Mostrar lista")
    print("7. Salir")
    
#eleccion de opcion 

    eleccion = input("Elige una de las  opciones (1 a 7): ")

    if eleccion == "1":
        print("has escogido al opcion 1")
        elemento = input("escribe un elemento: ")
        lista.append(elemento) #Guarda la variable elemento 
        
    elif eleccion == "2":
        print("has escogido la opcion 2")
        antiguo = input("Escribe el elemento que quieres sustituir: ")
        nuevo = input("Escribe el nuevo elemnto: ")
        for x in range(len(lista)):
            if lista[x] == antiguo: 
                lista[x] = nuevo
                print("El elemento ha sido guardado con exito!")

    elif eleccion == "3":
        print("has escogido la opcion 3")
        buscado = input("¿que elemendo quieres buscar?: ")
        encontrado = False 
        for elemento in lista:
            if elemento == buscado: 
             encontrado = True 
        if encontrado:
            print(f"el elemento {buscado} esta en la lista")         
        else: 
            print(f"el elemento {buscado} no esta en la lista")
        
    elif eleccion == "4":
        print("has escogido la opcion 4")
        elim = input("elige el elemnto que desear borrar: ")
        if elim in lista:
            lista.remove(elim)
            print("el elemento ha sido borrado correctamente")

    elif eleccion == "5":
        print("has escogido la opcion 5")
        
        for i in range(len(lista)):
            if lista[i] not in lista2:
                lista2.append(lista[i])
        print(f"La lista actual es: {lista2}")
                
    elif eleccion == "6":
        print("has escogido la opcion 6")
        print(f"La lista actualmente es: {lista2}")

    elif eleccion == "7":
        print("¡Adios!")
        continuar = False


    