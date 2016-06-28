# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa Thread é responsável por pegar os dados enviados pelo Arduino. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from datetime import datetime
import time
from PyQt4 import QtCore


class ThreadMonitorar(QtCore.QThread):
    def __init__(self, tempoAmostragem, conexaoArduino, port):
        super(ThreadMonitorar, self).__init__()
        self.tempoAmostragem = int(tempoAmostragem)
        self.conexaoArduino = conexaoArduino
        self.port = port
        self.comando = "#temp"
        self.__flag = False

    def __del__(self):
        self.wait()

    def run(self):
        # INICIA A CONEXÃO COM ARDUINO
        self.serial = self.conexaoArduino.start_communication(self.port)
        time.sleep(1)
        self.getMessage(self.tempoAmostragem)

        while True:
            self.getMessage(self.tempoAmostragem)

    def getMessage(self, tempoAmostragem):
        if tempoAmostragem != 2:
            tempoAmostragem -= 2

        self.serial.write(self.comando.encode())
        time.sleep(1)
        # LEIO A MENSAGEM. A MENSAGEM TEM ESSE FORMATO - b'23.50 24.50'
        mensagem = self.serial.readline()
        # PEGO O TEMPO QUE FOI PEGO A MENSAGEM
        text = str(datetime.now())
        # TRANSFORMO PARA ESSE - ['b', '23.50 24.50', '']
        listMensagem = str(mensagem).split("'")
        # TRANSFORMO PARA ESSE ['23.50', '24.50']
        lstTemps = listMensagem[1].split(" ")

        # MODIFICO O TEMPO PARA PEGAR SO A HORA, MINUTO E SEGUNDO
        lstTemps.append(text[11:19])

        if "Erro" in lstTemps:
            self.emit(QtCore.SIGNAL("updateTemps(PyQt_PyObject, QString)"), lstTemps, "Erro")
            self.terminate()
        else:
            self.emit(QtCore.SIGNAL("updateTemps(PyQt_PyObject, QString)"), lstTemps, "ok")
