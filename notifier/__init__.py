import os

from flask import Flask


def create_app(test_config=None):
    # Creación y configuración de la app
        # instance_relative_config = True hace que se carguen los archivos de 
        # cofiguración, que no deben deben ser commiteados
    app = Flask(__name__, instance_relative_config=True)

    # Configuración por defecto que usará la app como las bases de datos y la SECRET KEY
    # para mantener los datos seguros
    app.config.from_mapping(
        # 'dev' es un valor de prueba, mientras estamos desarrllando
         SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Carga la configuración con valores cogidos del archivo 'config.py'
        # Aquí por ejemplo se guarda la SECRET_KEY
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carga la configuración que pasemos
        app.config.from_mapping(test_config)

    # Se asegura de crear la carpeta de la instancia, necesaria para la base de datos
    # Por ahora no hace falta
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # Inicializamos la base de datos
    from notifier import db
    db.init_app(app)

    # Registramos el Blueprint para nuestro servicio
    from notifier import notifier_rest
    app.register_blueprint(notifier_rest.api)

     # Hello World
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    
    return app
