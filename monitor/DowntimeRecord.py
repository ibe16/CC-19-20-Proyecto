from datetime import datetime

import sys
sys.path.append('monitor')
import DowntimeRecord_model
from DowntimeRecord_model import DowntimeRecordModel
from DowntimeRecord_model import Session
from DowntimeRecord_model import engine
from DowntimeRecord_model import Base

# Creamos el esquema de la base de datos
Base.metadata.create_all(engine)

# Creamos una nueva sesion
session = Session()

class DowntimeRecord:
    """Clase para realizar las operaciones con la BD"""


    def get_downtime_record(self, service):
        """Devuelve los downtimes que se han registrado de un servicio"""
        data = session.query(DowntimeRecordModel).filter(DowntimeRecordModel.service == service).all()
        result = { }
        if data is not [ ]:
            for element in data:
                if element.service not in result.keys():
                    result[element.service]=[element.id]
                else:
                    result[element.service].append(element.id)

        return result


    def get_downtime(self, id):
        """Consulta la información de un downtime concreto"""
        downtime = session.query(DowntimeRecordModel).get(id)
        result = { }
        if downtime is not None:
            result['service']= downtime.service
            result['date_start']= downtime.date_start.strftime("%d/%m/%Y, %H:%M:%S")
            if downtime.date_end is None:
                result['date_end'] = " "
            else:
                result['date_end']=downtime.date_end.strftime("%d/%m/%Y, %H:%M:%S")
 
        return result


    def start_downtime(self, service, date_start):
        """Crea una nueva entrada para un downtime"""
        downtime = DowntimeRecordModel(service, date_start)
        session.add(downtime)
        session.commit()

        return downtime.id 


    def end_downtime(self, id, date_end):
        """Almacena la fecha de finalización de un downtime"""
        if self.get_downtime(id):
            downtime = session.query(DowntimeRecordModel).get(id)
            downtime.date_end = date_end
            session.add(downtime)
            session.commit()

            return downtime.id
        else:
            raise ValueError ("El id no existe")

    def delete_downtime(self, id):
        """Borra el registro de un downtime"""
        if self.get_downtime(id):
            downtime = session.query(DowntimeRecordModel).get(id)
            session.delete(downtime)
            session.commit()
        else: 
            raise ValueError ("El id no existe")
        



# if __name__ == "__main__":
#     d = DowntimeRecord()
#     #id = d.start_downtime("GitHub Actions", datetime.now())
#     #print(id)
#     #d.end_downtime(id, 'GitHub Actions', datetime.now())
#     #d.delete_downtime(1)
#     #d.get_downtime_record('GitHub Actions')
#     #d.get_downtime(1)