##
##  Gestion de datos con BASH
##  ===========================================================================
##
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##  Cuantos registros hay en el archivo 'person' para city = 'Los Angeles (California)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash

contador=$(grep -c 'Los Angeles (California)' person)
echo "$contador"
