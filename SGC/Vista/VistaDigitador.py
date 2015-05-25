# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from CrearAspirante import CrearAspirante
from CrearPreinscripcion import CrearPreinscripcion
from RegistrarLT import RegistrarLT



( Ui_VistaDigitador, QDialog ) = uic.loadUiType( 'VistaDigitador.ui' )

class VistaDigitador ( QDialog ):

    def __init__ ( self, parent = None):
        self.crearAsp=CrearAspirante()
        self.crearPre=CrearPreinscripcion()
        self.registrarlt=RegistrarLT()

        QDialog.__init__( self, parent )
        self.ui = Ui_VistaDigitador()
        self.ui.setupUi( self )
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btAspirante, SIGNAL("clicked()"), self.aspirante_clicked)
        self.connect(self.ui.btPreinscribir, SIGNAL("clicked()"), self.preinscribir_clicked)
        self.connect(self.ui.btRegistrarLT, SIGNAL("clicked()"), self.registrarlt_clicked)


    def __del__ ( self ):
        self.ui = None

    def cancelar_clicked(self):
        self.close()

    def aspirante_clicked(self):
        self.crearAsp.show()

    def preinscribir_clicked(self):
        self.crearPre.show()

    def registrarlt_clicked(self):
        self.registrarlt.show()