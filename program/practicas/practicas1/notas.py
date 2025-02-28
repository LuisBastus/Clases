#Crea un diccionario llamado estudiantes donde las claves sean los nombres de 
# los estudiantes y los valores sean sus notas.

catalogo = {}
continuar = True 

while continuar:
    print("\nNotas de estudiantes")
    print("-----------------------------------")
    print("1. Añadir estudiantes")
    print("2. eliminar estudiante")
    print("3. Buscar Estudiante")
    print("4. Mostar Lista de estudiantes")
    print("5. Vaciar lista")
    print("6. Salir")
    print("----------------------------------------")
    
    eleccion = input("Escribe la opcion que deseas realizar: ")
    
    if eleccion == "1":
        print("has escogiodo la opcion 1")
        estudiante = input("Escribe el estudiante que deseas agregar: ")
        nota = int(input("Escribe la nota del estudiante: "))
        catalogo[estudiante] = [nota]
        print("La informacion ha sido guardada correctamente")
    
    if eleccion == "2":
       print("has escogido la opcion 2")
       eliminar = input("escribe el estudiante que deseas eliminar: ")
       if eliminar in catalogo:
           catalogo.pop(eliminar)
           print("el estudiante ha sido eliminado con exito")
       else: 
           print("el estudiante no existe en la lista")
           
    if eleccion == "3":
        print("has escogido la opcion 3")
        buscar = input("Escribe el estudiante que deseas buscar: ")
        if buscar in catalogo:
            print(f"el estudiante {buscar} se encuentra en la lista")
        else:
            print(f"el estudiante {buscar} no se encuentra en la lista")
            
    if eleccion == "4":
        print("has escogido la opcion 4")
        print(catalogo)
        
    if eleccion == "5":
        print("has escogido la eleccion 5")
        catalogo.clear()
        print("la lista ha sido borrada con exito")
    
    if eleccion == "6":
        print("saliendo del programa")
        continuar = False 