from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

( Ui_ConsultarCurso, QDialog ) = uic.loadUiType( 'ConsultarCurso.ui' )

class ConsultarCurso ( QDialog ):
    """ConsultarCurso inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_ConsultarCurso()
        self.ui.setupUi( self )
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.salir_clicked)

    def __del__ ( self ):
        self.ui = None
    
    def salir_clicked(self):
        self.close()