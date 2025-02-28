agenda = []
grupos = []
continuar = True
while continuar:
    print("\nMenu")
    print("1. Contacos")
    print("2. grupos")
    print("3. salir")

    eleccion = input("Elige una opción del 1 al 3: ")

    if eleccion == "1": 
        seguir = True 
        while seguir:
            print("\n Que haras?")
            print("----------------------------")
            print("1.crear contacto")
            print("2.Buscar y editar contacto") 
            print("3.Eliminar contacto")
            print("4.Mostrar agenda")
            print("5.Salir")
            
            eleccion2 = input ("elige una opcion. ")
        
            if eleccion == "1":
                print("opcion: 1")
                contacto = input ("Nombre del contacto:")
                telefono = input ("Telefono principal: ")
                agenda.append([contacto, telefono])
                print("Contacto creado")
            
            elif eleccion == "2":
                print("opcion: 2")
                contacto = input("Nombre del contacto a buscar: ")
                encontrado = False 
                for i in range(len(agenda)):
                    if agenda [i][0] 
            
            elif eleccion == "5":
                print("saliendo del programa")
                seguir = False 
                
    

    elif eleccion == "3":
        print("saliendo del programa")
        continuar = False