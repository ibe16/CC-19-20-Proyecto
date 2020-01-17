import requests
import json
from datetime import datetime


# URL del API de los servicios que se van a monitorizar
# En este caso es el API de los servicios de Github, se puede consultar cuales son en esta web:
# https://www.githubstatus.com/
# Documentación de la API
# https://www.githubstatus.com/api/#summary 

URL="https://kctbh9vrtdwd.statuspage.io/api/v2/components.json"

class Monitor:
    """Clase para la lógica del Microservicio Monitor"""

    def __init__ (self, db=None):
        """Constructor de la clase"""
        self.__db = db
        # Estado en el que se pueden encontrar los servicios
        # Un estado distinto de operational se considerará downtime
        self._status = ['operational', 'degraded_performance', 'partial_outage', 'major_outage']

   
    def init(self, db):
        """Método para realizar la inyección de dependencias """
        self.__db = db

    
    def get_services_status(self):
        """Devuelve el estado en el que se encuentran los servicios"""
        response = requests.get(url = URL)
        data = response.json()
        result = {}
        
        for component in data['components']:
            result[component['name']] = component['status']

        return result

    
    def get_services_names(self):
        """Devuelve el nombre de los servicios que se están monitorizando"""
        response = requests.get(url = URL)
        data = response.json()
        result = []

        for component in data['components']:
            result.append(component['name'])

        return result

    
    def get_status_types(self):
        """Devuelve los estados en los que se pueden encontrar los servicios"""
        result={}
        result['status_types'] = self._status

        return result


    def get_service_status(self, service_name):
        """Devuelve el estado en el que se encuentra un servicio"""
        response = requests.get(url = URL)
        data = response.json()
        result = {}

        for component in data['components']:
            if component['name'] == service_name:
                result['status'] = component['status']

        return result


    def start_downtime(self, service_name):
        """Registra la hora de comienzo de un downtime para un servicio
            Devuelve un id para poder actualizar el downtime"""
        id = self.__db.start_downtime(service_name, datetime.now())
        return id


    def end_downtime(self, id):
        """Registra la hora de finalización de un downtime
            Se necesita el id para poder actualizar el downtime"""
        try:
            id = self.__db.end_downtime(id, datetime.now())
            return id
        except ValueError:
            raise ValueError ("El id no existe")


    def delete_downtime(self, id):
        """Borra un downtime
            Se necesita el id para borrar el downtime"""

        try:
            id = self.__db.delete_downtime(id)
        except ValueError:
            raise ValueError ("El id no existe")

    
    def get_downtime_record(self, service_name):
        """ Devuelve el registro con todos los downtime que ha sufrido un servicio"""
        result = self.__db.get_downtime_record(service_name)
        return result


    def get_downtime(self, id):
        """Devuelve los datos de un downtime concreto
            Se necesita el id"""
        result = self.__db.get_downtime(id)

        return result



# if __name__ == "__main__":
#     m = Monitor()
#     m.get_services_status()
#     m.get_services_names()
#     m.get_service_status('GitHub Actions')
#     m.get_status_types()