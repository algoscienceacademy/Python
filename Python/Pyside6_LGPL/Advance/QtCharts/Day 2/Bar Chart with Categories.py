import sys
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PySide6.QtCore import Qt

class BarChartExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bar Chart Example")

        # Create bar sets
        set0 = QBarSet("Jan")
        set1 = QBarSet("Feb")
        set2 = QBarSet("Mar")
        
        set0.append([1, 2, 3, 4])
        set1.append([5, 6, 7, 8])
        set2.append([9, 10, 11, 12])

        # Create bar series
        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        # Create chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Bar Chart Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Set categories
        axis_x = QBarCategoryAxis()
        axis_x.append(["A", "B", "C", "D"])
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Values")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Create chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set chart view as central widget
        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChartExample()
    window.show()
    sys.exit(app.exec())
