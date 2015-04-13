__author__ = 'family'

class Usuario:
    __cedula = ""
    __nombres = ""
    __apellidos = ""
    __direccion = ""
    __telefono = ""
    __correoElectronico = ""
    __fechaNacimiento = ""

    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento):
        self.__cedula = pa_cedula
        self.__nombres = pa_nombres
        self.__apellidos = pa_apellidos
        self.__direccion = pa_direccion
        self.__telefono = pa_telefono
        self.__correoElectronico = pa_correoElectronico
        self.__fechaNacimiento = pa_fechaNacimiento


    def getCedula(self):
        return self.__cedula

    def setCedula(self, pa_cedula):
        self.__cedula = pa_cedula


    def getNombres(self):
        return self.__nombres

    def setNombres(self, pa_nombres):
        self.__nombres = pa_nombres


    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, pa_apellidos):
        self.__apellidos = pa_apellidos


    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, pa_direccion):
        self.__direccion = pa_direccion


    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, pa_telefono):
        self.__telefono = pa_telefono


    def getCorreoElectronico(self):
        return self.__correoElectronico

    def setCorreoElectronico(self, pa_correoElectronico):
        self.__correoElectronico = pa_correoElectronico


    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def setFechaNacimiento(self, pa_fechaNacimiento):
        self.__fechaNacimiento = pa_fechaNacimiento;



usuario = Usuario("123","B", "R", "Cra 2", "323", "a@aol.com", "Dic 13")
print usuario.getCedula()