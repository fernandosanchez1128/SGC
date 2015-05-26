from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

from Control.ControlCoordinador import ControlCoordinador
( Ui_NotasEstudiante, QDialog ) = uic.loadUiType( 'NotasEstudiante.ui' )

class NotasEstudiante ( QDialog ):
    """NotasEstudiante inherits QDialog"""
    controlcordinador = ControlCoordinador()
    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_NotasEstudiante()
        self.ui.setupUi( self )
        self.connect(self.ui.reporte, SIGNAL("clicked()"), self.generar_reporte)
        self.connect(self.ui.salir, SIGNAL("clicked()"), self.close)

    def __del__ ( self ):
        self.ui = None

    def cargar_cursos (self, cedula_lt):
        mats = self.controlcordinador.cursosEstudiantes(cedula_lt)
        cursos = []
        for mat in mats:
            cursos.append(self.controlcordinador.buscarCursoId(mat.id_curso))
        for curso in cursos :
            self.ui.cursos.addItem(QString(curso.nombre))

    def generar_reporte (self):
        curso = str (self.ui.cursos.currentText())
        obj_curso = self.controlcordinador.buscarCurso(curso)
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
            exito =self.controlcordinador.estudiantes_departamento(str (ruta),fecha_ini,fecha_fin,obj_curso.id,curso,mes,str (year))
            if exito == 0 :
                QtGui.QMessageBox.warning(self, 'Error',"no se encontraron datos para generar reporte", QtGui.QMessageBox.Ok)
        else :
            QtGui.QMessageBox.warning(self, 'Error',"por favor seleccione un destino", QtGui.QMessageBox.Ok)