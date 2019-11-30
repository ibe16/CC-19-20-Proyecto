# Monitorización de líneas de producción
Proyecto para la asignatura de Cloud Computing en el Máster en Ingeniería Informática UGR.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ibe16/CC-19-20-Proyecto.svg?branch=master)](https://travis-ci.org/ibe16/CC-19-20-Proyecto)
[![codecov](https://codecov.io/gh/ibe16/CC-19-20-Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/ibe16/CC-19-20-Proyecto)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


---

## Integración continua
Como herramienta de intregración continua se han usado:
1. **TravisCI**: Se encarga de ejecutar los test unitarios y de cobertura del proyecto. Se comprueban que los test funcionan correctamente en las versiones de Python de la 3.4 a las 3.8-dev, para el sistema operatico Linux (por defecto). Los resultados del test de cobertura se mandan a **Codecov** para su visualización. 
> Para más información sobre la configuración **TravisCI** se puede consultar el archivo de configuración [.travis.yml][enlace_travis].

2. **Github Actions**: Ejecuta tanto los test unitarios como los de cobertura del proyecto en las versiones de Linux disponibles (16 y 18). Se comprueban las versiones de Python desde la  3.5 a la 3.8. También puede enviar los resultados de los test de cobertura a **Codecov**, pero se ha omitido esta función para no mandar el mismo resultado por duplicado. 
> Para más información sobre el workflow usado se puede consultar el archivo [pythonpackage.yml][enlace_workflow] que incluye notas aclarotorias.

[enlace_travis]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.travis.yml
[enlace_workflow]:https://github.com/ibe16/CC-19-20-Proyecto/blob/master/.github/workflows/pythonpackage.yml