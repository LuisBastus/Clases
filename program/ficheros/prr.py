#!/usr/bin/env python3

import datetime
import json

tasks = [
    {
        "title": "Exemple 1",
        "date": datetime.datetime.now(),
        "done": False
    }, 
    {
        "title": "Exemple 2",
        "date": datetime.datetime.now(),
        "done": True
    }
]

sep = "\n------------"

opcio = None
final = 6

def save_tasks_to_file():
    try:
        with open("tasks.json", "w") as file:
            json.dump([{
                "title": task["title"],
                "date": task["date"].strftime("%Y-%m-%d %H:%M:%S"),
                "done": task["done"]
            } for task in tasks], file)
        print("Dades desades correctament.")
    except Exception as e:
        print(f"Error en desar les dades: {e}")

while opcio != final:

    print("\n1. Veure tasques")
    print("2. Crear tasca")
    print("3. Modificar tasca")
    print("4. Eliminar tasca")
    print("5. Desar i sortir")
    print("6. Sortir")

    try:
        opcio = int(input("\nIntrodueix una opció: "))
    except ValueError:
        print("Opció no vàlida. Introdueix un número enter.")
        continue
    
    if opcio == 1:
        print("Has escollit l'opció 1")
        
        x = {
            "Fetes": [],
            "No fetes": []
        }
        for task in tasks:
            if task["done"]:
                x["Fetes"].append(task)
            else: 
                x["No fetes"].append(task)

        for key, lista in x.items():
            print(f"{sep}\n{key} ({len(lista)}){sep}")
            for index, task in enumerate(lista):
                title = task['title']
                date = task['date'].strftime("%d/%m/%y %H:%M")
                print(f"Tasca {index+1}. {title} - {date}")

    elif opcio == 2:
        print("Has escollit l'opció 2")
        title = input("Introdueix el títol de la tasca: ")
        tasks.append({
            "title": title,
            "date": datetime.datetime.now(),
            "done": False
        })
        print("Tasca creada.")

    elif opcio == 3:
        print("Has escollit l'opció 3")
        for index, task in enumerate(tasks):
            title = task['title']
            date = task['date'].strftime("%d/%m/%y %H:%M")
            print(f"Tasca {index+1}. {title} - {date} - {'Feta' if task['done'] else 'No feta'}")
        try:
            task_num = int(input("Introdueix el número de la tasca a modificar: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1]["done"] = not tasks[task_num-1]["done"]
                print("Tasca modificada.")
            else:
                print("Número de tasca no vàlid.")
        except ValueError:
            print("Número de tasca no vàlid.")

    elif opcio == 4:
        print("Has escollit l'opció 4")
        for index, task in enumerate(tasks):
            title = task['title']
            date = task['date'].strftime("%d/%m/%y %H:%M")
            print(f"Tasca {index+1}. {title} - {date} - {'Feta' if task['done'] else 'No feta'}")
        try:
            task_num = int(input("Introdueix el número de la tasca a eliminar: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num-1)
                print("Tasca eliminada.")
            else:
                print("Número de tasca no vàlid.")
        except ValueError:
            print("Número de tasca no vàlid.")

    elif opcio == 5:
        save_tasks_to_file()
        break

    elif opcio == final:
        print("Fins aviat!")

    else:
        print("Opció incorrecta.")
