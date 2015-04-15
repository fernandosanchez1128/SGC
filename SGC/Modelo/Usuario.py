__author__ = 'family'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
engine = create_engine('sqlite:///usuario.db', echo=True)
Base = declarative_base()


class Usuario (Base):
    __tablename__ = 'usuario'

    cedula = Column(String(40), primary_key=True)
    nombres = Column(String(50), index=True)
    apellidos = Column(String(50), index=True)
    direccion = Column(String(40), index=True)
    telefono = Column(String(40), index=True)
    correoElectronico = Column(String(40), index=True, nullable=False)
    fechaNacimiento = Column(Date, index=True)

    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento):
        self.cedula = pa_cedula
        self.nombres = pa_nombres
        self.apellidos = pa_apellidos
        self.direccion = pa_direccion
        self.telefono = pa_telefono
        self.correoElectronico = pa_correoElectronico
        self.fechaNacimiento = pa_fechaNacimiento


    def getCedula(self):
        return self.cedula

    def setCedula(self, pa_cedula):
        self.cedula = pa_cedula


    def getNombres(self):
        return self.nombres

    def setNombres(self, pa_nombres):
        self.nombres = pa_nombres


    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, pa_apellidos):
        self.apellidos = pa_apellidos


    def getDireccion(self):
        return self.direccion

    def setDireccion(self, pa_direccion):
        self.direccion = pa_direccion


    def getTelefono(self):
        return self.telefono

    def setTelefono(self, pa_telefono):
        self.telefono = pa_telefono


    def getCorreoElectronico(self):
        return self.correoElectronico

    def setCorreoElectronico(self, pa_correoElectronico):
        self.correoElectronico = pa_correoElectronico


    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def setFechaNacimiento(self, pa_fechaNacimiento):
        self.fechaNacimiento = pa_fechaNacimiento


Base.metadata.create_all(engine)
