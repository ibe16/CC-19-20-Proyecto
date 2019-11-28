# Usamos como base la iamgen de alpine con python 3.6 instalado
FROM python:3.6-alpine

# Encaragdo de mantener el contenedor
LABEL maintainer="Irene Béjar <irenebejar@correo.ugr.es>"

# Copiamos solo los archivos locales necesarios al contenedor
COPY ./notifier/*.py /notifier/

# Nos colocamos en la raíz para poder ejecutar el microservicio
WORKDIR /

# Instalamos sólo las dependencias necesarias
RUN pip install flask gunicorn

# Exponemos el puerto 5000 del contenedor
EXPOSE 5000

# Configura el contenedor para correrlo como un ejecutable
# Esta orden no se ignora cuando se ejecuta el contenedor con parámetros
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:80 --workers=4  \"notifier:create_app()\""]