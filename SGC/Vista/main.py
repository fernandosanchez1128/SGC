import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from CrearAspirante import CrearAspirante
from RegistrarLT import RegistrarLT
from CrearPreinscripcion import CrearPreinscripcion

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project' )

    # create widget
    w = RegistrarLT()
    #w = CrearAspirante()
    #w= CrearPreinscripcion()
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
