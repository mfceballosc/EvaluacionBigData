## Informacion para solucionar taller

[enlace del tema](https://jdvelasq.github.io/curso_big_data/apache_hadoop/__index__.html)


```bash
docker run --rm -it --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 -v "$PWD":/workspace jdvelasq/hadoop:2.10.1
```

```bash
# para windows
docker run --rm -it --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 -v "%cd%" :/workspace jdvelasq/hadoop:2.10.1

# Otro comando funcional es:
docker run --rm -it --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 -v "%cd%:/workspace" jdvelasq/hadoop:2.10.1

# activar entorno ya creado
docker start -ai bf865c57b37c21612d648f47cd2ab840e54fed1699b852b9c86a85eafad36909


```

```cmd
rem copiar el archivo de local a hadoop
docker cp 02-hadoop-20/q01-10/credit.csv hadoop:workspace/credit.csv  
```

credit_history  1
critical        293       
delayed 88
fully repaid    40        
fully repaid this bank  49
repaid  530

credit_history	1
critical	293
delayed	88
fully repaid	40
fully repaid this bank	49
repaid	530