# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Essa Thread é responsável por controlar o tempo percorrido pelo software. >

author: Cassiano Kunsch das Neves
last edited: <17/04/2016>
"""
import threading
import time


class ThreadTimer(threading.Thread):
    def __init__(self, interface):
        super(ThreadTimer, self).__init__()
        self._stop_flag = False
        self.inicio = 0
        self.hora = 0
        self.interface = interface

    def run(self):
        while True:
            time.sleep(1)
            if self.inicio == 3600:
                self.hora += 1
                self.inicio = 0

            text = "%02d:%02d:%02d" % (self.hora, self.inicio / 60, self.inicio % 60)
            self.interface.setTime(text)

            self.inicio = self.inicio + 1

            if self._stop_flag:
                break

    def stop(self):
        self._stop_flag = True
        self.join()
