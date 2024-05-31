##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2596-5551-1068?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
id='3608-2596-5551-1068'
result=$(grep -i $id bank.csv | awk -F',' '{print $2}')
fullname=$(grep -i $result person | awk -F',' '{gsub(/"/, "", $5); print $5}')
echo "$fullname"