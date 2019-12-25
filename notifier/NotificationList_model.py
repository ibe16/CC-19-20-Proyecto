# -*- coding: utf-8 -*-

from pymodm import connect
from pymodm import MongoModel, fields

import json
import re
from collections import OrderedDict

connect('mongodb://localhost:27017/notifier', alias='notifier')

class NotificationList_model(MongoModel):
    id_line=fields.CharField(primary_key=True)
    email=fields.ListField(field=fields.EmailField(required=True, primary_key=True), required=True)

    class Meta:
        connection_alias='notifier'
        collection_name='notification_list'
        final = True

# if __name__ == "__main__":
#     NotificationList_model('1', [ ]).save()
    

# class NotificationList_model:
#     def __init__ (self, uri, dbname, collection_name):
#         self.__client = MongoClient(uri)
#         self.__db = self.__client[dbname]

#         # Borramos la colección y la volvemos a crear
#         self.__collection =self.__db.get_collection(collection_name)
#         self.__collection.drop()
#         #self.__db.create_collection(collection_name)

#         # Cargar el esquema de la base de datos
#         with open('db_schema.json') as json_file:
#             schema = json.load(json_file)


#         # query = [('collMod', collection_name),
#         #          ('validator', schema),
#         #          ('validatorLevel', 'strict'),
#         #          ('validationAction', 'error')
#         #         ]

#         query = { 'collMod': collection_name, 'validator': {"$jsonSchema": schema } }
#         #query = {'validator' : schema}

        
#         # query = OrderedDict(query)
#         #print(query)
#         self.__db.create_collection(name=collection_name)
#         self.__db.command(query)

#         # Cargamos la colección de nuevo
#         self.__collection =self.__db.get_collection(collection_name)

#         self.__collection.insert_one({'id_line':"1", 'email':["email@email.com"]})

# if __name__ == "__main__":

#     uri='mongodb://localhost:27017/'
#     dbname='notifier'
#     collection_name='notification_list'
#     n = NotificationList_model(uri, dbname, collection_name)

# {
#     "bsonType": "object",
#     "required": ["id_line"],
#     "properties": {
#         "_id":{ },
#         "id_line": {
#             "bsonType" : "string",
#             "description" : "El ID de una línea debe ser un String"
#         },
#         "emails": {
#             "bsonType" : ["array"],
#             "minItems" : 1,
#             "uniqueItems" : true,
#             "additionalProperties" : false,
#             "items" : {
#                 "bsonTypes" : "string",
#                 "description" : "Los 'emails' deben ser un string"
#             }
#         }
#     }
# }

# { "$and":
#     [
#         { "id_line":[ 
#             { "$exist" : true},
#             { "$type": "string" } ]
#         },
#         { "email": [
#             { "$exist" : true},
#             { "$type": "array" } ]
#         }
#     ]
# }
