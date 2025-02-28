def menu():
    print("\n1. Añadir elemento")
    print("2. Sustituir elemento")
    print("3. Buscar elemento")
    print("4. Eliminar elemento")
    print("5. Eliminar repetidos")
    print("6. Mostrar la lista")
    print("7. Salir")

def añadir_elemento(lista):
    elemento = input("Introduce el elemento a añadir: ")
    lista.append(elemento)
    print(f"¡Elemento '{elemento}' añadido correctamente!")

def sustituir_elemento(lista):
    elemento_a_sustituir = input("Introduce el elemento a sustituir: ")
    nuevo_elemento = input("Introduce el nuevo elemento: ")
    
    # Búsqueda manual sin usar index()
    for i in range(len(lista)):
        if lista[i] == elemento_a_sustituir:
            lista[i] = nuevo_elemento
            print("¡Elemento sustituido correctamente!")
            return
    
    print("¡Elemento no encontrado!")

def buscar_elemento(lista):
    elemento_a_buscar = input("Introduce el elemento a buscar: ")
    apariciones = 0
    
    # Búsqueda manual sin usar count()
    for elemento in lista:
        if elemento == elemento_a_buscar:
            apariciones += 1

    if apariciones > 0:
        print(f"El elemento '{elemento_a_buscar}' aparece {apariciones} veces en la lista.")
    else:
        print("¡Elemento no encontrado!")

def eliminar_elemento(lista):
    elemento_a_eliminar = input("Introduce el elemento a eliminar: ")

    # Elimina la primera aparición manualmente
    for i in range(len(lista)):
        if lista[i] == elemento_a_eliminar:
            del lista[i]
            print(f"¡Elemento '{elemento_a_eliminar}' eliminado correctamente!")
            return
    
    print("¡Elemento no encontrado!")

def eliminar_repetidos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:  # Corregido aquí
            elementos_unicos.append(elemento)
    
    lista.clear()
    lista.extend(elementos_unicos)
    print("Repetidos eliminados, dejando solo la primera aparición de cada uno.")

def mostrar_lista(lista):
    if lista:
        print("Lista de la compra:")
        for i, elemento in enumerate(lista, 1):
            print(f"{i}. {elemento}")
    else:
        print("¡La lista está vacía!")

def main():
    lista_compra = []
    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            añadir_elemento(lista_compra)
        elif opcion == '2':
            sustituir_elemento(lista_compra)
        elif opcion == '3':
            buscar_elemento(lista_compra)
        elif opcion == '4':
            eliminar_elemento(lista_compra)
        elif opcion == '5':
            eliminar_repetidos(lista_compra)
        elif opcion == '6':
            mostrar_lista(lista_compra)
        elif opcion == '7':
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida, por favor elige otra opción.")

if __name__ == "__main__":
    main()
