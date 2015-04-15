from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Singleton import Singleton

from CrearCurso import CrearCurso
from ConsultarCurso import ConsultarCurso 

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

@Singleton
class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
    
    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect(self.ui.btCrear, SIGNAL("clicked()"), self.crear_clicked)
        self.connect(self.ui.btConsultar, SIGNAL("clicked()"), self.consultar_clicked)

    def __del__ ( self ):
        self.ui = None

    def crear_clicked(self):
        venCrear =  CrearCurso().exec_()
        
    def consultar_clicked(self):
        venConsultar =  ConsultarCurso().exec_()
    