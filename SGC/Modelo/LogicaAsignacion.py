from sqlalchemy.exc import *
from ORM.Asignacion import Asignacion
from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from sqlalchemy import exceptions

class LogicaAsignacion():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("")

    def agregar_asignacion(self,asignacion):
        exito = 1
        paso_integrity_error = False;
        # self.session.add(asignacion)
        # self.session.commit()
        # self.session.close()
        try :
            self.session.add(asignacion)
            self.session.commit()
            self.session.close()
        except IntegrityError:
            paso_integrity_error = True
            print "violacion de integridad en la llave primaria"
            self.session.close()
            return 0

        except DataError:
            print "exception1"
            return 2
            self.session.close()

        except :
            return 3
            self.session.close()
        return exito




    def consulta_asignacion (self,id_curso,id_cohorte,id_actividad):
        asignacion = self.session.query(Asignacion).filter_by(id_curso=id_curso,id_cohorte = id_cohorte,id_actividad = id_actividad).first()
        self.session.close()
        return asignacion

    def editar_asignacion(self, id_curso,id_cohorte,id_actividad, new_fecha):
        exito =1
        try:
            asignacionEditada = self.session.query(Asignacion).filter_by(id_actividad=id_actividad,id_curso = id_curso,id_cohorte = id_cohorte).first()
            asignacionEditada.fecha_hora = new_fecha
            self.session.commit()
            self.session.close()
        except Exception :
            return 0
            self.session.close()

        return exito

