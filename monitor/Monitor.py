import requests
import json
from datetime import datetime



URL="https://kctbh9vrtdwd.statuspage.io/api/v2/components.json"

class Monitor:
    def __init__ (self, db=None):
        self.__db = db
        self._status = ['operational', 'degraded_performance', 'partial_outage', 'major_outage']

    def init(self, db):
        self.__db = db

    def get_services_status(self):
        response = requests.get(url = URL)
        data = response.json()
        result = {}
        
        for component in data['components']:
            result[component['name']] = component['status']

        print(result)
        return result

    def get_services_names(self):
        response = requests.get(url = URL)
        data = response.json()
        result = []

        for component in data['components']:
            result.append(component['name'])

        print(result)
        return result

    def get_status_types(self):
        result={}
        result['status_types'] = self._status

        print(result)
        return result

    def get_service_status(self, service_name):
        response = requests.get(url = URL)
        data = response.json()
        result = {}

        for component in data['components']:
            if component['name'] == service_name:
                result['status'] = component['status']

        print(result)
        return result

    def start_downtime(self, service_name):
        id = self.__db.start_downtime(service_name, datetime.now())
        return id

    def end_downtime(self, id, service_name):
        try:
            id = self.__db.end_downtime(id, service_name, datetime.now())
            return id
        except ValueError:
            raise ValueError ("El id no existe")

    def delete_downtime(self, id):
        try:
            id = self.__db.delete_downtime(id)
        except ValueError:
            raise ValueError ("El id no existe")

    def get_downtime_record(self, service_name):
        result = self.__db.get_downtime_record(service_name)
        return result

    def get_downtime(self, id):
        result = self.__db.get_downtime(id)

        return result



if __name__ == "__main__":
    m = Monitor()
    m.get_services_status()
    m.get_services_names()
    m.get_service_status('GitHub Actions')
    m.get_status_types()