# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa thread é responsável por gravar o arquivo >

author: Cassiano Kunsch das Neves
last edited: <12/12/2015>
"""

from Model.Gravador import GravaArquivo
import threading


class ThreadGravar(threading.Thread):
    def __init__(self,  diretorioArqDestino, lst_dados, referinterface):
        super(ThreadGravar, self).__init__()
        self.dados = lst_dados
        self.diretorioDestino = diretorioArqDestino
        self.referinterface = referinterface

    def run(self):
        GravaArquivo.startGravacao(self.diretorioDestino, self.dados, self.referinterface)
