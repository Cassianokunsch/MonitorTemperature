# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from PyQt4.QtCore import QSize
from PyQt4.QtGui import (QFont, QTextEdit, QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox)
from View.LayoutTimeSampling import LayoutTimeSampling
from View.LayoutFile import LayoutFile
from View.LayoutSelectCOM import LayoutSelectCOM
from View.LayoutButtons import LayoutButtons


class LayoutInformations(QHBoxLayout):
    def __init__(self, parent):
        super(LayoutInformations, self).__init__()
        self.settings(parent)

    def settings(self, parent):
        # CRIANDO O GRUPOBOXINFOS PARA POR OS WIDGETS
        self.groupBoxInfos = QGroupBox(parent)
        self.groupBoxInfos.setMaximumSize(QSize(16777215, 16777215))

        # CRIANDO OS LAYOUT'S
        self.LayoutTimeSampling = LayoutTimeSampling(parent)
        self.LayoutFile = LayoutFile(parent)
        self.LayoutSelectCOM = LayoutSelectCOM(parent)
        self.LayoutButtons = LayoutButtons(parent)

        self.creatTextBrowser()
        self.label()

        self.verticalLayoutInformations = QVBoxLayout(self.groupBoxInfos)
        self.verticalLayoutInformations.setMargin(11)
        self.verticalLayoutInformations.setSpacing(6)

        # ADICOINANDO O LAYOUT TIME AMOSTRAGEM, LABEL, LAYOUT ARQUIVO,
        # TEXTO LOG E GRID NO LAYOUT VERTICAL
        self.verticalLayoutInformations.addLayout(self.LayoutTimeSampling)
        self.verticalLayoutInformations.addWidget(self.lbArquivo)
        self.verticalLayoutInformations.addLayout(self.LayoutFile)
        self.verticalLayoutInformations.addLayout(self.LayoutSelectCOM)
        self.verticalLayoutInformations.addWidget(self.TextLog)
        self.verticalLayoutInformations.addLayout(self.LayoutButtons)

        # ADICIONANDO O GRUPOBOX NO LAYOUT INFOS
        self.addWidget(self.groupBoxInfos)

    def creatTextBrowser(self):
        # DEFININDO O TAMANHO DA FONTE
        font = QFont()
        font.setPointSize(11)

        # CRIANDO O TEXTO DE LOG
        self.TextLog = QTextEdit(self.groupBoxInfos)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum,  QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLog.sizePolicy().hasHeightForWidth())
        self.TextLog.setReadOnly(True)
        # self.TextLog.setEnabled(False)
        self.TextLog.setFont(font)
        self.TextLog.setSizePolicy(sizePolicy)
        self.TextLog.setMaximumSize(QSize(600, 100))

    def label(self):
        # CRIANDO O LABEL PARA SELECIONAR O LOCAL DO ARQUIVO
        self.lbArquivo = QLabel(self.groupBoxInfos)
        self.lbArquivo.setText("Selecione onde quer salvar o novo arquivo: ")
