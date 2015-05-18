# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from Control.ControlDigitador import *



( Ui_VistaPreinscripcion, QDialog ) = uic.loadUiType( 'VistaPreinscribir.ui' )

class CrearPreinscripcion ( QDialog ):

    def __init__ ( self, parent = None):
        self.ControlDigi = ControlDigitador()
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaPreinscripcion()
        self.ui.setupUi( self )
        cursos=self.ControlDigi.consultarCursos()
        for curso in cursos:
            self.ui.comboCursos.addItem(curso.nombre)
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btAceptar, SIGNAL("clicked()"), self.inscribir_clicked)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)


    def __del__ ( self ):
        self.ui = None

    def cancelar_clicked(self):
        self.close()

    def buscar_clicked(self):
        ced=str(self.ui.txtCedula.text())
        asp=self.ControlDigi.consultarAspirante(ced)
        self.ui.txtNombres.setText(asp.nombres)
        self.ui.txtApellidos.setText(asp.apellidos)

    def inscribir_clicked(self):
        print("Capturando Informacion...")
        parametros=[]
        cedula=str(self.ui.txtCedula.text())
        f_nacimiento=str(QDate.currentDate().toPyDate())

        cursotemp=str(self.ui.comboCursos.currentText())
        newcurso=self.ControlDigi.consultarIdCurso(cursotemp)
        print("AKSNDOAI:",newcurso.id)
        parametros.append(cedula)
        parametros.append(newcurso.id)
        parametros.append(f_nacimiento)
        self.ControlDigi.agregarPreinscripcion(parametros)

