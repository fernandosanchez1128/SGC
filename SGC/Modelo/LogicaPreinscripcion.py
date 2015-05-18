from sqlalchemy.orm import sessionmaker

from ORM.Preinscripcion import Preinscripcion
from ORM.basetest import *


class LogicaPreinscripcion():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("contructorPre")

    def agregarPreinscripcion(self, preinscripcion):
        self.session.add(preinscripcion)
        self.session.commit()
        self.session.close()
