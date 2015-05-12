from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from LeaderTeacher import LeaderTeacher
Column(Integer, Sequence('sec_etnoeducacion'), primary_key=True)
class Etnoeducacion(Base):
	__tablename__ = 'etnoeducacion'
	id = Column(Integer,Sequence('sec_etnoeducacion'),primary_key=True)
	etnoeducacion = Column(String, nullable=False)
	cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))
	
	def __repr__(self):
		return "<etnoeducacion(etnoeducacion='%s')>" % self.etnoeducacion
	
Base.metadata.create_all(engine)
