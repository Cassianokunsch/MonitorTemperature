# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from PyQt4.QtCore import Qt, QSize, QRect
from PyQt4.QtGui import (QHBoxLayout, QLCDNumber, QLabel, QGroupBox)


class LayoutTemperature(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutTemperature, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        # CRIANDO O GRUPOBOXTEMPS PARA POR OS LABELS E LCD'S
        self.groupBoxTemps = QGroupBox(parent)

        # CRIANDO O LABEL PARA INFORMAR O QUE O LCD ESTÁ MOSTRANDO
        self.lbTemp1 = QLabel(self.groupBoxTemps)
        self.lbTemp1.setGeometry(QRect(70, 10, 127, 10))
        self.lbTemp1.setMaximumSize(QSize(16777215, 10))
        self.lbTemp1.setText("Termometro 1")
        self.lbTemp1.setAlignment(Qt.AlignCenter)

        # CRIANDO O LABEL PARA INFORMAR O QUE O LCD ESTÁ MOSTRANDO
        self.lbTemp2 = QLabel(self.groupBoxTemps)
        self.lbTemp2.setGeometry(QRect(330, 10, 130, 10))
        self.lbTemp2.setMaximumSize(QSize(16777215, 10))
        self.lbTemp2.setText("Termometro 2")
        self.lbTemp2.setAlignment(Qt.AlignCenter)

        # CRIANDO O LCD PARA INFORMAR A TEMPERATURA DO TERMOMETRO 1
        self.lcdTemp1 = QLCDNumber(self.groupBoxTemps)
        self.lcdTemp1.setGeometry(QRect(30, 30, 211, 71))
        self.lcdTemp1.display("00.00")
        self.lcdTemp1.setDigitCount(6)

        # CRIANDO O LCD PARA INFORMAR A TEMPERATURA DO TERMOMETRO 2
        self.lcdTemp2 = QLCDNumber(self.groupBoxTemps)
        self.lcdTemp2.setGeometry(QRect(290, 30, 211, 71))
        self.lcdTemp2.display("00.00")
        self.lcdTemp2.setDigitCount(6)

        # COLOCANDO LAYOUT NO GRUPOBOXTEMPS
        self.addWidget(self.groupBoxTemps)
