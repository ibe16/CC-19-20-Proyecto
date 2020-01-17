# coding=utf-8
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer, DateTime

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
db = os.environ['POSTGRES_DB']
# URI para la conexión con la base de datos
uri = 'postgres+psycopg2://'+user+':'+password+'@'+host+':5432/'+db
engine = create_engine(uri)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class DowntimeRecordModel(Base):
    """Clase que contiene el modelo de la BD"""
    __tablename__ = 'downtimes'

    id = Column(Integer, primary_key=True)
    service = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    """La tabla contiene un id, el nombre del servicio, inició del downtime, final del downtime"""

    def __init__(self, service, date_start, date_end=None):
        self.service = service
        self.date_start = date_start
        self.date_end = date_end

