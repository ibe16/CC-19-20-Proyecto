from notifier import Notifier, NotificationList

from flask import current_app, g
from flask.cli import with_appcontext
import click

# Esta clase se ha hecho para cuando pinche la base da datos

# g es un objeto especial, único para cada petición
# current_app es un objeto especial que apunta hacia la aplicación que maneja la petición

n = NotificationList.NotificationList()
notifier = Notifier.Notifier()

def get_notifier():
    if 'notifier' not in g:
        #g.db= n
        notifier.init(n)
        g.notifier = notifier

    return g.notifier

# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()
#         print("BD cerrada")

def init_notifier():
    notifier = get_notifer()
    

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_notifier()
    click.echo('Initialized the database.')

def init_app(app):
    # Le dice a Flask que llame a la función "close_db" antes
    # de devolver la respuesta
    # app.teardown_appcontext(close_db)
    # Añade un nuevo comando
    app.cli.add_command(init_db_command)

    
