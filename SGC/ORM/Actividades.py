__author__ = 'family'
from sqlalchemy import (Float, Sequence,UniqueConstraint)

from basetest import *

Column(Integer, Sequence('sec_actividad'), primary_key=True)
class Actividades (Base):
    __tablename__ = 'actividades'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_actividad =  Column(Integer,Sequence('sec_actividad'), primary_key=True)
    nombre = Column(String (50))
    ponderado = Column(Float)
    __table_args__ = (UniqueConstraint('id_curso', 'nombre', name='unique_name'),)

    
Base.metadata.create_all(engine)

'''
Session = sessionmaker(bind=engine)
session = Session()
ac = Actividades (id_curso = 122, nombre = 2, ponderado = 0.2)

session.add(ac)
session.commit()

'''