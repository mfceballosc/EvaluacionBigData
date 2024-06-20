#!/bin/bash

# Archivo que se pasa como argumento al script (nuevo archivo detectado)
archivo_local="$1"

# Ruta en HDFS donde quieres copiar los archivos
ruta_hdfs="/ruta/en/hdfs/"

# Verificar si el archivo ya existe en HDFS
hdfs dfs -test -e "${ruta_hdfs}${archivo_local}"

# $? contiene el código de retorno del comando anterior (0 si existe, 1 si no existe)
if [ $? -ne 0 ]; then
    # Copiar el archivo local a HDFS
    hdfs dfs -put "${archivo_local}" "${ruta_hdfs}"
    echo "Archivo '$archivo_local' copiado a HDFS."
else
    echo "El archivo '$archivo_local' ya existe en HDFS, no se ha copiado."
fi


#!/bin/bash

# Ruta a la carpeta local que quieres monitorear
carpeta_local="/ruta/a/la/carpeta_local"

# Comando inotifywait para monitorear la carpeta local y ejecutar un script cuando hay cambios
inotifywait -m -e create --format '%w%f' "$carpeta_local" | while read archivo_nuevo
do
    # Llamar a tu script para copiar el archivo a HDFS
    bash /ruta/al/tu_script_copiar_a_hdfs.sh "$archivo_nuevo"

    from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

Spark

# Crear una instancia de SparkSession
spark = SparkSession.builder \
                    .appName("Streaming Copia a HDFS") \
                    .getOrCreate()

# Configurar la carpeta local a monitorear
carpeta_local = "/ruta/a/la/carpeta_local"

# Definir la ruta en HDFS donde quieres copiar los archivos
ruta_hdfs = "hdfs:///ruta/en/hdfs/"

# Definir la estructura del DataFrame para los datos de streaming
schema = "archivo STRING"

# Definir el DataFrame de streaming para monitorear la carpeta local
df_streaming = spark.readStream \
                    .format("csv") \
                    .option("header", "false") \
                    .schema(schema) \
                    .csv(carpeta_local)

# Función para copiar archivos a HDFS
def copiar_a_hdfs(df, epoch_id):
    # Filtrar archivos que aún no han sido copiados a HDFS
    archivos_nuevos = df.select("archivo") \
                        .filter(~col("archivo").contains("part-"))  # Filtrar archivos temporales de Spark

    # Copiar archivos nuevos a HDFS
    archivos_nuevos.write.mode("append").csv(ruta_hdfs)

# Configurar el procesamiento continuo y la acción de copia
streaming_query = df_streaming.writeStream \
                              .foreachBatch(copiar_a_hdfs) \
                              .trigger(processingTime='10 seconds') \
                              .start()

# Esperar hasta que se detenga el streaming
streaming_query.awaitTermination()
