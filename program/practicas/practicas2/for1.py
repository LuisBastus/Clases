lista = []
continuar = True 

while continuar: 
    print("\nEscge una opcion: ")
    print("1. Introduce un numero")
    print("2. Ver lista")
    

    eleccion = input("Escoge una opcion: ")
    
    if eleccion == "1":
        lista.append(input("introduce un numero: "))
        
    elif eleccion == "2":
        print(lista)
    
        
