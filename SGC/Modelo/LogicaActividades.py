from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Curso import Curso
from ORM.Actividades import Actividades
from ORM.basetest import *
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

    def consultarCursos (self)	:
        actividades = self.session.query(Actividades).all()
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

    def actividades_curso (self,id_curso):
        actividades = self.session.query(Actividades).filter_by(id_curso = id_curso).all()
        self.session.close()
        return actividades


# #
# log = LogicaActividades()
# # actividades = Actividades(nombre="nom3", id_curso=1, ponderado=0.4)
# # log.agregarActividades(actividades)
# log.actividades_curso(1)

