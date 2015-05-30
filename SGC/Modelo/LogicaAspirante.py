from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import *
from ORM.Aspirante import *
from ORM.basetest import *
from sqlalchemy import exc as sqlalchemy_exceptions



class LogicaAspirante():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica Aspirante")

    def agregarAspirante(self, aspirante):
        try:
            self.session.add(aspirante)
            self.session.commit()
            self.session.close()
            return "Exito"
        except Exception:
            print("ERROR BASE DATOS")
            self.session.close()
            return "Fracaso"

    def consultarAspirante(self, id_asp):
        try:
            aspirante=self.session.query(Aspirante).filter_by(cedula=id_asp).first()
            return aspirante
        except sqlalchemy_exceptions:
            self.session.close()

    def cerrarSesion(self):
        self.session.close()