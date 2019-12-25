import os
import sys
sys.path.append('notifier')
from NotificationList_model import NotificationList_model

class NotificationList:
    def read_email(self, email):
        results=list(NotificationList_model.objects.raw({'email': email}))

        print(results)
        return results
        

    def create(self, id_line, email):
        n = NotificationList_model(id_line, email)
        if n not in self.read_email(email):
            NotificationList_model.objects.raw({'_id' : id_line}).update({'$push':{'email':email}}, upsert=True)
        else:
            raise NameError ("El email ya existe")
        

    def delete(self, id_line, email):
        NotificationList_model.objects.raw({'_id' : id_line}).update({'$pull':{'email':email}})

    def update(self, id_line, old_email, new_email):
        
        if self.read_email(new_email) == [] and self.read_email(old_email) != []:
            self.delete(id_line, old_email)
            self.create(id_line, new_email)
        else:
            raise ValueError("No se pudo actualizar")




if __name__ == "__main__":
    NotificationList().delete("1", "uno@email.com")
#     # NotificationList().update("1", "irene@email.com", "bejar@email.com")
#     # NotificationList().create("2", "bejar@email.com")
      #  NotificationList().read_email("irene@email.com")