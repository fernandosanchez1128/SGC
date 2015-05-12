from LeaderTeacher import *
from sqlalchemy import (create_engine, Column, Boolean, Date, Integer, ForeignKey, ForeignKeyConstraint, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Actividades import *

from basetest import *

class Notas (Base):
	__tablename__ = 'notas'
	cedula_lt = Column(String(40), ForeignKey('leaderteacher.cedula'), primary_key=True)
	id_actividades = Column(Integer, ForeignKey('actividades.id_actividades'), primary_key=True)
	ForeignKeyConstraint(['cedula_lt', 'id_actividades'],['leaderteacher.cedula','actividades.id_actividades'])
	nota = Column(Float)
	asistencia = Column(Boolean)

Base.metadata.create_all(engine)
