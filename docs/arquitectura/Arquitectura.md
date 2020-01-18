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
    - Propocionar los datos sobre los servicios que se están monitorizando
    - Informar cuando se produzca una parada o cuando vuelva a arrancar la línea

- **Notifier:**
    - Suscribirse a las notificaciones de uno o varios servicios
    - Borrarse de las notificaciones de uno o varios servicios
    - Información sobre las suscripciones

Debido a que la operación de mandar todas las notificaciones puede ser una operación lenta se usará una cola de tareas (Celery) para no bloquear al microservicio que monitoriza mientras se realiza la operación. El resto de operaciones se realizarán mediante una interfaz REST.

Se proporcionará una API-GATEWAY para poder comunicarse con los microservicios.

[imagen]:MicroServices.jpg

## Arquitectura por capas
Se basa en separar la funcionalidad de un servicio en varias capas, para permitir que este sea más fácil de mantener, cambiar y escalar.
 
### Capas del microservicio Notifier
Las capas que contiene este microservicio son:
 
1. La capa que contiene el API REST, que configura las rutas con las que se atienden las peticiones.
2. Una capa con la lógica de negocio que maneja los modelos y controla los procesos que se tiene que seguir.
3. Una capa con los modelos de datos que se usan.
 
A continuación se muestra un esquema de las capas descritas:
![service_layers][layer_scheme_notifier]

### Capas del microservicio Monitor
Las capas que contiene el microservicio son:

1. La capa que contiene el API REST, que configura las rutas con las que se atienden las peticiones.
2. Una capa con la lógica de negocio que maneja los modelos y controla los procesos que se tiene que seguir.
3. Una capa con los modelos de datos que se usan.

A continuación, se muestra un esquema con las capas:
![service_layers][layer_scheme_monitor]

## Microservicio Notifier
Su función es guardar listas de correos a los que se les puede mandar una notificación. Su funcionamiento a través del API REST es el siguiente:
 
1. **GET: /hello**
   Muestra un 'Hello, World!'. Se usa durante el desarrollo para comprobar que el servicio responde.
  
2. **GET: /notifier/prueba**
   Otra prueba para el desarrollo. En este caso para comprobar que funciona el blueprint de Flask.
  
3. **POST: /notifier/email**
   Subscribe un email a una lista.
   Necesita como dato un `json` de la forma:
   ```json
   {
      "id_line":"<número_de_línea>",
      "email":"<email_válido>"
   }
   ```
 
4. **PUT: /notifier/email**
   Actualiza el email en una lista.
   Necesita como dato un `json` de la forma:
   ```json
   {
      "id_line": "<número_de_línea>",
      "old_email" : "<email_antiguo>",
      "new_email" : "<email_nuevo>"
   }
   ```
  
4. **DELETE: /notifier/email**
   Borra un email de una lista.
   Necesita como dato un `json` de la forma:
   ```json
   {
      "id_line":"<número_de_línea>",
      "email":"<email_válido>"
   }
   ```
  
5. **GET: /notifier/email**
   Devuelve un json indicando las suscripciones en la que se encuentra dicho email.
   ```json
   {
      "id_lines": ["1"]
   }
   ```

## Microservicio Monitor
1. **GET: /hello**
   Muestra un 'Hello, World!'. Se usa durante el desarrollo para comprobar que el servicio responde.

2. **GET: /monitor/status**
   Devuelve un json con el estado de los servicios
   ```json
   {
      'Git Operations': 'operational', 
      'API Requests': 'operational', 
      'Webhooks': 'operational', 
      'Visit www.githubstatus.com for more information': 'operational', 
      'Issues, PRs, Projects': 'operational', 
      'GitHub Actions': 'degraded_performance', 
      'GitHub Packages': 'operational', 
      'GitHub Pages': 'operational', 
      'Other': 'operational'
   }
   ```
   
3. **GET: /monitor/status/service**
   Devuelve un json con el estado del servicio. Necesita un json de la forma.
   ```json
   {
      "service": "<nombre>"
   }
   ```
   
4. **GET: /monitor/status/types**
   Devuelve los tipos de estados en los que se puede encontrar un servicio.
   ```json
   {
      "status_types" : ['operational', 'degraded_performance', 'partial_outage', 'major_outage']
   }
   ```
   
5. **GET: /services**
   Devuelve un json con los servicios que se están monitorizando.
   ```json
   {
      "services" : <lista con los servicios> 
   }
   ```
   
6. **GET: /downtime/record**
   Devuelve un json con los Ids de los downtimes de un servicio. Necesita un json con el servicio que se quiere consultar.
   ```json
   {
      "service": "<nombre>"
   }
   ```
   
7. **GET /downtime**
   Devuelve un json con la información del downtime que se quiere consultar. Necesita un json con el id del downtime.
   ```json
   {
      "id": número de id
   }
   ```
   
8. **DELETE: /downtime**
   Devuelve un json con la información del downtime que se quiere consultar. Necesita un json con el id del downtime.
   ```json
   {
      "id": número de id
   }
   ```
   





[layer_scheme_notifier]:esquema_capas.png
[layer_scheme_monitor]:esquema_capas_monitor.png
