suma = 0
contador = 0

num = int(input("escribe un numero: "))

while num != 0 :
    suma += num
    contador += 1
    num = int(input("escirbe otro numero: "))

if contador != 0 :
    media = suma / contador 
else:
    media = 0 

print(f"suma = {suma}")
print(f"mediana = {media}")
print("[fin del programa]")
    