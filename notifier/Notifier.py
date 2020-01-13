import os
import sys
sys.path.append('notifier')
import NotificationList
from notifier_celery import send_emails
import json



class Notifier:
    def __init__ (self, db=None):
        self.__db = db

    def init(self, db):
        self.__db = db

    def subscribe(self, id_line, email):
        try:
            self.__db.create(id_line, email)
        except NameError:
            raise NameError ("El email existe ya")

    def unsubscribe (self, id_line, email):
        self.__db.delete(id_line, email)

    def subscriptions(self, email):
        result = self.__db.read_email(email)

        if result == [ ]:
            raise ValueError ('El email no tiene subscripciones')
        else:
            response = {'id_lines' : [ ]}
            for r in result:
                response['id_lines'].append(r.id_line)

            return response

    def update(self, id_line, old_email, new_email):
        try:
            self.__db.update(id_line, old_email, new_email)
        except ValueError:
            raise ValueError("Argumentos inválidos")

    def notification(self, id_line):
        result = self.__db.read_line(id_line)
        if result != [ ] :
            send_emails.delay(id_line, result)

            
    # def __repr__(self):
    #     return self.__lines.__repr__()

    # def __len__(self):
    #     return self.__lines.__len__()

    # def __iter__(self):
    #     return self.__lines.__iter__()


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