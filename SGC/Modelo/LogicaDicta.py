from sqlalchemy.orm import sessionmaker

from ORM.Curso import *
from ORM.Dicta import Dicta


class LogicaDicta ():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__ (self) :
        #llamado para prueba del iterador
        print ("contructorAct")

    def consultarCursosProf(self, cedula):
        cursos=self.session.query(Dicta).filter_by(cedula_mt=cedula).all()
        print cursos
        self.session.close()
        return cursos

