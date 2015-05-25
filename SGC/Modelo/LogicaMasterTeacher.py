from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from ORM.MasterTeacher import MasterTeacher

class LogicaMasterTeacher():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica LeaderTeacher")

    def consultarMT(self, id_mt):
        mt=self.session.query(MasterTeacher).filter_by(cedula=id_mt).first()
        self.session.close()
        return mt