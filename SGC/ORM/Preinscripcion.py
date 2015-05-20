from sqlalchemy import (String, Date, Integer, ForeignKeyConstraint)
from basetest import *
from Curso import Curso
class Preinscripcion(Base):
    __tablename__ = 'preinscripcion'
    cedula_asp = Column(String(40),ForeignKey ('aspirante.cedula'), primary_key=True)
    id_curso = Column(Integer, primary_key=True)
    fecha = Column(Date,primary_key= True)
    __table_args__ = (ForeignKeyConstraint([id_curso],['curso.id']), {})
    #ForeignKeyConstraint(['id_curso'],['curso.id'])

Base.metadata.create_all(engine)