import re
import json

class Email:
    def __init__(self):
        self.__email_list = list()

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

# class EmailEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Email):
#             return obj._Email__email_list
            
#         return json.JSONEncoder.default(self, obj)

# class EmailDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

#     def object_hook(self, dct):
