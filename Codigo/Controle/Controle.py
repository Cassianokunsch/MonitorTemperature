# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Arquivo que faz a comunicação entre a view e o modelo. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from Util.ThreadMonitora import ThreadMonitorar
from Util.ThreadGravadora import ThreadGravar
from Util.ThreadBackup import ThreadBackup
from Util.ThreadLog import ThreadLog
from serial import Serial, SerialException
import sys


class Control(object):

    def instThreadMonitora(self, tempo, port):
        threadMonitora = ThreadMonitorar(tempo, self, port)
        return threadMonitora

    def startThreadMonitora(self, threadMonitora):
        threadMonitora.start()

    def stopThreadMonitora(self, threadMonitora):
        threadMonitora.terminate()

    def instThreadBackup(self, diretorioArqDestino, lst_dados):
        threadBackup = ThreadBackup(diretorioArqDestino, lst_dados)
        return threadBackup

    def startThreadBackup(self, threadBackup):
        threadBackup.start()

    def stopThreadBackup(self, threadBackup):
        threadBackup.terminate()

    def instThreadGravadora(self, diretorioArqDestino, lst_dados, message):
        threadGravadora = ThreadGravar(diretorioArqDestino, lst_dados, message)
        return threadGravadora

    def startThreadGravadora(self, threadGravadora):
        threadGravadora.start()

    def stopThreadGravadora(self, threadGravadora):
        threadGravadora.terminate()

    def instThreadLog(self, diretorioArqDestino, lst_dados):
        threadLog = ThreadLog(diretorioArqDestino, lst_dados)
        return threadLog

    def startThreadLog(self, threadLog):
        threadLog.start()

    def stopThreadLog(self, threadLog):
        threadLog.terminate()

    @staticmethod
    def find_ports():
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]
        ports = ['COM' + str(i + 1) for i in range(256)]
        result = []
        for port in ports:
            try:
                s = Serial(port)
                s.close()
                result.append(port)
            except(OSError, SerialException):
                pass

        return result

    @staticmethod
    def start_communication(port):
        comport = Serial(port, 9600, timeout=1, rtscts=True)
        return comport
