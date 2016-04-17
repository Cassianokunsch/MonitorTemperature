# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""
from PyQt4 import QtGui
import pandas


class Converte(object):

    @staticmethod
    def startConversao(diretorioArqOrigem, lstDadosArquivo, controlador):

        arquivoXlsx = pandas.ExcelFile(diretorioArqOrigem)

        colunaUm = pandas.ExcelFile.parse(arquivoXlsx, arquivoXlsx.sheet_names[0])

        lstNomesColuna = []

        for coluna in (colunaUm.columns):
            lstNomesColuna.append(coluna)

        tamanhoColuna = colunaUm[lstNomesColuna[0]].size
        controlador[1] = len(lstNomesColuna)

        lstDadosArquivo.append(tamanhoColuna)

        bufferDados = []
        for numLinha in range(tamanhoColuna):
            for coluna in (lstNomesColuna):
                row = colunaUm[coluna].iloc[numLinha]
                bufferDados.append(str(row))
                controlador[0] += 1
            lstDadosArquivo.append(bufferDados)
            bufferDados = []