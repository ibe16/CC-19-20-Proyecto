# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer, DateTime


engine = create_engine('postgres+psycopg2://postgres:1997bm@localhost/monitor')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class DowntimeRecordModel(Base):
    __tablename__ = 'downtimes'

    id = Column(Integer, primary_key=True)
    service = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)

    def __init__(self, service, date_start, date_end=None):
        self.service = service
        self.date_start = date_start
        self.date_end = date_end

