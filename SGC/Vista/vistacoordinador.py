from PyQt4 import uic, QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Singleton import Singleton

from CrearCurso import CrearCurso
from AsignarMT import AsignarMT
from Asignacion_cohortes import AsignacionCohortes
from Control.ControlCoordinador import ControlCoordinador

from datetime import date
import math

( Ui_VistaCoordinador, QMainWindow ) = uic.loadUiType( 'vistacoordinador.ui' )

@Singleton
class VistaCoordinador ( QMainWindow ):
    """VistaCoordinador inherits QMainWindow"""
    
    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_VistaCoordinador()
        self.ui.setupUi( self )
        self.control  = ControlCoordinador()
        self.connect(self.ui.btCrear, SIGNAL("clicked()"), self.crear_clicked)
        self.connect(self.ui.btConsultar, SIGNAL("clicked()"), self.consultar_clicked)
        self.connect(self.ui.btEditar, SIGNAL("clicked()"), self.editar_clicked)
       # self.connect(self.ui.btEliminar, SIGNAL("clicked()"), self.eliminar_clicked)
        self.connect(self.ui.btMatricular, SIGNAL("clicked()"), self.matricular_clicked)
        self.connect(self.ui.btAsignar, SIGNAL("clicked()"), self.asignar_clicked)
        self.connect(self.ui.btAsignarFecha, SIGNAL("clicked()"), self.asignarFecha_clicked)

    def __del__ ( self ):
        self.ui = None

    def crear_clicked(self):
        venCrear =  CrearCurso(None, 1).exec_()
        
    def consultar_clicked(self):
        venConsultar =  CrearCurso(None,2).exec_()

    def editar_clicked(self):
        venConsultar =  CrearCurso(None,3).exec_()
        
    def eliminar_clicked(self):
		venEliminar =  CrearCurso(None,4).exec_()

    def matricular_clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','', ("Text files (*.txt)" ))
        ano = date.today().year
        semestre  = math.ceil(float(date.today().month)/6)
        self.control.procesarMatriculados(fname, ano, semestre)

    def asignar_clicked(self):
        venAs = AsignarMT().exec_()

    def asignarFecha_clicked(self):
        v = AsignacionCohortes().exec_()
