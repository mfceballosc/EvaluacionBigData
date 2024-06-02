##
##  Gestion de datos con BASH
##  ===========================================================================
##
## descargar imagen ubuntu
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##
##  Cuantas tarjetas tienen el pin entre 980 y 990?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
contador_total=0
filtro="(980|981|982|983|984|985|986|987|988|989|990)"
for archivo in *.txt; do
    contador_archivo=$(grep -Eo ",\"$filtro\"," "$archivo" | wc -l)
  ((contador_total+=contador_archivo))
done
echo "$contador_total"