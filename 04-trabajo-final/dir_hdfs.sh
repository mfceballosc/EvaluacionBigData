#!/bin/bash

# Configuración de HDFS y los directorios
WAREHOUSE_DIR="/user/warehouse"
BRONZE_DIR="$WAREHOUSE_DIR/bronze"
SILVER_DIR="$WAREHOUSE_DIR/silver"
GOLD_DIR="$WAREHOUSE_DIR/gold"

# Función para crear un directorio si no existe
create_directory_if_not_exists() {
  local dir=$1
  hdfs dfs -test -d "$dir"
  if [ $? -ne 0 ]; then
    echo "Creando directorio $dir..."
    hdfs dfs -mkdir -p "$dir"
  else
    echo "El directorio $dir ya existe."
  fi
}

# Comprobar y crear el directorio warehouse
create_directory_if_not_exists "$WAREHOUSE_DIR"

# Crear los subdirectorios bronze, silver y gold
create_directory_if_not_exists "$BRONZE_DIR"
create_directory_if_not_exists "$SILVER_DIR"
create_directory_if_not_exists "$GOLD_DIR"

echo "Se crearon los directorios correctamente"