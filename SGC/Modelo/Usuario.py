__author__ = 'family'

class Usuario:
    _cedula = ""
    _nombres = ""
    _apellidos = ""
    _direccion = ""
    _telefono = ""
    _correoElectronico = ""
    _fechaNacimiento = ""

    def __init__(self, pa_cedula, pa_nombres, pa_apellidos, pa_direccion, pa_telefono, pa_correoElectronico, pa_fechaNacimiento):
        self._cedula = pa_cedula
        self._nombres = pa_nombres
        self._apellidos = pa_apellidos
        self._direccion = pa_direccion
        self._telefono = pa_telefono
        self._correoElectronico = pa_correoElectronico
        self._fechaNacimiento = pa_fechaNacimiento


    def getCedula(self):
        return self._cedula

    def setCedula(self, pa_cedula):
        self._cedula = pa_cedula


    def getNombres(self):
        return self._nombres

    def setNombres(self, pa_nombres):
        self._nombres = pa_nombres


    def getApellidos(self):
        return self._apellidos

    def setApellidos(self, pa_apellidos):
        self._apellidos = pa_apellidos


    def getDireccion(self):
        return self._direccion

    def setDireccion(self, pa_direccion):
        self._direccion = pa_direccion


    def getTelefono(self):
        return self._telefono

    def setTelefono(self, pa_telefono):
        self._telefono = pa_telefono


    def getCorreoElectronico(self):
        return self._correoElectronico

    def setCorreoElectronico(self, pa_correoElectronico):
        self._correoElectronico = pa_correoElectronico


    def getFechaNacimiento(self):
        return self._fechaNacimiento

    def setFechaNacimiento(self, pa_fechaNacimiento):
        self._fechaNacimiento = pa_fechaNacimiento;



usuario = Usuario("123","B", "R", "Cra 2", "323", "a@aol.com", "Dic 13")
print usuario._apellidos