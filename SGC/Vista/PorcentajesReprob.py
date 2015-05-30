__author__ = 'JuanD'
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

from datetime import datetime,date
from PyQt4.QtGui import QFileDialog
from Singleton import Singleton
from Control.ControlCoordinador import ControlCoordinador
( Ui_PorcReprob, QDialog ) = uic.loadUiType( 'porcentaje_reprobados.ui' )

@Singleton
class PorcentajesReprob( QDialog ):
    """Asignacion inherits QMainWindow"""
    controlcordinador = ControlCoordinador()
    def __init__ ( self,parent = None):
        QDialog.__init__( self, parent )
        self.ui = Ui_PorcReprob()
        self.ui.setupUi( self )
        self.cargar_cursos()
        self.connect(self.ui.btnReporte, SIGNAL("clicked()"), self.generar_reporte)
        self.connect(self.ui.btnSalir, SIGNAL("clicked()"), self.close)



    def __del__ ( self ):
        self.ui = None

    def cargar_cursos (self):
        cursos = self.controlcordinador.consultar_cursos()
        for curso in cursos :
            self.ui.comboCurso.addItem(QString(curso.nombre))



    def generar_reporte (self):
        semestre = str (self.ui.comboSemestre.currentText())
        curso = str (self.ui.comboCurso.currentText())
        obj_curso = self.controlcordinador.buscarCurso(curso)
        id_curso=obj_curso.id
        year = int (self.ui.year.cleanText())
        print year,semestre,curso, id_curso

        ruta = QFileDialog.getSaveFileName(self, 'Guardar Reporte', '', selectedFilter='*.pdf')
        if ruta:
            exito =self.controlcordinador.porcentaje_reprobado(str(ruta), id_curso, curso, str(year), semestre)
            if exito == 0 :
                QtGui.QMessageBox.warning(self, 'Error',"No se encontraron datos para generar reporte\npara este curso"
                                                        " en el semestre seleccionado",
                                          QtGui.QMessageBox.Ok)
        else :
            QtGui.QMessageBox.warning(self, 'Error',"Por favor seleccione un destino", QtGui.QMessageBox.Ok)