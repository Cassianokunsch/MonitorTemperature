# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa thread é responsável por fazer o backup dos dados para caso ocorra
erro>

author: Cassiano Kunsch das Neves
last edited: <17/04/2016>
"""
import time
from Util.Gravador import GravaArquivo
from PyQt4 import QtCore


class ThreadBackup(QtCore.QThread):
    def __init__(self, diretorioArqDestino, lst_dados):
        super(ThreadBackup, self).__init__()
        self.diretorioArqDestino = diretorioArqDestino
        self.lst_dados = lst_dados
        self.message = "Backup salvo com sucesso!!!\n"
        self.__flag = False

    def run(self):
        while True:
            if self.__flag:
                self.quit()
            time.sleep(30)
            GravaArquivo.startGravacao(self.diretorioArqDestino, self.lst_dados, self, self.message)

    def stop(self):
        self.__flag = True
