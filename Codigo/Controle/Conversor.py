# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""

import threading
from Util.ThreadConversora import ThConversor
from Util.ThreadGravadora import ThreadGravar


class Conversor(object):

    @staticmethod
    def starThreadConversora(dadosArquivo, diretorioArqOrigem, controlador):
        thread = ThConversor(dadosArquivo, diretorioArqOrigem, controlador)
        thread.start()

    @staticmethod
    def starThreadGravadora(diretorioArqDestino, lst_dados, obj):
        thread = ThreadGravar(diretorioArqDestino, lst_dados, obj)
        thread.start()