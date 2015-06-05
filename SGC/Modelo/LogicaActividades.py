from sqlalchemy.orm import sessionmaker

from ORM.Actividades import *
from ORM.basetest import *


class LogicaActividades():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorAct")

    def agregarActividades(self, actividades):
        self.session.rollback()
        self.session.add(actividades)
        self.session.commit()
        self.session.close()

    def consultarActividades(self):
        self.session.rollback()
        actividades = self.session.query(Actividades).all()
        return actividades

    def consultarActividadesXCurso(self, id_curso_ac):
        self.session.rollback()
        actividades = self.session.query(Actividades).filter_by(id_curso=id_curso_ac).all()
        self.session.close()
        return actividades

    def consultarCursos(self):
        self.session.rollback()
        actividades = self.session.query(Actividades).all()
        #self.session.close()
        return actividades

    def consultarActividad (self,nombre,id_curso):
        self.session.rollback()
        actividad = self.session.query(Actividades).filter_by(nombre = nombre , id_curso = id_curso).first()
        self.session.close()
        return actividad
    def consultarActividad_codigo (self,id_actividad,id_curso):
        self.session.rollback()
        actividad = self.session.query(Actividades).filter_by(id_actividad = id_actividad, id_curso = id_curso).first()
        self.session.close()
        return actividad

    def editarActividades(self, idActividad, newActividades):
        self.session.rollback()
        actividades = self.session.query(Actividades).filter_by(id_actividades=idActividad).first()
        actividades.nombre = newActividades.nombre
        actividades.id_curso = newActividades.id_curso
        actividades.ponderado = newActividades.ponderado
        self.session.commit()
        self.session.close()

    def eliminarActividades(self, idActividad):
        self.session.rollback()
        actividades = self.session.query(Actividades).filter_by(id_actividades=idActividad).first()
        self.session.delete(actividades)
        self.session.commit()
        self.session.close()

    def eliminarActividadesXCurso(self, idCurso_el):
        self.session.rollback()
        actividades = self.session.query(Actividades).filter_by(id_curso=idCurso_el).all()
        for actividad in actividades:
            self.session.delete(actividad)
            self.session.commit()
        self.session.close()
#BRAYAN
    def actividades_curso(self, id_curso):
        self.session.rollback()
        actividades = self.session.query(Actividades).filter_by(id_curso=id_curso).all()
        #self.session.close()
        return actividades


# #
# log = LogicaActividades()
# # actividades = Actividades(nombre="nom3", id_curso=1, ponderado=0.4)
# # log.agregarActividades(actividades)
# log.actividades_curso(1)

