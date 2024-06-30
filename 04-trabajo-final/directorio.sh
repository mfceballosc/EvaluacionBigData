#!bin/bash

# Crear warehouse
DIRECTORIO="warehouse/raw"

if [ -d "$DIRECTORIO" ]; then
    echo "El directorio ya existe "$DIRECTORIO""
else
 mkdir -p "$DIRECTORIO"
 echo "Se ha creado el directorio "$DIRECTORIO""
 fi

 # Entrar a la zona donde se almacenan los datos y traerlos a raw
#  ORIGEN="base.data"
#  DESTINO="warehouse/raw"
#  NOMBRE_BD="03042024.parquet"

#  if [ -f "$ORIGEN/$NOMBRE_BD" ]; then
#     echo "La base de datos '$NOMBRE_BD' existe en '$ORIGEN'"
#     echo "Copiando la base de datos a '$DESTINO'..."

#     cp "$ORIGEN/$NOMBRE_BD" "$DESTINO"

#     if [ -f "$DESTINO/$NOMBRE_BD" ]; then
#         echo "La base de datos se ha copiado exitosamente a '$DESTINO'"
#     else
#         echo "Error: No se pudo copiar la base de datos a '$DESTINO'"
#     fi
# else
#     echo "Error: La base de datos '$NOMBRE_BD' no existe en '$ORIGEN'"
# fi
        

