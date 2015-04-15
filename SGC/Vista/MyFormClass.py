from PyQt4 import uic

( Ui_MyFormClass, QMainWindow ) = uic.loadUiType( 'MyFormClass.ui' )

class MyFormClass ( QMainWindow ):
    """MyFormClass inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MyFormClass()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
