# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <15/04/2016>
"""

from PyQt4.QtCore import (SIGNAL, QRect, Qt)
from PyQt4.QtGui import (QMainWindow, QGridLayout, QHBoxLayout, QLCDNumber, QLabel, QFileDialog,
                         QVBoxLayout, QGroupBox, QPushButton, QWidget, QComboBox, QLineEdit, QIcon, QPixmap, QMessageBox)

from Controle.Controle import ThreadMonitora, ComunicacaoArduino, ThreadTime, ControlInterface

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        self.setupUi()
        self.serial = ComunicacaoArduino.start_communication()
        self.controle = ControlInterface()
        self.dadosTempo = []
        self.dados = []

    def startThreadTime(self):
        #self.thTime = ControlInterface()
        self.controle.starThreadTime(self)
        #self.connect(self.th, SIGNAL("updade(QString)"), self.setTime)
        #self.thTime = ThreadTime()
        #self.thTime.connect(self.thTime, SIGNAL("updade(QString)"), self.setTime)
        #self.thTime.start()

    def startThreadMonitora(self):
        self.buttonStart.setDisabled(True)
        self.buttonStop.setDisabled(False)
        self.controle.starThreadMonitora(self.serial, self)
        #self.workThread = ThreadMonitora(self.serial)
        #self.workThread.connect(self.workThread, SIGNAL("PyQt_PyObject"), self.setTemps)
        #self.workThread.start()

    def stopThreadMonitora(self):
        self.controle.stopThreadMonitora()
        #self.workThread.terminate()
        #GravaArquivo.startGravacao(self.LEditArqDes.text(), self.dados)
        self.controle.starThreadGravadora(self.LEditArqDes.text(), self.dados)

    def stopThreadTime(self):
        #self.thTime.stopThreadTime()
        self.controle.stopThreadTime()

    def startThreads(self):
        if self.LEditArqDes.text() != '':
            self.startThreadMonitora()
            self.startThreadTime()
        else:
            reply = QMessageBox.critical(self, 'Aviso', "Selecione onde quer salvar o arquivo!", QMessageBox.Ok)

    def stopThreads(self):
        self.stopThreadMonitora()
        self.stopThreadTime()

    def setTemps(self, temps):
        self.lcdTemp1.display(temps[0])
        self.lcdTemp2.display(temps[1])
        temps.append(self.dadosTempo[len(self.dadosTempo)-1])
        self.dados.append(temps)

    def setTime(self, time):
        if time not in self.dadosTempo:
            self.lcdTime.display(time)
            self.dadosTempo.append(time)

    def setupUi(self):
        self.setMaximumSize(580, 460)
        self.setMinimumSize(580, 460)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)

        self.cboxSetupAndActions()
        self.cboxTemps()
        self.currentTime()

    def cboxSetupAndActions(self):
        self.HLayoutSetupAndActions = QHBoxLayout()
        self.HLayoutSetupAndActions.setMargin(11)
        self.HLayoutSetupAndActions.setSpacing(6)

        self.groupBoxSetupAndActions = QGroupBox(self.centralWidget)
        self.groupBoxSetupAndActions.setTitle("Configurações e Ações")

        self.buttonStart = QPushButton(self.groupBoxSetupAndActions)
        self.buttonStart.setGeometry(QRect(270, 80, 121, 23))
        self.buttonStart.setText("Start")
        self.buttonStart.clicked.connect(self.startThreads)

        self.buttonStop = QPushButton(self.groupBoxSetupAndActions)
        self.buttonStop.setGeometry(QRect(400, 80, 121, 23))
        self.buttonStop.setText("Stop")
        self.buttonStop.clicked.connect(self.stopThreads)
        self.buttonStop.setDisabled(True)

        self.LbArqDes = QLabel("Selecione onde quer salvar o novo arquivo:", self.groupBoxSetupAndActions)
        self.LbArqDes.setGeometry(QRect(20, 20, 220, 16))

        self.LEditArqDes = QLineEdit(self.groupBoxSetupAndActions)
        self.LEditArqDes.setReadOnly(True)
        self.LEditArqDes.setGeometry(QRect(20, 40, 350, 21))

        self.BtnBrowser2 = QPushButton("Browser...", self.groupBoxSetupAndActions)
        self.BtnBrowser2.clicked.connect(self.pegaArqDestino)
        self.BtnBrowser2.setGeometry(QRect(370, 39, 80, 23))
        icon = QIcon()
        icon.addPixmap(QPixmap(("View\\Imagens\\pasta.png")), QIcon.Normal, QIcon.Off)
        self.BtnBrowser2.setIcon(icon)

        self.HLayoutSetupAndActions.addWidget(self.groupBoxSetupAndActions)

        self.gridLayout.addLayout(self.HLayoutSetupAndActions, 2, 0, 1, 1)

    def cboxTemps(self):
        self.hlLcdsTemp = QHBoxLayout()
        self.hlLcdsTemp.setMargin(11)
        self.hlLcdsTemp.setSpacing(6)

        self.groupBoxLcdsTemp = QGroupBox(self.centralWidget)

        self.lbTemp1 = QLabel(self.groupBoxLcdsTemp)
        self.lbTemp1.setGeometry(QRect(70, 10, 127, 10))
        self.lbTemp1.setText('Termômetro 1')
        self.lbTemp1.setAlignment(Qt.AlignCenter)

        self.lbTemp2 = QLabel(self.groupBoxLcdsTemp)
        self.lbTemp2.setGeometry(QRect(330, 10, 130, 10))
        self.lbTemp2.setText('Termômetro 2')
        self.lbTemp2.setAlignment(Qt.AlignCenter)

        self.lcdTemp1 = QLCDNumber(self.groupBoxLcdsTemp)
        self.lcdTemp1.setGeometry(QRect(30, 30, 211, 71))
        self.lcdTemp1.display("00.00")

        self.lcdTemp2 = QLCDNumber(self.groupBoxLcdsTemp)
        self.lcdTemp2.setGeometry(QRect(290, 30, 211, 71))
        self.lcdTemp2.display("00.00")

        self.hlLcdsTemp.addWidget(self.groupBoxLcdsTemp)

        self.gridLayout.addLayout(self.hlLcdsTemp, 0, 0, 1, 1)

    def currentTime(self):
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)

        self.groupBox_2 = QGroupBox(self.centralWidget)
        self.groupBox_2.setTitle("")

        self.lbCurrentTime = QLabel(self.groupBox_2)
        self.lbCurrentTime.setGeometry(QRect(230, 0, 91, 20))
        self.lbCurrentTime.setText("Tempo percorrido")

        self.lcdTime = QLCDNumber(self.groupBox_2)
        self.lcdTime.setGeometry(QRect(140, 20, 251, 81))
        self.lcdTime.setDigitCount(8)
        self.lcdTime.display("00:00:00")

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

    def pegaArqDestino(self):
        reply = QMessageBox.information(self, 'Aviso', "Selecione a pasta para salvar o arquivo",
                                              QMessageBox.Ok)
        self.nome_arquivoDestino = QFileDialog.getSaveFileName(self, "Selecionar o local para salvar o arquivo",
                                                                     filter="All(*.csv)")  ##Abre um arquivo
        self.LEditArqDes.setText(self.nome_arquivoDestino)

