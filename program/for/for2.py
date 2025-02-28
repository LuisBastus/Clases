cantidad = int(input("¿Cuántos números quieres introducir? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

suma = sum(numeros)

print(f"La suma de los números introducidos es: {suma}")

