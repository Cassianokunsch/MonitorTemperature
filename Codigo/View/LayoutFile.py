# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from PyQt4.QtGui import (QPushButton, QLineEdit, QIcon, QPixmap, QHBoxLayout)


class LayoutFile(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutFile, self).__init__()
        self.parent = parent
        self.settings()

    def settings(self):
        # CRIANDO O LINEEDIT PARA MOSTRAR O CAMINHO DO ARQUIVO
        self.lineEditWay = QLineEdit(self.parent)
        self.lineEditWay.setReadOnly(True)

        self.addWidget(self.lineEditWay)

        # CRIANDO O BOTAO PARA SELECIONAR O ARQUIVO
        self.btnBrowser = QPushButton(self.parent)
        self.btnBrowser.setText("Browser...")
        self.btnBrowser.clicked.connect(self.parent.messageBox)
        icon = QIcon()
        diretorio = "View\\Imagens\\pasta.png"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.btnBrowser.setIcon(icon)

        # ADIONANDO OS WIDGETS NO LAYOUT
        self.addWidget(self.btnBrowser)
