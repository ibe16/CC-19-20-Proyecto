# -*- coding: utf-8 -*-

import os

from pymodm import connect
from pymodm import MongoModel, fields

import json
import re
from collections import OrderedDict

# Realizamos la conexión con la BD
connect(os.environ['MONGO_URI'], alias='notifier')

class NotificationList_model(MongoModel):
    """Modelo para la base de datos
        Indicamos que:
        1) La lista donde se suscribe el email es el ID de nuestro documento y en un String
        2) Los emails deben tener un formato válido y deben ser únicos para la lista en la que se encuentren"""
    id_line=fields.CharField(primary_key=True)
    email=fields.ListField(field=fields.EmailField(required=True, primary_key=True), required=True)

    class Meta:
        """Indicamos el alias para la BD y la colección donde vamos a almacenar los datos"""
        connection_alias='notifier'
        collection_name='notification_list'
        final = True

