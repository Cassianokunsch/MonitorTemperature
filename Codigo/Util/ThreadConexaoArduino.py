# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa Thread é responsável por verificar a conecxão com o Arduino >

author: Cassiano Kunsch das Neves
last edited: <17/04/2016>
"""
import threading
import time


class ThConexao(threading.Thread):
    def __init__(self, interface, conexaoArduino, port):
        super(ThConexao, self).__init__()
        self._stop_flag = False
        self.interface = interface
        self.conexaoArduino = conexaoArduino
        self.serial = None
        self.port = port

    def run(self):
        while True:
            self.interface.setInformation("Conectando ao Arduino...\n")
            self.serial = self.conexaoArduino.start_communication(self.port)

            if "Arduino não conectado!" == self.serial:
                self.interface.setWarning("Arduino não conectado!\n")
                time.sleep(0.1)
                self.interface.setWarning("Tentando novamente em...")
                for i in range(10):
                    if i < 9:
                        self.interface.setWarning(str(i))
                    else:
                        self.interface.setWarning(str(i) + "\n")
                    time.sleep(1)
            else:
                self.interface.setInformation("Arduino conectado\n")
                self.interface.onButtons()
                self.interface.setSerial(self.serial)
                self._stop_flag = True

            if self._stop_flag:
                break

    def stop(self):
        self._stop_flag = True
        self.join()
