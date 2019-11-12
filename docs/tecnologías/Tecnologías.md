# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Lenguajes y tecnologías usadas

### Lenguaje de programación
**Python** el lenguaje escogido para programar ambos microservicios. Se ha elegido este lenguaje, a parte de por la sencillez y la rapidez de aprendizaje, por la cantidad de información que hay acerca de él y por permitir escribir un código bastante organizado. También dispone de un montón de módulos que le dan una gran versatilidad ante cualquier problema.

### Framework
Como microframework para implementar las APIs REST se usará **Flask**. Es bastante común, pero ofrece una serie de ventajas:
- Es ligero
- Hay mucha documentación sobre cómo usarlo
- Fácil de desplegar
- Cómodo para hacer APIs sencillas (como es mi caso)

### Bases de datos
Se usarán **MySQL** para gestionar y consultar mejor los datos de tipo *DATE* y  **MongoDB** para almacenar a donde hay qué mandar las notificaciones, para que sea más cómodo gestionar las listas.

### Cola de eventos
Por la simplicidad de los eventos a manejar se buscaba una cola de eventos que fuese simple y trabajase a alto nivel. Por lo comentado en clase escogí **Celery**. Hay bastante documentación sobre como configurarlo y usarlo y ofrece más que suficiente para los requisitos de la aplicación. Además de que se integra muy bien con Python.

### Configuración distribuida
Como servicio de configuración distribuida se usará **Consul** ya que guarda pares clave-valor y permite registrar los servicios.