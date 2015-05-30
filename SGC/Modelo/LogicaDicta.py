from sqlalchemy.orm import sessionmaker
from sqlalchemy import between#,funcfilter

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
        cursos=self.session.query(Dicta).join(Cohorte).filter(Dicta.cedula_mt == cedula,Cohorte.fecha_inicio <= fecha,Cohorte.fecha_fin >= fecha).order_by(Dicta.id_curso).all()
        print cursos
        self.session.close()
        return cursos

    def agregarDicta(self,cedula_mt, id_curso, id_cohorte):
        self.session.rollback()
        dicta = Dicta(cedula_mt = cedula_mt, id_curso = id_curso, id_cohorte=id_cohorte)
        self.session.add(dicta)
        self.session.commit()
        self.session.close()
'''
lo = LogicaDicta()
lo.agregarDicta("2246", 7, 6)
'''