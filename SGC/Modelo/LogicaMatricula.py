from sqlalchemy.orm import sessionmaker

from LogicaCohorte import LogicaCohorte
from LogicaCursos import LogicaCursos
from ORM.Matricula import Matricula
from ORM.basetest import *
from ORM.Curso import Curso
from ORM.Cohorte import Cohorte
from ORM.Usuario import Usuario
from ORM.LeaderTeacher import LeaderTeacher


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

    def editar_nota(self, ncedula_lt, nid_cohorte, nid_curso, new_nota):
        matricula = self.session.query(Matricula).filter_by(cedula_lt=ncedula_lt, id_cohorte=nid_cohorte,
                                                            id_curso=nid_curso).first()
        matricula.nota_definitiva = new_nota
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

    def estudiantes_aprobados_curso (self,fecha_ini,fecha_fin,id_curso):
        reporte=self.session.query(LeaderTeacher.cedula,Usuario.nombres,Usuario.apellidos,
                                   Matricula.nota_definitiva).\
            filter(Matricula.id_curso == id_curso,Matricula.cedula_lt == LeaderTeacher.cedula,
                   LeaderTeacher.cedula == Usuario.cedula, Matricula.id_curso ==Cohorte.id_curso,
                   Cohorte.fecha_fin>=fecha_ini, Cohorte.fecha_fin <= fecha_fin,
                   Matricula.nota_definitiva >= 3.0).order_by(LeaderTeacher.departamento_secretaria).all()
        self.session.close()
        return reporte

    def estudiantes_departamento_unique (self, fecha_ini,fecha_fin,id_curso,dpto):
        reporte=self.session.query(LeaderTeacher.cedula,Usuario.nombres,Usuario.apellidos,
                                   LeaderTeacher.departamento_secretaria,Matricula.nota_definitiva).\
            filter(Matricula.id_curso == id_curso,Matricula.cedula_lt == LeaderTeacher.cedula,
                   LeaderTeacher.cedula == Usuario.cedula, Matricula.id_curso ==Cohorte.id_curso,
                   Cohorte.fecha_inicio>=fecha_ini, Cohorte.fecha_inicio <= fecha_fin,
                   LeaderTeacher.departamento_secretaria == dpto).order_by(LeaderTeacher.departamento_secretaria).all()
        self.session.close()
        return reporte


    def estudiantes_departamento (self,fecha_ini,fecha_fin,id_curso):
        reporte=self.session.query(LeaderTeacher.cedula,Usuario.nombres,Usuario.apellidos,
                                   LeaderTeacher.departamento_secretaria,Matricula.nota_definitiva).\
            filter(Matricula.id_curso == id_curso,Matricula.cedula_lt == LeaderTeacher.cedula,
                   LeaderTeacher.cedula == Usuario.cedula, Matricula.id_curso ==Cohorte.id_curso,
                   Cohorte.fecha_inicio>=fecha_ini, Cohorte.fecha_inicio <= fecha_fin).order_by(LeaderTeacher.departamento_secretaria).all()
        self.session.close()
        return reporte
        #sql de la consulta
        ''''select us.cedula, nombres,apellidos, nota_definitiva, municipio,departamento_secretaria from matricula as mat, leaderteacher as lead,
usuario as us, cohorte as coh where mat.id_curso = 1  and mat.cedula_lt = lead.cedula and
mat.id_curso = coh.id_curso  and coh.fecha_inicio between '2015/05/01' and '2015/05/30'
and lead.cedula = us.cedula order by lead.departamento_secretaria'''''

    def promedio_departamento (self,fecha_ini,fecha_fin,id_curso):
        promedios = self.session.query(func.avg(Matricula.nota_definitiva),LeaderTeacher.departamento_secretaria).\
            filter(Matricula.id_curso == id_curso,Matricula.cedula_lt == LeaderTeacher.cedula,
                   Matricula.id_curso ==Cohorte.id_curso,Cohorte.fecha_inicio>=fecha_ini,
                   Cohorte.fecha_inicio <= fecha_fin).group_by(LeaderTeacher.departamento_secretaria).all()
        self.session.close()
        return promedios
#BRAYAN
    def cinco_peor_avance(self, fecha_act):
        tuples= self.session.query(func.avg(Matricula.nota_definitiva), Matricula.id_curso).\
            filter(Matricula.id_cohorte ==Cohorte.id_cohorte, Matricula.id_curso ==Cohorte.id_curso,
                   Cohorte.fecha_fin<=fecha_act).\
            group_by(Matricula.id_curso).order_by(func.avg(Matricula.nota_definitiva).asc()).all()
        if len(tuples)<=5:
            return tuples
        return tuples[:5]


       

'''


log = LogicaMatricula()
#Matricula = Matricula(cedula_lt="t", id_cohorte=1, id_curso=123, nota_definitiva=4.8)

log.agregarMatricula("1145", 4, 2015, 2)

'''
