from sqlalchemy import (Boolean, Float, ForeignKeyConstraint)
from basetest import *

class Notas(Base):
    __tablename__ = 'notas'
    cedula_lt = Column(String(40),  primary_key=True)
    id_actividades = Column(Integer, primary_key=True)
    id_curso = Column(Integer,primary_key= True)
    id_cohorte = Column(Integer, primary_key=True)
    ForeignKeyConstraint(['cedula_lt', 'id_actividades','id_curso','id_cohorte'], ['leaderteacher.cedula', 'actividades.id_actividades','cohorte.id_curso','cohorte.id_cohorte'])
    nota = Column(Float)
    asistencia = Column(Boolean)



Base.metadata.create_all(engine)
