# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.
 
 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 
 
---

## Bases de datos
Se usarán **PostgreSQL** para gestionar y consultar mejor los datos de tipo *DATE* y  **MongoDB** para almacenar a donde hay qué mandar las notificaciones, para que sea más cómodo gestionar las listas.

Para la implementación de ambas bases de datos se ha usado un ORM para mapear los objetos de la base de datos a objetos de Pyhton y marcar los esquemas que deben seguir estos. Para los dos microservicos se ha usado en mismo patrón: una clase para definir cómo son los objetos y que realiza la conexión a la base de datos y otra clase que define las operaciones con la base de datos. 

Para el **Microservicio Notifier** estas clases son:
- [NotificationList_model.py][enlace_NotificationList_model]
- [NotificationList.py][enlace_NotificationList]

Para el **Microservicio Monitor** estas clases son:
- [DowntimeRecord_model.py][enlace_DowntimeRecord_model]
- [DowntimeRecord.py][enlace_DowntimeRecord]

### Notifier
El ORM que se ha usado es `PyMODM` que está construido sobre `Pymongo`. Aquí se puede encontrar un enlace a la [documentación oficial][offi_docu_pymodm].

El motivo por el cual se elegió usar un ORM en vez de directamente el drive de MongoDB que existe para Python fue la necesidad de indicar unas restricciones sobre los datos. En concreto, en los emails que se almacenan, no deben ser una cadena cualquiera si no un email válido. Con el ORM es tan simple como hacer una clase que sea tu modelo ([NotificationList_model.py][enlace_NotificationList_model]) donde se indica los datos que vas a usar y de que tipo van a ser. En este caso tenemos dos tipos:
1. Un String que sirve como ID para el documento y para guardar el nombre de la lista de correo. De este modo una lista de correo es única en toda la BD.
2. Una lista de Emails, cada email único en la lista en la que se encuentra. De este modo, la BD no nos deja insertar emails que no son válidos y los emails solo se pueden insertar una vez en una lista de correo.

Después se ha implementado una clase que utiliza este modelo e implementa todas las operaciones con la BD([NotificationList.py][enlace_NotificationList]). Un objeto de la clase `NotificationList` es el que se usará más tarde para realizar la **inyección de dependencias**.

Por último, la clase [Notifier.py][enlace_Notifier] hace uso de un objeto que implemente una conexión a base de datos.

En el fichero [db.py][enlace_db_notifier] se puede ver como se realiza la **inyección de dependencias**.

Para más información se puede consultar cualquier enlace a los archivos anteriores que contienen más documentación.

### Monitor
Este microservicio usa una BD SQL, concretamente `PostgreSQL`. El motivo principal de usar una BD de este tipo era que fuese más cómodo organizar los datos de downtime. 

Para la implementación se ha usado el ORM `SQLAlchemy`. Aquí se puede consultar la [documentación oficial][offi_docu_sqlalchemy].

El motivo por el cual se ha usado un ORM aquí es facilitar las consultas SQL que se realizan sobre la BD. De esta forma no hace falta usar SQL directamente en el código. sino que tenemos ina abstracción. Además los resultados de estas consultas se mapean a objetos Python directamente. Al igual que en el microservicio anterior se ha usado dos clases:
- [DowntimeRecord_model.py][enlace_DowntimeRecord_model] que implementa el modelo de la base de datos. La tabla que se describe contiene un id, el nombre del servicio, inició del downtime, final del downtime.
- [DowntimeRecord.py][enlace_DowntimeRecord] que implementa la consultas y más tarde será el objeto con el que se realiza la **inyección de dependencias**.

Y también, al igual que en el microservicio anterior, la clase [Monitor.py][enlace_monitor] hace uso de un objeto que implementa una conexión a base de datos. 

En el fichero [db.py][enlace_db_monitor] se puede ver como se realiza la **inyección de dependencias**.

Para más información se puede consultar cualquier enlace a los archivos anteriores que contienen más documentación.

[enlace_DowntimeRecord]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/monitor/DowntimeRecord.py

[enlace_DowntimeRecord_model]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/monitor/DowntimeRecord_model.py 

[enlace_monitor]: https://github.com/ibe16/CC-19-20-Proyecto/blob/master/monitor/Monitor.py

[enlace_Notifier]: https://github.com/ibe16/CC-19-20-Proyecto/blob/master/notifier/Notifier.py

[enlace_NotificationList_model]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/notifier/NotificationList_model.py

[enlace_NotificationList]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/notifier/NotificationList.py

[offi_docu_pymodm]:https://pymodm.readthedocs.io/en/stable/

[offi_docu_sqlalchemy]:https://docs.sqlalchemy.org/en/13/