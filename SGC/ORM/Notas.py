from sqlalchemy import (Boolean, Float, ForeignKeyConstraint)
from basetest import *


class Notas(Base):
    __tablename__ = 'notas'
    cedula_lt = Column(String(40), ForeignKey('leaderteacher.cedula'), primary_key=True)
    id_actividades = Column(Integer, ForeignKey('actividades.id_actividades'), primary_key=True)
    ForeignKeyConstraint(['cedula_lt', 'id_actividades'], ['leaderteacher.cedula', 'actividades.id_actividades'])
    nota = Column(Float)
    asistencia = Column(Boolean)


Base.metadata.create_all(engine)
