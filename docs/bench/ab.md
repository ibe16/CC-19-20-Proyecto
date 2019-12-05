# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Resultados del benchmark
Se han analizado tres imágenes oficiales de `Python` con distintas características. Estas son las siguientes:
- **python:3.6-alpine**
- **python:3.6-slim-stretch**
- **python:3.6-slim-buster**

Lo que ha primado a la hora de elegirlas, a parte de que son imágenes oficiales que incluyen la versión del lenguaje con la que se está desarrollando, es el espacio que ocupan. Se ha procurado escoger aquellas imágenes que ocupen menos espacio, para que el tiempo de descarga sea el mínimo posible.

```shell
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
python                     3.6-slim-stretch    fa79f489b3bf        7 days ago          151MB
python                     3.6-slim-buster     add6920a081f        7 days ago          174MB
python                     latest              0a3a95c81a2b        7 days ago          932MB
python                     3.6-alpine          8880aaf979d2        2 weeks ago         94.7MB
```

Si nos rigiesemos solo por esta característca la imagen elegiriamos la imagen de `alpine`. 

A continuación se hará un test de rendimiento y se analizarán los resultados. Para ello se usará `Apache Bench`. La orden que vamos a usar para analizar la imágenes es la siguiente:

```shell
$ ab -n 10000 -c 1000 <url>
```

Los argumentos indican lo siguiente:
- -n 10000: Se harán 10000 peticiones 
- -c 1000: Habrá como máximo 1000 peticiones de manera concurrente

### Bench para `alpine`

```shell
Concurrency Level:      1000
Time taken for tests:   8.372 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1730000 bytes
HTML transferred:       130000 bytes
Requests per second:    1194.47 [#/sec] (mean)
Time per request:       837.188 [ms] (mean)
Time per request:       0.837 [ms] (mean, across all concurrent requests)
Transfer rate:          201.80 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   95 297.1      0    1050
Processing:     5  228 636.9     35    7323
Waiting:        4  228 636.9     34    7323
Total:         26  323 844.2     35    8345

```

El resultado es el siguiente:
- En total se ha tardado 8.372 segundos en completar el test
- La petición más rápida se ha completado en 26 ms
- La peticióm más lenta se ha completado en 8345 ms

### Bench para `slim-stretch`

```shell
Concurrency Level:      1000
Time taken for tests:   4.727 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1730000 bytes
HTML transferred:       130000 bytes
Requests per second:    2115.64 [#/sec] (mean)
Time per request:       472.669 [ms] (mean)
Time per request:       0.473 [ms] (mean, across all concurrent requests)
Transfer rate:          357.43 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0  103 307.9      0    1046
Processing:    16  259 755.6     35    3683
Waiting:       16  259 755.6     35    3683
Total:         19  362 986.6     35    4720

```
El resultado es el siguiente:
- En total se ha tardado 7.727 segundos en completar el test
- La petición más rápida se ha completado en 19 ms
- La peticióm más lenta se ha completado en 4720 ms

### Becnh para `slim-buster`

```shell
Concurrency Level:      1000
Time taken for tests:   8.473 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1730000 bytes
HTML transferred:       130000 bytes
Requests per second:    1180.22 [#/sec] (mean)
Time per request:       847.296 [ms] (mean)
Time per request:       0.847 [ms] (mean, across all concurrent requests)
Transfer rate:          199.39 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    3   9.5      0      44
Processing:     9  342 986.6     35    7664
Waiting:        9  342 986.6     35    7663
Total:         15  345 994.0     35    7701

```

El resultado es el siguiente:
- En total se ha tardado 8.473 segundos en completar el test
- La petición más rápida se ha completado en 15 ms
- La peticióm más lenta se ha completado en 7701 ms

### Conclusiones
La imagen que ofrece mejor compromiso entre rendimiento y espacio es la `sim-strech` y por tanto será la que se usé. Es la más rápida procesadon peticiones y solo ocupa 151MB.