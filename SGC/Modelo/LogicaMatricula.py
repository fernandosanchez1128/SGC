from sqlalchemy.orm import sessionmaker
from sqlalchemy import distinct

from LogicaCohorte import LogicaCohorte
from ORM.Matricula import Matricula
from ORM.Cohorte import Cohorte
from ORM.LeaderTeacher import LeaderTeacher
from ORM.basetest import *


class LogicaMatricula():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructorAct")

    def agregarMatricula(self, cedula_lt, id_curso, ano, semestre):
        lc = LogicaCohorte()
        ult_coh = lc.ultimoCohorte(id_curso, ano, semestre)
        if ult_coh == None:
            lc.agregarCohorte(id_curso, ano, semestre)
            ult_coh = lc.ultimoCohorte(id_curso, ano, semestre)
        else:
            num_e = self.consultarNestudiantes(id_curso, ult_coh.id_cohorte)
            if num_e == 30:
                lc.agregarCohorte(id_curso, ano, semestre)
                ult_coh = lc.ultimoCohorte(id_curso, ano, semestre)
        mat = Matricula(cedula_lt=cedula_lt, id_curso=id_curso, id_cohorte=ult_coh.id_cohorte, nota_definitiva=0)
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

    def consultar_cursos_estudiantes(self, cedula_lt):
        registros = self.session.query(Matricula).filter_by(cedula_lt=cedula_lt).all()
        self.session.close()
        return registros

    def consultar_estudiantes_aprobados(self, idCurso, anoBuscar, semestreBuscar):
        departamentos=self.session.query(distinct(LeaderTeacher.dpto_secretaria)).join(Matricula).join(Cohorte).\
            filter(Cohorte.id_curso==idCurso).filter(Cohorte.semestre == semestreBuscar).\
            filter(Cohorte.ano == anoBuscar).all()
        print departamentos

        dep_porcentajes=[]
        for dep in departamentos:
            aprobados = int(self.session.query(LeaderTeacher).join(Matricula).join(Cohorte).
            filter(Cohorte.id_curso == idCurso).filter(Cohorte.semestre == semestreBuscar).
                filter(Cohorte.ano == anoBuscar).filter(LeaderTeacher.dpto_secretaria == dep[0].encode("utf-8")).
                filter(Matricula.nota_definitiva>2.5).count())
            print "aprobados", aprobados

            reprobados = int(self.session.query(LeaderTeacher).join(Matricula).join(Cohorte).
            filter(Cohorte.id_curso == idCurso).filter(Cohorte.semestre == semestreBuscar).
                filter(Cohorte.ano == anoBuscar).filter(LeaderTeacher.dpto_secretaria == dep[0].encode("utf-8")).
                filter(Matricula.nota_definitiva<=2.5).count())

            print "reprobados", reprobados

            total = aprobados+reprobados
            if total==0:
                porcentaje=0.0
            else:
                porcentaje = float(aprobados)*100.0/total
            dep_porcentajes.append((dep[0].encode("utf-8"), porcentaje))

        self.session.close()
        print dep_porcentajes
        return dep_porcentajes



    def consultar_estudiantes_reprobados(self, idCurso, anoBuscar, semestreBuscar):
        departamentos=self.session.query(distinct(LeaderTeacher.dpto_secretaria)).join(Matricula).join(Cohorte).\
            filter(Cohorte.id_curso==idCurso).filter(Cohorte.semestre == semestreBuscar).\
            filter(Cohorte.ano == anoBuscar).all()
        print departamentos

        dep_porcentajes=[]
        for dep in departamentos:
            aprobados = int(self.session.query(LeaderTeacher).join(Matricula).join(Cohorte).
            filter(Cohorte.id_curso == idCurso).filter(Cohorte.semestre == semestreBuscar).
                filter(Cohorte.ano == anoBuscar).filter(LeaderTeacher.dpto_secretaria == dep[0].encode("utf-8")).
                filter(Matricula.nota_definitiva>2.5).count())
            print "aprobados", aprobados

            reprobados = int(self.session.query(LeaderTeacher).join(Matricula).join(Cohorte).
            filter(Cohorte.id_curso == idCurso).filter(Cohorte.semestre == semestreBuscar).
                filter(Cohorte.ano == anoBuscar).filter(LeaderTeacher.dpto_secretaria == dep[0].encode("utf-8")).
                filter(Matricula.nota_definitiva<=2.5).count())

            print "reprobados", reprobados

            total = aprobados+reprobados
            if total==0:
                porcentaje=0.0
            else:
                porcentaje = float(reprobados)*100.0/total
            dep_porcentajes.append((dep[0].encode("utf-8"), porcentaje))

        self.session.close()
        print dep_porcentajes
        return dep_porcentajes


'''


log = LogicaMatricula()
#Matricula = Matricula(cedula_lt="t", id_cohorte=1, id_curso=123, nota_definitiva=4.8)

log.agregarMatricula("1145", 4, 2015, 2)

'''
