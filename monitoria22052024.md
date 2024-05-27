# Monitoria 22-05-2024

Descargar imagen de hadoop con el siguiente comando:

Al terminar el ejercicio debemos subirlo a drive ya solucionado

```cmd
docker run --rm -it --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 -v "%cd%":/workspace jdvelasq/hadoop:2.10.1
```
Una vez dentro de la imagen ejecuto 

```cmd
rem verifico mi ubicación
pwd
ls -la

rem voy a la carpeta, accedemos a la carpeta de hola mundo

cd 00-hola_mundo-10\q01-10

rem edito el python y ejecuto
python question.py

```
## Nota con respecto al trabajo final

```cmd
rem con sockets podemos generar los datos emulando una maquina


rem generar datos sinteticos

rem spark - info en un HDFS almacenamiento Zona de datos raw

rem Tienen una pregunta de negocio. Para dar respuesta: ETL - Transformar datos SQL - Hive, (flujo imagen 1)

rem Aún no se ha definido el tamaño de los datos a generar

rem para presentar se puede usar Power BI

rem **************************************************
rem importante hacer la prueba del socket
rem **************************************************



```

![imagen 1](/imgs/img1.png)



