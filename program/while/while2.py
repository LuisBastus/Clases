num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1

lista = list(range(num1, num2 + 1))
print(f"Hemos creado la lista {lista}")

i = 0
while i < len(lista):
    numero = lista[i]
    if numero % 2 == 0:
        print(f"El {numero} es par")
    else:
        print(f"El {numero} es impar")
    i += 1
