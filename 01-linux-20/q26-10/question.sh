##
##  Gestion de datos con BASH
##  ===========================================================================
##
## descargar imagen ubuntu
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##
##  Cuantas personas nacieron en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash

archivo="person"
trimestre="(01|02|03)"
contador=$(grep -Eo "\+([0-9]{4})\-$trimestre\-[0-9]{2}\+" "$archivo" | wc -l)
echo $contador