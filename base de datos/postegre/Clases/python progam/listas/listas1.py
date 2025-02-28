# Crear la lista vacía
lista = []

# Pedir 4 números al usuario
while len(lista) < 4:
    x = input("Introduce un número: ")
    try:
        # Convertir la entrada a número y agregarlo a la lista
        num = float(x)  
        lista.append(num)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Mostrar cada número con su cuadrado y cubo
print("\nResultados:")
for elemento in lista:
    cuadrado = elemento ** 2
    cubo = elemento ** 3
    print(f"Número: {elemento}, Cuadrado: {cuadrado}, Cubo: {cubo}")
