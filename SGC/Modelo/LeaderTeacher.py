__author__ = 'cenesis'

from Usuario import Usuario

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
engine = create_engine('sqlite:///leaderteacher.db', echo=True)
Base = declarative_base()

class LeaderTeacher(Base, Usuario):
    __tablename__ = 'leaderteacher'

    cedula = Column(Integer, ForeignKey('usuario.cedula'), primary_key=True)
    sede = Column(String(40))
    institucion = ""
    codigoInstitucion = ""
    grado = 0
    departamentoSecretaria= ""
    municipioSecretaria = ""
    tutorProgramaPTA = False
    usuarioColombiaAprende = False
    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento, pa_sede, pa_institucion, pa_codigoInstitucion, pa_grado, pa_departamentoSecretaria, pa_municipioSecretaria, pa_tutorProgramaPTA, pa_usuarioColombiaAprende):
        self.setCedula(self, pa_cedula)
        self.setNombres(self, pa_nombres)
        self.setApellidos(self, pa_apellidos)
        self.setDireccion(self, pa_direccion)
        self.setTelefono(self, pa_telefono)
        self.setCorreoElectronico(self, pa_correoElectronico)
        self.setFechaNacimiento(self, pa_fechaNacimiento)
        self.sede = pa_sede
        self.institucion = pa_institucion
        self.codigoInstitucion = pa_codigoInstitucion
        self.grado = pa_grado
        self.departamentoSecretaria= pa_departamentoSecretaria
        self.municipioSecretaria = pa_municipioSecretaria
        self.tutorProgramaPTA = pa_tutorProgramaPTA
        self.usuarioColombiaAprende = pa_usuarioColombiaAprende



