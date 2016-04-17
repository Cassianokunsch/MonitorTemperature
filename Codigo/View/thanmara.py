

from PyQt4.QtGui import QMainWindow, QApplication, QPushButton
import sys


class Thanmara(QMainWindow):
    def __init__(self):
        super(Thanmara, self).__init__(None)
        self.resize(400, 400)
        self.botao = QPushButton('Thanmara', self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Thanmara()
    ui.show()
    sys.exit(app.exec_())