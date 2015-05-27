__author__ = 'braymrr'
from ORM.Curso import Curso
from ORM.basetest import *
from Modelo.LogicaCursos import LogicaCursos
from ORM.Matricula import *
from ORM.LeaderTeacher import *
from ORM.Cohorte import *
import pygal
from pygal.style import *
import reportlab


import sys

class Reporte:
    Session = sessionmaker(bind=engine)
    session = Session()

    def cursos_mas_asistentes(self,fechai):
        matricula=self.session.query(func.count(Matricula.cedula_lt), Curso.nombre).filter(Matricula.id_curso==Cohorte.id_curso, Matricula.id_cohorte==Cohorte.id_cohorte, Matricula.id_curso==Curso.id, Cohorte.fecha_inicio>=fechai,Cohorte.fecha_inicio<=fechai).group_by(Curso.nombre).order_by(func.count(Matricula.cedula_lt)).all()
        #LISTA DE LISTAS
        num=[]
        nombres=[]
        mes="agosto"
        ano='2015'
        i=0
        y=0
        for mat in matricula:
            print mat
            num.append(matricula[i][0])
            nombres.append(matricula[i][1])
            i+=1
        print(num)
        print(nombres)
        bar_chart = pygal.Bar()
        bar_chart.title = 'Cursos con mas asistentes en el mes de '+mes+' del '+ano
        bar_chart.x_labels = map(str, nombres)
        for i in range(0,len(num)):
            valores=[None]*(len(num)-1)
            valores.insert(i,num[i])
            bar_chart.add(nombres[i], valores)
        bar_chart.render_to_file('Top10.svg')



    def estudiantes_por_dpto(self):
        pass
        # filtrar si cada estudiante esta matriculado un cohorte en esta fecha
        #agrupar por estudiante.departamento

    def porc_estudiantes_aprobaron(self):
        pass
        #filtro de estudiante si tiene cohortes este semestre y
        #filtrar si la nota definitiva en todas las matriculas es >3.0
        #comparar con el numero de LT matriculados


# r=Reporte()
# r.cursos_mas_asistentes()
