# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from PyQt4.QtGui import (QSpacerItem, QSizePolicy, QHBoxLayout,
                         QPushButton, QIcon, QPixmap)


class LayoutButtons(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutButtons, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                  QSizePolicy.Minimum)

        # CRIANDO O BOTAO DE START
        self.buttonStart = QPushButton(parent)
        self.buttonStart.setText("Start")
        self.buttonStart.clicked.connect(parent.authenticationData)
        icon = QIcon()
        diretorio = "View\\Imagens\\start_icon.png"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.buttonStart.setIcon(icon)

        # CRIANDO O BOTAO DE STOP
        self.buttonStop = QPushButton(parent)
        self.buttonStop.setText("Stop")
        self.buttonStop.clicked.connect(parent.stopThreads)
        self.buttonStop.setDisabled(True)

        # ADICIONANDO O BOTAO START E O BOTAO DE STOP NO GRID DE COMANDOS
        self.addItem(spacerItem1)
        self.addWidget(self.buttonStart)
        self.addWidget(self.buttonStop)
