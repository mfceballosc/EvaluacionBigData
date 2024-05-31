##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros quedan en el archivo 'person' si se eliminan los 
##  registros con 'city' = 'Albuquerque (New Mexico)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
registro='Albuquerque (New Mexico)'

grep -v "$registro" person | tail -n +2 | awk -F',' '{gsub(/"/, "", $1); print $1}' > temp

registros=$(wc -l < temp)
echo "$registros"
rm temp
