__author__ = 'family'

from ORM.Curso import Curso
from ORM.Actividades import Actividades
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.LogicaMatricula import LogicaMatricula

class ControlCoordinador:

    def __init__(self):
        #self.logCurso = LogicaCurso()
        self.logicaCursos = LogicaCursos()

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

    def numeroCohortes(self,id_curso):
        num = len(self.logicaCursos.consultarCurso_id(id_curso).cohortes)
        return num

    def procesarMatriculados(self, ruta_ar, ano, semestre):
        with open(ruta_ar) as f:
            content = f.readlines()
        print content[0][7:-1]
        curso = content[0][7:-1]
        id_curso = self.logicaCursos.consultarCurso(curso).id
        for cont in content:
            print "CUROSOO", cont[:7]
            if cont[:7]=="Curso: ":
                curso = cont[7:-1]
                id_curso = self.logicaCursos.consultarCurso(curso).id
            else:
                logMat  = LogicaMatricula()
                logMat.agregarMatricula(cont[:-1],id_curso,ano,semestre)

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