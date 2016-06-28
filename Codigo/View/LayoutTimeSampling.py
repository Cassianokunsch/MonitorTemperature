# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from PyQt4.QtCore import Qt, QSize
from PyQt4.QtGui import (QSpacerItem, QSizePolicy, QHBoxLayout, QLabel, QLineEdit, QIntValidator)

class LayoutTimeSampling(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutTimeSampling, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        # CRIANDO LABEL PARA SELECIONAR O TEMPO DE AMOSTRAGEM
        self.lbTimeAmostragem = QLabel(parent)
        mensagem = "Digite o tempo de amostragem em segundos (Deve ser no mínimo 2 segundos): "
        self.lbTimeAmostragem.setText(mensagem)
        self.lbTimeAmostragem.setAlignment(Qt.AlignCenter)

        # CRIANDO O LINEEDIT PARA SELECIONAR O TEMPO DE AMOSTRAGEM
        self.LETimeAmostragem = QLineEdit(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LETimeAmostragem.sizePolicy().hasHeightForWidth())
        self.LETimeAmostragem.setSizePolicy(sizePolicy)
        self.LETimeAmostragem.setMaximumSize(QSize(40, 16777215))
        self.LETimeAmostragem.setLayoutDirection(Qt.LeftToRight)
        self.validator = QIntValidator(0, 999999, self)
        self.LETimeAmostragem.setValidator(self.validator)

        # CRIANDO UM SPACER PARA ORGANIZAR DENTRO DO LAYOUT OS ITENS
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # ADICIONANDO OS WIDGETS NO LAYOUT
        self.addWidget(self.lbTimeAmostragem)
        self.addWidget(self.LETimeAmostragem)
        self.addItem(spacerItem)
