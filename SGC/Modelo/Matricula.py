from Observable import *

class Matricula (object, observable):
	
	id_lt = ""
	id_curso = ""
	nota_definitiva = 0
	
	def __init__ (self,curso,actividad,lt,nota) :
		self.id_curso = id_curso
		self.id_lt = id_lt
		self.nota_definitiva  = 0
		
	def update 	(self,observable):
		#actualizacion
		nota = observable.getNota();
		#consulta peso de la actividad
		modificarNotaDef (peso_actividad,nota)
		
		
	def modificarNotaDef (self,peso_actividad,nota) :
		#objMatricula = consulta en la matricula
		#objMatricula.nota_definitiva = nota_definitiva + nota * peso_actividad
		
		
			 

