# -*- coding: utf8 -*-
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from plugin.mplotwidgets.techmplot import TechMPlot
import matplotlib.pyplot as plt
from PyQt4.QtCore import Qt

class TechWidget(TechMPlot, FigureCanvasQTAgg):
    def __init__(self, parent=None, *args):
        self.fig = plt.figure()
        FigureCanvasQTAgg.__init__(self, self.fig)
        TechMPlot.__init__(self, self.fig, *args)
        self.setParent(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()
