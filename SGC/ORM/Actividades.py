__author__ = 'family'
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from basetest import *
Column(Integer, Sequence('sec_actividad'), primary_key=True)
class Cohorte (Base):
    __tablename__ = 'asignacion'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_actividad =  Column(Integer,Sequence('sec_actividad'), primary_key=True)
    nombre = Column(String (20), unique = True)
    ponderado = Column(Float)
    curso = relationship("Curso")
    
Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''

