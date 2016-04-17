# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""
import threading
import time

class ThreadMonitorar(threading.Thread):
    def __init__(self, serial, interface):
        super(ThreadMonitorar, self).__init__()
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