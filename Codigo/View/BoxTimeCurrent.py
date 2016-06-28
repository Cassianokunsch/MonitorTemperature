# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from PyQt4.QtCore import Qt, QSize, QRect, QTimer, SIGNAL
from PyQt4.QtGui import (QMainWindow, QFont, QSpacerItem, QStatusBar,
                         QTextEdit, QGridLayout, QSizePolicy, QColor,
                         QTextCursor, QHBoxLayout, QLCDNumber, QLabel,
                         QFileDialog, QVBoxLayout, QGroupBox, QPushButton,
                         QWidget, QLineEdit, QIcon, QTextBrowser, QPen,
                         QPixmap, QMessageBox, QIntValidator, QComboBox)


class LayoutTimeCurrent(QVBoxLayout):
    def __init__(self, parent):
        super(LayoutTimeCurrent, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        # CRIANDO O GRUPOBOXTIMECURRENTE PARA COLOCAR  O LABEL E O LCD
        # PARA CONTROLAR O TEMPO
        self.groupBoxTimeCurrent = QGroupBox(parent)

        # CRIANDO O LABEL DE INFORMAR O QUE É O LCD ESTÁ MOSTRANDO
        self.lbTimeCurrent = QLabel(self.groupBoxTimeCurrent)
        self.lbTimeCurrent.setGeometry(QRect(230, 0, 91, 20))
        self.lbTimeCurrent.setMaximumSize(QSize(16777215, 20))
        self.lbTimeCurrent.setText("Tempo percorrido")

        # CRIANDO O LCD PARA MOSTRAR O TEMPO PERCORRIDO
        self.lcdTimeCurrent = QLCDNumber(self.groupBoxTimeCurrent)
        self.lcdTimeCurrent.setGeometry(QRect(140, 20, 251, 81))
        self.lcdTimeCurrent.setDigitCount(8)
        self.lcdTimeCurrent.display("00:00:00")

        # COLOCANDO LAYOUT NO GRUPOBOXTIMECURRENT
        self.addWidget(self.groupBoxTimeCurrent)
