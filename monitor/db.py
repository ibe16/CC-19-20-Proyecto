from monitor import Monitor, DowntimeRecord



from flask import current_app, g
from flask.cli import with_appcontext
import click

# g es un objeto especial, único para cada petición
# current_app es un objeto especial que apunta hacia la aplicación que maneja la petición

# Objeto para realizar la inyección de dependencias
m = DowntimeRecord.DowntimeRecord()
# Lógica de negocio
monitor = Monitor.Monitor()

def get_monitor():
    if 'monitor' not in g:
        # Inyección de dependencias
        monitor.init(m)
        g.monitor = monitor

    return g.monitor


# Métodos para iniciar la base de datos sin tener que iniciar la aplicación
# usados durante la creación de la aplicación y para testear
def init_monitor():
    monitor = get_monitor()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_monitor()
    click.echo('Initialized the database.')

def init_app(app):
    app.cli.add_command(init_db_command)