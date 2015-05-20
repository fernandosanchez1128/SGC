import sys
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control.ControlLogin import ControlLogin
from datetime import*
from vistacoordinador import *

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
            fechaAcceso=objUsuario.fecha_ultimo_acceso
            fechaActual=date.today()
            delta=timedelta(days=180)

            if objUsuario.contrasena==str(self.ui.txtPassword.text()):
                if tipoUsuario=='coordinador':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        w = VistaCoordinador.Instance()
                        w.setWindowTitle( 'Coordinador' )
                        w.show()
                    else:
                        if fechaAcceso>=fechaActual-delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            w = VistaCoordinador.Instance()
                            w.setWindowTitle( 'Coordinador' )
                            w.show()
                        else:
                            QMessageBox.information(self, "Login", "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                                   "por lo tanto su cuenta fue inhabilitada, por favor\n"
                                                                   "contacte al administrador para reactivarla")
                elif tipoUsuario=='leaderteacher':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        QMessageBox.information(self, "Login", "Ingresa Leader Teacher")
                    else:
                        if fechaAcceso>=fechaActual-delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            QMessageBox.information(self, "Login", "Ingresa Leader Teacher")
                        else:
                            QMessageBox.information(self, "Login", "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                                   "por lo tanto su cuenta fue inhabilitada, por favor\n"
                                                                   "contacte al administrador para reactivarla")
                elif tipoUsuario=='masterteacher':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        QMessageBox.information(self, "Login", "Ingresa Master Teacher")
                    else:
                        if fechaAcceso>=fechaActual-delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            QMessageBox.information(self, "Login", "Ingresa Master Teacher")
                        else:
                            QMessageBox.information(self, "Login", "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                                   "por lo tanto su cuenta fue inhabilitada, por favor\n "
                                                                   "contacte al administrador para reactivarla")
                elif tipoUsuario=='digitador':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        QMessageBox.information(self, "Login", "Ingresa Digitador")
                    else:
                        if fechaAcceso>=fechaActual-delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            QMessageBox.information(self, "Login", "Ingresa Digitador")
                        else:
                            QMessageBox.information(self, "Login", "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                                   "por lo tanto su cuenta fue inhabilitada, por favor\n "
                                                                   "contacte al administrador para reactivarla")
                else:
                    QMessageBox.information(self, "Login", "Perfil de usuario desconocido")
            else:
                QMessageBox.information(self, "Login", "Usuario o Contrasena Invalidos")



    def __del__ ( self ):
        self.ui = None