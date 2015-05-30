from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaActividades import LogicaActividades
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
from Modelo.LogicaNotas import  LogicaNotas
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.Certificado import Certificado

import time


class FachadaLt():
    logCursos = LogicaCursos()
    logActividades = LogicaActividades()
    logMatricula = LogicaMatricula()
    logUsuario = LogicaUsuario()
    logNotas  = LogicaNotas()
    logCohorte = LogicaCohorte()
    certificado= Certificado()

    def __init__(self):
        print "constructor"


    def consulta_cursos_estudiante(self, cedula_lt):
        # reemplazar por cedula LT
        registros = self.logMatricula.consultar_cursos_estudiantes(cedula_lt)
        return registros


    def consulta_curso(self, id_curso):
        curso = self.logCursos.consultarCurso_id(id_curso)
        return curso

    def consulta_curso_by_name(self, nombre_curso):
        curso = self.logCursos.consultarCurso(nombre_curso)
        return curso


    def cerrar_session_curso (self):
        self.logCursos.cerrarSesion()

    def actividades (self):
        actividades =self.logActividades.consultarActividades()
        return actividades

    def consultar_actividad (self,nombre,id_curso):
        actividad = self.logActividades.consultarActividad(nombre,id_curso)
        return actividad

    def registro_matricula (self, ncedula_lt, nid_cohorte, nid_curso):
        matricula = self.logMatricula.consultarMatricula(ncedula_lt,nid_cohorte,nid_curso)
        return matricula

    def consultar_nota (self,id_curso,id_actividad,cedula_lt,id_cohorte):
        nota = self.logNotas.consultarNota(id_actividad,cedula_lt,id_curso,id_cohorte)
        return nota

    def consultar_cohorte (self,id_curso,id_cohorte):
        cohorte = self.logCohorte.consulta_cohorte(id_curso,id_cohorte)
        return cohorte

    def consular_asignacion (self,id_curso,id_cohorte,id_actividad):
        asignacion = self.logAsignacion.consulta_asignacion(id_curso,id_cohorte, id_actividad)
        return asignacion

    def descargaCertificado(self, ruta, nombre, cedula, nota, nomCurso):
        self.certificado.generaCertificado(ruta, nombre, cedula, nota, nomCurso)

    def buscarPersona(self, cedula):
        return self.logUsuario.buscarUsuario(cedula)











