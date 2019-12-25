#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

class Email:
    """
    Clase para representar listas de Emails.
    @author: Irene Béjar Maldonado
    """

    def __init__(self):
        """
        Contructor. Crea una lista para almacena emails.
        """
        self.__email_list = list()

    def __validate_email(self, email):
        """
        Comprueba que un email tenga un formato válido.
        Recibe un email y devuelve True si es válido y False si no lo es.
        """
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if (re.search(regex,email)):
            return True
        else:
            return False
    
    def add(self, email):
        """
        Añade un email válido a la lista.
        Recibe un email.
        Lanza una excepción ValueError si el email no tiene un formato válido.
        """
        if (self.__validate_email(email)):
            self.__email_list.append(email)
        else:
            raise ValueError('Email no válido')

    def remove(self, email):
        """
        Elimina un email de la lista.
        Recibe un email.
        Lanza una excepción ValueError si el email no existe.
        """
        try:
            self.__email_list.remove(email)
        except ValueError:
            raise ValueError ('El email no existe')

    def __len__(self):
        """
        Sobrecarga del operador len para poder consultar el número de elementos.
        """
        return len(self.__email_list)

    def __repr__(self):
        """
        Sobrecarga del operador repr para darle formato a un objeto de tipo Email.
        """
        return self.__email_list.__repr__()

    def __iter__(self):
        """
        Sobrecarga del operador iter para poder iterar en un objeto de tipo Email.
        """
        return self.__email_list.__iter__()



def fallback_encoder(value):
    """
    Función para poder codificar objetos de tipo Email como bson.
    Se usa para poder insertar Emails en MongoDB.
    """
    if isinstance(value, Email):
        return list(value)
    return value



# class EmailEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Email):
#             return obj._Email__email_list
            
#         return json.JSONEncoder.default(self, obj)

# class EmailDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

#     def object_hook(self, dct):
