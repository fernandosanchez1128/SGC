import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistaLogin import *

#from mainwindow import MainWindow

if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')


    venCrear =  VistaLogin().exec_()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
