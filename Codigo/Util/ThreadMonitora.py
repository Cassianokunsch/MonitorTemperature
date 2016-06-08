# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa Thread é responsável por pegar os dados enviados pelo Arduino. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
import threading
import time


class ThreadMonitorar(threading.Thread):
    def __init__(self, interface, tempoAmostragem, conexaoArduino, port):
        super(ThreadMonitorar, self).__init__()
        self._stop_flag = False
        self.interface = interface
        self.tempoAmostragem = tempoAmostragem
        self.conexaoArduino = conexaoArduino
        self.port = port
        self.comando = "#temp"

    def run(self):
        self.serial = self.conexaoArduino.start_communication(self.port)
        time.sleep(1)
        self.getMessage(self.tempoAmostragem)
        while True:
            if self._stop_flag:
                break

            self.getMessage(self.tempoAmostragem)

    def getMessage(self, tempoAmostragem):
        if tempoAmostragem != 2:
            tempoAmostragem -= 2

        self.serial.write(self.comando.encode())
        time.sleep(tempoAmostragem)
        # Mensagem tem esse formato - b'23.50 24.50'
        mensagem = self.serial.readline()
        # Vai pra esse formato ['b', '23.50 24.50', '']
        listMensagem = str(mensagem).split("'")
        # Vai pra isso ['23.50', '24.50']
        lstTemps = listMensagem[1].split(" ")

        self.interface.setTemps(lstTemps)
        time.sleep(1)
        if "Erro" in lstTemps:
            self.stop()

    def stop(self):
        self._stop_flag = True
        # self.join()
