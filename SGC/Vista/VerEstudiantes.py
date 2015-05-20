from PyQt4 import uic

from Control.ControlCoordinador import ControlCoordinador

( Ui_VerEstudiantes, QDialog ) = uic.loadUiType( 'VerEstudiantes.ui' )
class VerEstudiantes ( QDialog ):
    """VerEstudiantes inherits QDialog"""

    def __init__ ( self, parent = None , id_curso=0):
        QDialog.__init__( self, parent )
        self.ui = Ui_VerEstudiantes()
        self.ui.setupUi( self )
        self.id_curso = id_curso
        self.control = ControlCoordinador()
        cohortes = self.control.numeroCohortes(id_curso)
        self.ui.sbCohortes.setMinimum(1)
        self.ui.sbCohortes.setMaximum(cohortes)
        self.ui.tableWidget.setRowCount(cohortes)

    def __del__ ( self ):
        self.ui = None
