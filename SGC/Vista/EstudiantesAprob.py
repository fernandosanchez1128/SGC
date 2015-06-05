from PyQt4 import uic
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

from datetime import datetime,date
from PyQt4.QtGui import QFileDialog
from Singleton import Singleton
from Control.ControlCoordinador import ControlCoordinador
( Ui_Asignacion, QMainWindow ) = uic.loadUiType( 'estudiantes_dpto.ui' )


class EstudiantesAprob( QMainWindow ):
    """Asignacion inherits QMainWindow"""
    controlcordinador = ControlCoordinador()
    def __init__ ( self,parent = None):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_Asignacion()
        self.ui.setupUi( self )
        self.cargar_cursos()
        self.connect(self.ui.reporte, SIGNAL("clicked()"), self.generar_reporte)
        self.connect(self.ui.salir, SIGNAL("clicked()"), self.close)



    def __del__ ( self ):
        self.ui = None

    def cargar_cursos (self):
        cursos = self.controlcordinador.consultar_cursos()
        for curso in cursos :
            self.ui.cursos.addItem(QString(curso.nombre))



    def generar_reporte (self):
        meses ={'Enero':1,'Febrero':2,'Marzo':3,'Abril':4,'Mayo':5,'Junio':6,
                'Julio':7,'Agosto':8,'Septiembre':9,'Octubre':10,'Noviembre':11,'Diciembre':12}
        mes = str (self.ui.mes.currentText())
        curso = str (self.ui.cursos.currentText())
        obj_curso = self.controlcordinador.buscarCurso(curso)
        nmes = meses[mes]
        year = int (self.ui.year.cleanText())
        print year,nmes,curso
        num_dias =0
        if nmes == 2:
            num_dias = 28
        elif (nmes == 4 or nmes == 6 or nmes == 4 or nmes == 9 or nmes == 11):
            num_dias =30
        else:
            num_dias =31

        fecha_ini = date(year,nmes,1)
        fecha_fin = date(year,nmes,num_dias)
        ruta = QFileDialog.getSaveFileName(self, 'Guardar Reporte', '', selectedFilter='*.pdf')
        if ruta:
            exito =self.controlcordinador.estudiantes_aprobados_curso(str (ruta),fecha_ini,fecha_fin,obj_curso.id,curso,mes,str (year))
            if exito == 0 :
                QtGui.QMessageBox.warning(self, 'Error',"no se encontraron datos para generar reporte", QtGui.QMessageBox.Ok)

        else :
            QtGui.QMessageBox.warning(self, 'Error',"por favor seleccione un destino", QtGui.QMessageBox.Ok)



