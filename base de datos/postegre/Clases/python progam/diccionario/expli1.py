diccionario={"nombre": "carlos",
             "edad": 27,
             "curso": ["python",
                      "javascript",
                      "html"]

             }

print(diccionario["nombre"][0])

print(diccionario.get("nombre"))

print(len(diccionario))

#si la clave no existe, agrega el elemento 
diccionario[anyCurs]=2023
#si la clave existe, modifica el elemento 
diccionario["nombre"]="toni"

print("diccionario actiualizado:", diccionario)

#utilizar el metodo update()

diccionario.update({"anyCurs":2023})

diccionario.update({"nombre":"toni"})

#eliminar metodo pop

#si la clave no existe, eliminar el elemento permiten

diccionario.pop("anyCurs")

del diccionario["nombre"]

#

for k in diccionario:
    #opcion 1
    print(k)
    #opcion 2
    print(dicionario[k])
    #opcion 3
    for k in diccionario.keys()
    print(dicionario[k])
    #opciono 4
     for k in diccionario.values()
    print(v)

#copiar diccionario

diccionariocopiado.copy()
print(diccionariocopiado)

#copia con la funcion de contrucion dict()

diccionariocopiado=dict(diccioanrio)
print(diccionariocopiado)

#creacion de un diccionario vacio

diccionario=()
print(diccionario)

#creacion de un diccionario vacio con metodo dict()

diccionario=dict()
print(diccionario)

#diferencia entre listas y diccionario

#listas PERMITEN duplicados 
#diccionarios NO permiten duplicados 