# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Arquivo que faz a comunicação entre a view e o modelo. >

author: Cassiano Kunsch das Neves
last edited: <15/04/2016>
"""

from Util.ThreadMonitora import ThreadMonitorar
from Util.ThreadGravadora import ThreadGravar
from Util.ThreadTime import ThreadTimer
from Util.ThreadGravaInTime import ThGravaInTime
from Util.ThreadConexaoArduino import ThConexao
from serial import Serial, SerialException
import subprocess


class ComunicacaoArduino(object):

    @staticmethod
    def start_communication():

        try:
            comport = Serial(ComunicacaoArduino.get_serial_port(), 9600, timeout=1, rtscts=True)

            return comport

        except SerialException:
            return "Arduino não conectado!"

    @staticmethod
    def get_serial_port():
        ports = subprocess.getoutput('python -m serial.tools.list_ports').split()

        return ports[0]


class ControlInterface(object):

    def starThreadTime(self, referInterface):
        self.threadTime = ThreadTimer(referInterface)
        self.threadTime.start()

    def stopThreadTime(self):
        if hasattr(self, 'threadTime'):
            self.threadTime.stop()

    def starThreadMonitora(self, serial, referInterface, tempo):
        self.threadMonitora = ThreadMonitorar(serial, referInterface, tempo)
        self.threadMonitora.start()

    def stopThreadMonitora(self):
        if hasattr(self, 'threadMonitora'):
            if self.threadMonitora.isAlive():
                self.threadMonitora.stop()

    def starThreadGravaPeriodicamente(self, diretorioArqDestino, lst_dados, referInterface):
        self.threadPeriodicamente = ThGravaInTime(diretorioArqDestino, lst_dados, referInterface)
        self.threadPeriodicamente.start()

    def stopThreadGravaPeriodicamente(self):
        if hasattr(self, 'threadPeriodicamente'):
            self.threadPeriodicamente.stop()

    def startThreadConexao(self, referInterface):
        self.threadConexao = ThConexao(referInterface, ComunicacaoArduino)
        self.threadConexao.start()

    def stopThreadConexao(self):
        if hasattr(self, 'threadConexao'):
            self.threadConexao.stop()

    @staticmethod
    def starThreadGravadora(diretorioArqDestino, lst_dados, referinterface):
        thread = ThreadGravar(diretorioArqDestino, lst_dados, referinterface)
        thread.start()
