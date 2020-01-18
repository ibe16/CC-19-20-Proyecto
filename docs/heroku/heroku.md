# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.
 
 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 
 
---

## Heroku
La imagen del microservicio está desplegada en Heroku. Para comprobarlo se puede usar la url: https://cc-notifier.herokuapp.com/hello.
 
Se ha elegido Heroku como PaaS por ser relativamente famoso, ya que hace que haya mucha documentación sobre él. Además, es gratuito y muy sencillo de usar.
 
> **Antes de empezar**
> Heroku asigna en una variable de entorno un puerto por defecto que se tiene que usar como <puerto_interno> en el Dockerfile. Es decir, no se puede poner un número de puerto explícito para levantar nuestro servicio, si no, que deberemos leer este valor desde una variable de entorno. En este caso la variable que hay que usar es `$PORT`. Se puede consultar en el archivo [Dockerfile][enlace_dockerfile] cómo hacerlo.
 
Para desplegarla se han seguido los siguientes pasos:
1. Descargarse la interfaz de comandos `Heroku CLI`
2. Crear una aplicación:
   ```shell
   $ heroku create <nombre_aplicación>
   ```
   > Tras este comando debe aparecer un nuevo repositorio `remote` llamado `heroku`. Se puede comprobar fácilmente haciendo `git remote -v`.
3. Creamos el fichero `heroku.yml` en la raíz de nuestra aplicación. Para ver como se ha construido se puede consultar el propio [fichero][enlace_herokuyml], aunque, básicamente, lo que hacemos es indicar que vamos a usar el `Dockerfile`.
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
 
> Cómo añadido se ha vinculado el repositorio de `Github` para que cuando se haga `push` automáticamente se despliegue la aplicación. Para más información se puede consultar la [documentación][offi_docu_heroku_gh] donde se explica el proceso.


[enlace_dockerfile]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/notifier/Dockerfile

[enlace_herokuyml]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/heroku.yml

[offi_docu_heroku_gh]:https://devcenter.heroku.com/articles/github-integration#enabling-github-integration