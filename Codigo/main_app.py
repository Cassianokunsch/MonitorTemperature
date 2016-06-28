# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Arquivo que inicia a interface. >

author: Cassiano Kunsch das Neves
last edited: <12/04/2016>
"""

from PyQt4.QtGui import QApplication
import sys
from View.MainWindow import MainWindow
from Controle.Controle import Control
from Model.Model import Model


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = Control()
        self.main_view = MainWindow(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
