def mostrar_menu_principal():
    print("\nElige una de las siguientes opciones:")
    print("1) Peso")
    print("2) Temperatura")
    print("3) Distancia")
    print("4) Altura")
    print("5) Tiempo")
    print("6) [Salir]")

def mostrar_menu_peso():
    print("\nElige una unidad de origen:")
    print("1) kg")
    print("2) oz")

def mostrar_menu_temperatura():
    print("\nElige una unidad de origen:")  
    print("1) Celsius (C)")
    print("2) Fahrenheit (F)")

def mostrar_menu_distancia():
    print("\nElige una unidad de origen:")
    print("1) km")
    print("2) millas")

def mostrar_menu_altura():
    print("\nElige una unidad de origen:")
    print("1) cm")
    print("2) pies (ft)")

def mostrar_menu_tiempo():
    print("\nElige una unidad de origen:")
    print("1) segundos (s)")
    print("2) cronómetro (h:m:s)")

def convertir_peso(unidad, cantidad):
    if unidad == 1:  # kg a oz
        return cantidad * 35.27, "oz"
    elif unidad == 2:  # oz a kg
        return cantidad / 35.27, "kg"

def convertir_temperatura(unidad, cantidad):
    if unidad == 1:  # C a F
        return (cantidad * 9/5) + 32, "F"
    elif unidad == 2:  # F a C
        return (cantidad - 32) * 5/9, "C"

def convertir_distancia(unidad, cantidad):
    if unidad == 1:  # km a millas
        return cantidad / 1.609344, "millas"
    elif unidad == 2:  # millas a km
        return cantidad * 1.609344, "km"

def convertir_altura(unidad, cantidad):
    if unidad == 1:  # cm a pies
        pies = cantidad / 30.48
        pulgadas = (pies - int(pies)) * 12
        return f"{int(pies)} pies y {pulgadas:.2f} pulgadas", ""
    elif unidad == 2:  # pies a cm
        pies = int(input("Introduce el número de pies: "))
        pulgadas = float(input("Introduce el número de pulgadas: "))
        return (pies * 30.48) + (pulgadas * 2.54), "cm"

def convertir_tiempo(unidad, cantidad):
    if unidad == 1:  # segundos a h:m:s
        horas = cantidad // 3600
        minutos = (cantidad % 3600) // 60
        segundos = cantidad % 60
        return f"{horas}h:{minutos}m:{segundos}s", ""
    elif unidad == 2:  # h:m:s a segundos
        horas = int(input("Introduce las horas: "))
        minutos = int(input("Introduce los minutos: "))
        segundos = int(input("Introduce los segundos: "))
        return (horas * 3600) + (minutos * 60) + segundos, "s"

def gestionar_conversion(opcion):
    if opcion == 1:  # Peso
        mostrar_menu_peso()
        unidad = int(input("Unidad: "))
        if unidad not in [1, 2]:
            print("¡Opción incorrecta!")
            return
        cantidad = float(input("Introduce la cantidad: "))
        resultado, unidad_dest = convertir_peso(unidad, cantidad)
    
    elif opcion == 2:  # Temperatura
        mostrar_menu_temperatura()
        unidad = int(input("Unidad: "))
        if unidad not in [1, 2]:
            print("¡Opción incorrecta!")
            return
        cantidad = float(input("Introduce la cantidad: "))
        resultado, unidad_dest = convertir_temperatura(unidad, cantidad)
    
    elif opcion == 3:  # Distancia
        mostrar_menu_distancia()
        unidad = int(input("Unidad: "))
        if unidad not in [1, 2]:
            print("¡Opción incorrecta!")
            return
        cantidad = float(input("Introduce la cantidad: "))
        resultado, unidad_dest = convertir_distancia(unidad, cantidad)

    elif opcion == 4:  # Altura
        mostrar_menu_altura()
        unidad = int(input("Unidad: "))
        if unidad not in [1, 2]:
            print("¡Opción incorrecta!")
            return
        cantidad = float(input("Introduce la cantidad: "))
        resultado, unidad_dest = convertir_altura(unidad, cantidad)
    
    elif opcion == 5:  # Tiempo
        mostrar_menu_tiempo()
        unidad = int(input("Unidad: "))
        if unidad not in [1, 2]:
            print("¡Opción incorrecta!")
            return
        cantidad = int(input("Introduce la cantidad en segundos: "))
        resultado, unidad_dest = convertir_tiempo(unidad, cantidad)
    
    else:
        print("¡Opción incorrecta!")
        return

    print(f"El resultado de la conversión es: {resultado} {unidad_dest}")

# Programa principal
while True:
    mostrar_menu_principal()
    opcion = int(input("Opción: "))
    
    if opcion == 6:
        print("¡Gracias por usar el conversor! ¡Hasta pronto!")
        break
    elif opcion in [1, 2, 3, 4, 5]:
        gestionar_conversion(opcion)
    else:
        print("¡La opción seleccionada no existe!")
