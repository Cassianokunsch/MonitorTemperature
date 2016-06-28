# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O código abaixo é para gravar os dados em um arquivo.csv. >

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""
import xlsxwriter
from PyQt4 import QtCore


class GravaArquivo(object):

    @staticmethod
    def startGravacao(diretorioArqDestino, dados, referinterface, message):

        workbook = xlsxwriter.Workbook(diretorioArqDestino)
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0
        worksheet.write(row, col, "Tempo")
        worksheet.write(row, col + 1, "Termometro 1")
        worksheet.write(row, col + 2, "Termometro 2")
        row += 1

        for temp1, temp2, time in dados:
            worksheet.write(row, col, time)
            worksheet.write(row, col + 1, temp1)
            worksheet.write(row, col + 2, temp2)
            row += 1

        workbook.close()
        referinterface.emit(QtCore.SIGNAL("saveFile(QString, QString)"), message, "black")
