from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from LeaderTeacher import LeaderTeacher
Column(Integer, Sequence('sec_areas'), primary_key=True)
class AreasDesempenadas(Base):
	__tablename__ = 'areas_desempenadas'
	id = Column(Integer,Sequence('sec_areas'),primary_key=True)
	area = Column(String, nullable=False)
	cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))
	
	def __repr__(self):
		return "<Area(area='%s')>" % self.area
	
Base.metadata.create_all(engine)
