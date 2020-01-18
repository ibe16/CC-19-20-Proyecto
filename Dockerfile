# Este Dockerfile se encuentra en el directorio raíz y no en la carpeta del módulo correspondiente por dos motivos:
# El primeroes poder copiar los archivos necesarios
# El segundo pasar los tests

# Usamos como base la iamgen slim (debian) con python 3.6 instalado
FROM python:3.6-slim

# Encargado de mantener el contenedor
LABEL maintainer="Irene Béjar <irenebejar@correo.ugr.es>"

# Copiamos solo los archivos locales necesarios para el funcionamiento del microservicio al contenedor
# Este miicroservicio usa un método del otro microservicio, concretamente el que invoca a Celery
COPY ./monitor/*.py /monitor/
COPY ./notifier/*.py /notifier/

# Nos colocamos en la raíz para poder ejecutar el microservicio
WORKDIR /

# Argumentos necesarios para la creación del contenedor, los proporciona el docker compose
ARG POSTGRES_USER=${POSTGRES_USER}
ARG POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ARG POSTGRES_HOST=${POSTGRES_HOST}
ARG POSTGRES_DB=${POSTGRES_DB}
ARG PORT_MONITOR=${PORT_MONITOR}

# Variables de entorno necesarias para el funcionamiento del microservico, las proporciona el docker compose
ENV CELERY_BROKER_URL=${CELERY_BROKER_URL}
ENV CELERY_BACKEND=${CELERY_BACKEND}
ENV SECRET_KEY=${SECRET_KEY}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV PORT_MONITOR=${PORT_MONITOR}
ENV MONGO_URI='mongodb://localhost/db'
ENV CORREO=${CORREO}
ENV PASSWORD=${PASSWORD}
ENV SMTP_PORT=${SMTP_PORT}
ENV SMTP_SERVER=${SMTP_SERVER}
ENV PORT_NOTIFIER=${PORT_NOTIFIER}
ENV SECRET_KEY=${SECRET_KEY}

# Instalamos sólo las dependencias necesarias, sin usar el requirements.txt
RUN apt-get update -y
RUN apt-get install libpq-dev -y
RUN pip install flask gunicorn requests sqlalchemy psycopg2-binary Celery pymodm

# Indicamos el puerto en el que se escucha el microservicio.
EXPOSE ${PORT_MONITOR}

# Creamos un usuario sin permisos de administrador para ejecutar el servidor
# Esto se hace por seguridad
# RUN useradd -m normaluser
# USER normaluser

#RUN ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT_MONITOR} --workers=4  \"monitor:create_app()\""]
#RUN celery -A monitor.monitor_celery worker --beat --loglevel=debug

# Levantamos el microservicio con Gunicorn
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT_MONITOR} --workers=4  \"monitor:create_app()\""]
