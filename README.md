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

Más información sobre la [arquitectura][arquitectura].

## Lenguajes y tecnologías usadas
El proyecto se desarrolla usando Python más:
    - Flask para la interfaz REST
    - Celery para gestionar los eventos
    - MySQL y MongoDB como bases de datos
    - Consul para la configuración distribuida

Más información sobre [lenguajes y tecnologías usadas][tecnologías].

## Prerrequisitos
Las versiones de Python compatibles con el proyecto son:
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
La herramienta de construcción usada es ```Invoke```

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

En el momento de la ejecución se pueden listar las tareas disponibles usanso ```invoke --list```.

Para más informacoión sobre los comandos que se ejecutan consulte el fichero [tasks.py][enlace_tasks].

## Integración continua
Como herramienta de intregración continua se ha usado:
1. **TravisCI**: Se encarga de ejecutar los test unitarios y de cobertura del proyecto. Se comprueban que los test funcionan correctamente en las versiones de Python de la 3.4 a las 3.8-dev, para el sistema operatico Linux (por defecto). Los resultados del test de cobertura se mandan a **Codecov** para su visualización. 
> Para más información sobre la configuración **TravisCI** se puede consultar el archivo de configuración [.travis.yml][enlace_travis].

2. **Github Actions**: Ejecuta tanto los test unitarios como los de cobertura del proyecto en las últimas versiones de Linux, Windows y MacOS. Se comprueban las versiones de Python desde la  3.5 a la 3.8. La versión 3.4 en MacOS da problemas al instalar las dependencias. También puede enviar los resultados de los test de cobertura a **Codecov**, pero se ha omitido esta función para no mandar el mismo resultado por duplicado. 
> Para más información sobre el workflow usado se puede consultar el archivo [pythonpackage.yml][enlace_workflow] que incluye notas aclarotorias.


[arquitectura]:https://ibe16.github.io/CC-19-20-Proyecto/docs/arquitectura/Arquitectura
[enlace_dependencias]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/requirements.txt
[enlace_tasks]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/tasks.py
[enlace_travis]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.travis.yml
[enlace_workflow]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.github/workflows/pythonpackage.yml
[tecnologías]:https://ibe16.github.io/CC-19-20-Proyecto/docs/tecnologías/Tecnologías
