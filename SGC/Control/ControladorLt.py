from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Curso import *
from LogicaCursos import *
from Cursos import *
class ControladorLt ():
	
	logCursos = LogicaCursos ()
	def __init__ (self) :
		print "constructor"
		

	def agregarCurso (self)	:
		curso1 = Curso ('curso1', 'd1')
		self.logCursos.agregarCurso (curso1)
		curso2 = Curso ('curso2', 'd2')
		self.logCursos.agregarCurso (curso2)
	
		
	def consulta_cursos_lt (self)	:
		
		cursos = self.logCursos.consultarCursos()
		cursos_iterator = Cursos (cursos).iterator();
		
		while (cursos_iterator.hasNext()) :
			print cursos_iterator.next().nombre
	
			
	#~ def main ():
	#~ if __name__=="__main__":
		#~ main()			
		
		
				

	
	
	
	
