continuar = True

while continuar:
    print("\nEscoge una opcione")
    print("----------------------")
    print("1. peso")
    print("2. temperatura")
    print("3. distancia")
    print("4. altura")
    print("5. tiempo")
    print("6. salir")

    eleccion = input("escribe la opcion que deseas: ")
    
    if eleccion == "1":
        print("\nhas escogido la opcion 1")
        print("-----------------------------")
        print("1. Kg")
        print("2. oz")
        
        eleccion2 = input("Selecciona una unidad: ")
        
        if eleccion2 == "1":
            print("opcion 1:")
            kg = float(input("Escribe la cantidad en kg: "))
            oz = kg * 35.27
            print(f"{kg}kg Serian {oz}oz.")
        
        if eleccion2 == "2":
            print("opcion 2:")
            oz = float(input("Escribe la cantidad en oz: "))
            kg = oz / 35.27
            print(f"{oz}oz Serian {kg}kg.") 
            
        
        
    if eleccion == "2":
        print("\nhas escogido la opcion 2")
        print("---------------------------")
        print("1. Grados Centigrados: ")
        print("2. Grados Fahrenheit")
        
        eleccion2 = input("Escoge la opcion")
        
        if eleccion2 == "1":
            print("opncion 1:")
            C = float(input("Escribe los grados Cº: "))
            F = 9 / 5 * C + 32
            print(f"{C}Cº Serian {F}Fº.") 
        
        if eleccion2 == "2":
            print("opcion 2")
            F = float(input("Escribe los grados Fº: "))
            C = (F - 32) * 5 / 9 
            print(f"{F}Fº Serian {C}Cº.") 
        
      
    if eleccion == "3":
        print("\nhas escogido la opcion 3")
        print("--------------------------")
        print("1.Km")
        print("2.millas")
        
        eleccion2 = input("Escribe la opcion: ")
        
        if eleccion2 == "1":
            print("opcion 1")
            km = float(input("Escribe la opcion en Km: "))
            mi = 1,609344 * km
            print(f"{km}km son {mi} millas")
        
        if eleccion2 == "2":
            print("opcion 2")
            mi = float(input("Escribe la opcion en millas: "))
            km = mi / 0.62137
            print(f"{mi}millas son {km} km")
     
    if eleccion == "4":
        print("\nhas escogido la opcion 4")
        print("-------------------------")
        print("1. cm")
        print("2. pulgadas")
        
        eleccion2 = input("Escribe la opcion: ")
        
        if eleccion2 == "1":
            print("opcion 1")
            cm = float(input("escribe el tamaño en cm: "))
            
            
            
    if eleccion == "5":
        print("has escogido la opcion 5")
        hora = float(input("escribe el la hora:"))
        seg = 60 * 60 * hora 
        print(seg)     
        segu = float(input("escribe los segundos: "))
        hora = segu / 60 / 60
        print(hora)
    
    if eleccion == "6":
        print("Saliendo...")
        continuar = False 