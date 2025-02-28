#!/usr/bin/env python3

import datetime

tasks = [
    {
        "title": "Ejemplo 1",
        "date": datetime.datetime.now(),
        "done": False
    }, 
    {
        "title": "Ejemplo 2",
        "date": datetime.datetime.now(),
        "done": True
    }
]

sep = "\n------------"

opcion = None
final = 6

while opcion != final:

    print("\n1. Ver tareas")
    print("2. Crear tarea")
    print("3. Modificar tarea")
    print("4. Eliminar tarea")
    print("5. Guardar y salir")
    print("6. Salir")

    opcion = int(input("\nIntroduce una opción: "))
    
    if opcion == 1:
        #######################################################
        # Mostrar dos listas de tareas (hechas y no hechas) 
        #######################################################
        x = {
            "Hechas": [],
            "No hechas": []
        }
        for index, task in enumerate(tasks):
            if (task["done"]):
                x["Hechas"].append(task)
            else: 
                x["No hechas"].append(task)

        for key, list in x.items():
            print(f"{sep}\n{key} ({len(list)}){sep}")
            for index, task in enumerate(list):
                title = task['title']
                date = task['date'].strftime("%d/%m/%y %H:%M")
                print(f"Tarea {index+1}. {title} - {date}")
                
    

    elif opcion == 2:
        print("Has escogifo la opcion 2")
        tarea = input("Escribe la tarea que deseas guardar: ")
        fecha = datetime.datetime.now()(input("Escribe la fecha de la tarea: "))
        
        tasks[title] = [date,done]
        
        
 
    elif opcion == 3:
        #######################################################
        # Marcar una tarea como hecha o no hecha
        #######################################################
        print("Implementa esto")
 
    elif opcion == 4:
        #######################################################
        # Eliminar una tarea de la lista
        #######################################################
        print("Implementa esto")
 
    elif opcion == 5:
        #######################################################
        # Guardar datos actuales en un archivo
        #######################################################
        print("Implementa esto")
 
    elif opcion == final:
        #######################################################
        # Cerrar el programa
        #######################################################
        print("¡Hasta pronto!")

    else:
        print("Opción incorrecta.")
