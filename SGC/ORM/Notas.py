from sqlalchemy import (Boolean, Float, ForeignKeyConstraint)
from basetest import *
from sqlalchemy import UniqueConstraint

class Notas(Base):
    __tablename__ = 'notas'
    cedula_lt = Column(String(40),  primary_key=True)
    id_actividades = Column(Integer, primary_key=True)
    id_curso = Column(Integer)
    ForeignKeyConstraint(['cedula_lt', 'id_actividades','id_curso'], ['leaderteacher.cedula', 'actividades.id_actividades','actividades.id_curso'])
    nota = Column(Float)
    asistencia = Column(Boolean)



Base.metadata.create_all(engine)
