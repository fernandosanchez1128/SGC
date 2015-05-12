from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaDicta import LogicaDicta
from Modelo.LogicaActividades import LogicaActividades
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
class FachadaMt ():
	
	logCursos = LogicaCursos ()
	logDicta = LogicaDicta()
	logActividades = LogicaActividades()
	logMatricula = LogicaMatricula()
	logUsuario = LogUsuario()
	def __init__ (self) :
		print "constructor"
		

	def consulta_cursos_prof (self, cedulaMt)	:
		#reemplazar por cedula MT
		registros = self.logDicta.consultarCursosProf("1")
		return registros
	
		
	def consulta_curso (self,id_curso)	:
		curso = self.logCursos.consultarCurso(id_curso)
		return curso
		
	def consulta_curso_by_name (self,nombre_curso)	:
		curso = self.logCursos.consulta_by_name(nombre_curso)
		return curso
		
		
	def actividades_curso (self,id_curso)	:
		actividades = self.logActividades.actividades_curso(id_curso)
		return actividades;
	
	
	def estudiantes_curso (self,id_curso,id_cohorte):
		regsMatricula =self.logMatricula.consultar_estudiantes(id_curso,id_cohorte)
		estudiantes = []
		for reg in regsMatricula :
			estudiante = self.logUsuario.buscarUsuario(reg.cedula_lt)
			estudiantes.append(estudiante)
		return estudiantes	
		
				

	
	
	
	
