__author__ = 'cenesis'

from Usuario import Usuario

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('sqlite:///masterteacher.db', echo=True)
Base = declarative_base()

class MasterTeacher(Base, Usuario):
    __tablename__ = 'masterteacher'

    __cedula = Column(Integer, ForeignKey('usuario._Usuario__cedula'), primary_key=True)

    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento):
        self.setCedula(pa_cedula)
        self.setNombres(pa_nombres)
        self.setApellidos(pa_apellidos)
        self.setDireccion(pa_direccion)
        self.setTelefono(pa_telefono)
        self.setCorreoElectronico(pa_correoElectronico)
        self.setFechaNacimiento(pa_fechaNacimiento)


Base.metadata.create_all(engine)

#mt = MasterTeacher("123","B", "R", "Cra 2", "323", "a@aol.com", "Dic 13")