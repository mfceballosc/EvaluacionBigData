##
##  Gestion de datos con BASH
##  ===========================================================================
##
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##  Cuantos registros tiene el archivo 'data.csv'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
registros=$(wc -l < data.csv)
echo "$registros"

