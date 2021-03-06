from notifier import Notifier, NotificationList



from flask import current_app, g
from flask.cli import with_appcontext
import click

# g es un objeto especial, único para cada petición
# current_app es un objeto especial que apunta hacia la aplicación que maneja la petición

# Objeto para realizar la inyección de dependencias
n = NotificationList.NotificationList()
# Lógica de negocio
notifier = Notifier.Notifier()

def get_notifier():
    if 'notifier' not in g:
        # Inyección de dependencias
        notifier.init(n)
        g.notifier = notifier

    return g.notifier

# Métodos para iniciar la base de datos sn tener que iniciar la aplicación
# usados durante la creación de la aplicación y para testear
def init_notifier():
    notifier = get_notifier()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_notifier()
    click.echo('Initialized the database.')

def init_app(app):
    app.cli.add_command(init_db_command)

    
