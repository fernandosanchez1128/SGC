from sqlalchemy.orm import sessionmaker
from ORM.basetest import *

class LogicaLeaderTeacher():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica LeaderTeacher")


    def agregarLT(self, let):
        print("ENTRO EN AGREGAR LT")
        self.session.add(let)
        self.session.commit()
        self.session.close()


    def consultarLT(self, id_lt):
        lt=self.session.query(LeaderTeacher).filter_by(cedula=id_lt).first()
        return lt

    def cerrarSesion(self):
        self.session.close()