# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Configuración del despliegue en DockerHub desde Github
Para poder configurar el despliegue automático en `DockerHub` desde `Github` al hacer un `push` he seguido la [documentación][offi_docu_heroku_gh] de Docker donde se explica.

Lo primero que tenemos que hacer en configurar las builds automáticas en nuestro repositorio. Esta opción se encuentra en la pestaña `Builds`. A continuación, seleccionamos la plataforma donde se encuentra el repositorio externo que queremos configurar,

Después, tenemos que rellenar la información que nos pide:

![imagen][info_github]

Para comprobar que la `build` tiene exito, solo tenemos que hacer `push` en nuestro repositorio de `Github` y comprobar el estado de esta:

![imagen][estado_build]


[estado_build]:estado.png

[info_github]:config_DockerHub_gh.png

[offi_docu_docker_gh]:https://docs.docker.com/docker-hub/builds/