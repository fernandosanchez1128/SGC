from sqlalchemy.orm import sessionmaker


from basetest import *
from ORM.Notas import Notas


class LogicaNotas():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorNotas")

    def agregarNotas(self, notas):
        exito = True
        try:
            self.session.add(notas)
            self.session.commit()
            self.session.close()
        except Exception:
            exito = False
            self.session.close()
        return exito



    def consultarNota(self, actividad, idLT,id_curso,id_cohorte):
        notas = self.session.query(Notas).filter_by(id_actividad=actividad, cedula_lt=idLT,id_curso = id_curso,id_cohorte = id_cohorte).first()
        self.session.close()
        return notas

    def editarNotas(self, idActividad, idLT,id_curso, id_cohorte, newNota,asistencia):
        notaEditada = self.session.query(Notas).filter_by(id_actividad=idActividad, cedula_lt=idLT,id_curso = id_curso,id_cohorte = id_cohorte).first()
        notaEditada.nota = newNota
        notaEditada.asistencia = asistencia
        self.session.commit()
        self.session.close()

    def eliminarNotas(self, idActividad, idLT):
        notas = self.session.query(Notas).filter_by(id_actividad=idActividad, cedula_lt=idLT).first()
        self.session.delete(notas)
        self.session.commit()
        self.session.close()
