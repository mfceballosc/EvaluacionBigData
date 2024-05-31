##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'ccn' del archivo 'data.csv' para el primer 
##  registro?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
file="data.csv"
columna=1

dato=$(awk -F',' -v col="$columna" '{if (NR==2) print $col}' "$file")

echo "$dato"