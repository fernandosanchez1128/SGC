import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#from vistacoordinador import VistaCoordinador
from PreinscribirLT import PreinscribirLT
from RegistrarLT import RegistrarLT

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project' )

    # create widget
    #w = RegistrarLT()
    w = PreinscribirLT()
    #w.setWindowTitle( 'Pre' )
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
