# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""
import xlsxwriter

class GravaArquivo(object):

    @staticmethod
    def startGravacao(diretorioArqDestino, dados):
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(diretorioArqDestino)
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0
        worksheet.write(row, col, "Tempo")
        worksheet.write(row, col + 1, "Termometro 1")
        worksheet.write(row, col + 2, "Termometro 2")
        row += 1

        # Iterate over the data and write it out row by row.
        for temp1, temp2, time  in (dados):
            worksheet.write(row, col, time)
            worksheet.write(row, col + 1, temp1)
            worksheet.write(row, col + 2, temp2)
            row += 1

        workbook.close()