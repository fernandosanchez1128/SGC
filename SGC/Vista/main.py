import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

<<<<<<< .merge_file_hxBjsc
from vistacoordinador import VistaCoordinador
#from VistaMt import MainWindow
=======
from VistaLogin import VistaLogin
>>>>>>> .merge_file_Jk2KBc

if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')
<<<<<<< .merge_file_hxBjsc
    # create widget
    w = VistaCoordinador.Instance()
=======
    print "hola"
    w = VistaLogin()
>>>>>>> .merge_file_Jk2KBc
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
