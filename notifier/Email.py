import re

class Email:
    def __init__(self):
        self.__email_list = []

    def __validate_email(self, email):
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if (re.search(regex,email)):
            return True
        else:
            return False
    
    def add(self, email):
        if (self.__validate_email(email)):
            self.__email_list.append(email)
        else:
            raise ValueError('Email no válido')

    def remove(self, email):
        try:
            self.__email_list.remove(email)
        except ValueError:
            raise ValueError ('El email no existe')

    def __len__(self):
        return len(self.__email_list)

    def __repr__(self):
        return self.__email_list.__repr__()

    def __iter__(self):
        return self.__email_list.__iter__()
    

    