from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Curso import *

from basetest import *
class LogicaCursos ():
	#def __init__ (self) :
	Session = sessionmaker(bind=engine)
	session = Session()
	def __init__ (self) :
		#llamado para prueba del iterador 
		print ("contructor2")
		
	def agregarCurso (self, curso)	:
		self.session.add(curso)
		self.session.commit()
		self.session.close ()
		
	def consultarCursos (self)	:
		cursos = self.session.query(Curso).all()	
		self.session.close()	
		return cursos
		
	def consultarCurso(self, id_curso_mod):
		curso = self.session.query(Curso).filter_by(id_curso= id_curso_mod).first()
		self.session.close()	
		return curso
		
	def modificarCurso (self, id_curso_mod, curso_mod):
		curso = self.session.query(Curso).filter_by(id_curso= id_curso_mod).first()
		curso.nombre= curso_mod.nombre
		curso.descripcion= curso_mod.descripcion
		self.session.commit()
		self.session.close ()
		
	def eliminarCurso (self, id_curso_el):
		curso = self.session.query(Curso).filter_by(id_curso= id_curso_el).first()
		self.session.delete(curso)
		self.session.commit()
		self.session.close ()
		
'''
log = LogicaCursos()
curso = Curso(id_curso = 123, nombre= 'miocursomodificado', descripcion='descripcion')
log.agregarCurso(curso)
#cursos= log.consultarCursos()
#print cursos[0].nombre
'''
