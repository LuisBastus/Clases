# Inicializamos la lista vacía
calificaciones = ()

# Solicitamos las notas para 3 unidades formativas (UF1, UF2 y UF3)
for i in range(1, 4):
    nombre_uf = input(f"Introduce el nombre de la UF{i}: ")
    nota_uf = float(input(f"Introduce la calificación de {nombre_uf}: "))
    calificaciones.append(nombre_uf)
    calificaciones.append(nota_uf)

# Calcula la nota media
total_notas = 0
num_notas = 0

# Recorremos la lista y sumamos solo las calificaciones numéricas
for i in range(1, len(calificaciones), 2):
    total_notas += calificaciones[i]
    num_notas += 1

nota_media = total_notas / num_notas

# Mostramos el resultado
print(f"La nota media es {nota_media:.2f}")
