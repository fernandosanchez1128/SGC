__author__ = 'cenesis'

from Usuario import Usuario

class MasterTeacher(Usuario):

    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento):
        self.setCedula(self, pa_cedula)
        self.setNombres(self, pa_nombres)
        self.setApellidos(self, pa_apellidos)
        self.setDireccion(self, pa_direccion)
        self.setTelefono(self, pa_telefono)
        self.setCorreoElectronico(self, pa_correoElectronico)
        self.setFechaNacimiento(self, pa_fechaNacimiento)