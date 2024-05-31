##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'key' del archivo 'data.csv' para el 
##  registro 3?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
file="data.csv"
columna=3

dato=$(awk -F',' -v col="$columna" '{if (NR==4) print $col}' "$file")

echo "$dato"