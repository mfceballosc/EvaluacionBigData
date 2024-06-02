##
##  Gestion de datos con BASH
##  ===========================================================================
##
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##
##  Cuantas tarjetas se vencen en el trimestre Q2 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
salida="temp"

> "$salida"

contador_total=0
trimestre="(Apr|May|Jun)"

for archivo in *.txt; do
  contador_archivo=$(grep -cE ",\"$trimestre/[0-9]{2,4}\"," "$archivo")

  if [ "$contador_archivo" -gt 0 ]; then
    grep -E ",\"$trimestre/[0-9]{2,4}\"," "$archivo" >> "$salida"
  fi
  ((contador_total+=contador_archivo))
done

echo "$contador_total"

rm "$salida"