#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Error: Se requiere al menos un nombre de usuario."
    read -p "Introduce los nombres de usuario separados por espacio: " input
    set -- $input
    if [ $# -lt 1 ]; then
        echo "Error: No se proporcionaron nombres válidos."
        exit 1
    fi
fi

group1="grupo1"
group2="grupo2"

if ! getent group "$group1" >/dev/null; then
    sudo groupadd "$group1"
fi
if ! getent group "$group2" >/dev/null; then
    sudo groupadd "$group2"
fi

gestionar_usuarios() {
    local index=1
    for user in "$@"; do
        if id "$user" &>/dev/null; then
            echo "El usuario $user ya existe."
        else
            sudo useradd -m "$user"
            echo "Usuario $user creado."
        fi

        if (( index % 2 == 1 )); then
            sudo usermod -g "$group1" "$user"
            echo "Usuario $user añadido a grupo primario $group1."
        else
            sudo usermod -g "$group2" "$user"
            echo "Usuario $user añadido a grupo primario $group2."
        fi
        
        (( index++ ))
    done
}

gestionar_usuarios "$@"
