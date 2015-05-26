__author__ = 'family'

from ORM.Curso import Curso
from ORM.Actividades import Actividades
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaMasterTeacher import LogicaMasterTeacher
from Modelo.LogicaLeaderTeacher import LogicaLeaderTeacher
from Modelo.LogicaDicta import LogicaDicta

from Modelo.LogicaUsuario import LogicaUsuario
from Modelo.Certificado import Certificado
from Modelo.LogicaCohorte import LogicaCohorte
from Modelo.Reporte import Reporte


class ControlCoordinador:
    logCohorte = LogicaCohorte()
    reporte = Reporte()

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
        curso = Curso(nombre= nombre, descripcion=descripcion, actividades = obj_actividades)
        self.logicaCursos.agregarCurso(curso)

    def modificarCurso(self, nombre_c, descripcion_c, actividades):
        obj_actividades = []
        for actividad in actividades:
            nombre_ac = actividad[0]
            ponderado_ac = actividad[1]
            obj_actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac)
            obj_actividades.append(obj_actividad)
        curso = Curso(nombre= nombre_c, descripcion=descripcion_c, actividades = obj_actividades)
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

    def procesarMatriculados(self, ruta_ar, ano, semestre):
        with open(ruta_ar) as f:
            content = f.readlines()
        print content[0][7:-1]
        curso = content[0][7:-1]
        id_curso = self.logicaCursos.consultarCurso(curso).id
        for cont in content:
            if cont[:7]=="Curso: ":
                curso = cont[7:-1]
                id_curso = self.logicaCursos.consultarCurso(curso).id
            else:
                logMat  = LogicaMatricula()
                logMat.agregarMatricula(cont[:-1],id_curso,ano,semestre)

    def consultarMT(self, cedula):
        log_m = LogicaMasterTeacher()
        mt = log_m.consultarMT(cedula)
        return mt

    def consultarLT(self, cedula):
        log_l = LogicaLeaderTeacher()
        return log_l.consultarLT(cedula)

    def agregarDicta(self, cedula_mt, id_curso, id_cohorte):
        log_d = LogicaDicta()
        log_d.agregarDicta(cedula_mt,id_curso,id_cohorte)

    def consultarCohorteN(self, id_curso, ano, semestre, N):
        cohorte  = self.logCohorte.cohorteN(id_curso, ano, semestre, N)
        return cohorte

    def consultarNumCohortes(self, id_curso, ano, semestre):
        cohortes = self.logCohorte.numCohortes(id_curso,ano, semestre)
        return cohortes

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

    def consultar_est_mat(self, id_curso, id_cohorte):
        return self.logicaMatricula.consultar_estudiantes(id_curso,id_cohorte)

    def anular_matricula(self, cedula, id_curso):
        coh= self.logicaMatricula.consultar_cohorte_estudiante(cedula,id_curso)
        self.logicaMatricula.eliminarMatricula(cedula,coh.id_cohorte, id_curso)

    def mat_lt_curso(self, cedula, id_curso):
        coh= self.logicaMatricula.consultar_cohorte_estudiante(cedula,id_curso)
        return coh

    def estudiantes_aprobados_curso (self,ruta,fecha_ini,fecha_fin,id_curso,nombre_curso,mes,anio):
        exito =1
        reporte = self.logicaMatricula.estudiantes_aprobados_curso(fecha_ini,fecha_fin,id_curso)
        if reporte !=[] :
            self.reporte.estudiants_aprob_curso(reporte,ruta,nombre_curso,mes,anio)
        else:
            exito =0
        return exito

    def estudiantes_departamento_unique (self,fecha_ini,fecha_fin,id_curso,dpto,nombre_curso,mes,anio):
        reporte =self.logicaMatricula.estudianes_departamento_unique(fecha_ini,fecha_fin,id_curso,dpto)
        print reporte
        if reporte != None:
            self.reporte.detalle_estudiantes_por_dpto(reporte, "/home/fernando/report.pdf",nombre_curso,mes,anio)

    def estudiantes_departamento (self,ruta,fecha_ini,fecha_fin,id_curso,nombre_curso,mes,anio):
        exito =1
        reporte =self.logicaMatricula.estudiantes_departamento(fecha_ini,fecha_fin,id_curso)
        print reporte
        if reporte != []:
            promedios = self.logicaMatricula.promedio_departamento(fecha_ini,fecha_fin,id_curso)
            self.reporte.detalle_estudiantes_por_dpto(reporte,promedios,ruta,nombre_curso,mes,anio)
        else:
            exito =0

        return exito


    def cerrarSesion(self):
        self.logicaCursos.cerrarSesion()

#ControlCoordinador().estudiantes_departamento("2015/05/01","2015/05/30",1,"curso1","Mayo", "2015")
#ControlCoordinador().estudiantes_departamento_unique("2015/05/01","2015/05/30",1,"antioquia","curso1","Mayo", "2015")
#ControlCoordinador().estudiantes_aprobados_curso("2015/05/01","2015/05/30",1,"curso1","Mayo", "2015")
'''
con =  ControlCoordinador()
#actividades = [["act1", 0.2], ["act2", 0.5], ["act3", 0.3]]
#con.crearCurso("curso 3", "descripcion curso 3", actividades)
curso = con.buscarCurso("curso 3")
print curso.actividades[1].nombre
con.cerrarSesion()
'''