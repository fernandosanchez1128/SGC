from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

from Control.ControlCoordinador import ControlCoordinador
( Ui_NotasEstudiante, QDialog ) = uic.loadUiType( 'NotasEstudiante.ui' )

class NotasEstudiante ( QDialog ):
    """NotasEstudiante inherits QDialog"""
    controlcordinador = ControlCoordinador()
    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_NotasEstudiante()
        self.ui.setupUi(self)
        self.cedula_lt = None
        self.connect(self.ui.reporte, SIGNAL("clicked()"), self.generar_reporte)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        self.connect(self.ui.salir, SIGNAL("clicked()"), self.close)

    def __del__ ( self ):
        self.ui = None

    def cargar_cursos (self):
        if self.cedula_lt!=None:
            mats = self.controlcordinador.cursosEstudiantes(self.cedula_lt)
        cursos = []
        for mat in mats:
            cursos.append(self.controlcordinador.buscarCursoId(mat.id_curso))
        for curso in cursos :
            self.ui.cursos.addItem(QString(curso.nombre))

    def buscar_clicked(self):
        self.ui.leCedula.setEnabled(False)
        self.cedula_lt = str(self.ui.leCedula.text())
        lt = self.controlcordinador.consultarLT(self.cedula_lt ).nombres
        self.ui.leNombre.setText(lt)
        self.controlcordinador.cerrarSesionLT()
        self.cargar_cursos()


    def generar_reporte (self):
        curso = str (self.ui.cursos.currentText())
        obj_curso = self.controlcordinador.buscarCurso(curso)

        ruta = QFileDialog.getSaveFileName(self, 'Guardar Reporte', '', selectedFilter='*.pdf')
        if ruta and self.cedula_lt!=None:
            exito = self.controlcordinador.notas_estudiante(str (ruta),self.cedula_lt, obj_curso.id)
            if exito == 0 :
                QtGui.QMessageBox.warning(self, 'Error',"no se encontraron datos para generar reporte", QtGui.QMessageBox.Ok)

        else :
            QtGui.QMessageBox.warning(self, 'Error',"Por favor seleccione un destino y un lt", QtGui.QMessageBox.Ok)