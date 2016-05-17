# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Arquivo que inicia a interface. >

author: Cassiano Kunsch das Neves
last edited: <12/04/2016>
"""

from PyQt4.QtGui import QApplication
import sys
from View.Interface import InterfaceMonitora

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = InterfaceMonitora()
    ui.show()
    sys.exit(app.exec_())
