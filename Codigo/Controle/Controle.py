# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <15/04/2016>
"""

from Util.ThreadGravadora import ThreadGravar
from PyQt4.QtCore import SIGNAL, QThread
import time
from serial import Serial
import subprocess

import threading

# class ThreadMonitora(QThread):
#     def __init__(self, serial):
#         QThread.__init__(self)
#         self.serial = serial
#
#     def __del__(self):
#         self.wait()
#
#     def run(self):
#         while True:
#             comando = "#temp"
#             temperaturas = []
#
#             self.serial.write(comando.encode())
#             time.sleep(1)
#             temperatura = self.serial.readline()
#             temperatura = str(temperatura).split("'")
#
#             temperaturas.append(temperatura[1][:5])
#             temperaturas.append(temperatura[1][5:])
#
#             self.emit(SIGNAL('PyQt_PyObject'), temperaturas)

# class ThreadTime(QThread):
#     def __init__(self):
#         QThread.__init__(self)
#         self.inicio = 0
#         self.hora = 0
#
#     def __del__(self):
#         self.wait()
#
#     def run(self):
#         while True:
#             time.sleep(0.1)
#             if self.inicio == 3600:
#                 self.hora += 1
#                 self.inicio = 0
#
#             text = "%02d:%02d:%02d" % (self.hora, self.inicio / 60, self.inicio % 60)
#             self.emit(SIGNAL("updade(QString)"), text)
#
#             self.inicio = self.inicio + 0.1
#             self.inicio = round(self.inicio, 1)

class ComunicacaoArduino(object):

    @staticmethod
    def start_communication():
        comport = Serial(ComunicacaoArduino.get_serial_port(), 9600, timeout=1, rtscts=True)

        return comport

    @staticmethod
    def get_serial_port():
        ports = subprocess.getoutput('python -m serial.tools.list_ports').split()

        return ports[0]


class ThreadMonitora(threading.Thread):
    def __init__(self, serial, interface):
        super(ThreadMonitora, self).__init__()
        self._stop_flag = False
        self.serial = serial
        self.interface = interface

    def run(self):
        while True:
            comando = "#temp"
            temperaturas = []

            self.serial.write(comando.encode())
            time.sleep(1)
            temperatura = self.serial.readline()
            temperatura = str(temperatura).split("'")

            temperaturas.append(temperatura[1][:5])
            temperaturas.append(temperatura[1][5:])

            self.interface.setTemps(temperaturas)

            if self._stop_flag:
                break

    def stop(self):
        self._stop_flag = True
        self.join()


class ThreadTime(threading.Thread):
    def __init__(self, interface):
        super(ThreadTime, self).__init__()
        self._stop_flag = False
        self.inicio = 0
        self.hora = 0
        self.interface = interface

    def run(self):
      while True:
          time.sleep(0.1)
          if self.inicio == 3600:
              self.hora += 1
              self.inicio = 0

          text = "%02d:%02d:%02d" % (self.hora, self.inicio / 60, self.inicio % 60)
          self.interface.setTime(text)

          self.inicio = self.inicio + 0.1
          self.inicio = round(self.inicio, 1)

          if self._stop_flag:
            break

    def stop(self):
        self._stop_flag = True
        self.join()



class ControlInterface(object):

    def starThreadTime(self, referInterface):
        self.threadTime = ThreadTime(referInterface)
        self.threadTime.start()

    def stopThreadTime(self):
        self.threadTime.stop()

    def starThreadMonitora(self, serial, referInterface):
        self.threadMonitora = ThreadMonitora(serial, referInterface)
        self.threadMonitora.start()

    def stopThreadMonitora(self):
        self.threadMonitora.stop()

    @staticmethod
    def starThreadGravadora(diretorioArqDestino, lst_dados):
        thread = ThreadGravar(diretorioArqDestino, lst_dados)
        thread.start()