from sqlalchemy.orm import sessionmaker

from ORM.Preinscripcion import Preinscripcion
from ORM.basetest import *
from sqlalchemy import exc as sqlalchemy_exceptions


class LogicaPreinscripcion():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("contructorPre")

    def agregarPreinscripcion(self, preinscripcion):
        try:
            self.session.add(preinscripcion)
            self.session.commit()
            self.session.close()
        except Exception:
            self.session.close()

    def cerrarSesion(self):
        self.session.close()