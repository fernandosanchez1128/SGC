__author__ = 'family'
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)

from basetest import *

class Usuario (Base):
    __tablename__ = 'usuario'

    cedula = Column(String(40), primary_key=True)
    nombres = Column(String(50), index=True)
    apellidos = Column(String(50), index=True)
    direccion = Column(String(40), index=True)
    telefono = Column(String(40), index=True)
    correo_electronico = Column(String(40), index=True, nullable=False)
    fecha_nacimiento = Column(Date, index=True)
    
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }

Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''
