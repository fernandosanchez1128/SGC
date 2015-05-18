import sys
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control.ControlLogin import ControlLogin

( Ui_VistaLogin, QDialog ) = uic.loadUiType( 'VistaLogin.ui' )

class VistaLogin ( QDialog ):
    """VistaLogin inherits QDialog"""

    def __init__ ( self, parent = None ):
        self.control = ControlLogin()
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaLogin()
        self.ui.setupUi( self )
        self.ui.txtPassword.setEchoMode(QLineEdit.Password)
        self.connect(self.ui.btnInicio, SIGNAL("clicked()"), self.inicio_clicked)

    def inicio_clicked(self):
        username=str(self.ui.txtUsuario.text())
        objUsuario=self.control.buscarUsuarioUsername(username)

        if objUsuario is None:
            QMessageBox.information(self, "Login", "Usuario o Contrasena Invalidos")
        else:
            tipoUsuario=str(objUsuario.type)
            print "TipoUsuario"
            print tipoUsuario

            if objUsuario.contrasena==str(self.ui.txtPassword.text()):
                if tipoUsuario=='coordinador':
                    QMessageBox.information(self, "Login", "Ingresa Coordinador")
                elif tipoUsuario=='leaderteacher':
                    QMessageBox.information(self, "Login", "Ingresa Leader Teacher")
                elif tipoUsuario=='masterteacher':
                    QMessageBox.information(self, "Login", "Ingresa Master Teacher")
                elif tipoUsuario=='digitador':
                    QMessageBox.information(self, "Login", "Ingresa Digitador")
                else:
                    QMessageBox.information(self, "Login", "Perfil de usuario desconocido")
            else:
                QMessageBox.information(self, "Login", "Usuario o Contrasena Invalidos")



    def __del__ ( self ):
        self.ui = None