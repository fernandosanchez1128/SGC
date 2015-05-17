from PyQt4 import uic

( Ui_Asignacion, QMainWindow ) = uic.loadUiType( 'Asignacion.ui' )

class Asignacion ( QMainWindow ):
    """Asignacion inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_Asignacion()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
