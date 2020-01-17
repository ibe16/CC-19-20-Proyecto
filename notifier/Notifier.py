import os
import sys
sys.path.append('notifier')
import NotificationList
from notifier_celery import send_emails
import json



class Notifier:
    '''Clase para la lógica del microservicio Notifier '''


    def __init__ (self, db=None):
        """Constructor de la clase"""
        self.__db = db


    def init(self, db):
        """Método que aporta una base de datos, para realizar la inyección de dependencias"""
        self.__db = db


    def subscribe(self, id_line, email):
        """Subscribe un email a la lista que se le indique"""
        try:
            self.__db.create(id_line, email)
        except NameError:
            raise NameError ("El email existe ya")


    def unsubscribe (self, id_line, email):
        """Borra un email de la lista que se le indique"""
        self.__db.delete(id_line, email)


    def subscriptions(self, email):
        """Devuelve las suscripciones que tenga el email que se proporciona"""
        result = self.__db.read_email(email)

        if result == [ ]:
            raise ValueError ('El email no tiene subscripciones')
        else:
            response = {'id_lines' : [ ]}
            for r in result:
                response['id_lines'].append(r.id_line)

            return response


    def update(self, id_line, old_email, new_email):
        """Actualiza un email suscripto a una lista concreta"""
        try:
            self.__db.update(id_line, old_email, new_email)
        except ValueError:
            raise ValueError("Argumentos inválidos")


    def notification(self, id_line):
        """Envía una notificación a todos los correos de una lista"""
        result = self.__db.read_line(id_line)
        if result != [ ] :
            # Se invoca a la tarea de Celery de manera asíncrona
            send_emails.delay(id_line, result)
            #send_emails.apply_async(args=[id_line, result], queue='notifier', routing_key='notifier.import')


# if __name__ == "__main__":
#     d = NotificationList.NotificationList()
#     n = Notifier(d)

#     #n.subscribe('1', 'irenebejar@correo.ugr.es')
#     n.notification('1')

# #     # print(n.subscriptions('bejar@email.com'))

# #     f = open("data.csv", 'w')
# #     f.write("id")
# #     for i in range(1000000):
# #         f.write("%d\n" % (i))