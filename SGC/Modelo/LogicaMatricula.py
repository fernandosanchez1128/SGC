from sqlalchemy.orm import sessionmaker

from ORM.Matricula import Matricula
from ORM.basetest import *


class LogicaMatricula():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorAct")

    def agregarMatricula(self, matricula):
        self.session.add(matricula)
        self.session.commit()
        self.session.close()

    def consultarMatricula(self, ncedula_lt, nid_cohorte, nid_curso):
        matricula = self.session.query(Matricula).filter_by(cedula_lt=ncedula_lt, id_cohorte=nid_cohorte,
                                                            id_curso=nid_curso).first()
        self.session.close()
        return matricula

    def editarMatricula(self, ncedula_lt, nid_cohorte, nid_curso, newMatricula):
        matricula = self.session.query(Matricula).filter_by(cedula_lt=ncedula_lt, id_cohorte=nid_cohorte,
                                                            id_curso=nid_curso).first()
        matricula.nota_definitiva = newMatricula.nota_definitiva
        self.session.commit()
        self.session.close()

    def eliminarMatricula(self, ncedula_lt, nid_cohorte, nid_curso):
        matricula = self.session.query(Matricula).filter_by(cedula_lt=ncedula_lt, id_cohorte=nid_cohorte,
                                                            id_curso=nid_curso).first()
        self.session.delete(matricula)
        self.session.commit()
        self.session.close()

    def consultarNestudiantes(self, id_curso, id_cohorte):
        cantidad = self.session.query(Matricula).filter_by(id_cohorte=id_cohorte, id_curso=id_curso).count()
        self.session.close()
        return cantidad

    def consultar_estudiantes(self, id_curso, id_cohorte):
        cantidad = self.session.query(Matricula).filter_by(id_cohorte=id_cohorte, id_curso=id_curso).all()
        self.session.close()
        return cantidad

    def consultar_cursos_estudiantes(self, cedula_lt):
        registros = self.session.query(Matricula).filter_by(cedula_lt = cedula_lt).all()
        self.session.close()
        return registros
        
    
        
       



'''
log = LogicaMatricula()
#Matricula = Matricula(cedula_lt="t", id_cohorte=1, id_curso=123, nota_definitiva=4.8)
print log.consultarNestudiantes(123,1)
#log.agregarMatricula(Matricula)
'''
