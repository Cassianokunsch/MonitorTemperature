# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""

from PyQt4.QtCore import QThread, SIGNAL
import time

class ThMonitora(QThread):
    def __init__(self, serial):
        QThread.__init__(self)
        self.serial = serial

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            comando = "#temp"
            self.serial.write(comando.encode())
            print(2)
            time.sleep(2)
            temperatura = self.serial.readline()
            temperatura = str(temperatura).split("'")
            self.emit(SIGNAL('update(QString)'), temperatura[1])
            print(temperatura[1])