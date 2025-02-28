"""""
file = open('program/ficheros/pruebaxd.csv', 'r')
#print(file)
lineas = file.readlines()
print(lineas)
file.close()
"""""

with open('program/ficheros/pruebaxd.csv', 'r') as archivo:
    lineas = archivo.readlines()
    print(lineas)
    
for l in lineas:
    print(lineas)