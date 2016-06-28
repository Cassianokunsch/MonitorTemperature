# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa thread é responsável por gravar o log do software >

author: Cassiano Kunsch das Neves
last edited: <12/12/2015>
"""
from PyQt4 import QtCore


class ThreadLog(QtCore.QThread):
    def __init__(self,  diretorioArqDestino, lst_dados):
        super(ThreadLog, self).__init__()
        self.lstInfo = lst_dados
        self.diretorioDestino = diretorioArqDestino

    def run(self):
        # PEGANDO O TAMANHO DA LISTA DE DADOS
        sizeLst = len(self.lstInfo)

        # CRIANDO O ARQUIVO DE LOG
        arquivo = open(self.diretorioDestino[:-4] + "LOG.txt", "w")

        # ESCREVENDO O CONTEUDO DO ARQUIVO DE LOG
        arquivo.write("--INFORMAÇÕES SOBRE O TESTE--\n\n")
        arquivo.write("INÍCIO - ")
        # PEGANDO A DATA, HORA, MINUTO, E SEGUNDOS, INICIAL SALVOS NA LISTA DE DADOS
        arquivo.write(str(self.lstInfo[0])[:19] + "\n")
        arquivo.write("FINAL - ")
        # PEGANDO A DATA, HORA, MINUTO, E SEGUNDOS, FINAL SALVOS NA LISTA DE DADOS
        arquivo.write(str(self.lstInfo[sizeLst-1])[:19] + "\n\n")
        arquivo.write("TEMPO DE DURAÇÃO: ")
        # CALCULANDO O TEMPO DE DURAÇÃO DE SOFTWARE
        arquivo.write(str(self.lstInfo[sizeLst-1] - self.lstInfo[0])[:7])
        arquivo.write("\n\n")
        # ESCREVENDO AS INFORMAÇÕES DA LISTA DE LOG
        arquivo.write("--LOG DO SOFTWARE--\n\n")
        for info in self.lstInfo[1:sizeLst-1]:
            arquivo.write(info)

        arquivo.close()
        self.terminate()
