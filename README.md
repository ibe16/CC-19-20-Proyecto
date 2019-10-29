# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.

## Descripción del proyecto
Con este proyecto se quiere monitorizar los downtimes de las líneas de una fábrica. Consta de 2 entidades:
- **PlantMonitoring:** Se encarga de leer los datos de las líneas y almacenarlos en una base de datos. Los datos que se almacenan son el instante en el que se produce un downtime y la duración de este.
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

Se proporcionará una API-GATEWAY para poder comunicarse con los microservicios.

[imagen]:/docs/img/MicroServices.jpg

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
