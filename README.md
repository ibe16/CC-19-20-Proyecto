# CC-19-20-Proyecto
Proyecto para la asignatura de Cloud Computing UGR.

## Descripción del proyecto
Se desarrollará una aplicación para la gestión de listas de tareas. Esto permitirá mantenerte organizado con varias listas y ver en tu calendario las próximas deadlines.

Para ello se utilizará la arquitectura basada en microservicios, en este caso, dos que interactúan entre sí. A su vez, para establecer la comunicación entre ellos se usarán colas de eventos, de modo que se produzca una comunicación asíncrona.

Los dos microservicios que se implementarán serán:
- **Lista de Tareas**: Gestionará las tareas de cada lista almacenadas en una base de datos no relacional
- **Calendario**: Gestiona eventos y recordatorios