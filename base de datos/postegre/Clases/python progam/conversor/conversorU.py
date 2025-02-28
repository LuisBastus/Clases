def mostrar_menu_principal():
    print("\nElige una de las siguientes opciones:")
    print("1) Peso")
    print("2) Temperatura")
    print("3) Distancia")
    print("4) Altura")
    print("5) Tiempo")
    print("6) [Salir]")

def mostrar_menu_unidades(opcion):
    if opcion == 1:
        print("\nElige una unidad de origen:")
        print("1) kg")
        print("2) oz")
    # Se pueden añadir otros menús de unidades para otras opciones

def obtener_opcion_principal():
    while True:
        mostrar_menu_principal()
        try:
            opcion = int(input("\nOpción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print(f"¡La opción {opcion} no existe!")
        except ValueError:
            print("Por favor, introduce un número válido.")

def obtener_opcion_unidad():
    while True:
        try:
            unidad = int(input("\nUnidad: "))
            if unidad == 1 or unidad == 2:
                return unidad
            else:
                print(f"¡La opción {unidad} no existe!")
        except ValueError:
            print("Por favor, introduce un número válido.")

def iniciar_programa():
    while True:
        opcion_principal = obtener_opcion_principal()
        if opcion_principal == 6:
            print("Saliendo del programa...")
            break
        else:
            print(f"Has elegido la opción {opcion_principal}")
            mostrar_menu_unidades(opcion_principal)
            unidad_origen = obtener_opcion_unidad()
            print(f"Has elegido la unidad {unidad_origen}")

iniciar_programa()

