# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from PyQt4.QtGui import (QMainWindow, QIcon, QPixmap, QMessageBox)
from View.WidgetTemperature import WidgetTemperatures


class MainWindow(QMainWindow):
    def __init__(self, Model, Controle):
        super(MainWindow, self).__init__(None)
        self.setupUi(Model, Controle)

    def setupUi(self, Model, Controle):
        self.setMaximumSize(578, 430)
        self.setMinimumSize(578, 430)
        self.resize(578, 430)
        self.centralWidget = WidgetTemperatures(self, Model, Controle)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle("Monitor de Temperatura")

        icon = QIcon()
        diretorio = "View\\Imagens\\favicon.ico"
        icon.addPixmap(QPixmap(diretorio), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def closeEvent(self, event):
        typeMsg = "Aviso"
        msgSair = "Deseja sair?"
        reply = QMessageBox.question(self, typeMsg, msgSair,
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            #self.controle.stopThreadMonitora()
            #self.controle.stopThreadTime()
        else:
            event.ignore()
