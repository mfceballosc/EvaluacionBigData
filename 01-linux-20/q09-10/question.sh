##
##  Gestion de datos con BASH
##  ===========================================================================
##
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##  Cual es el valor del campo 'ccn' del archivo 'data.csv' para el 
##  registro 10?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
file="data.csv"
columna=1
dato=$(awk -F',' -v col="$columna" '{if (NR==11)  print $col}' "$file")
echo "$dato"
