# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.
 
 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 
 
---

## Docker
Para desplegar los servidores de los microservicios para poder hacer pruebas de carga se ha decidido utilizar contenedores de `Docker`. Para hacer esta tarea más sencilla de ha usado la herramienta `docker-compose` que permite indicar de manera sencilla las imágenes, argumentos, redes, variables de entorno, etc. necesarias para el despliegue. Concretamente se han utilizado 4 contenedores para:
1. El microservicio Notifier.
2. La base de datos MongoDB que usa el microservico anterior.
3. El microservicio Monitor.
4. La base de datos PostgreSQL que usa el microservico anterior.

### Microservicio Notifier
Contenedor: https://hub.docker.com/r/ibe16/notifier

Enlace al [Dockerfile.][dockerfile_notifier]
 
La imagen anterior se ha construido teniendo como base `python:3.6-slim-stretch`, una imagen del DockerHub oficial de `Python` que usa `Debian 9` como sistema operativo y contiene `python 3.6` instalado. Después se han instalado las dependencias necesarias para el funcionamiento del servicio, que son `Flask` y `Gunicorn`.
 
Se ha elegido la imagen `python:3.6-slim-stretch` siguiendo los siguientes criterios:
1. Proviene del repositorio oficial del lenguaje que se está usando.
2. Contiene la versión del lenguaje con la que se está desarrollando ya instalada.
3. Es la que mejor rendimiento ofrece en relación al espacio que ocupa. Se pueden ver en la [documentación][docu_bench] correspondiente los benchmark que se han realizado para hacer esta elección.
 
A continuación, se muestra el resto de imágenes que se barajaron:
```shell
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
python                     3.6-slim-stretch    fa79f489b3bf        7 days ago          151MB
python                     3.6-slim-buster     add6920a081f        7 days ago          174MB
python                     latest              0a3a95c81a2b        7 days ago          932MB
python                     3.6-alpine          8880aaf979d2        2 weeks ago         94.7MB
```
Podemos comprobar como la versión con `Alpine`es la más ligera. La versión `stretch` está basada en Debian 9. La versión `buster` también está basada en Debian. Con la palabra `slim` quiere decir que es una versión reducida de estos sistemas.


### Microservico Monitor
Contenedor: https://hub.docker.com/r/ibe16/monitor

Enlace al [Dockerfile.][dockerfile_monitor]

La imagen de este microservicio se ha construido a partir de la imagen `python.3.6-slim` porque es la única donde se ha podido instalar una dependencia necesaria para poder usar el paquete
de `Python` que conecta con la base de datos. Se ha probado con todas las imágenes propuestas para el microservicio anterior, ya que estás eran las más rápidas que se encontrarón, sin embargo no permitían la instalación de dicho paquete. 
 
### Uso 
> Para poder usar el `docker-compose` es necesario instalarlo previamente. Se puede realizar fácilmente siguiendo su [documentación][offi_docu_docker]. También es conveniente configurarlo para usarlo sin la necesidad de hacer `sudo`.
 
1. Para construir la imagen a partir del `docker-compose` ejecutamos:
   ```shell
   $ docker-compose build 
   ```
   > Contruye las imágenes necesarias en el directorio actual y construye la red para que se puedan comunicar. 
   > Por defecto la <etiqueta> que se coloca en los microservicios es `latest`.
 
2. Para descargar la imagen desde DockerHub:
   ```shell
   $ docker pull ibe16/notifier:latest
   ```

   ```shell
   $ docker pull ibe16/monitor:latest
   ```
 
3. Para ejecutar la imagen en local:
   ```shell
   $ docker-compose up
   ```

4. Para parar todo:
   ```shell
   $ docker-compose down
   ```
   > Para ver que el contenedor se ejecuta correctamente se puede consultar la url `http://0.0.0:<puerto_externo>/hello` que devolverá un 'Hello, World!'.
 
Para más información se puede consultar el [docker-compose][enlace_dockercompose].
 
> El repositorio de `DockerHub` se ha configurado para que se actualice la imagen cada vez que se haga un `push` al repositorio de `Github`. Para más información se puede consultar la [documentación][docu_docker_gh] donde explica cómo realizarlo.


[dockerfile_monitor]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/Dockerfile

[dockerfile_notifier]: https://github.com/ibe16/CC-19-20-Proyecto/blob/master/notifier/Dockerfile

[docu_docker_gh]:https://ibe16.github.io/CC-19-20-Proyecto/docs/arquitectura/despliegue_git

[enlace_dockercompose]: https://github.com/ibe16/CC-19-20-Proyecto/blob/master/docker-compose.yml

[offi_docu_docker]:https://docs.docker.com/compose/install/