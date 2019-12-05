# Usamos como base la iamgen de alpine con python 3.6 instalado
FROM python:3.6-slim-stretch

# Encaragdo de mantener el contenedor
LABEL maintainer="Irene Béjar <irenebejar@correo.ugr.es>"

# Copiamos solo los archivos locales necesarios al contenedor
COPY ./notifier/*.py /notifier/

# Nos colocamos en la raíz para poder ejecutar el microservicio
WORKDIR /

# Argumento que se pasa durante la construcción. Si no se proporciona ninguno por defecto será el 8080.
ARG PORT=8080

# Establecemos una variable de entorno para el contenedor
ENV PORT=${PORT}

# Instalamos sólo las dependencias necesarias
RUN pip install flask gunicorn

# Exponemos el puerto que se pasa como argumento o por defecto el 8080 del contenedor
EXPOSE ${PORT}

# Levantamo el microservicio con Gunicorn
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} --workers=4  \"notifier:create_app()\""]