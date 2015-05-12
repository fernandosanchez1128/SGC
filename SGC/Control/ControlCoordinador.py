__author__ = 'family'

from ORM.Curso import Curso
from ORM.Actividades import Actividades
from Modelo.LogicaCursos import LogicaCursos

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
        curso = Curso(nombre= nombre, descripcion=descripcion, actividades = obj_actividades)
        self.logicaCursos.agregarCurso(curso)

    def modificarCurso(self, nombre_c, descripcion_c, actividades):
        curso = Curso(nombre= nombre_c, descripcion=str(self.ui.teDescripcion.toPlainText()))
        self.logicaCursos.modificarCurso(nombre_c, curso)
        i=0
        curso = self.logicaCursos.consultarCurso(nombre_c)
        self.logicaActividades.eliminarActividadesXCurso(curso.id)
        while i<self.ui.sbNumActividades.value():
            nombre_ac = str(self.ui.twActividades.item(i, 0).text())
            ponderado_ac = float(self.ui.twActividades.item(i, 1).text())
            actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac, id_curso =curso.id )
            self.logicaActividades.agregarActividades(actividad)
            i+=1


con =  ControlCoordinador()
actividades = [["act1", 0.2], ["act2", 0.5]]
con.crearCurso("curso 1", "descripcion curso 1", actividades)