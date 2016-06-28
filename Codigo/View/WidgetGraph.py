# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Esse arquivo é a interface gráfica do software. >

author: Cassiano Kunsch das Neves
last edited: <16/05/2016>
"""
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import (QGridLayout, QWidget)
from View.Graph import Graph


class WidgetGraph(QWidget):
    def __init__(self, parent):
        super(WidgetGraph, self).__init__()
        self.settings()

    def settings(self):

        self.graphTemp = Graph()
        xdict = dict(enumerate(['a:000:00', 'b', 'c', 'd', 'e', 'f']))
        self.graphTemp.update([1, 2, 3, 4, 5, 6], xdict)

        self.connect(self, SIGNAL("Update(PyQt_PyObject, PyQt_PyObject, QString)"), self.update)

        self.gridLayout_2 = QGridLayout(self)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)

        self.gridLayout_2.addWidget(self.graphTemp, 0, 0, 1, 1)

    def update(self, list, list2, color):
        self.graphTemp.update(list, list2, color)
        # self.graphTemp.plotItem.plot(list, pen=QPen(QColor(color)))
