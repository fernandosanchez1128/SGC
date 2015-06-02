from reportlab.lib.styles import ParagraphStyle

__author__ = 'braymrr'
from ORM.Curso import Curso
from ORM.basetest import *
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.pagesizes import A4
from Modelo.LogicaCursos import LogicaCursos
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.pdfgen.canvas import Canvas
# Importa el tamaNo de pagina carta
from reportlab.lib.pagesizes import letter
import pygal
from pygal.style import *
from reportlab.lib import colors
from reportlab.lib.styles import _baseFontName, _baseFontNameI
import os

class Reporte:
    Session = sessionmaker(bind=engine)
    session = Session()

    def cursos_mas_asistentes(self):
        pass
        # filtro fecha de inicio y fin de cohorte de cada curso pertenece el mes actual a eso
        #agrupo por id_curso

        # se cuenta en numero de matriculados de cada curso
        #ordena de menor a mayor y se traen los 10 primeros

#BRAYAN
    #ruta con nombre .svg
    def cursos_menos_avance(self, cursos, promedios, ruta):
        bar_chart = pygal.Bar()
        bar_chart.title = 'Cursos con menos potencial de avance, tomando como criterio las notas definitivas'
        nombres = map(lambda x: (x.nombre), cursos)
        bar_chart.x_labels = map(str, nombres)
        for i in range(0,len(promedios)):
            valores=[None]*(len(promedios)-1)
            valores.insert(i,promedios[i])
            bar_chart.add(nombres[i], valores)
        bar_chart.render_to_file(ruta)

    def estudiantes_por_dpto(self):
        pass
        # filtrar si cada estudiante esta matriculado un cohorte en esta fecha
        #agrupar por estudiante.departamento

    def porc_estudiantes_aprobaron(self):
        pass
        #filtro de estudiante si tiene cohortes este semestre y
        #filtrar si la nota definitiva en todas las matriculas es >3.0
        #comparar con el numero de LT matriculados

#BRAYAN
    def notas_estudiante(self, ruta, cedula_lt, id_curso, acts, notas, nota_def):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        if nota_def!=None:
            t = Table([acts+["Nota Definitiva"], notas+[nota_def]],rowHeights=28,hAlign="LEFT",)
        else:
            t = Table([acts, notas],rowHeights=28,hAlign="LEFT",)
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        logCurso  = LogicaCursos()
        curso = logCurso.consultarCurso_id(id_curso)
        msg = "Detalles de las notas del estudiante con cedula: " + cedula_lt+ " en el curso "+ curso.nombre
        titulo = Paragraph(msg, bodyStyle)
        # t.setStyle([('FONTSIZE',(0,0), (-1, -1), 16),
        #             ('FONTSIZE',(0,0), (1, 0), 17),
        #             ('FONT',(0,0), (-1, -1), 'Helvetica'),
        #             ('FONT',(0,0), (4, 0), 'Helvetica-Bold'),
        #             ('VALIGN',(0,0), (-1, -1), 'TOP'),
        #             ('GRID',(0,0),(-1,-1),1,colors.black),
        #             ('ALIGN', (0,0), (-1, -1), 'LEFT')
        #             ])
        story.append(titulo)
        story.append(Spacer(0, 20))
        # story.append(encabezado)
        story.append(t)
        story.append(Spacer(0, 20))
        doc.build(story)
        os.system(ruta)

    def detalle_estudiantes_por_dpto(self, reporte,promedios, ruta,curso,mes,anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Cedula","Nombres","Apellidos","Departamento","Definitiva")] + reporte,rowHeights=28,hAlign="LEFT",)
        story=[]
        bodyStyle = ParagraphStyle('Body', fontName=_baseFontName, fontSize=24, leading=28, spaceBefore=6,
                                   align = "CENTER")
        msg = "Detalles de Estudiantes del Curso " + curso + " Durante el Mes de " +mes+ " del ano " + anio
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
        # story.append(encabezado)
        story.append(t)
        story.append(Spacer(0, 20))
        story.append(sub_titulo)
        story.append(Spacer(0, 20))
        story.append(t_prom)
        doc.build(story)
        os.system(ruta)


    def estudiants_aprob_curso (self, reporte, ruta,curso,mes,anio):
        doc = SimpleDocTemplate(ruta, pagesize = A4)
        t = Table(data = [("Cedula","Nombres","Apellidos","Definitiva")] + reporte,rowHeights=28,hAlign="LEFT",)
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

	

