__author__ = 'family'

from ORM.Curso import Curso
from ORM.Actividades import Actividades
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
from Modelo.Certificado import Certificado
from Modelo.LogicaCohorte import LogicaCohorte
class ControlCoordinador:
    logCohorte = LogicaCohorte()

    def __init__(self):
        #self.logCurso = LogicaCurso()
        self.logicaCursos = LogicaCursos()
        self.logicaMatricula = LogicaMatricula()
        self.logicaUsuario = LogicaUsuario()
        self.certificado= Certificado()


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

    def modificar_cohorte(self, id_curso,id_cohorte,fecha_inicio,fecha_fin):
        exito = self.logCohorte.modificar_cohorte(id_curso,id_cohorte,fecha_inicio,fecha_fin)
        return exito


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
        matriculas=self.logicaMatricula.consultar_cursos_estudiantes(cedula)
        return matriculas

    def descargaCertificado(self, ruta, nombre, cedula, nota, nomCurso):
        self.certificado.generaCertificado(ruta, nombre, cedula, nota, nomCurso)

    def buscarPersona(self, cedula):
        return self.logicaUsuario.buscarUsuario(cedula)

    def consultar_cursos (self):
        cursos = self.logicaCursos.consultarCursos()
        return cursos

    def cerrarSesion(self):
        self.logicaCursos.cerrarSesion()


'''
con =  ControlCoordinador()
#actividades = [["act1", 0.2], ["act2", 0.5], ["act3", 0.3]]
#con.crearCurso("curso 3", "descripcion curso 3", actividades)
curso = con.buscarCurso("curso 3")
print curso.actividades[1].nombre
con.cerrarSesion()
'''