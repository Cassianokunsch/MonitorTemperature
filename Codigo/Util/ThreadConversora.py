# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""
from Model.Conversor import Converte
import threading


class ThConversor(threading.Thread):
    def __init__ (self, dadosArquivo, diretorioArqOrigem, controlador):
        super(ThConversor, self).__init__()
        self.dados = dadosArquivo
        self.origem = diretorioArqOrigem
        self.controlador = controlador

    def run(self):
        Converte.startConversao(self.origem, self.dados, self.controlador)