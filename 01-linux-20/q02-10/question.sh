##
##  Programación en Bash
##  ===========================================================================
##
## descargar imagen ubuntu
## docker run --rm -it --name ubuntu -v "%cd%":/workspace jdvelasq/ubuntu:20.04
## ejecutar una imagen ya descargada
## docker exec -it ubuntu bash
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
## 
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original. 
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##   
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
##
##  ===========================================================================
#!/bin/bash
# echo "***************************************************************"
# echo "***************************************************************"
for file in data*.csv; do
    i=1
    n_fila=1
    while read -r line || [[ -n $line ]]; do
   # Dividir la línea en campos utilizando la coma como delimitador
   if [[ -n "$line" ]]; then
        if [[ "$line" =~ ^([^[:space:]]+)[[:space:]]+(.+)$ ]]; then
            col1="${BASH_REMATCH[1]}"
            rest="${BASH_REMATCH[2]}"
        fi
        IFS=',' read -ra arreglo <<< "$rest"
        for field in "${arreglo[@]}"; do
            echo "$file,$n_fila,$col1,$field"
        done
        n_fila=$((n_fila + 1))
    fi
    done < "$file"
done
##  >>> Fin del código <<<
##  ===========================================================================

