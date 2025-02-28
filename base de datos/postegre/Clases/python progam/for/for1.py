num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un segundo número: "))

min_num = min(num1, num2)
max_num = max(num1, num2)

lista = list(range(min_num, max_num + 1))

print(f"Hemos creado la lista {lista}")

for num in lista:
    if num % 2 == 0:
        print(f"El {num} es par")
    else:
        print(f"El {num} es impar")





