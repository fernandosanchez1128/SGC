from sqlalchemy import (Boolean, Float, ForeignKeyConstraint)
from basetest import *

class Notas(Base):
    __tablename__ = 'notas'
    cedula_lt = Column(String(40),ForeignKey = ('leaderteacher.cedula'), primary_key=True)
    id_actividades = Column(Integer,ForeignKey = ('actividades.id_actividades'), primary_key=True)
    id_curso = Column(Integer,primary_key= True)
    id_cohorte = Column(Integer, primary_key=True)
    ForeignKeyConstraint(['id_curso','id_cohorte'], ['cohorte.id_curso','cohorte.id_cohorte'])
    nota = Column(Float)
    asistencia = Column(Boolean)



Base.metadata.create_all(engine)
