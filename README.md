# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Descripción del proyecto
Con este proyecto se quiere monitorizar los downtimes de las líneas de una fábrica. Consta de 2 entidades:
- **PlantMonitoring:** Se encarga de leer los datos de las líneas y almacenarlos en una base de datos. Los datos que se almacenan son el instante en el que se produce un downtime y la duración de este.
- **Notifier:** Su función es notificar a una lista de contactos que se ha producido un downtime y volver a avisar cuando se restablezca la línea.

## Arquitectura
Como arquitectura se ha eligido una arquitectura basada en microservicios, donde cada microservicio corresponde con las entidades descritas.

Más información sobre la [arquitectura][arquitectura] del todo el sistema.

### Arquitectura por capas
Se basa en separar la funcionalidad de un servicio en varias capas, para permitir que este sea más fácil de mantener, cambiar y escalar. Las principales capas en las que se fragmentan los servicios son:
1. Capa de presentación, corresponden a las interfaces de usuario.
2. Capa con la lógica del negocio, que contiene los procesos que se ejecutan.
3. La capa de datos, que gestiona la persistencia de estos.

### Capas del microservicio Notifier
Este microservicio se ha implementado siguiendo también una arquitectura de capas, al estilo de lo anteriormente explicado.
1. La capa que contiene el API REST, que configura las rutas con las que se atienden las peticiones.
2. Una capa con la lógica de negocio que maneja los modelos y controla los procesos que se tiene que seguir.
3. Una capa con los modelos de datos que se usan.

A continuación se muestra un esquema de las capas descritas:
![service_layers][layer_scheme]


## Lenguajes y tecnologías usadas
El proyecto se desarrolla usando Python más:
- Flask para la interfaz REST
- Celery para gestionar los eventos
- MySQL y MongoDB como bases de datos
- Consul para la configuración distribuida

Más información sobre [lenguajes y tecnologías usadas][tecnologías].

## Prerrequisitos
Las versiones de Python compatibles con el proyecto son:
    Linux:
        -Mínima: 3.4
        -Máxima: 3.8 y su versión de desarrollo

Para poder usar la herramienta de construcción es necesario:
1. Instalarla con:

    ```
    pip install invoke
    ```

2. Instalar las dependencias
    ```
    pip install -r requirements.txt
    ```

En cualquiera de los dos casos quedará disponible

## Herramienta de construcción
buildtool: tasks.py

La herramienta de construcción usada es ```Invoke```.

Para poder usar la herramienta de construcción es necesario:
1. Instalarla con:

    ```shell
    $ pip install invoke
    ```

2. Instalar las dependencias
    ```shell
    $ pip install -r requirements.txt
    ```

En cualquiera de los dos casos quedará disponible.

Se han configurado cuatro tareas. Estas son:
1. Instalar las dependencias necesarias
    ```shell
    $ invoke install
    ```
    > Instala todas la dependencias necesarias para el proyecto. Si previamente se ha ejecutado ```pip install -r requirements.txt``` no es necasio ejecutar esta tarea.

    > Se pueden consutar las dependencias usadas en el archivo [requirements.txt][enlace_dependencias]

2. Ejecutar los test unitarios 
    ```shell
    $ invoke test
    ```
    > Ejecuta todos los test unitarios. Para ello se ha usado el framework ```Pytest```.

3. Ejecutar los test de cobertura
    ```shell
    $ invoke coverage
    ```
    > Ejecuta los test de cobertura y almacena los resultados en un archivo ```.coverage```. Para la ejecución de estos test se ha usado un el módulo ```pytest-cov``` que proporciona ```Pytest```.
4. Limpiar los archivos generados por los test
    ```shell
    $ invoke clean
    ```
    >Incluido el archivo ```.coverage```.

5. Levantar el microservicio
    ```shell
    $ invoke start <ip> <puerto>
    ```
    > Levanta el microservicio usando [Gunicorn][offi_docu_gunicorn], un servidor WSGI HTTP para `Python`. Si no se indica la ip y el puerto donde se quiere enlazar el servicio por defecto se establecerá `0.0.0.0:5000`
    > Para comprobar que se ha levantado adecuadamente se puede consultar `http:\\<ip>:<puerto>\hello`. Esto devolverá un `Hello, World!`

6. Parar el microservicio
    ```shell
    $ invoke stop
    ```
    > Mata el proceso donde se ejecutaba el microservicio.

En el momento de la ejecución se pueden listar las tareas disponibles usanso ```invoke --list```.

Para más información sobre los comandos que se ejecutan y su opciones de configuración consulte el fichero [tasks.py][enlace_tasks].

## Integración continua
Como herramienta de intregración continua se ha usado `TravisCI` y `Github Actions`. Para más información sobre que se realiza con ambas herramientas puede ir a la [documentación correspodiente][docu_integracion]. También puede consultar los archivos de configuración de [TravisCI][enlace_Travis] y el [workflow de Github Actions][enlace_workflow].

## Docker
Contenedor: https://hub.docker.com/repository/docker/ibe16/notifier

La imagen anterior se ha construido teniendo como base `python:3.6-alpine`, una imagen del DockerHub oficial de `Python` que usa `alpine` como sistema operativo y contiene `python 3.6` instalado. Después se han instalado las dependencias necesarias para el funcionamiento del servicio, que son `Flask` y `Gunicorn`.

Se ha elegido la imagen `python:3.6-alpine` siguiendo los siguientes criterios:
1. Proviene del repositorio oficial del lenguaje que se está usando.
2. Contiene la versión del lenguaje con la que se está desarrollando ya instalada.
3. Es la que menos espacio ocupa de todas las posibilidades que se barajaron. La imagen usa `Alpine` que se caracteriza por ser ligero y eficiente.

A continuación, se muestra el resto de imagenes que se barajaron:
```shell
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
python                     3.6-slim-stretch    fa79f489b3bf        7 days ago          151MB
python                     3.6-slim-buster     add6920a081f        7 days ago          174MB
python                     latest              0a3a95c81a2b        7 days ago          932MB
python                     3.6-alpine          8880aaf979d2        2 weeks ago         94.7MB
```
Podemos comprobar como la versión con `Alpine`es la más ligera. La versión `stretch` está basada en Debian 9. La versión `buster` también está basada en Debian. Con la palabra `slim` quiere decir que es una versión reducida de estos sistemas. Si en el futuro la imagen que contiene `Alpine` diese problemas, se optaría por una de estas dos.

### Uso
> Para poder usar el Dockerfile es necesario instalar previamente el Docker. Se puede realizar fácilmente siguiendo su [documentación][offi_docu_docker]. También es conveniente configurarlo para usarlo sin la necesidad de hacer `sudo`.

1. Para construir la imagen a partir del Dockerfile ejecutamos:
    ```shell
    $ docker build --build-arg PORT=<puerto_interno> --tag <nombre_imagen> .
    ```
    > Contruye la imagen en el directorio actual. Pasamos como argumento el <puerto_interno> donde se levantará `Gunicorn`. Si no se pasa ningún argumento por defecto el <puerto_interno> será el 8080.

2. Para descargar la imagen desde DockerHub:
    ```shell
    $ docker pull ibe16/notifier:latest
    ```
    > El puerto interno será el por defecto.

2. Para ejecutar la imagen en local:
    ```shell
    $ docker run --rm -p <puerto_externo>:<puerto_interno> <nombre_imagen>
    ```
    > El <puerto_externo> indica el puerto por el que accedemos al contenedor. Para ver que el contenedor se ejecuta correctamente se puede consultar la url `http://0.0.0:<puerto_externo>/hello` que devolverá un 'Hello, World!'.

Para más información se puede consultar el [Dockerfile][enlace_dockerfile].

> El repositorio de `DockerHub` se ha configurado para que se actualice la imagen cada vez que se hago un `push` al repositorio de `Github`

## Heroku
La imagen del microservicio está desplegada en Heroku. Para comprobarlo se puede usar la url: https://cc-notifier.herokuapp.com/hello.

Se ha elegido Heroku como PaaS por ser relativamente famoso, ya que hace que haya mucha documentación sobre él. Además, es gratuito y muy sencillo de usar.

> **Antes de empezar**
> Heroku asigna en una variable de entorno un puerto por defecto que se tiene que usar como <puerto_interno> en el Dockerfile. Es decir, no se puede poner un número de puerto explícito para levantar nuestro servicio, si no, que deberemos leer este valor desde una variable de entono. En este caso la variable que hay que usar es `$PORT`. Se puede consultar en el archivo [Dockerfile][enlace_dockerfile] como hacerlo.

Para desplegarla se han seguido los siguientes pasos:
1. Descargarse la interfaz de comandos `Heroku CLI`
2. Crear una aplicación:
    ```shell
    $ heroku create <nombre_aplicación>
    ```
    > Tras este comando debe aparecer un nuevo repositorio `remote` llamado `heroku`. Se puede comprobar facilmente haciendo `git remote -v`.
3. Creamos el fichero `heroku.yml` en la raíz de nuestra aplicación. Para ver como se ha contruido se puede consultar el propio [fichero][enlace_herokuyml], aunque, básicamente, lo que hacemos es indicar que vamos a usar el `Dockerfile`.
4. Hacer `commit` de los cambios.
5. Establecer como imagen del SO la de Docker.
    ```shell
    $ heroku stack:set container
    ```
    > Con esto indicamos que vamos usar Docker. En Heroku `stack` es una imagen de sistema operativo. Por defecto se usa `Heroku-18`, pero nosotros queremos usar `container`que es la correspondiente a Docker.
6. Hacemos `push` de nuestra aplicación a Heroku.
    ```shell
    $ git push heroku master
    ```
Tras esto podemos consultar en `Heroku` el despliegue de la aplicación.

> Cómo alternativa o añadido se puede vincular el repositorio de `Github` para que cuando se haga `push` automáticamente se despliegue la aplicación. 


[arquitectura]:https://ibe16.github.io/CC-19-20-Proyecto/docs/arquitectura/Arquitectura

[docu_integracion]:https://ibe16.github.io/CC-19-20-Proyecto/docs/ic/integracion_continua

[enlace_dependencias]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/requirements.txt

[enlace_dockerfile]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/Dockerfile

[enlace_herokuyml]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/heroku.yml

[enlace_tasks]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/tasks.py

[enlace_travis]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.travis.yml

[enlace_workflow]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.github/workflows/pythonpackage.yml

[offi_docu_gunicorn]: https://gunicorn.org/

[offi_docu_docker]:https://docs.docker.com/install/linux/docker-ce/ubuntu/

[tecnologías]:https://ibe16.github.io/CC-19-20-Proyecto/docs/tecnologías/Tecnologías

[layer_scheme]:docs/arquitectura/esquema_capas.jpg
