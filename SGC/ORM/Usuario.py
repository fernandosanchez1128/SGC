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
    correo_electronico = Column(String(40), index=True, nullable=False, unique=True)
    contrasena = Column(String(40), index=True, nullable=False)
    fecha_nacimiento = Column(Date, index=True)
    fecha_ultimo_acceso = Column(Date, index=True)
    
    type = Column(String(50))



Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# user = Usuario (cedula  = 124, correo_electronico='c@ah.com', contrasena= 'c', type = 'coordinador')
#
# session.add(user)
# session.commit()
#
