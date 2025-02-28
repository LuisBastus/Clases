#!/bin/bash
bash script1.sh
continuar = True 
 v
while continuar; do
    echo "MENÚ PRINCIPAL:"    
    echo "1) Crear conjunto de directorios"   
    echo "2) Comprobar exixtencia y mostrar detalles"
    echo "3) Cambiar"
    echo "0) Salir"
    read -p "Seleccione una opción: " opcion
    #bash script1.sh
    
    case $opcion in
    
        0) echo "Saliendo"
            continuar = False
            ;;
        1)
            
            directorios
            echo "En proceso"
            ;;
    esac
        *) read -p "Presione Enter para continuar..."
        
done

