from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from ORM.Curso import *
class LogicaActividades ():
	Session = sessionmaker(bind=engine)
	session = Session()

	def __init__ (self) :
		#llamado para prueba del iterador
		print ("contructorAct")

	def agregarActividades (self, actividades)	:
		self.session.add(actividades)
		self.session.commit()
		self.session.close ()

	def consultarActividades (self)	:
		actividades = self.session.query(Actividades).all()
		self.session.close()
		return actividades

	def consultarActividadesXCurso (self, id_curso_ac)	:
		actividades = self.session.query(Actividades).filter_by(id_curso= id_curso_ac).all()
		self.session.close()
		return actividades

	def editarActividades (self,  idActividad, newActividades):
		actividades = self.session.query(Actividades).filter_by(id_actividades= idActividad).first()
		actividades.nombre = newActividades.nombre
		actividades.id_curso = newActividades.id_curso
		actividades.ponderado = newActividades.ponderado
		self.session.commit()
		self.session.close ()

	def eliminarActividades (self,  idActividad):
		actividades = self.session.query(Actividades).filter_by(id_actividades= idActividad).first()
		self.session.delete(actividades)
		self.session.commit()
		self.session.close ()

	def eliminarActividadesXCurso (self,  idCurso_el):
		actividades = self.session.query(Actividades).filter_by(id_curso= idCurso_el).all()
		for actividad in actividades:
			self.session.delete(actividad)
			self.session.commit()
		self.session.close ()

'''
log = LogicaActividades()
actividades = Actividades(nombre="nom2", id_curso=122, ponderado=0.4)
log.agregarActividades(actividades)
ac = log.consultarActividades()[0]
print ac.curso
'''
