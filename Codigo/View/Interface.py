# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
import sys
import pyqtgraph as pg
import numpy as np
from PyQt4.QtCore import Qt, QSize, QRect, QTimer, SIGNAL
from PyQt4.QtGui import (QMainWindow, QFont, QSpacerItem, QStatusBar,
                         QTextEdit, QGridLayout, QSizePolicy, QColor,
                         QTextCursor, QHBoxLayout, QLCDNumber, QLabel,
                         QFileDialog, QVBoxLayout, QGroupBox, QPushButton,
                         QWidget, QLineEdit, QIcon, QTextBrowser, QPen,
                         QPixmap, QMessageBox, QIntValidator, QComboBox)
from time import strftime
from Controle.Controle import ControlInterface, ComunicacaoArduino


class InterfaceMonitora(QMainWindow):
    def __init__(self):
        super(InterfaceMonitora, self).__init__(None)
        self.dadosTempo = []
        self.dadosTemp1 = []
        self.dadosTemp2 = []
        self.dadosTempo3 = []
        self.dados = []
        self.controle = ControlInterface()
        self.setupUi()
        self.creatBoxTimeCurrent()
        self.creatBoxTemps()
        self.creatStatusBar()
        self.addLayout()

    def setupUi(self):
        #self.setMaximumSize(549, 537)
        self.setMinimumSize(1270, 600)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        icon = QIcon()
        diretorio = "View\\Imagens\\favicon.ico"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)

    def setWarning(self, warning):
        self.TextLog.setTextColor(QColor("red"))
        if len(warning) > 2:
            warning = strftime('[%H:%M:%S]') + warning

        self.TextLog.insertPlainText(warning)
        self.TextLog.moveCursor(QTextCursor.End)

    def setInformation(self, information):
        self.TextLog.setTextColor(QColor("black"))
        self.TextLog.insertPlainText(strftime('[%H:%M:%S]') + information)
        self.TextLog.moveCursor(QTextCursor.End)

    def onButtons(self):
        self.buttonStart.setDisabled(False)
        self.btnBrowser.setDisabled(False)

    def startThreads(self):
        if self.lineEditWay.text() != "":
            if self.LETimeAmostragem.text() == "":
                self.LETimeAmostragem.setText("2")
            self.startThreadTime()
            self.startThreadMonitora()
        else:
            typeMsg = "Aviso"
            msgSelecionaArq = "Preencha os campos corretamente!"
            reply = QMessageBox.critical(self, typeMsg, msgSelecionaArq,
                                         QMessageBox.Ok)

    def startThreadTime(self):
        self.controle.starThreadTime(self)

    def startThreadMonitora(self):
        self.buttonStart.setDisabled(True)
        self.buttonStop.setDisabled(False)
        tempoAmostragem = int(self.LETimeAmostragem.text())
        self.setInformation("Iniciando monitoramento...\n")
        self.controle.starThreadMonitora(self, tempoAmostragem, self.selectionPortCOM())
        self.setInformation("Monitorando...\n")

    def stopThreads(self):
        self.buttonStop.setEnabled(False)
        self.stopThreadTime()
        self.stopThreadMonitora()
        # self.stopThreadInTime()

    def informationReadTemps(self, Ntemp, lstTemps):
        self.buttonStop.setEnabled(False)
        self.setWarning("Erro na leitura do termometro " + str(Ntemp) + "!\n")
        self.setErroTemps(lstTemps)
        self.setInformation("Salvando desse ponto em diante...\n")
        self.stopThreadTime()
        self.stopThreadMonitora()

    def stopThreadMonitora(self):
        self.controle.stopThreadMonitora()
        diretorio = self.lineEditWay.text()
        self.controle.starThreadGravadora(diretorio, self.dados, self)

    def stopThreadTime(self):
        self.controle.stopThreadTime()

    def setErroTemps(self, temps):
        self.lcdTemp1.display(temps[0])
        self.lcdTemp2.display(temps[1])

    def setTemps(self, temps):
        if "Erro" in temps:
            for pos in range(len(temps)):
                if temps[pos] == "Erro":
                    self.informationReadTemps(pos, temps)
        else:
            self.lcdTemp1.display(temps[0])
            self.lcdTemp2.display(temps[1])
            temps.append(self.dadosTempo[len(self.dadosTempo) - 1])
            self.dados.append(temps)
            self.dadosTemp1.append(float(self.dados[len(self.dados)-1][0]))
            self.dadosTemp2.append(float(self.dados[len(self.dados)-1][1]))
            #self.dadosTempo3.append(float(self.dados[len(self.dados)-1][2]))
            self.emit(SIGNAL("Update(PyQt_PyObject, QString)"), self.dadosTemp1, "#FF0000")
            self.emit(SIGNAL("Update(PyQt_PyObject, QString)"), self.dadosTemp2, "#0000FF")
            #self.emit(SIGNAL("Update(PyQt_PyObject, QString)"), self.dadosTempo3, "#FF0000")

    def setTime(self, time):
        if time not in self.dadosTempo:
            self.lcdTimeCurrent.display(time)
            self.dadosTempo.append(time)

    def messageBox(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Selecione a pasta para salvar o arquivo")
        msg.setWindowTitle("Ajuda")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec() == QMessageBox.Ok:
            self.fileDialogSaveArq()

    def fileDialogSaveArq(self):
        dlg = QFileDialog(self)
        mensagem = "Selecionar o local para salvar o arquivo"
        file = dlg.getSaveFileName(self, mensagem, "", "All(*.csv)")
        if file:
            self.lineEditWay.setText(file)

    def creatBoxTimeCurrent(self):
        # CRIANDO UM LAYOUT HORIZONTAL PARA COLOCAR O GRUPOBOXTIMECURRENT
        self.LayoutTempoCurrent = QVBoxLayout()

        # CRIANDO O GRUPOBOXTIMECURRENTE PARA COLOCAR  O LABEL E O LCD
        # PARA CONTROLAR O TEMPO
        self.groupBoxTimeCurrent = QGroupBox(self.centralWidget)

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

        # COLOCANDO LAYOUT NO GRUPOBOXTIMECURRENT E ADICIONANDO O LAYOUT NO
        # GRIDLAYOUT PRINCIPAL
        self.LayoutTempoCurrent.addWidget(self.groupBoxTimeCurrent)
        #self.gridLayout.addLayout(self.LayoutTempoCurrent, 1, 0, 1, 1)

    def creatBoxTemps(self):
        # CRIANDO O LAYOUT HORIZONTAL PARA COLOCAR AS TEMPERATURAS
        self.LayoutTemps = QHBoxLayout()

        # CRIANDO O GRUPOBOXTEMPS PARA POR OS LABELS E LCD'S
        self.groupBoxTemps = QGroupBox(self.centralWidget)

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

        # COLOCANDO LAYOUT NO GRUPOBOXTEMPS E ADICIONANDO O LAYOUT NO
        # GRIDLAYOUT PRINCIPAL
        self.LayoutTemps.addWidget(self.groupBoxTemps)

        #self.gridLayout.addLayout(self.LayoutTemps, 0, 0, 1, 1)

    def creatLayoutTimeAmostragem(self):
        # CRIANDO O LAYOUT HORIZONTAL PARA POR O LABEL DE AMOSTRAGEM O
        # LINEEDIT DE AMOSTRAGEM
        self.HLayoutTimeAmostragem = QHBoxLayout()

        # CRIANDO LABEL PARA SELECIONAR O TEMPO DE AMOSTRAGEM
        self.lbTimeAmostragem = QLabel(self.groupBoxInfos)
        mensagem = "Digite o tempo de amostragem em segundos (Deve ser no mínimo 2 segundos): "
        self.lbTimeAmostragem.setText(mensagem)
        self.lbTimeAmostragem.setAlignment(Qt.AlignCenter)

        # CRIANDO O LINEEDIT PARA SELECIONAR O TEMPO DE AMOSTRAGEM
        self.LETimeAmostragem = QLineEdit(self.groupBoxInfos)
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
        self.HLayoutTimeAmostragem.addWidget(self.lbTimeAmostragem)
        self.HLayoutTimeAmostragem.addWidget(self.LETimeAmostragem)
        self.HLayoutTimeAmostragem.addItem(spacerItem)

    def creatLayoutArquivo(self):
        # CRIANDO O LABEL PARA SELECIONAR O LOCAL DO ARQUIVO
        self.lbArquivo = QLabel(self.groupBoxInfos)
        self.lbArquivo.setText("Selecione onde quer salvar o novo arquivo: ")

        # CRIANDO O LAYOUT HORIZONTAL PARA POR
        self.HLayoutArquivo = QHBoxLayout()

        # CRIANDO O LINEEDIT PARA MOSTRAR O CAMINHO DO ARQUIVO
        self.lineEditWay = QLineEdit(self.groupBoxInfos)
        self.lineEditWay.setReadOnly(True)

        self.HLayoutArquivo.addWidget(self.lineEditWay)

        # CRIANDO O BOTAO PARA SELECIONAR O ARQUIVO
        self.btnBrowser = QPushButton(self.groupBoxInfos)
        self.btnBrowser.setText("Browser...")
        self.btnBrowser.clicked.connect(self.messageBox)
        icon = QIcon()
        diretorio = "View\\Imagens\\pasta.png"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.btnBrowser.setIcon(icon)
        #self.btnBrowser.setDisabled(True)

        # ADIONANDO OS WIDGETS NO LAYOUT
        self.HLayoutArquivo.addWidget(self.btnBrowser)

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

    def creatLayoutBotoes(self):
        # CRIANDO O GRIDLAYOUT PARA OS COMANDOS E O SPACERITEM
        self.layoutBotoes = QHBoxLayout()
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                  QSizePolicy.Minimum)

        # CRIANDO O BOTAO DE START
        self.buttonStart = QPushButton(self.groupBoxInfos)
        self.buttonStart.setText("Start")
        self.buttonStart.clicked.connect(self.startThreads)
        icon = QIcon()
        diretorio = "View\\Imagens\\start_icon.png"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.buttonStart.setIcon(icon)
        #self.buttonStart.setDisabled(True)

        # CRIANDO O BOTAO DE STOP
        self.buttonStop = QPushButton(self.groupBoxInfos)
        self.buttonStop.setText("Stop")
        self.buttonStop.clicked.connect(self.stopThreads)
        self.buttonStop.setDisabled(True)

        # ADICIONANDO O BOTAO START E O BOTAO DE STOP NO GRID DE COMANDOS
        self.layoutBotoes.addItem(spacerItem1)
        self.layoutBotoes.addWidget(self.buttonStart)
        self.layoutBotoes.addWidget(self.buttonStop)

    def creatComboBox(self):
        # CRIANDO O LAYOUT PARA POR O COMBOBOX E O LABEL
        self.layoutComboBox = QHBoxLayout()

        # CRIANDO O COMBOBOX
        self.comboBox = QComboBox(self.groupBoxInfos)
        self.comboBox.currentIndexChanged.connect(self.selectionPortCOM)

        # LISTANDO AS PORTAS COM DISPONIVEIS
        self.lstPort = ComunicacaoArduino.find_ports()
        if self.lstPort == []:
            self.comboBox.addItem("Nenhum dispositivo conectado. Reinicie o programa.")
        else:
            self.comboBox.addItems(self.lstPort)

        # CRIANDO O LABEL
        mensagem = "Selecione a porta COM conectada ao Arduino: "
        self.labelComboBox = QLabel(mensagem, self.groupBoxInfos)

        # ADICIONANDO O COMBOBOX E O LABEL AO LAYOUT
        self.layoutComboBox.addWidget(self.labelComboBox)
        self.layoutComboBox.addWidget(self.comboBox)

    def selectionPortCOM(self):
        return self.comboBox.currentText()

    def creatStatusBar(self):
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def addLayout(self):
        # CRIANDO O LAYOUT HORIZONTAL PARA POR O GRUPOBOXINFOS
        self.LayoutInfos = QHBoxLayout()

        # CRIANDO O GRUPOBOXINFOS PARA POR OS WIDGETS
        self.groupBoxInfos = QGroupBox(self.centralWidget)
        self.groupBoxInfos.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4 = QVBoxLayout(self.groupBoxInfos)
        self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)

        # CRIANDO OS LAYOUT'S
        self.creatLayoutTimeAmostragem()
        self.creatLayoutArquivo()
        self.creatComboBox()
        self.creatTextBrowser()
        self.creatLayoutBotoes()
        self.graph()

        # ADICOINANDO O LAYOUT TIME AMOSTRAGEM, LABEL, LAYOUT ARQUIVO,
        # TEXTO LOG E GRID NO LAYOUT VERTICAL
        self.verticalLayout_4.addLayout(self.HLayoutTimeAmostragem)
        self.verticalLayout_4.addWidget(self.lbArquivo)
        self.verticalLayout_4.addLayout(self.HLayoutArquivo)
        self.verticalLayout_4.addLayout(self.layoutComboBox)
        self.verticalLayout_4.addWidget(self.TextLog)
        self.verticalLayout_4.addLayout(self.layoutBotoes)

        # ADICIONANDO O GRUPOBOX NO LAYOUT INFOS
        self.LayoutInfos.addWidget(self.groupBoxInfos)

        # ADICIONANDO O LAYOUT INFOS NO GRID PRINCIPAL
        #self.gridLayout.addLayout(self.LayoutInfos, 2, 0, 1, 1)

        self.verticalLayouts = QVBoxLayout()
        self.verticalLayouts.setMargin(11)
        self.verticalLayouts.setSpacing(6)
        self.verticalLayouts.addLayout(self.LayoutTemps)
        self.verticalLayouts.addLayout(self.LayoutTempoCurrent)
        self.verticalLayouts.addLayout(self.LayoutInfos)

        self.horizontalMaior = QHBoxLayout()
        self.horizontalMaior.setMargin(11)
        self.horizontalMaior.setSpacing(6)

        self.horizontalMaior.addLayout(self.verticalLayouts)
        self.horizontalMaior.addWidget(self.widget)

        self.gridLayout.addLayout(self.horizontalMaior, 0, 0, 1, 1)

    def graph(self):
        self.widget = QWidget(self.centralWidget)

        self.maxTime = 5
        self.graphTemp = pg.PlotWidget(title="Temperatura x Tempo")
        self.graphTemp.showGrid(True, True)
        self.graphTemp.setLabel('left', 'Temperatura', units='°C')
        self.graphTemp.setLabel('bottom', 'Tempo', units='s')
        #self.graphTemp.setRange(xRange=[3, self.maxTime], yRange=[-50, 50])

        self.connect(self, SIGNAL("Update(PyQt_PyObject, QString)"), self.update)

        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)

        self.gridLayout_2.addWidget(self.graphTemp, 0, 0, 1, 1)

    def update(self, list, color):
        self.graphTemp.plotItem.plot(list, pen=QPen(QColor(color)))

    def closeEvent(self, event):
        typeMsg = "Aviso"
        msgSair = "Deseja sair?"
        reply = QMessageBox.question(self, typeMsg, msgSair,
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.controle.stopThreadMonitora()
            self.controle.stopThreadTime()
        else:
            event.ignore()

class TimeAxisItem(pg.AxisItem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def tickStrings(self):
            # PySide's QTime() initialiser fails miserably and dismisses args/kwargs
            return [QTime().addMSecs(value).toString('mm:ss') for value in values]
