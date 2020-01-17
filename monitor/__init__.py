# coding=utf-8

import os

from flask import Flask
from celery import Celery


from celery import Celery

def create_app(test_config=None):
    # Creación y configuración de la app
        # instance_relative_config = True hace que se carguen los archivos de 
        # cofiguración, que no deben deben ser commiteados
    app = Flask(__name__, instance_relative_config=True)

    # Configuración por defecto que usará la app como las bases de datos y la SECRET KEY
    # para mantener los datos seguros
    app.config.from_mapping(
        SECRET_KEY=os.environ['SECRET_KEY']
    )

    if test_config is None:
        # Carga la configuración con valores cogidos del archivo 'config.py'
        # Aquí por ejemplo se guarda la SECRET_KEY que se usará para testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carga la configuración que pasemos
        app.config.from_mapping(test_config)



    # Inicializamos la base de datos
    from monitor import db
    db.init_app(app)

    # Registramos el Blueprint para nuestro servicio
    from monitor import monitor_rest
    app.register_blueprint(monitor_rest.api)

     # Hello World
    @app.route('/hello')
    def hello():
        return 'Hello, this is MonitorMicroService!'

    
    return app