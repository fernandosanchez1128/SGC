from sqlalchemy.orm import sessionmaker

from ORM.Aspirante import *
from ORM.basetest import *


class LogicaAspirante():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica Aspirante")

    def agregarAspirante(self, aspirante):
        self.session.add(aspirante)
        self.session.commit()
        self.session.close()

    def consultarAspirante(self, id_asp):
        aspirante=self.session.query(Aspirante).filter_by(cedula=id_asp).first()
        return aspirante