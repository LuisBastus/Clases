#!/bin/bash

echo "Aquest script munta particions permaments"
echo "Només es necessita el disc, la partició, una etiqueta i una ruta de muntatge"


# lectura de variables
read -p "Disc (valors en el rang [a-z]): " disc
read -p "Partició (valors en el rang [1-10]): " part
read -p "Etiqueta (lletres minúscules, màxim 20 caracters): " etiq
read -p "Punt de muntatge (directori existent, ruta absoluta): " dir

# construcció del nom de la partició
particio="/dev/sd"$disc$part
echo "Amb els valors introduïts es muntarà la partició $particio amb l'etiqueta $etiq"

# assignació de l'etiqueta a la partició
e2label $particio $etiq
echo "Etiqueta creada $(e2label $particio)"

# construcció de la línia que munta la partició
liniaFSTAB="LABEL=$etiq	$dir	ext4	defaults	0	0"
echo "Línia FSTAB $liniaFSTAB"

# addició  de la línia que munta la partició a l'arxiu fstab
echo $liniaFSTAB >> /etc/fstab
tail -1 /etc/fstab

# relectura de l'arxiu /etc/fstab
mount -a

# misssatge final
echo "Partició $particio muntada amb l'etiqueta $etiq"
lsblk -f | grep $particio

# log amb data creació
Log="Muntatge_$(date)";
Log="Muntatge_$(date | tr ' ' '_')";
echo "Partició $particio muntada amb l'etiqueta $etiq a data $(date)" > "$dir/$Log"
ls $dir


