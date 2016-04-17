# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <15/04/2016>
"""

from Util.ThreadMonitora import ThreadMonitorar
from Util.ThreadGravadora import ThreadGravar
from Util.ThreadTime import ThreadTimer

from serial import Serial
import subprocess

class ComunicacaoArduino(object):

    @staticmethod
    def start_communication():
        comport = Serial(ComunicacaoArduino.get_serial_port(), 9600, timeout=1, rtscts=True)

        return comport

    @staticmethod
    def get_serial_port():
        ports = subprocess.getoutput('python -m serial.tools.list_ports').split()

        return ports[0]


class ControlInterface(object):

    def starThreadTime(self, referInterface):
        self.threadTime = ThreadTimer(referInterface)
        self.threadTime.start()

    def stopThreadTime(self):
        self.threadTime.stop()

    def starThreadMonitora(self, serial, referInterface):
        self.threadMonitora = ThreadMonitorar(serial, referInterface)
        self.threadMonitora.start()

    def stopThreadMonitora(self):
        self.threadMonitora.stop()

    @staticmethod
    def starThreadGravadora(diretorioArqDestino, lst_dados):
        thread = ThreadGravar(diretorioArqDestino, lst_dados)
        thread.start()