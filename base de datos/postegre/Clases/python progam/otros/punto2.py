#!/usr/bin/env python3

# algoritmo contador 

FIN= '#'
# contadores

cons = 0
voc = 0

#introduce vocales y consonantes 

x = input("escribe un caracter:")

# bucle
while x != FIN:
    if x== "a" or x== "e" or x=="i" or x=="o" or x=="u":
        voc += 1
    elif x =='?':
         total= voc + cons  
         print(f'el recuento es: {total}')
    elif x=='*':
         voc = 0
         cons = 0
         print(f'el programa se ha reiniciado')
    elif x == '$':
        if voc < cons: 
         print(f'hay mas vocales que constantes')
        elif voc > cons:  
         print(f'hay mas vocales')
        elif voc == cons:
         print(f'hay empate entre consonantes y vocales')

    else :
        cons += 1
        print("atencion constante")

  #solicitar caracter
    x = input("escribe un caracter: ")

#calcula el total 

total= cons + voc

#mostrar el resultado 
print(f'el total de caracteres introducidos es {total}')
print(f"tens {voc} vocals i {cons} consonat")
