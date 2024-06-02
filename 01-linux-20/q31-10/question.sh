##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es la cantidad maxima de tarjetas que tiene un banco?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
maximo=0

for archivo in *.txt; do
    n_filas=$(($(wc -l < "$archivo") - 1))
    if ((n_filas > maximo)); then
        echo $archivo
        maximo=$n_filas
    fi
done
echo "$maximo"