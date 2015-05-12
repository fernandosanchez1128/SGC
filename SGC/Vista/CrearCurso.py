from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Modelo.Curso import Curso

( Ui_CrearCurso, QDialog ) = uic.loadUiType( 'CrearCurso.ui' )

class CrearCurso ( QDialog ):
    """CrearCurso inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_CrearCurso()
        self.ui.setupUi( self )
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        self.connect(self.ui.sbNumActividades, SIGNAL("valueChanged(int)"), self.change_actividades)
        self.connect(self.ui.btCancelar, SIGNAL("clicked()"), self.cancelar_clicked)

    def __del__ ( self ):
        self.ui = None
    
    def change_actividades(self):
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        
    def cancelar_clicked(self):
        self.close()
