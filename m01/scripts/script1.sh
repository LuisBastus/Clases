#!/bin/bash
crear_directorios() {
    ruta_base=$1

    nombres_directorios=("$@")
    
    if [ ! -d "$ruta_base" ]; 
        mkdir -p "$ruta_base"
    fi

    for nombre in "${nombres_directorios[@]}"; do
        ruta_completa="$ruta_base/$nombre"
        mkdir -p "$ruta_completa"  echo "Directorio ceado: $ruta_completa"
    done
}

ruta_base="mis_directorios"
nombres_directorios=("dir1" "dir2" "dir3" "subdir/dir4")
crear_directorios "$ruta_base" "${nombres_directorios[@]}"
