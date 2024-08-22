import sys
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtCore import Qt

class PieChartExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pie Chart Example")

        # Create pie series
        series = QPieSeries()
        series.append("Apples", 10)
        series.append("Bananas", 20)
        series.append("Cherries", 30)
        series.append("Dates", 40)

        # Create chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Pie Chart Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Create chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set chart view as central widget
        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PieChartExample()
    window.show()
    sys.exit(app.exec())
