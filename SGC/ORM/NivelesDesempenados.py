from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from LeaderTeacher import LeaderTeacher
Column(Integer, Sequence('sec_niveles'), primary_key=True)
class Niveles(Base):
	__tablename__ = 'niveles'
	id = Column(Integer,Sequence('sec_niveles'),primary_key=True)
	niveles = Column(String, nullable=False)
	cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))
	
	def __repr__(self):
		return "<niveles(niveles='%s')>" % self.niveles
	
Base.metadata.create_all(engine)
