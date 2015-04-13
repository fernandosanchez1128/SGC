__author__ = 'cenesis'

from Usuario import Usuario

class LeaderTeacher(Usuario):
    sede = ""
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
