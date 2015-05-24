from ORM.Asignacion import Asignacion
from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from psycopg2 import IntegrityError,Error,NotSupportedError,extensions,Warning

class LogicaAsignacion():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("")

    def agregar_asignacion(self,asignacion):
        exito = 1
        paso_integrity_error = False;
        try:
            self.session.add(asignacion)
            self.session.commit()
            self.session.close()
        # except psycopg2.IntegrityError:
        #     paso_integrity_error = True
        #     print "integridad"
        #     exito = 0
        #     self.session.close()
        except Exception:
            print "excepcion"
            if (paso_integrity_error == False):
                exito = 0
            self.session.close()
        return exito




    def consulta_asignacion (self,id_curso,id_cohorte,id_actividad):
        asignacion = self.session.query(Asignacion).filter_by(id_curso=id_curso,id_cohorte = id_cohorte,id_actividad = id_actividad).first()
        self.session.close()
        return asignacion

    def editar_asignacion(self, id_curso,id_cohorte,id_actividad, new_fecha):
        asignacionEditada = self.session.query(Asignacion).filter_by(id_actividad=id_actividad,id_curso = id_curso,id_cohorte = id_cohorte).first()
        asignacionEditada.fecha_hora = new_fecha
        self.session.commit()
        self.session.close()