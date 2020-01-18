# Usamos como base la iamgen slim-strech (debian) con python 3.6 instalado
FROM python:3.6-slim-stretch

# Encargado de mantener el contenedor
LABEL maintainer="Irene Béjar <irenebejar@correo.ugr.es>"

# Copiamos solo los archivos locales necesarios para el funcionamiento del microservicio al contenedor
COPY ./*.py /notifier/

# Nos colocamos en la raíz para poder ejecutar el microservicio
WORKDIR /

# Argumentos necesarios para la creación del contenedor, los proporciona el docker compose
ARG PORT_NOTIFIER=${PORT_NOTIFIER}
ARG MONGO_URI=${MONGO_URI}
ARG SECRET_KEY=${SECRET_KEY}

# Variables de entorno necesarias para el funcionamiento del microservico, las proporciona el docker compose
ENV CELERY_BROKER_URL=${CELERY_BROKER_URL}
ENV CELERY_BACKEND=${CELERY_BACKEND}
ENV MONGO_URI=${MONGO_URI}
ENV CORREO=${CORREO}
ENV PASSWORD=${PASSWORD}
ENV SMTP_PORT=${SMTP_PORT}
ENV SMTP_SERVER=${SMTP_SERVER}
ENV PORT_NOTIFIER=${PORT_NOTIFIER}
ENV SECRET_KEY=${SECRET_KEY}

# Instalamos sólo las dependencias necesarias, sin usar el requirements.txt
RUN pip install flask gunicorn pymodm Celery eventlet

# Indicamos el puerto en el que se escucha el microservicio.
EXPOSE ${PORT_NOTIFIER}

# Creamos un usuario sin permisos de administrador para ejecutar el servidor
# Esto se hace por seguridad
RUN useradd -m normaluser
USER normaluser

# RUN ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT_NOTIFIER} --workers=4 --daemon \"notifier:create_app()\""]
# RUN celery -A notifier.notifier_celery worker 

# Levantamos el microservicio con Gunicorn
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT_NOTIFIER} --workers=4 \"notifier:create_app()\""]
