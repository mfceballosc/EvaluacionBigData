


[datos demograficos](https://www.medellin.gov.co/es/centro-documental/proyecciones-poblacion-viviendas-y-hogares/)



# Clase final

[Documentacion de spark](https://spark.apache.org/docs/latest/sql-data-sources-csv.html)
```cmd
docker run --rm -it \
    --name spark \
    -p 4040:4040 \
    -p 50070:50070 \
    -p 8088:8088 \
    -p 8888:8888 \
    -v "$PWD":/workspace \
    jdvelasq/spark:3.1.3
```

```cmd

docker run --rm -it --name spark -p 4040:4040 -p 50070:50070 -p 8088:8088 -p 8888:8888 -v "%cd%":/workspace jdvelasq/spark:3.1.3

```
