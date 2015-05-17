from sqlalchemy.orm import sessionmaker

from ORM.Aspirante import *
from ORM.basetest import *


class LogicaAspirante():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica...")

    def agregarAspirante(self, aspirante):
        self.session.add(aspirante)
        self.session.commit()
        self.session.close()