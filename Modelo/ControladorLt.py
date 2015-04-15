from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Curso import *
from Cursos import *
class ControladorLt ():
	
	
	def __init__ (self) :
		#llamado para prueba del iterador 
		print ("contructor")

		
		
	def consulta_cursos_lt (self)	:
		
		#engine = create_engine('mysql://fersanq:@localhost/test', echo=True)
		engine = create_engine('sqlite:///cursos.db', echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		
		curso1 = Curso ('curso3', 'd3')
		curso2 = Curso ('curso4', 'd4')
		cursos = [curso1,curso2]
		#caso de insercion 
		#session.add_all(cursos)
		#session.commit()
		#caso con una consulta
		#cursos = Cursos (session.query(Curso).filter(Curso.id>1).all()).iterator()
		#cursos = Cursos (session.query(Curso).filter(Curso.id>1).all()).iterator()
		cursos = Cursos ([curso1,curso2]).iterator()
		while (cursos.hasNext()) :
			print cursos.next().nombre
				
		session.close()	

	
	
	
	
