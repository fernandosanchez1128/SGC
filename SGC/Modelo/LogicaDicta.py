from sqlalchemy.orm import sessionmaker
from sqlalchemy import between,funcfilter

from ORM.basetest import *
from ORM.Cohorte import Cohorte
from ORM.Dicta import Dicta


class LogicaDicta ():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__ (self) :
        #llamado para prueba del iterador
        print ("contructorAct")

    def consultarCursosProf(self, cedula,fecha):
        cursos=self.session.query(Dicta).join(Cohorte).filter(Dicta.cedula_mt == cedula,Cohorte.fecha_inicio <= fecha,Cohorte.fecha_fin >= fecha).all()
        print cursos
        self.session.close()
        return cursos

