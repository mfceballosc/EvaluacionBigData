##
##  Gestion de datos con BASH
##  ===========================================================================
##
## descargar imagen ubuntu
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##
##  Cuantas personas tienen 'AA' como iniciales de su nombre?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash

archivo="person"
patron="\"[Aa][A-Za-z]* [Aa][A-Za-z]*\""
contador=$(grep -E "$patron" "$archivo" | wc -l)
echo $contador

