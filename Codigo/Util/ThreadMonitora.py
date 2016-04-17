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
            i = 0
            aux = ''
            temperaturas = []

            self.serial.write(comando.encode())
            time.sleep(1)
            temperatura = self.serial.readline()
            temperatura = str(temperatura).split("'")

            while (temperatura[1][i]!= " "):
                aux+=temperatura[1][i]
                i+=1
            i+=1
            aux2 = ''

            for num in range(i, len(temperatura[1])):
                aux2+=temperatura[1][num]



            temperaturas.append(aux)
            temperaturas.append(aux2)

            self.interface.setTemps(temperaturas)

            if self._stop_flag:
                break

    def stop(self):
        self._stop_flag = True
        self.join()