__author__ = 'nelson'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,ForeignKeyConstraint, String, Table,Sequence, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from basetest import *

class Aspirante(Base):
    __tablename__ = 'aspirante'
    cedula = Column(String(20), primary_key=True)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    direccion = Column(String(40))
    telefono = Column(String(40))
    correo_electronico = Column(String(40), nullable=False)
    fecha_nacimiento = Column(Date)
    municipio = Column(String(40))
    genero = Column(String(10))
    institucion = Column(String(50))
    escalafon = Column(String(40)   )
    sede = Column(String(40))
    codigo_dane = Column(String(20))
    dpto_secretaria  = Column(String(20))
    tutor = Column(Boolean)
    usuario_col_aprende = Column(Boolean)
    #id_curso = Column(Integer)
    #ForeignKeyConstraint(['id_curso'],['curso.id'])

from Preinscripcion import Preinscripcion
    
Base.metadata.create_all(engine)
