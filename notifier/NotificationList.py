import os
import sys
sys.path.append('notifier')
from NotificationList_model import NotificationList_model

class NotificationList:
    """Clase para realizar las operaciones con la BD"""


    def read_email(self, email):
        """Devuelve los objetos que contengan el email que se porporciona"""
        results=list(NotificationList_model.objects.raw({'email': email}))
        return results


    def read_line(self, id_line):
        """Devuelve un vector los emails que se encuentren en la lista proporcionada"""
        try:
            results=NotificationList_model.objects.values().get({'_id': id_line})
            results=results['email']
        except:
            results=[ ]
        
        return results


    def create(self, id_line, email):
        """Añade un email a una lista"""
        n = NotificationList_model(id_line, email)
        if n not in self.read_email(email):
            NotificationList_model.objects.raw({'_id' : id_line}).update({'$push':{'email':email}}, upsert=True)
        else:
            raise NameError ("El email ya existe")


    def delete(self, id_line, email):
        """Borra un email de una lista"""
        NotificationList_model.objects.raw({'_id' : id_line}).update({'$pull':{'email':email}})


    def update(self, id_line, old_email, new_email):
        """Actualiza un email en una lista"""
        if self.read_email(new_email) == [] and self.read_email(old_email) != []:
            self.delete(id_line, old_email)
            self.create(id_line, new_email)
        else:
            raise ValueError("No se pudo actualizar")




# if __name__ == "__main__":
#     NotificationList().delete("1", "uno@email.com")
# #     # NotificationList().update("1", "irene@email.com", "bejar@email.com")
# #     # NotificationList().create("2", "bejar@email.com")
#       #  NotificationList().read_email("irene@email.com")