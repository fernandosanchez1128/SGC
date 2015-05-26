from sqlalchemy.orm import sessionmaker

from LogicaCohorte import LogicaCohorte
from LogicaCursos import LogicaCursos
from ORM.Matricula import Matricula
from ORM.basetest import *


class LogicaMatricula():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorAct")

    def agregarMatricula(self, cedula_lt, id_curso, ano, semestre):
        lc = LogicaCohorte()
        ult_coh = lc.ultimoCohorte(id_curso,ano,semestre)
        if ult_coh==None:
            lc.agregarCohorte(id_curso, ano, semestre)
            ult_coh = lc.ultimoCohorte(id_curso,ano,semestre)
        else:
            num_e = self.consultarNestudiantes(id_curso,ult_coh.id_cohorte)
            if num_e==30:
                lc.agregarCohorte(id_curso, ano, semestre)
                ult_coh = lc.ultimoCohorte(id_curso,ano,semestre)
        mat = Matricula(cedula_lt= cedula_lt, id_curso= id_curso, id_cohorte = ult_coh.id_cohorte, nota_definitiva =0)
        self.session.add(mat)
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

    def consultar_cursos_estudiantes (self,cedula_lt):
        registros = self.session.query(Matricula).filter_by(cedula_lt = cedula_lt).all()
        self.session.close()
        return registros

    def consultar_cohorte_estudiante(self, cedula, id_curso):
        mat = self.session.query(Matricula).filter_by(id_curso=id_curso, cedula_lt=cedula).first()
        self.session.close()
        return mat
    
        
       

'''


log = LogicaMatricula()
#Matricula = Matricula(cedula_lt="t", id_cohorte=1, id_curso=123, nota_definitiva=4.8)

log.agregarMatricula("1145", 4, 2015, 2)

'''
