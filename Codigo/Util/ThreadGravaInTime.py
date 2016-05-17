# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa thread é responsável por fazer o backup dos dados para caso ocorra
erro>

author: Cassiano Kunsch das Neves
last edited: <17/04/2016>
"""
import threading
import time
from Util.ThreadGravadora import ThreadGravar


class ThGravaInTime(threading.Thread):
    def __init__(self, diretorioArqDestino, lst_dados, referinterface):
        super(ThGravaInTime, self).__init__()
        self._stop_flag = False
        self.diretorioArqDestino = diretorioArqDestino
        self.lst_dados = lst_dados
        self.interface = referinterface

    def run(self):
        while True:
            time.sleep(60)
            thread = ThreadGravar(self.diretorioArqDestino, self.lst_dados, self.interface)
            thread.start()

            if self._stop_flag:
                break

    def stop(self):
        self._stop_flag = True
        self.join()
