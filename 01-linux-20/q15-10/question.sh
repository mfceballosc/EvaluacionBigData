##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es la 'ciudad (estado)' en la posicion 3 del archivo 'person', si el 
##  archivo se organiza alfabeticamente por el campo 'ssn'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#!/bin/bash
city=$(sort -t',' -k1,1 person | awk -F',' 'NR==3 {print $3}')
echo "$city"