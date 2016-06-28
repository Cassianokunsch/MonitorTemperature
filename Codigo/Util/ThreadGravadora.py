# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa thread é responsável por gravar o arquivo >

author: Cassiano Kunsch das Neves
last edited: <12/12/2015>
"""

from Util.Gravador import GravaArquivo
from PyQt4 import QtCore


class ThreadGravar(QtCore.QThread):
    def __init__(self,  diretorioArqDestino, lst_dados, message):
        super(ThreadGravar, self).__init__()
        self.dados = lst_dados
        self.diretorioDestino = diretorioArqDestino
        self.message = message

    def run(self):
        GravaArquivo.startGravacao(self.diretorioDestino, self.dados, self, self.message)
        self.terminate()
