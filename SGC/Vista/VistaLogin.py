import sys
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control.ControlLogin import ControlLogin
from datetime import *
from vistacoordinador import *
from VistaLt import VistaLt
from VistaMt import MainWindow
from VistaDigitador import VistaDigitador

( Ui_VistaLogin, QDialog ) = uic.loadUiType('VistaLogin.ui')


class VistaLogin(QDialog):
    """VistaLogin inherits QDialog"""

    def __init__(self, parent=None):
        self.control = ControlLogin()
        QDialog.__init__(self, parent)
        self.ui = Ui_VistaLogin()
        self.ui.setupUi(self)
        self.ui.txtPassword.setEchoMode(QLineEdit.Password)
        self.connect(self.ui.btnInicio, SIGNAL("clicked()"), self.inicio_clicked)
        self.validaciones()
        self.ui.txtUsuario.textChanged.connect(self.check_state)
        self.validacion()

    def validaciones(self):
        validador = QIntValidator()
        exp_correo = QRegExp('^.*[@].*[.].*')
        exp_cadena = QRegExp('.+')
        val_correo = QRegExpValidator(exp_correo)
        val_vacio = QRegExpValidator(exp_cadena)
        self.ui.txtUsuario.setValidator(val_correo)

    def check_state(self):
        print "cambio", (1 and 2)
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        print state;
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def validacion(self):
        usuario = self.ui.txtUsuario.validator().validate(self.ui.txtUsuario.text(), 0)[0]
        print "validacion ", usuario
        if (usuario) == 2:
            print "paso en true"
            return True
        else:
            print "paso en false"
            return False

    def buscaCaracter(self, caracter, cadena):
        booleano = False
        for letra in cadena:
            if letra == caracter:
                booleano = True
        return booleano

    def inicio_clicked(self):
        username = str(self.ui.txtUsuario.text())
        objUsuario = self.control.buscarUsuarioUsername(username)

        if (username == ""):
            QMessageBox.information(self, "Login", "El campo usuario no puede estar vacio")
        elif (self.validacion() != 1):
            if (self.buscaCaracter("@", username) == True):
                QMessageBox.information(self, "Login", "Usuario debe contener un punto despues del arroba")
            elif (self.buscaCaracter(".", username) == True):
                QMessageBox.information(self, "Login", "Usuario debe contener un arroba antes del punto")
            else:
                QMessageBox.information(self, "Login", "Usuario debe contener un @ y luego un punto")
        elif objUsuario is None:
            QMessageBox.information(self, "Login", "Usuario o contrasena erroneos")
        else:
            tipoUsuario = str(objUsuario.type)
            fechaAcceso = objUsuario.fecha_ultimo_acceso
            fechaActual = date.today()
            delta = timedelta(days=180)

            if objUsuario.contrasena == str(self.ui.txtPassword.text()):
                if tipoUsuario == 'coordinador':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        w = VistaCoordinador.Instance()
                        w.setWindowTitle('Coordinador')
                        w.show()
                    else:
                        if fechaAcceso >= fechaActual - delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            w = VistaCoordinador.Instance()
                            w.setWindowTitle('Coordinador')
                            w.show()
                        else:
                            QMessageBox.information(self, "Login",
                                                    "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                    "por lo tanto su cuenta fue inhabilitada, por favor\n"
                                                    "contacte al administrador para reactivarla")
                elif tipoUsuario == 'leaderteacher':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        QMessageBox.information(self, "Login", "Ingresa Leader Teacher")
                    else:
                        if fechaAcceso >= fechaActual - delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            a = VistaLt.Instance(1,objUsuario)
                            a.setWindowTitle('LeaderTeacher')
                            a.show()
                        else:
                            QMessageBox.information(self, "Login",
                                                    "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                    "por lo tanto su cuenta fue inhabilitada, por favor\n"
                                                    "contacte al administrador para reactivarla")
                elif tipoUsuario == 'masterteacher':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        w = MainWindow.Instance(1,objUsuario)
                        w.setWindowTitle('MasterTeacher')
                        w.show()
                    else:
                        if fechaAcceso >= fechaActual - delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            w = MainWindow.Instance(1,objUsuario)
                            w.setWindowTitle('MasterTeacher')
                            w.show()
                        else:
                            QMessageBox.information(self, "Login",
                                                    "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                    "por lo tanto su cuenta fue inhabilitada, por favor\n "
                                                    "contacte al administrador para reactivarla")
                elif tipoUsuario == 'digitador':
                    if fechaAcceso is None:
                        self.control.modificarFechaAcceso(username, fechaActual)
                        w = VistaDigitador.Instance()
                        w.setWindowTitle('Digitador')
                        w.show()
                    else:
                        if fechaAcceso >= fechaActual - delta:
                            self.control.modificarFechaAcceso(username, fechaActual)
                            w = VistaDigitador.Instance()
                            w.setWindowTitle('Digitador')
                            w.show()
                        else:
                            QMessageBox.information(self, "Login",
                                                    "Su ultimo acceso al sistema fue hace mas de 180 dias\n"
                                                    "por lo tanto su cuenta fue inhabilitada, por favor\n "
                                                    "contacte al administrador para reactivarla")
                else:
                    QMessageBox.information(self, "Login", "Perfil de usuario desconocido")
            else:
                QMessageBox.information(self, "Login", "Usuario o contrasena erroneos")


    def __del__(self):
        self.ui = None
