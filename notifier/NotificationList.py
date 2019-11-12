from Email import Email

class NotificationList:
    def __init__ (self, lines = {}):
        self.__lines = lines

    def subscribe(self, id_line, email):
        try:
            if id_line not in self.__lines.keys(): 
                emails = Email()
                emails.add(email)   
                self.__lines[id_line] = emails    
            else:
                self.__lines[id_line].add(email)
        
        except ValueError:
            raise ValueError('Email no válido')

    def unsubscribe (self, id_line, email):
        try:
            if len(self.__lines[id_line]) == 1 and email in self.__lines[id_line]:
                del (self.__lines[id_line])
            else:
                self.__lines[id_line].remove(email)

        except KeyError:
            raise KeyError ('La línea no existe')

        except ValueError:
            raise ValueError ('El email no existe')
            
    def __repr__(self):
        return self.__lines.__repr__()

    def __len__(self):
        return self.__lines.__len__()

    def __iter__(self):
        return self.__lines.__iter__()
