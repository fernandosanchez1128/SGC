__author__ = 'cenesis'

from Usuario import Usuario

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('sqlite://usuario.db', echo=True)
Base = declarative_base()

class LeaderTeacher(Usuario):
    __tablename__ = 'leaderteacher'

    __cedula = Column(Integer, ForeignKey('usuario.__cedula'), primary_key=True)
    __sede = Column(String(40))
    __institucion = ""
    __codigoInstitucion = ""
    __grado = 0
    __departamentoSecretaria= ""
    __municipioSecretaria = ""
    __tutorProgramaPTA = False
    __usuarioColombiaAprende = False
    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento, pa_sede, pa_institucion, pa_codigoInstitucion, pa_grado, pa_departamentoSecretaria, pa_municipioSecretaria, pa_tutorProgramaPTA, pa_usuarioColombiaAprende):
        self.setCedula(self, pa_cedula)
        self.setNombres(self, pa_nombres)
        self.setApellidos(self, pa_apellidos)
        self.setDireccion(self, pa_direccion)
        self.setTelefono(self, pa_telefono)
        self.setCorreoElectronico(self, pa_correoElectronico)
        self.setFechaNacimiento(self, pa_fechaNacimiento)
        self.__sede = pa_sede
        self.__institucion = pa_institucion
        self.__codigoInstitucion = pa_codigoInstitucion
        self.__grado = pa_grado
        self.__departamentoSecretaria= pa_departamentoSecretaria
        self.__municipioSecretaria = pa_municipioSecretaria
        self.__tutorProgramaPTA = pa_tutorProgramaPTA
        self.__usuarioColombiaAprende = pa_usuarioColombiaAprende



