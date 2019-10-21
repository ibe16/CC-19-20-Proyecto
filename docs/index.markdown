---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

theme: jekyll-theme-cayman
---

# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.

## Descripción del proyecto
Con este proyecto se quiere monitorizar los downtimes de las líneas de una fábrica. Consta de 2 entidades:
- **PlantMonitoring:** Se encarga de leer los datos de las líneas y almacenarlos en una base de datos. Los datos que se almacenan son el intante en el que se pruduce un downtime y la duración de este.
- **Notifier:** Su función es notificar a una lista de contactos que se ha producido un downtime y volver a avisar cuando se restablezca la línea.

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

Ambos microservicios se programarán con Python usando el framework Flask: Como base de datos se utilizará MySQL en el microservicio *PlantMonitoring* ya que facilitará las consultas de los downtimes, y MongoDB en *Notifier* por la simplicidad de los datos a almacenar.

Se usará Consul como sistema de configuración distribuida.

Se proporcionará una API-GETWAY para poder comunicarse con los microservicios.

[imagen]:https://github.com/ibe16/CC-19-20-Proyecto/tree/master/docs/img/MicroServices.jpg