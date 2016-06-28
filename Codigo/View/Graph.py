import pyqtgraph as pg


class Graph2(pg.PlotWidget):
    def __init__(self):
        super(Graph, self).__init__(None, title="Temperatura x Tempo")
        self.settings()

    def settings(self):
        # ATIVANDO O GRID X E Y
        self.showGrid(True, True)
        # COLOCANDO LEGENDA PARA OS EIXOS X E Y
        self.setLabel('left', 'Temperatura', units='°C')
        self.setLabel('bottom', 'Tempo', units='s')
        self.setMenuEnabled(False)

    def updateGraph(self, list, color):
        self.plotItem.plot(list, pen=pg.QtGui.QPen(pg.QtGui.QColor(color)))


class Graph(pg.GraphicsWindow):
    def __init__(self):
        super(Graph, self).__init__(None)
        self.settings()

    def settings(self):
        x = ['a:000:00', 'b', 'c', 'd', 'e', 'f']
        y = [1, 2, 3, 4, 5, 6]
        xdict = dict(enumerate(x))
        # CRIANDO AS INFORMAÇÕES DO EIXO Y
        self.stringaxis = pg.AxisItem(orientation='bottom')
        #stringaxis.setTicks([xdict.items()])

        # CRIANDO UM PLOT
        self.plot = self.addPlot(axisItems={'bottom': self.stringaxis})
        # ATIVANDO O GRID X E Y
        self.plot.showGrid(True, True)
        # COLOCANDO LEGENDA PARA OS EIXOS X E Y
        self.plot.setLabel('left', 'Temperatura', units='°C')
        self.plot.setLabel('bottom', 'Tempo', units='H:M:S')

        #x = list(xdict.keys())

        # CRIANDO UMA CURVA
        #c = pg.PlotCurveItem()
        #c.setData(x, y)

        # CRIANDO UMA CURVA
        #c1 = pg.PlotCurveItem()
        #c1.setData([4, 5, 6], [4, 5, 6])

        # ADICIONANDO AS CURVAS NO PLOT
        #plot1.addItem(c)
        #plot1.addItem(c1)

    def update(self, listTemp, listTempo):
        self.stringaxis.setTicks([listTempo.items()])
        x = list(listTempo.keys())
        y = listTemp
        curva = pg.PlotCurveItem()
        curva.setData(x, y)
        self.plot.addItem(curva)
