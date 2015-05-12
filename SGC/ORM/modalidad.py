from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from LeaderTeacher import LeaderTeacher
Column(Integer, Sequence('sec_mod'), primary_key=True)
class Modalidad(Base):
	__tablename__ = 'modalidad'
	id = Column(String(20),Sequence('sec_mod'),primary_key=True)
	modalidad = Column(String, nullable=False)
	cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))
	
	def __repr__(self):
		return "<modalidad(modalidad='%s')>" % self.modalidad
	
Base.metadata.create_all(engine)
