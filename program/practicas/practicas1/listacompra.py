#lista de la compra

lista = []
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
        if antiguo in lista: 
            nuevo = input("Escribe el nuevo elemnto: ")
            for x in range(len(lista)):
                if lista[x] == antiguo: 
                    lista[x] = nuevo
                    print("El elemento ha sido guardado con exito!")
        else:
            print(f"El elemento {antiguo} esta en la lista")

    elif eleccion == "3":
        print("has escogido la opcion 3")
        buscado = input("¿que elemendo quieres buscar?: ")
        if buscado in lista: 
            print(f"el elemento {buscado} esta en la lista")
        else: 
             print(f"el elemento1 {buscado} no esta en la lista")
        
    elif eleccion == "4":
        print("has escogido la opcion 4")
        elim = input("elige el elemnto que desear borrar: ") #crea una variable 
        if elim in lista:
            lista.remove(elim) #usar variable crada para usar funcion 
            print("el elemento ha sido borrado correctamente")
            
        else:
            print 

    elif eleccion == "5":
        print("has escogido la opcion 5")
        lista2 = []
        for i in lista:
            if i not in lista2: 
                lista2.append(i)
            lista = lista2
        print("Los elementos repetidos han sido eliminados")
             
        
    #solo pinta la lista del apartado 5           
    elif eleccion == "6":
        print("has escogido la opcion 6")
        print(f"La lista actual sin elementos repetidos es: {lista}")

    elif eleccion == "7":
        print("¡Adios!")
        continuar = False
    