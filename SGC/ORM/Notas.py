from sqlalchemy import (Boolean, Float, ForeignKeyConstraint)
from basetest import *

class Notas(Base):
    __tablename__ = 'notas'
    cedula_lt = Column(String(40),ForeignKey ('leaderteacher.cedula'), primary_key=True)
    id_actividad = Column(Integer, primary_key=True)
    id_curso = Column(Integer,primary_key= True)
    id_cohorte = Column(Integer, primary_key=True)
    nota = Column(Float)
    asistencia = Column(Boolean)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte],['cohorte.id_curso','cohorte.id_cohorte']),{})
    __table_args__ = (ForeignKeyConstraint([id_actividad, id_curso],['actividades.id_actividad','actividades.id_curso']),{})



Base.metadata.create_all(engine)
