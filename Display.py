import sys
from PyQt5.QtChart import QCandlestickSeries, QChart, QChartView, QCandlestickSet
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt



class Display:

    def __init__(self):
        self.data = []
        self.app = QApplication(sys.argv)
        self.series = QCandlestickSeries()
        self.series.setDecreasingColor(Qt.red)
        self.series.setIncreasingColor(Qt.green)
        self.win = QMainWindow()

        self.tm = []  # stores str type data

    def load_data(self, _data):
        self.data = _data
        # data format [[Open] [High] [Low] [Close] ]
        for i in range(len(self.data[0])):
            self.series.append(QCandlestickSet(float(self.data[0][i]),
                                               float(self.data[1][i]),
                                               float(self.data[2][i]),
                                               float(self.data[3][i])))
            self.tm.append(str(i))
            i = i + 1

    def set_window_size(self, width, high, grid_x = 20, grid_y = 20):
        self.win.setGeometry(grid_x, grid_y, width, high)

    def run_app(self):

        chart = QChart()
        chart.addSeries(self.series)  # candle

        chart.createDefaultAxes()
        chart.legend().hide()

        chart.axisX(self.series).setCategories(self.tm)

        chart_view = QChartView(chart)

        self.win.setGeometry(50, 50, 800, 500)
        self.win.setCentralWidget(chart_view)
        self.win.show()
        sys.exit(self.app.exec_())
