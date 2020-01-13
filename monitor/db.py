from monitor import Monitor, DowntimeRecord



from flask import current_app, g
from flask.cli import with_appcontext
import click

# Esta clase se ha hecho para cuando pinche la base da datos

# g es un objeto especial, único para cada petición
# current_app es un objeto especial que apunta hacia la aplicación que maneja la petición

m = DowntimeRecord.DowntimeRecord()
monitor = Monitor.Monitor()

def get_monitor():
    if 'monitor' not in g:
        #g.db= n
        monitor.init(m)
        g.monitor = monitor

    return g.monitor


def init_monitor():
    monitor = get_monitor()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_monitor()
    click.echo('Initialized the database.')

def init_app(app):
    app.cli.add_command(init_db_command)