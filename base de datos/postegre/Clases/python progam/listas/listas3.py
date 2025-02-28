# Inicialitzem la llista de notes amb alguns valors d'exemple
uf_notes = {"UF1": 5.53, "UF2": 7.53}

# Funció per mostrar totes les notes
def mostrar_notes():
    if uf_notes:
        for uf, nota in uf_notes.items():
            print(f"{uf} té una nota de {nota:.2f}")
    else:
        print("No hi ha cap nota enregistrada.")

# Funció per modificar una nota existent
def modificar_nota():
    if not uf_notes:
        print("No hi ha cap UF per modificar.")
        return
    # Mostrem les UFs disponibles per modificar
    print("De quina UF vols modificar la nota?")
    ufs = list(uf_notes.keys())
    for i, uf in enumerate(ufs, start=1):
        print(f"{i}. {uf}")
    
    # Escollim la UF i validem la selecció
    try:
        seleccion = int(input("Introdueix el número de la UF que vols modificar: ")) - 1
        if 0 <= seleccion < len(ufs):
            nova_nota = float(input("Introdueix la nova nota: "))
            uf_notes[ufs[seleccion]] = nova_nota
            print("Nota modificada correctament.")
        else:
            print("Selecció no vàlida.")
    except ValueError:
        print("Entrada no vàlida. Si us plau, introdueix un número.")

# Funció per esborrar una UF
def esborrar_uf():
    if not uf_notes:
        print("No hi ha cap UF per esborrar.")
        return
    # Mostrem les UFs disponibles per esborrar
    print("Quina UF vols esborrar?")
    ufs = list(uf_notes.keys())
    for i, uf in enumerate(ufs, start=1):
        print(f"{i}. {uf}")
    
    # Escollim la UF i validem la selecció
    try:
        seleccion = int(input("Introdueix el número de la UF que vols esborrar: ")) - 1
        if 0 <= seleccion < len(ufs):
            del uf_notes[ufs

