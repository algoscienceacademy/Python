import sys
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Qt

class ChartExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Line Chart")

        # Create line series
        series = QLineSeries()
        series.append(0, 6)
        series.append(2, 4)
        series.append(3, 8)
        series.append(7, 4)
        series.append(10, 5)

        # Create chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Simple Line Chart Example")
        chart.createDefaultAxes()

        # Create chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set chart view as central widget
        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChartExample()
    window.show()
    sys.exit(app.exec())
