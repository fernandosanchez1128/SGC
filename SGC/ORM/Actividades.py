__author__ = 'family'
from sqlalchemy import (Float, Sequence,UniqueConstraint)

from basetest import *

Column(Integer, Sequence('sec_actividad'), primary_key=True)
class Actividades (Base):
    __tablename__ = 'actividades'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_actividad =  Column(Integer,Sequence('sec_actividad'), primary_key=True)
    nombre = Column(String (20))
    ponderado = Column(Float)
    __table_args__ = (UniqueConstraint('id_curso', 'nombre', name='unique_name'),)

    
Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''

