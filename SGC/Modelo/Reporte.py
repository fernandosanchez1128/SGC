# -*- coding: utf-8 -*-
from reportlab.lib.styles import ParagraphStyle

__author__ = 'braymrr'
from ORM.Curso import Curso
from ORM.basetest import *

from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.pagesizes import A4
# from Modelo.LogicaCursos import LogicaCursos
# from reportlab.lib.units import cm, mm, inch, pica
# from reportlab.pdfgen.canvas import Canvas
# # Importa el tamaNo de pagina carta
# from reportlab.lib.pagesizes import letter
# from ORM.Matricula import *
# from ORM.LeaderTeacher import *
from ORM.Cohorte import Cohorte
import pygal
from pygal.style import *
from reportlab.lib import colors
from reportlab.lib.styles import _baseFontName, _baseFontNameI
from reportlab import *
import os
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

    def detalle_estudiantes_por_dpto(self, reporte,promedios, ruta,curso,mes,anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Cedula","Nombres","Apellidos","Departamento","Definitiva")] + reporte,rowHeights=28,hAlign="LEFT",)
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        msg = "Detalles de Estudiantes del Curso " + curso + " Durante el Mes de " +mes+ " del año " + anio
        titulo = Paragraph(msg, bodyStyle)
        t.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
                    ('FONTSIZE',(0,0), (1, 0), 17),
                    ('FONT',(0,0), (-1, -1), 'Helvetica'),
                    ('FONT',(0,0), (4, 0), 'Helvetica-Bold'),
                    ('VALIGN',(0,0), (-1, -1), 'TOP'),
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('ALIGN', (0,0), (-1, -1), 'LEFT')
                    ])
        t_prom = Table(data = [("Promedio","Departamento")] + promedios,rowHeights=28,hAlign="LEFT",)
        t_prom.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
                    ('FONTSIZE',(0,0), (1, 0), 17),
                    ('FONT',(0,0), (-1, -1), 'Helvetica'),
                    ('FONT',(0,0), (1, 0), 'Helvetica-Bold'),
                    ('VALIGN',(0,0), (-1, -1), 'TOP'),
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('ALIGN', (0,0), (-1, -1), 'LEFT')
                    ])
        msg2 = "Promedio de las Notas de los Estudiantes por Departamento"
        sub_titulo = Paragraph(msg2, bodyStyle)
        story.append(titulo)
        story.append(Spacer(0, 20))
        story.append(t)
        story.append(Spacer(0, 20))
        story.append(sub_titulo)
        story.append(Spacer(0, 20))
        story.append(t_prom)
        doc.build(story)
        os.system(ruta)


    def estudiants_aprob_curso (self, reporte, ruta,curso,mes,anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Cedula", "Nombres", "Apellidos", "Definitiva")] + reporte, rowHeights=28, hAlign="LEFT",)
        # encabezado = Table(
        #     data = [['Cantidad', 'DEPARTAMENTO']],rowHeights=28,hAlign="LEFT")
        # encabezado.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
        #             ('FONT',(0,0), (-1, -1), 'Helvetica'),
        #             ('VALIGN',(0,0), (-1, -1), 'TOP'),
        #             ('GRID',(0,0),(-1,-1),1,colors.black),
        #             ('ALIGN', (0,0), (-1, -1), 'LEFT')])
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        msg = "Estudiantes Que Aprobaron el Curso " + curso + " Durante el Mes de " +mes+ " del ano " + anio
        titulo = Paragraph(msg, bodyStyle)
        t.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
                    ('FONTSIZE',(0,0), (1, 0), 17),
                    ('FONT',(0,0), (-1, -1), 'Helvetica'),
                    ('FONT',(0,0), (3, 0), 'Helvetica-Bold'),
                    ('VALIGN',(0,0), (-1, -1), 'TOP'),
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('ALIGN', (0,0), (-1, -1), 'LEFT')


                    ])
        story.append(titulo)
        story.append(Spacer(0, 10))
        # story.append(encabezado)
        story.append(t)
        doc.build(story)
        os.system(ruta)


    def porcentajes_aprob_curso (self, reporte, ruta, curso, semestre, anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Departamento","Porcentaje Aprobados")] + reporte,rowHeights=28,hAlign="LEFT",)
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        msg = "Porcentaje de estudiantes que aprobaron " + str(curso) + " durante el semestre " + str(semestre) + " del "\
              + str(anio)
        titulo = Paragraph(msg, bodyStyle)
        #t.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
        #            ('FONTSIZE',(0,0), (1, 0), 17),
        #            ('FONT',(0,0), (-1, -1), 'Helvetica'),
        #            ('FONT',(0,0), (3, 0), 'Helvetica-Bold'),
        #            ('VALIGN',(0,0), (-1, -1), 'TOP'),
        #            ('GRID',(0,0),(-1,-1),1,colors.black),
        #            ('ALIGN', (0,0), (-1, -1), 'LEFT') ])
        story.append(titulo)
        story.append(Spacer(0, 10))
        story.append(t)
        doc.build(story)
        os.system(ruta)


    def porcentajes_reprob_curso (self, reporte, ruta, curso, semestre, anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Departamento","Porcentaje Reprobados")] + reporte,rowHeights=28,hAlign="LEFT",)
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        msg = "Porcentaje de estudiantes que reprobaron " + str(curso) + " durante el semestre " + str(semestre) + " del "\
              + str(anio)
        titulo = Paragraph(msg, bodyStyle)
        #t.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
        #            ('FONTSIZE',(0,0), (1, 0), 17),
        #            ('FONT',(0,0), (-1, -1), 'Helvetica'),
        #            ('FONT',(0,0), (3, 0), 'Helvetica-Bold'),
        #            ('VALIGN',(0,0), (-1, -1), 'TOP'),
        #            ('GRID',(0,0),(-1,-1),1,colors.black),
        #            ('ALIGN', (0,0), (-1, -1), 'LEFT') ])
        story.append(titulo)
        story.append(Spacer(0, 10))
        story.append(t)
        doc.build(story)
        os.system(ruta)

	

