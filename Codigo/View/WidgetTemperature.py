# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import (QGridLayout, QHBoxLayout, QVBoxLayout, QWidget,
                         QMessageBox, QFileDialog, QColor, QTextCursor)
from View.BoxTemperature import LayoutTemperature
from View.BoxInformations import LayoutInformations
from time import strftime
import datetime


class WidgetTemperatures(QWidget):
    def __init__(self, parent, Model, Controle):
        super(WidgetTemperatures, self).__init__()
        self.model = Model
        self.controle = Controle
        self.addLayout()
        self.verificaArduino()

    def addLayout(self):
        self.verticalLayouts = QVBoxLayout()
        self.verticalLayouts.setMargin(11)
        self.verticalLayouts.setSpacing(6)

        # CRIANDO BOX DE TEMPERATURAS
        self.LayoutInfos = LayoutInformations(self)
        self.LayoutTemps = LayoutTemperature(self)

        self.verticalLayouts.addLayout(self.LayoutTemps)
        self.verticalLayouts.addLayout(self.LayoutInfos)

        # self.horizontalMaior = QHBoxLayout()
        # self.horizontalMaior.setMargin(11)
        # self.horizontalMaior.setSpacing(6)

        # self.horizontalMaior.addLayout(self.verticalLayouts)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)

        self.gridLayout.addLayout(self.verticalLayouts, 0, 0, 1, 1)

    def verificaArduino(self):
        combo = self.LayoutInfos.LayoutSelectCOM.comboBox
        AllItems = [combo.itemText(i) for i in range(combo.count())]
        mensagem = 'Nenhum dispositivo conectado. Reinicie o programa.'
        if mensagem in AllItems:
            self.LayoutInfos.LayoutButtons.buttonStart.setDisabled(True)
            self.LayoutInfos.LayoutFile.btnBrowser.setDisabled(True)

    def authenticationData(self):
        if self.LayoutInfos.LayoutFile.lineEditWay.text() != "":
            self.startThreadMonitora()
            self.startThreadBackup()
        else:
            typeMsg = "Aviso"
            msgSelecionaArq = "Preencha os campos corretamente!"
            reply = QMessageBox.critical(self, typeMsg, msgSelecionaArq, QMessageBox.Ok)

    def setInformation(self, information, color):
        self.LayoutInfos.TextLog.setTextColor(QColor(color))
        self.info = strftime('[%H:%M:%S]') + information
        # ADICIONANDO OS DADOS NO "BANCO" AHAHAHAHAHAA
        self.model.appendDateLog(self.info)
        self.LayoutInfos.TextLog.insertPlainText(self.info)
        self.LayoutInfos.TextLog.moveCursor(QTextCursor.End)

    def on_offButtons(self):
        self.LayoutInfos.LayoutButtons.buttonStart.setDisabled(True)
        self.LayoutInfos.LayoutButtons.buttonStop.setDisabled(False)

    def startThreadMonitora(self):
        self.on_offButtons()
        # PEGANDO A HORA EM QUE COMEÇA O MONITORAMENTO
        self.model.appendDateLog(datetime.datetime.now())
        self.setInformation("Iniciando monitoramento...\n", "black")
        time = self.LayoutInfos.LayoutTimeSampling.LETimeAmostragem.text()
        if time == "":
            self.LayoutInfos.LayoutTimeSampling.LETimeAmostragem.setText("2")
            time = 2
        port = self.selectionPortCOM()
        # INSTANCIANDO A THREAD, CONECTANDO-A A UM EVENTO E INICIANDO-A
        self.threadMonitora = self.controle.instThreadMonitora(time, port)
        self.connect(self.threadMonitora, SIGNAL("updateTemps(PyQt_PyObject, QString)"), self.updateTemps)
        self.controle.startThreadMonitora(self.threadMonitora)
        self.setInformation("Monitorando...\n", "black")

    def startThreadBackup(self):
        diretorioArqDestino = self.LayoutInfos.LayoutFile.lineEditWay.text()
        lst_dados = self.model.getDateTemperature()
        self.threadBackup = self.controle.instThreadBackup(diretorioArqDestino, lst_dados)
        self.connect(self.threadBackup, SIGNAL("saveFile(QString, QString)"), self.setInformation)
        self.controle.startThreadBackup(self.threadBackup)

    def informationErro(self, temps):
        self.LayoutInfos.LayoutButtons.buttonStop.setEnabled(False)
        self.setInformation("Erro na leitura do termometro\n", "red")
        self.LayoutTemps.lcdTemp1.display(temps[0])
        self.LayoutTemps.lcdTemp2.display(temps[1])
        self.setInformation("Salvando desse ponto em diante...\n", "black")
        self.stopThreadBackup()
        self.startThreadGravadora()

    def updateTemps(self, temps, erro):
        if "Erro" == erro:
            self.informationErro(temps)
        else:
            if "-" in temps[0]:
                self.LayoutTemps.lcdTemp1.display(temps[0][:6])
            if "-" in temps[1]:
                self.LayoutTemps.lcdTemp2.display(temps[1][:6])
            else:
                self.LayoutTemps.lcdTemp1.display(temps[0][:5])
                self.LayoutTemps.lcdTemp2.display(temps[1][:5])
            self.saveDados(temps)

    def saveDados(self, dados):
        self.model.appendDateTemperature(dados)

    def stopThreads(self):
        # PARANDO A THREAD DE MONITORAMENTO E DESABILITANDO O BOTAO DE STOP
        self.LayoutInfos.LayoutButtons.buttonStop.setEnabled(False)
        self.stopThreadMonitora()
        self.stopThreadBackup()

    def stopThreadMonitora(self):
        self.controle.stopThreadMonitora(self.threadMonitora)
        self.startThreadGravadora()

    def startThreadGravadora(self):
        diretorio = self.LayoutInfos.LayoutFile.lineEditWay.text()
        message = "Arquivo salvo com sucesso!!!\n"
        lst_dados = self.model.getDateTemperature()
        self.threadGravadora = self.controle.instThreadGravadora(diretorio, lst_dados, message)
        self.connect(self.threadGravadora, SIGNAL("saveFile(QString, QString)"),  self.saveLog)
        self.controle.startThreadGravadora(self.threadGravadora)

    def saveLog(self, info, color):
        self.setInformation(info, color)
        # PEGANDO A HORA FINAL DO SOFTWARE
        self.model.appendDateLog(datetime.datetime.now())
        self.startLog()

    def startLog(self):
        diretorio = self.LayoutInfos.LayoutFile.lineEditWay.text()
        lst_dados = self.model.getDateLog()
        self.threadLog = self.controle.instThreadLog(diretorio, lst_dados)
        self.controle.startThreadLog(self.threadLog)

    def stopThreadBackup(self):
        self.controle.stopThreadBackup(self.threadBackup)

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
            self.LayoutInfos.LayoutFile.lineEditWay.setText(file)

    def selectionPortCOM(self):
        return self.LayoutInfos.LayoutSelectCOM.comboBox.currentText()
