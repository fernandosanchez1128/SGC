from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Control.ControlCoordinador import ControlCoordinador

from datetime import date
import math

( Ui_VerEstudiantes, QDialog ) = uic.loadUiType( 'VerEstudiantes.ui' )
class VerEstudiantes ( QDialog ):
    """VerEstudiantes inherits QDialog"""

    def __init__ ( self, parent = None , id_curso=0):
        QDialog.__init__( self, parent )
        self.ui = Ui_VerEstudiantes()
        self.ui.setupUi( self )
        self.id_curso = id_curso
        self.control = ControlCoordinador()
        self.ano = date.today().year
        self.semestre  = math.ceil(float(date.today().month)/6)
        cohortes = self.control.consultarNumCohortes(id_curso,self.ano,self.semestre)
        self.ui.sbCohortes.setMinimum(1)
        self.ui.sbCohortes.setMaximum(cohortes)
        self.change_cohortes()
        self.connect(self.ui.sbCohortes, SIGNAL("valueChanged(int)"), self.change_cohortes)

    def __del__ ( self ):
        self.ui = None
        self.control.cerrarSesion()

    def change_cohortes(self):
        cohorte = self.control.consultarCohorteN(self.id_curso,self.ano,self.semestre,self.ui.sbCohortes.value()-1)
        ests  = self.control.consultar_est_mat(self.id_curso,cohorte.id_cohorte)
        self.ui.tableWidget.setRowCount(len(ests))
        i = 0
        for est in ests:
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.ui.tableWidget.item(i, 0).setText(est.cedula_lt)
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem())
            nombre = self.control.consultarLT(est.cedula_lt).nombres
            self.ui.tableWidget.item(i, 1).setText(nombre)
            self.ui.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.ui.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            i += 1