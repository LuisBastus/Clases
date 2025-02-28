# Crear una lista vacía para las calificaciones
calificaciones = []

# Recoger los datos de 3 unidades formativas (nombre UF y calificación)
for i in range(1, 4):
    uf = input(f"Introduce el nombre de la UF{i}: ")
    try:
        nota = float(input(f"Introduce la calificación de {uf}: "))
        calificaciones.append(uf)
        calificaciones.append(nota)
    except ValueError:
        print("Por favor, introduce un número válido para la calificación.")

# Calcular la nota media
total = 0
for i in range(1, len(calificaciones), 2):  # Tomar solo las notas (en posiciones impares)
    total += calificaciones[i]

media = total / 3

# Mostrar la lista y la nota media
print("\nLista de calificaciones:", calificaciones)
print(f"La nota media es {media:.2f}")

# Inicializar variables para las notas máximas y mínimas
max_nota = calificaciones[1]  # Empezamos con la primera calificación
min_nota = calificaciones[1]
pos_max = 1
pos_min = 1

# Recorrer la lista para encontrar máximos y mínimos (solo las notas, en posiciones impares)
for i in range(1, len(calificaciones), 2):
    if calificaciones[i] >= max_nota:
        max_nota = calificaciones[i]
        pos_max = i
    if calificaciones[i] <= min_nota:
        min_nota = calificaciones[i]
        pos_min = i

# Mostrar los resultados
print(f"La nota máxima es {max_nota} y está en la posición {pos_max}.")
print(f"La nota mínima es {min_nota} y está en la posición {pos_min}.")
