# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O código abaixo é para gravar os dados em uma lista de Python simulando um
 banco de dados.>

author: Cassiano Kunsch das Neves
last edited: <10/12/2015>
"""


class Model(object):

    def __init__(self):
        self.dateTemperature = []
        self.dateLog = []

    def appendDateTemperature(self, temperatures):
        self.dateTemperature.append(temperatures)

    def appendDateLog(self, dateLog):
        self.dateLog.append(dateLog)

    def getDateTemperature(self):
        return self.dateTemperature

    def getDateLog(self):
        return self.dateLog
