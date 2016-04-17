# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <12/04/2016>
"""

from PyQt4.QtGui import QApplication
import sys
from View.Interface import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())