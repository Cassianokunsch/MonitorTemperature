# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from Controle.Controle import Control
from PyQt4.QtGui import (QHBoxLayout, QLabel, QComboBox)


class LayoutSelectCOM(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutSelectCOM, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        # CRIANDO O COMBOBOX
        self.comboBox = QComboBox(parent)

        # LISTANDO AS PORTAS COM DISPONIVEIS
        self.lstPort = Control.find_ports()
        if self.lstPort == []:
            self.comboBox.addItem("Nenhum dispositivo conectado. Reinicie o programa.")
        else:
            self.comboBox.addItems(self.lstPort)

        # CRIANDO O LABEL
        mensagem = "Selecione a porta COM conectada ao Arduino: "
        self.labelComboBox = QLabel(mensagem, parent)

        # ADICIONANDO O COMBOBOX E O LABEL AO LAYOUT
        self.addWidget(self.labelComboBox)
        self.addWidget(self.comboBox)
