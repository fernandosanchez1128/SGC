from PyQt4 import uic, QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sqlalchemy.exc import SQLAlchemyError

from datetime import date
from Control.ControlCoordinador import ControlCoordinador
( Ui_AsignarMT, QDialog ) = uic.loadUiType( 'AsignarMT.ui' )

class AsignarMT ( QDialog ):
    """AsignarMT inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_AsignarMT()
        self.ui.setupUi( self )
        self.busco = False
        self.control_c = ControlCoordinador()
        self.ui.sbAno.setMinimum(date.today().year)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        self.connect(self.ui.btAsignar, SIGNAL("clicked()"), self.asignar_clicked)
        self.connect(self.ui.btCancelar, SIGNAL("clicked()"), self.close)

    def __del__ ( self ):
        self.ui = None

    def buscar_clicked(self):
        self.busco = True
        cedula = str(self.ui.leCedula.text())
        mt = self.control_c.consultarMT(cedula)
        if not mt==None:
            self.ui.leCedula.setEnabled(False)
            self.ui.leNombre.setText(mt.nombres)
        else:
            QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                          QString.fromUtf8("El Master Teacher no existe."))

    def asignar_clicked(self):
        try:
            nombre_c = str(self.ui.leNombreC.text())
            if not nombre_c.strip()=="" and self.busco:
                cedula = str(self.ui.leCedula.text())
                curso  = self.control_c.buscarCurso(nombre_c)
                if not curso == None:
                    cohorte = self.control_c.consultarCohorteN(curso.id, self.ui.sbAno.value(), self.ui.sbSemestre.value(),self.ui.sbCohorte.value()-1)
                    self.control_c.agregarDicta(cedula,curso.id,cohorte.id_cohorte)
            self.close()
            self.control_c.cerrarSesion()
        except SQLAlchemyError:
            QtGui.QMessageBox.warning(self, self.tr("Error en BD"),
                                          QString.fromUtf8("Ha ocurrido un error en la base de datos.\nVerifique que el curso escrito y el cohorte seleccionado existan."))
        except:
            QtGui.QMessageBox.warning(self, self.tr("Error inesperado"),
                                          QString.fromUtf8("Ha ocurrido un error inesperado."))