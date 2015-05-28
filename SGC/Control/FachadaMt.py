from sqlalchemy.exc import *
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaDicta import LogicaDicta
from Modelo.LogicaActividades import LogicaActividades
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
from Modelo.LogicaNotas import  LogicaNotas
from ORM.Notas import Notas
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.LogicaAsignacion import LogicaAsignacion
from ORM.Asignacion import Asignacion
from PyQt4 import QtGui
import time


class FachadaMt():
    logCursos = LogicaCursos()
    logDicta = LogicaDicta()
    logActividades = LogicaActividades()
    logMatricula = LogicaMatricula()
    logUsuario = LogicaUsuario()
    logNotas  = LogicaNotas()
    logCohorte = LogicaCohorte()
    logAsignacion = LogicaAsignacion()

    def __init__(self):
        print "constructor"


    def consulta_cursos_prof(self, cedulaMt):
        # reemplazar por cedula MT
        fecha = time.strftime("%d/%m/%y")
        registros = self.logDicta.consultarCursosProf(cedulaMt,fecha)

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
            nota_ant = self.logNotas.consultarNota(id_actividad,cedula,id_curso,id_cohorte).nota
            self.logNotas.editarNotas(id_actividad,cedula,id_curso,id_cohorte,nota_ingresada,asistencia)
            self.actualizarDefinitiva(2,cedula,id_curso,id_cohorte,nota_ingresada,id_actividad,nota_ant)
        else :
            self.actualizarDefinitiva(1,cedula,id_curso,id_cohorte,nota_ingresada,id_actividad,0)

    def actualizarDefinitiva (self,caso,id_lt,id_curso,id_cohorte,nota_ingresada,id_actividad,nota_ant):
        reg_mat = self.logMatricula.consultarMatricula(id_lt,id_cohorte,id_curso)
        nota_def = reg_mat.nota_definitiva
        print "nota_antes" , nota_def
        actividad = self.logActividades.consultarActividad_codigo(id_actividad,id_curso)
        ponderado = actividad.ponderado
        if caso == 1:
            nota_def += nota_ingresada * ponderado
        else :
            print "paso por else"
            print nota_ant, nota_ingresada
            nota_def -= nota_ant * ponderado
            nota_def += nota_ingresada * ponderado
        print "nota_despues" , nota_def
        self.logMatricula.editar_nota(id_lt,id_cohorte,id_curso,nota_def)



    def consultar_cohorte (self,id_curso,id_cohorte):
        cohorte = self.logCohorte.consulta_cohorte(id_curso,id_cohorte)
        return cohorte

    def consular_asignacion (self,id_curso,id_cohorte,id_actividad):
        asignacion = self.logAsignacion.consulta_asignacion(id_curso,id_cohorte, id_actividad)
        return asignacion

    def agregar_entrega (self,id_curso,id_cohorte,id_actividad,fecha):
        asignacion = Asignacion(id_curso = id_curso,id_cohorte=id_cohorte,id_actividad = id_actividad,fecha_hora = fecha)
        exito = self.logAsignacion.agregar_asignacion(asignacion)
        if (exito ==0) :
            proc_exitoso = self.logAsignacion.editar_asignacion(id_curso,id_cohorte,id_actividad,fecha)
            print proc_exitoso
            if (proc_exitoso == 0 ):
                return 3
            else :
                return 2
        elif (exito == 2 ):
            return 4
        elif (exito == 3):
            return 5
        else:
            return 1



