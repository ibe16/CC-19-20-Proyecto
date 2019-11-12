# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Arquitectura
Como arquitectura se ha eligido una arquitectura basada en microservicios, donde cada microservicio corresponde con las entidades descritas.

![arquitectura][imagen]

Las operaciones que realizará cada microservicio son:
- **PlantMonitoring:**
    - Propocionar los datos sobre downtimes entre dos periodos de tiempo
    - Propocionar los datos sobre las líneas que se están monitorizando
    - Informar cuando se produzca una parada o cuando vuelva a arrancar la línea

- **Notifier:**
    - Suscribirse a las notificaciones de una o varias lineas
    - Borrarse de las notificaciones de una o varias lineas
    - Información sobre las suscripciones

Debido a que la operación de mandar todas las notificaciones puede ser una operación lenta se usará una cola de tareas (Celery) para no bloquear al microservicio que monitoriza mientras se realiza la operación. El resto de operaciones se realizarán mediante una interfaz REST.

Se proporcionará una API-GATEWAY para poder comunicarse con los microservicios.

[imagen]:MicroServices.jpg