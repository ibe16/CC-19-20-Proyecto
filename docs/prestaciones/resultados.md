# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.
 
 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 
 
---


## Evaluación de prestaciones

Prestaciones: stress_test.yml

Para la evaluación de las prestaciones de ambos microservicos se ha utlizado `Taurus`. El objetivo que se quiere conseguir es alcanzar las 1000 peteciones/s con 10 usuarios concurrentes. 

### Fichero YML
Para poder realizar test con Taurus lo primero que tenemos que realizar es un fichero YML que contendrá las pruebas de carga que vamos a realizar. El fichero utlizado será [stress_test.yml][enlace_stress_test].

Para realizar los test todos los microservicios y sus bases de datos se encuentran en contenedores Docker en local.

Como los test contienen varios escenarios, iremos explicando qué se ha hecho y los resultados sobre estos:

### Primer escenario: Microservicio Notifier
En un primer momento para este microservicio se diseño un test que incluía una secuencias de POST, GET, DELETE. Debido al tiempo que se tarda en hacer un POST y un DELETE el servicio no llegaba al mínimo de prestaciones. Da igual los cambios que se realizasen en el servidor o en la BD, estas prestaciones no mejoraban, en algunos casos incluso empeoraban. Por este motivo se diseño el siguiente test.

El test que se va a realizar sobre este microservicio es:
- Una petición POST que registra un nuevo email. Como tenemos 10 usuarios diferentes y todos realizarán la misma petción solo tendrá exito una de ellas. Las demás se comprobará que devuelvan un error 403.
- Peticiones GET consultando las listas en las que se encuentra el email anterior. Se comprobará que devuelva un código 200 o 404 (en caso de que no exista).

Primero se testeo el microservicio con la base de datos ya implementada y el servidor Gunicorn con 4 workers síncronos, los resultados obtenidos fueron los siguientes:

![n_test1](notifier_sync_w4.png)

Cómo podemos comprobar el microservicio cumple perfectamente las prestaciones que se le exigen. Aún así se han intentado mejorar.

Para la siguiente prueba que se realizó se configuró un poco más Gunicorn, en concreto se usarón workers asíncronos. Por defecto los que se usan son síncronos, pero también está la opción de utilizar los otros llamados `evenlet` y `gevent`. También se va a ajustar el número de workers al número óptimo para el procesador con esta fórmula:(2*CPU_CORES)+1. La máquina donde se está ejecutando el test dispone de 4 núcleos, por tanto se pueden tener 9 workers.

Los resultados fueron:
![n_test2](notifier_async_w9.png)

El uso de worker asíncronos puede haberse visto degradado por el número de workers usados, ya que el servidor no es el único proceso en la máquina. Se realizó otra prueba dejando el número de workers en 4.

Los resultados fueron:
![n_test3](notifier_async_w4.png)

En las dos pruebas se obtuvieron resultados similares, además, ocurre un error `java.net.SocketException`, que no tiene nada que ver con el código que se está ejecutando, por lo que el problema puede deberse a las limitaciones que ofrece la imagen del contenedor, ya que la realizar la misma prueba con el servicio desplegado local este error no sucede. 

Los resultados que se obtienen en local con 9 workers de tipo asíncrono son:
![n_test4](notifier_async_w9_local.png)

Podemos comprobar que se mejora tanto las peticiones por segundo como el ancho de banda, por lo que en local se desplegará de este modo. En Docker se quedará la configuración con workers síncronos.

### Segundo escenario: Microservico Monitor
Para este microservicio se diseño el siguiente test:
- 5 peticiones GET que a su vez hacen consultas al API de Github.
- 1 petición GET que devuelve los estados en los que se puede encontrar un servicio.

El primer test, al igual que con el microservicio anterior, se realizará con 4 workers de tipo síncrono en la imagen de Docker. Los resultados:
![m_test1](monitor_sync_w4_slim.png)

Como se puede ver los resultados son muy pobres, apenas se llega a las 25 peticiones por segundo. Esto no se debe a que el microservicio tenga un rendimiento pobre si no, que el API de Github no permite que hagamos tantas peticiones seguidas. Mockeando el resultado que debería devolvernos el API conseguimos lo siguiente:
![m_test2](monitor_mock.png)

Este resultado de por si ya es más que aceptable, pero se realizará una última prueba en local para testear los workers asíncronos:
![m_test3](monitor_w9_asyn_local.png)

### Tercer escenario: Resultado final con ambos microservicios levantados
Aquí se han medido las prestaciones con los dos servicios levantados. Las peticiones son las mismas que por separado, excepto, que en el mciroservicio Monitor, en vez de Mockear las peticiones al API de Github solo se harán una vez.

Los resultados para las imágenes de Docker son:
![test1](monitor-notifier.png)

Para los servicios en local:
![test2](monitor-notifier-local.png)


[enlace_stress_test]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/stress_test.yml
