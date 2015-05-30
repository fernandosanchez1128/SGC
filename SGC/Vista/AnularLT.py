# -*- coding: utf-8 -*-
from PyQt4 import uic, QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sqlalchemy.exc import SQLAlchemyError

from datetime import date
from Control.ControlCoordinador import ControlCoordinador
( Ui_AnularLT, QDialog ) = uic.loadUiType( 'AnularLT.ui' )

class AnularLT ( QDialog ):
    """AnularLT inherits QDialog"""

    def __init__ ( self, parent = None , id_curso =0):
        QDialog.__init__( self, parent )
        self.ui = Ui_AnularLT()
        self.ui.setupUi( self )
        self.id_curso = id_curso
        self.control_c = ControlCoordinador()
        self.connect(self.ui.btBuscarL, SIGNAL("clicked()"), self.buscarL_clicked)
        self.connect(self.ui.btAnular, SIGNAL("clicked()"), self.anular_clicked)
        self.connect(self.ui.btCancelar, SIGNAL("clicked()"), self.close)

    def __del__ ( self ):
        self.ui = None


    def buscarL_clicked(self):
        self.busco = True
        cedula = str(self.ui.leCedula.text())
        lt = self.control_c.consultarLT(cedula)
        mat = self.control_c.mat_lt_curso(cedula,self.id_curso)
        if not (lt==None or mat==None):
            self.ui.leCedula.setEnabled(False)
            self.ui.leNombreL.setText(lt.nombres)
        else:
            QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                          QString.fromUtf8("El Leader Teacher no existe o no está matriculado."))


    def anular_clicked(self):
        try:
            if self.busco:
                cedula = str(self.ui.leCedula.text())
                self.control_c.anular_matricula(cedula,self.id_curso)
            self.close()
            self.control_c.cerrarSesion()
        except SQLAlchemyError:
            QtGui.QMessageBox.warning(self, self.tr("Error en BD"),
                                          QString.fromUtf8("Ha ocurrido un error en la base de datos.\nVerifique que el curso escrito y el cohorte seleccionado existan."))
        except:
            QtGui.QMessageBox.warning(self, self.tr("Error inesperado"),
                                          QString.fromUtf8("Ha ocurrido un error inesperado."))