# Usamos como base la iamgen slim-strech (debian) con python 3.6 instalado
FROM python:3.6-slim-stretch

# Encargado de mantener el contenedor
LABEL maintainer="Irene Béjar <irenebejar@correo.ugr.es>"

# Copiamos solo los archivos locales necesarios para el funcionamiento del microservicio al contenedor
COPY ./notifier/*.py /notifier/

# Nos colocamos en la raíz para poder ejecutar el microservicio
WORKDIR /

# Definimos un argumento que se puede pasar durante la construcción.
# Así no se tiene que declarar una variable de entorno si no se quiere. 
# Si no se proporciona ninguno por defecto será el 8080.
ARG PORT=8080

# Establecemos las variables de entorno para el contenedor
# Definimos el puerto
ENV PORT=${PORT}

# Instalamos sólo las dependencias necesarias, sin usar el requirements.txt
RUN pip install flask gunicorn

# Indicamos el puerto en el que se escucha el microservicio.
# Por defecto es el (=(=))
EXPOSE ${PORT}

# Creamos un usuario sin permisos de administrador para ejecutar el servidor
# Esto se hace por seguridad
RUN useradd -m normaluser
USER normaluser

# Levantamos el microservicio con Gunicorn
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} --workers=4  \"notifier:create_app()\""]