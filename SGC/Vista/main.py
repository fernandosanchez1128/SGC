import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from vistacoordinador import VistaCoordinador
#from VistaMt import MainWindow
from VistaLogin import VistaLogin


if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')

    # create widget
    w = VistaCoordinador.Instance()

    print "hola"
    w = VistaLogin()

    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
