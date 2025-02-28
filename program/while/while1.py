numeros = []
while True:
    numero = float(input("Introduce número: "))
    if numero < 0:
        break
    numeros.append(numero)

# Sumar los números 
i = 0
suma = 0
while i < len(numeros):
    suma += numeros[i]
    i += 1

print(f"La suma de los números introducidos es: {suma}")

