__author__ = 'family'

from Modelo import Curso

class ControlCoordinador:

    def __init__(self):
        #self.logCurso = LogicaCurso()
        return None

    def crearCurso(self, nombre, descripcion):
        curso = Curso(nombre, descripcion)

    #si tipo es 1 el criterio es el codigo del curso, si es 2 el criterio es el nombre
    def consultarCurso(self, criterio, tipo):
        respuesta = ["nombre", "descripcion"]
        return respuesta

    #si tipo es 1 el criterio es el codigo del curso, si es 2 el criterio es el nombre
    def modificarCurso(self, criterio, tipo, descripcion):
        #modificacion de descripcion
        return None
