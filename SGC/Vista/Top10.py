from PyQt4 import uic
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import sys
from datetime import datetime,date
from PyQt4.QtGui import QFileDialog
from Control.ControlCoordinador import *

from Control.ControlLogin import ControlLogin
from datetime import *
from vistacoordinador import *
from VistaDigitador import VistaDigitador


( Ui_VistaTop10, QDialog ) = uic.loadUiType( 'VistaTop10.ui' )

class Top10 ( QDialog ):

    def __init__ ( self, parent = None, modo=1):
        self.control = ControlCoordinador()
        QDialog.__init__( self, parent )
        self.reporte=modo
        self.ui = Ui_VistaTop10()
        self.ui.setupUi( self )
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.salir_clicked)
        self.connect(self.ui.btgenerar, SIGNAL("clicked()"), self.generar_clicked)
        if self.reporte!=1:
            self.ui.label.setText("LTs por departamento en el mes")


    def __del__(self):
        self.ui = None

    def salir_clicked(self):
        self.close()

    def generar_clicked(self):
        meses ={'Enero':1,'Febrero':2,'Marzo':3,'Abril':4,'Mayo':5,'Junio':6,
                'Julio':7,'Agosto':8,'Septiembre':9,'Octubre':10,'Noviembre':11,'Diciembre':12}
        mes = str (self.ui.combomes.currentText())
        nmes = meses[mes]
        year = int (self.ui.txtano.value())
        num_dias =0
        if nmes == 2:
            num_dias = 28
        elif (nmes == 4 or nmes == 6 or nmes == 4 or nmes == 9 or nmes == 11):
            num_dias =30
        else:
            num_dias =31

        fecha = date(year,nmes,1)

        if(self.reporte==1):
            if(self.control.cursos_mas_asistentes(fecha)=="Exito"):
                QMessageBox.information(self, "Top10", "Reporte creado exitosamente, para visualizar la grafica abra el archivo top10.svg\n"
                                                       "Ubicado en la carpeta Vista")
            else:
                QMessageBox.information(self, "Top10", "No hay registros para esa fecha")
        else:
            if(self.control.lt_por_departamento(fecha)=="Exito"):
                QMessageBox.information(self, "LT-por-Dpto", "Reporte creado exitosamente, para visualizar la grafica abra el archivo lt-por-departamento.svg\n"
                                                       "Ubicado en la carpeta Modelo")
            else:
                QMessageBox.information(self, "LT-por-Dpto", "No hay registros para esa fecha")


'''
kas=Top10()
kas.show()
'''