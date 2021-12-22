import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.setWindowTitle('Эспрессо')

        res = self.con.cursor().execute('SELECT * FROM info').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        titles = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                  'описание вкуса', 'цена', 'объем упаковки']
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


app = QApplication(sys.argv)
ex = Coffee()
ex.show()
sys.exit(app.exec_())
