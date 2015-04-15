from PyQt4 import uic

( Ui_VerEstudiantes, QDialog ) = uic.loadUiType( 'VerEstudiantes.ui' )

class VerEstudiantes ( QDialog ):
    """VerEstudiantes inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_VerEstudiantes()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
