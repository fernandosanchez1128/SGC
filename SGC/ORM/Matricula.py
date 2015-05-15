
from LeaderTeacher import *
from sqlalchemy import (create_engine, Column, Date, Integer,Float,ForeignKey, ForeignKeyConstraint, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Curso import *
from Cohorte import *
from basetest import *


class Matricula (Base):
	
	__tablename__ = 'matricula'
	cedula_lt = Column(String(40),ForeignKey("leaderteacher.cedula"),  primary_key=True)
	id_curso = Column(Integer, ForeignKey("cohorte.id_curso"), primary_key=True )
	id_cohorte = Column(Integer,ForeignKey("cohorte.id_cohorte"), primary_key=True)
	nota_definitiva = Column(Float)



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
mat = Matricula(cedula_lt = 1144123, id_curso=78, id_cohorte = 654)
session.add(mat)
session.commit()