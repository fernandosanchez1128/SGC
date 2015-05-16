from sqlalchemy.orm import sessionmaker

from basetest import *
#from Notas import Notas


class LogicaNotas():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorNotas")

    def agregarNotas(self, notas):
        self.session.add(notas)
        self.session.commit()
        self.session.close()

    def consultarNota(self, actividad, idLT,id_curso,id_cohorte):
        notas = self.session.query(Notas).filter_by(id_actividades=actividad, cedula_lt=idLT,id_curso = id_curso,id_cohorte = id_cohorte).first()
        self.session.close()
        return notas

    def editarNotas(self, idActividad, idLT, newNota):
        notaEditada = self.session.query(Notas).filter_by(id_actividades=idActividad, cedula_lt=idLT).first()
        notaEditada.nota = newNota.nota
        notaEditada.asistencia = newNota.asistencia
        self.session.commit()
        self.session.close()

    def eliminarNotas(self, idActividad, idLT):
        notas = self.session.query(Notas).filter_by(id_actividades=idActividad, cedula_lt=idLT).first()
        self.session.delete(notas)
        self.session.commit()
        self.session.close()
