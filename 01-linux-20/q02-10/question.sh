##
##  Programación en Bash
##  ===========================================================================
##
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
for file in data*.csv; do
    i=1
    while read -r line; do
   # Dividir la línea en campos utilizando la coma como delimitador
        IFS='	' read -ra fields <<< "$line"
        col1="${fields[0]}"
        rest = "${fields[1]}"
        echo $rest
        IFS=',' read -ra restos <<< "$rest"
        # Iterar sobre los elementos restantes en la línea
        for ((j = 0; j < ${#restos[@]}; j++)); do
            letter="${restos[j]}"
            # Aquí puedes imprimir los campos según sea necesario
            # echo "$file,$i,$col1,$letter"
            echo "$file,$i,$col1,$letter"
        done
        ((i++))
    done < "$file"
done
##  >>> Fin del código <<<
##  ===========================================================================

