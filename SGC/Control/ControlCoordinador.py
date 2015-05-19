__author__ = 'family'

from ORM.Curso import Curso
from ORM.Actividades import Actividades
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.Certificado import Certificado
from Modelo.LogicaUsuario import LogicaUsuario


class ControlCoordinador:

    def __init__(self):
        #self.logCurso = LogicaCurso()
        self.logicaCursos = LogicaCursos()
        self.logicaMatricula = LogicaMatricula()
        self.logicaUsuario=LogicaUsuario()
        self.certificado=Certificado()

    def crearCurso(self, nombre, descripcion, actividades):
        obj_actividades = []
        for actividad in actividades:
            nombre_ac = actividad[0]
            ponderado_ac = actividad[1]
            obj_actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac)
            obj_actividades.append(obj_actividad)
        curso = Curso(nombre= nombre, descripcion=descripcion, actividades = obj_actividades, cohortes = [])
        self.logicaCursos.agregarCurso(curso)

    def modificarCurso(self, nombre_c, descripcion_c, actividades):
        obj_actividades = []
        for actividad in actividades:
            nombre_ac = actividad[0]
            ponderado_ac = actividad[1]
            obj_actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac)
            obj_actividades.append(obj_actividad)
        curso = Curso(nombre= nombre_c, descripcion=descripcion_c, actividades = obj_actividades, cohortes = [])
        self.logicaCursos.modificarCursoActividades(nombre_c,curso)

    def eliminarCurso(self, nombre):
        self.logicaCursos.eliminarCurso(nombre)

    def buscarCurso(self, nombre):
        return self.logicaCursos.consultarCurso(nombre)

    def buscarCursoId(self, id_curso):
        return self.logicaCursos.consultarCurso_id(id_curso)

    def numeroCohortes(self,id_curso):
        num = len(self.logicaCursos.consultarCurso_id(id_curso).cohortes)
        return num

    def cursosEstudiantes(self, cedula):
        cursos=self.logicaMatricula.consultar_cursos_estudiantes(cedula)
        return cursos

    def cerrarSesion(self):
        self.logicaCursos.cerrarSesion()

    def descargaCertificado(self, ruta, nombre, cedula, nota, nombreCurso):
        self.certificado.generaCertificado(ruta, nombre, cedula, nota, nombreCurso)

    def buscarPersona(self, cedula):
        persona=self.logicaUsuario.buscarUsuario(cedula)
        return persona



'''
con =  ControlCoordinador()
#actividades = [["act1", 0.2], ["act2", 0.5], ["act3", 0.3]]
#con.crearCurso("curso 3", "descripcion curso 3", actividades)
curso = con.buscarCurso("curso 3")
print curso.actividades[1].nombre
con.cerrarSesion()
'''