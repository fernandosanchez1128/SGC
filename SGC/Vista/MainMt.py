__author__ = 'fernando'
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ORM.Usuario import Usuario
from VistaMt import MainWindow

if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')
    # create widget
    usuario = Usuario(cedula = "1",nombres = "diego" ,apellidos = "sanchez quintero")
    w = MainWindow.Instance(1,usuario)
    w.setWindowTitle( 'My PyQt4 QtGui Project' )
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )

