lista=[]
continuar = True 

while continuar:
    print("\n---agenda de contatctos---")
    print("1.agregar contacto")
    print("2.buscar contacto")
    print("3.eliminar contacto")
    print("4.mostrar contactos")
    print("5.salir")
    
    eleccion == input("elige la accion a realizar:")
    
    while eleccion == "1":
        nombre = input("ingrese el nombre del contacto:")
        if nombre in lista:
            print("el contacto ya existe en la agenda")
        else:
            
