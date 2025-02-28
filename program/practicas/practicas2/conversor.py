continuar = True

while continuar:
    print("\nEscoge una opcione")
    print("1. peso")
    print("2. temperatura")
    print("3. distancia")
    print("4. altura")
    print("5. tiempo")
    print("6. salir")

    eleccion = input("escribe la opcion que deseas: ")
    
    if eleccion == "1":
        print("has escogido la opcion 1")
        kg = float(input("introduce el peso en kg "))
        oz = kg / 35.27
        print(f"el peso en en onzas es: {oz}")
        
    if eleccion == "2":
        print("has escogido la opcion 2")
        Cen = float(input("introduce la temperatura en grados centigrados: "))
        Fa = 9 / 5 * Cen + 3
        print(f"son {Fa}º")
    
    if eleccion == "3":
        print("has escogido la opcion 3")
        mi = float(input("Escribe las millas: "))
        km = mi / 0.62137
        print(f"son {km} km ")
    
    if eleccion == "4":
        print("has escogido la opcion 4")
        ft = float(input("escribe el tamaño en pies: "))
        cm = ft * 30.48
        inc = ft * 12
        print(f"{ft} pies son: {cm} cm y {inc} in")
        
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