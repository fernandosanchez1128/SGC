from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaDicta import LogicaDicta
from Modelo.LogicaActividades import LogicaActividades
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
from Modelo.LogicaNotas import  LogicaNotas
from ORM.Notas import Notas


class FachadaMt():
    logCursos = LogicaCursos()
    logDicta = LogicaDicta()
    logActividades = LogicaActividades()
    logMatricula = LogicaMatricula()
    logUsuario = LogicaUsuario()
    logNotas  = LogicaNotas()

    def __init__(self):
        print "constructor"


    def consulta_cursos_prof(self, cedulaMt):
        # reemplazar por cedula MT
        registros = self.logDicta.consultarCursosProf("1")
        return registros


    def consulta_curso(self, id_curso):
        curso = self.logCursos.consultarCurso_id(id_curso)
        return curso

    def consulta_curso_by_name(self, nombre_curso):
        curso = self.logCursos.consultarCurso(nombre_curso)
        return curso


    def actividades_curso(self, id_curso):
        actividades = self.logActividades.actividades_curso(id_curso)
        return actividades;


    def estudiantes_curso(self, id_curso, id_cohorte):
        regsMatricula = self.logMatricula.consultar_estudiantes(id_curso, id_cohorte)
        estudiantes = []
        for reg in regsMatricula:
            estudiante = self.logUsuario.buscarUsuario(reg.cedula_lt)
            estudiantes.append(estudiante)
        return estudiantes

    def cerrar_session_curso (self):
        self.logCursos.cerrarSesion()

    def actividades (self):
        actividades =self.logActividades.consultarActividades()
        return actividades

    def consultar_actividad (self,nombre,id_curso):
        actividad = self.logActividades.consultarActividad(nombre,id_curso)
        return actividad

    def consultar_nota (self,id_curso,id_actividad,cedula_lt,id_cohorte):
        nota = self.logNotas.consultarNota(id_actividad,cedula_lt,id_curso,id_cohorte)
        return nota

    def guardar_nota (self,id_actividad,id_curso,id_cohorte,cedula,nota_ingresada,asistencia):
        nota = Notas (id_curso = id_curso, id_actividad = id_actividad,id_cohorte = id_cohorte,cedula_lt =cedula,nota = nota_ingresada,asistencia = asistencia)
        exito = self.logNotas.agregarNotas(nota)
        if (exito == False):
            self.logNotas.editarNotas(id_actividad,cedula,id_curso,id_cohorte,nota_ingresada,asistencia)


