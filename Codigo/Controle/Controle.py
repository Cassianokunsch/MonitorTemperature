# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Arquivo que faz a comunicação entre a view e o modelo. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""

from Util.ThreadMonitora import ThreadMonitorar
from Util.ThreadGravadora import ThreadGravar
from Util.ThreadTime import ThreadTimer
from serial import Serial, SerialException
import sys


class ComunicacaoArduino(object):

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

class ControlInterface(object):

    def starThreadTime(self, referInterface):
        self.threadTime = ThreadTimer(referInterface)
        self.threadTime.start()

    def stopThreadTime(self):
        if hasattr(self, 'threadTime'):
            self.threadTime.stop()

    def starThreadMonitora(self, referInterface, tempo, port):
        self.threadMonitora = ThreadMonitorar(referInterface, tempo, ComunicacaoArduino, port)
        self.threadMonitora.start()

    def stopThreadMonitora(self):
        if hasattr(self, 'threadMonitora'):
            if self.threadMonitora.isAlive():
                self.threadMonitora.stop()

    @staticmethod
    def starThreadGravadora(diretorioArqDestino, lst_dados, referinterface):
        thread = ThreadGravar(diretorioArqDestino, lst_dados, referinterface)
        thread.start()
