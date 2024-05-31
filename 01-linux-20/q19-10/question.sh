##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2968-5750-1980?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash

id='3608-2968-5750-1980'
result=$(grep -i $id bank.csv | awk -F',' '{print $2}')
fullname=$(grep -i $result person | awk -F',' '{gsub(/"/, "", $5); print $5}')
echo "$fullname"

