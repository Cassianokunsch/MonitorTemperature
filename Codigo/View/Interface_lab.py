# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""

from PyQt4 import QtCore, QtGui
from Controle.Conversor import Conversor
from time import strftime


class AplicativoConversor(QtGui.QMainWindow):
    def __init__(self):
        super(AplicativoConversor, self).__init__()
        self.setupUi()

    def setupUi(self):
        # SETANDO O TAMANHO MAXIMO
        self.resize(675, 365)
        self.setMinimumSize(675, 365)
        self.setMaximumSize(675, 365)
        self.setWindowTitle("Xlsx 2 Txt")
        self.setWindowIcon(QtGui.QIcon("View\\Imagens\\icone.ico"))

        # Widget principal
        self.centralWidget = QtGui.QWidget(self)

        # Layout pricipal
        self.LayoutPrincipal = QtGui.QHBoxLayout(self.centralWidget)
        self.LayoutPrincipal.setMargin(3)
        self.LayoutPrincipal.setSpacing(3)

        self.LayoutWidget = QtGui.QVBoxLayout()
        self.LayoutWidget.setMargin(3)
        self.LayoutWidget.setSpacing(3)

        # CRIANDO TODOS OS LAYOUTS
        self.criaLayoutImagem()
        self.criaLayoutArqOri()
        self.criaLayoutArqDes()
        self.criaLayoutConversao()
        self.criaLayoutBtnConversao()

        # ADICIONANDO TODOS OS LAYOUTS NO LAYOUT PRINCIPAL
        self.LayoutWidget.addLayout(self.LayoutImagem)
        self.LayoutWidget.addLayout(self.LayoutArqOrigem)
        self.LayoutWidget.addLayout(self.LayoutArqDestino)
        self.LayoutWidget.addLayout(self.LayoutConversao)
        self.LayoutWidget.addLayout(self.LayoutBtnConversao)

        self.criaMenu()
        self.criaStatus()

        self.LayoutPrincipal.addLayout(self.LayoutWidget)

        self.setCentralWidget(self.centralWidget)

    def criaLayoutImagem(self):
        self.LBImagem = QtGui.QLabel()
        self.LBImagem.setPixmap(QtGui.QPixmap(("View\\Imagens\\title.png")))
        self.LBImagem.setAlignment(QtCore.Qt.AlignCenter)
        self.LayoutImagem = QtGui.QVBoxLayout()
        self.LayoutImagem.addWidget(self.LBImagem)

    def criaLayoutArqOri(self):
        # LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqOrigem = QtGui.QHBoxLayout()
        self.LayoutArqOrigem.setMargin(3)
        self.LayoutArqOrigem.setSpacing(3)

        # BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        ## CRIANDO OS BOTOES
        self.LbSelectArq = QtGui.QLabel("Selecione o arquivo que quer converter:", self.centralWidget)
        self.LEditArqOrig = QtGui.QLineEdit(self.centralWidget)
        self.LEditArqOrig.setReadOnly(True)
        self.btn_browser1 = QtGui.QPushButton("Browser...", self.centralWidget)
        self.btn_browser1.clicked.connect(self.pegaArqOrigem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(("View\\Imagens\\pasta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_browser1.setIcon(icon)

        ## ADICIONANDO OS BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqOrigem.addWidget(self.LbSelectArq)
        self.LayoutArqOrigem.addWidget(self.LEditArqOrig)
        self.LayoutArqOrigem.addWidget(self.btn_browser1)

    def criaLayoutArqDes(self):
        # LAYOUT DO SELECIONAR ARQUIVO DE DESTINO
        self.LayoutArqDestino = QtGui.QHBoxLayout()
        self.LayoutArqDestino.setMargin(3)
        self.LayoutArqDestino.setSpacing(3)

        # BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE DESTINO
        ## CRIANDO OS BOTOES
        self.LbArqDes = QtGui.QLabel("Selecione onde quer salvar o novo arquivo:", self.centralWidget)
        self.LEditArqDes = QtGui.QLineEdit(self.centralWidget)
        self.LEditArqDes.setReadOnly(True)
        self.BtnBrowser2 = QtGui.QPushButton("Browser...", self.centralWidget)
        self.BtnBrowser2.clicked.connect(self.pegaArqDestino)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(("View\\Imagens\\pasta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnBrowser2.setIcon(icon)

        ## ADICIONANDO OS BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqDestino.addWidget(self.LbArqDes)
        self.LayoutArqDestino.addWidget(self.LEditArqDes)
        self.LayoutArqDestino.addWidget(self.BtnBrowser2)

    def criaLayoutConversao(self):
        # LAYOUT DO QUE MOSTRA O STATUS DA CONVERSAO
        self.LayoutConversao = QtGui.QVBoxLayout()
        self.LayoutConversao.setMargin(3)
        self.LayoutConversao.setSpacing(3)

        # BOTOES DO LAYOUT QUE MOSTRA O STATUS DA CONVERSAO
        ## CRIANDO OS BOTOES
        self.CxTexto = QtGui.QTextEdit(self.centralWidget)
        self.CxTexto.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CxTexto.setFont(font)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA O STATUS DA CONVERSAO
        self.LayoutConversao.addWidget(self.CxTexto)

    def criaLayoutBtnConversao(self):
        # LAYOUT DO QUE TEM OS BOTOES PARA SAIR E CONVERTER
        self.LayoutBtnConversao = QtGui.QHBoxLayout()
        self.LayoutBtnConversao.setMargin(3)
        self.LayoutBtnConversao.setSpacing(3)

        # BOTOES DO LAYOUT QUE TEM OS BOTOES PARA SAIR E CONVERTER
        ## CRIANDO OS BOTOES
        spacerItem = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.BtnConverter = QtGui.QPushButton(" Converter!", self.centralWidget)
        self.BtnConverter.clicked.connect(self.startConversor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("View\\Imagens\\start_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnConverter.setIcon(icon1)

        self.BtnSair = QtGui.QPushButton(" Sair", self.centralWidget)
        self.BtnSair.clicked.connect(self.close)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("View\\Imagens\\log_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSair.setIcon(icon2)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA OS BOTOES DE CONVERTER E SAIR
        self.LayoutBtnConversao.addItem(spacerItem)
        self.LayoutBtnConversao.addWidget(self.BtnConverter)
        self.LayoutBtnConversao.addWidget(self.BtnSair)

    def creatProgressBar(self):
        if (self.LayoutConversao.count() == 2):
            self.progressBar.close()
            self.LayoutConversao.removeWidget(self.progressBar)
        self.progressBar = QtGui.QProgressBar()
        self.LayoutConversao.addWidget(self.progressBar)
        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def startConversor(self):
        if self.LEditArqOrig.text() != '' and self.LEditArqDes.text() != '':
            self.BtnConverter.setEnabled(False)
            self.CxTexto.clear()
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Convertendo arquivo...\n")
            self.CxTexto.moveCursor(QtGui.QTextCursor.End)
            self.dadosArquivo = []
            self.controlador = [0, 0, 0]
            self.abreArquivoXlsx()
        else:
            reply = QtGui.QMessageBox.critical(self, 'Aviso', "Insira arquivos válidos", QtGui.QMessageBox.Ok)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Arquivo salvo com sucesso!!!\n")
            self.BtnConverter.setEnabled(True)

        if self.dadosArquivo != [] and self.step < 50:
            self.tamanho = self.dadosArquivo[0] * self.controlador[1]
            if self.controlador[0] <= (self.dadosArquivo[0] * self.controlador[1]):
                self.step = ((len(self.dadosArquivo)-1)*50)//self.dadosArquivo[0]
                self.progressBar.setValue(self.step)

        if self.step >= 50:
            if self.controlador[2] <= (self.tamanho):
                self.step = (self.controlador[2]*50)/self.tamanho + 50
                self.progressBar.setValue(self.step)

        if self.step == 50:
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Conversão concluida com sucesso!!!\n")
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " Salvando arquivo...\n")
            Conversor.starThreadGravadora(self.nome_arquivoDestino, self.dadosArquivo, self.controlador)

    def doAction(self):
        self.timer.isActive()
        self.timer.start(100, self)

    def pegaArqOrigem(self):
        reply = QtGui.QMessageBox.information(self, 'Aviso', "Por favor insira o arquivo xlsx pra conversão", QtGui.QMessageBox.Ok)
        self.nome_arquivoOrigem = QtGui.QFileDialog.getOpenFileName(self, "Selecionar o arquivo xlsx", filter="All(*.xlsx)")
        self.LEditArqOrig.setText(self.nome_arquivoOrigem)

    def pegaArqDestino(self):
        reply = QtGui.QMessageBox.information(self,'Aviso',"Selecione a pasta para salvar o arquivo", QtGui.QMessageBox.Ok)
        self.nome_arquivoDestino = QtGui.QFileDialog.getSaveFileName(self, "Selecionar o local para salvar o arquivo", filter="All(*.txt)")  ##Abre um arquivo
        self.LEditArqDes.setText(self.nome_arquivoDestino)

    def abreArquivoXlsx(self):
        try:
            arquivoXlsx = open(self.nome_arquivoOrigem, "rt")
            arquivoXlsx.close()
            Conversor.starThreadConversora(self.dadosArquivo, self.nome_arquivoOrigem, self.controlador)
            self.creatProgressBar()
            self.progressBar.setValue(self.step)
            self.doAction()
        except:
            if (self.LayoutConversao.count() == 2):
                self.progressBar.close()
                self.LayoutConversao.removeWidget(self.progressBar)
            self.CxTexto.setTextColor(QtGui.QColor("red"))
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]') + " ERRO: ARQUIVO NÃO EXISTENTE\n")
            self.BtnConverter.setEnabled(True)
            self.CxTexto.setTextColor(QtGui.QColor("black"))

    def criaMenu(self):
        self.menuBar = QtGui.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.setMenuBar(self.menuBar)

    def criaStatus(self):
        self.statusBar = QtGui.QStatusBar(self)
        self.setStatusBar(self.statusBar)