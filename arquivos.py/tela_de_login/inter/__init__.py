from interface import *

class Main(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def iniciar():
    if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        myapp = Main()
        myapp.show()
        sys.exit(app.exec_())
