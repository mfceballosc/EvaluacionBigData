##
##  Gestion de datos con BASH
##  ===========================================================================
##
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##  Cual es el valor del campo 'quota' del archivo 'data.csv' para el 
##  ultimo registro?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
file="data.csv"
columna=5
dato=$(awk -F',' -v col="$columna" 'END {print $col}' "$file")
echo "$dato"