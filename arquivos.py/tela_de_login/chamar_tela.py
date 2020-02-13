from validador import fazer_login, validar
#from inter import *
from tela_login_ import *
import sys

class forms(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_tela_login()
        self.ui.setupUi(self)

        def logar():
            email = self.ui.lineEdit.text()
            senha = self.ui.lineEdit_2.text()
            resultado = fazer_login(email, senha)
            if 200 in resultado:
                print('\033[1;32m+'+  '\033[0;0m Login realizado com sucesso!')
                if validar(resultado[0]) == "OK":
                    print('Entrou')

            else:
                self.ui.aviso.setText('Erro! Email ou Senha inválido!')
        QtCore.QObject.connect(self.ui.bt_login, QtCore.SIGNAL('clicked()'), logar)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = forms()
    myapp.show()
    sys.exit(app.exec_())
