__author__ = 'JuanD'
from reportlab.pdfgen.canvas import Canvas
# Importa el tamaNo de pagina carta
from reportlab.lib.pagesizes import letter
#Importa las unidades de medida
from reportlab.lib.units import cm, mm, inch, pica
from datetime import *



class Certificado:
    def __init__(self):
        print "Constructor certificado"
        pass

    def generaCertificado(self, ruta, nombre, cedula, nota, nombreCurso):
        if nota <= 2.5:
            tipoCertificado = "asistencia"
        elif nota > 2.5 and nota <= 3.5:
            tipoCertificado = "participacion"
        elif nota > 3.5:
            tipoCertificado = "excelencia"
        else:
            print "error"

        fechaActual = date.today()

        #Carga la ruta y el tamaNo de pagina del archivo pdf
        pdf = Canvas(str(ruta), pagesize=(letter[1], letter[0]))

        pdf.setFont("Courier", 35)
        pdf.setFillColorRGB(0, 0, 0)
        pdf.drawCentredString(letter[1] / 2, inch * 7.5, "EL CENTRO DE INNOVACION EDUCATIVA")
        pdf.setFont("Courier", 35)
        pdf.drawCentredString(letter[1] / 2, inch * 6.8, "REGIONAL CIER-SUR")
        pdf.setFont("Courier", 20)
        pdf.drawCentredString(letter[1] / 2, inch * 5.2, "Le otorga a:")
        pdf.setFont("Courier", 25)
        pdf.drawCentredString(letter[1] / 2, inch * 4.5, nombre.upper())
        pdf.setFont("Courier", 15)
        pdf.drawCentredString(letter[1] / 2, inch * 4, "C.C. " + str(cedula))
        pdf.setFont("Courier", 20)
        pdf.drawCentredString(letter[1] / 2, inch * 3.0,
                              "El certificado de " + str(tipoCertificado).lower() + " en el curso:")
        pdf.setFont("Courier", 25)
        pdf.drawCentredString(letter[1] / 2, inch * 2.5, str(nombreCurso).upper())
        pdf.setFont("Courier", 15)
        pdf.drawCentredString(letter[1] / 2, inch * 2, "Por haber aprobado todos los modulos exigidos")
        pdf.setFont("Courier", 15)
        pdf.drawCentredString(letter[1] / 2, inch * 1, "Expedido en Santiago de Cali el " + str(fechaActual))
        pdf.showPage()
        pdf.save()