import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("MainUI.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.cellClicked.connect(self.Book_Clicked)
        self.tableWidget_2.cellClicked.connect(self.Member_Clicked)
        self.pushButton.clicked.connect(self.Rent_book)
        self.pushButton_2.clicked.connect(self.Return_book)

    def Book_Clicked(self, row):
        global row_1
        row_1 = row

        if self.tableWidget.item(row_1, 4).text() == '대출 됨':
            i = 0
            while i < 3:
                if self.tableWidget.item(row_1, 1).text() == self.tableWidget_2.item(i, 5).text():
                    self.lineEdit_6.setText(self.tableWidget_2.item(i, 0).text())
                    self.lineEdit_7.setText(self.tableWidget_2.item(i, 1).text())
                    self.lineEdit_8.setText(self.tableWidget_2.item(i, 2).text())
                    self.lineEdit_9.setText(self.tableWidget_2.item(i, 3).text())
                    self.lineEdit_10.setText(self.tableWidget_2.item(i, 4).text())
                    self.lineEdit_12.setText(self.tableWidget_2.item(i, 5).text())

                    break
                i += 1

        if row == 0:
            self.lineEdit.setText(self.tableWidget.item(0, 0).text())
            self.lineEdit_2.setText(self.tableWidget.item(0, 1).text())
            self.lineEdit_3.setText(self.tableWidget.item(0, 2).text())
            self.lineEdit_4.setText(self.tableWidget.item(0, 3).text())
            self.lineEdit_5.setText(self.tableWidget.item(0, 4).text())
        elif row == 1:
            self.lineEdit.setText(self.tableWidget.item(1, 0).text())
            self.lineEdit_2.setText(self.tableWidget.item(1, 1).text())
            self.lineEdit_3.setText(self.tableWidget.item(1, 2).text())
            self.lineEdit_4.setText(self.tableWidget.item(1, 3).text())
            self.lineEdit_5.setText(self.tableWidget.item(1, 4).text())
        elif row == 2:
            self.lineEdit.setText(self.tableWidget.item(2, 0).text())
            self.lineEdit_2.setText(self.tableWidget.item(2, 1).text())
            self.lineEdit_3.setText(self.tableWidget.item(2, 2).text())
            self.lineEdit_4.setText(self.tableWidget.item(2, 3).text())
            self.lineEdit_5.setText(self.tableWidget.item(2, 4).text())

    def Member_Clicked(self, row):
        global row_2
        row_2 = row

        if self.tableWidget_2.item(row_2, 5).text != '없음':
            i = 0
            while i < 3:
                if self.tableWidget_2.item(row_2, 5).text() == self.tableWidget.item(i, 1).text():
                    self.lineEdit.setText(self.tableWidget.item(i, 0).text())
                    self.lineEdit_2.setText(self.tableWidget.item(i, 1).text())
                    self.lineEdit_3.setText(self.tableWidget.item(i, 2).text())
                    self.lineEdit_4.setText(self.tableWidget.item(i, 3).text())
                    self.lineEdit_5.setText(self.tableWidget.item(i, 4).text())

                    break
                i += 1

        if row == 0:
            self.lineEdit_6.setText(self.tableWidget_2.item(0, 0).text())
            self.lineEdit_7.setText(self.tableWidget_2.item(0, 1).text())
            self.lineEdit_8.setText(self.tableWidget_2.item(0, 2).text())
            self.lineEdit_9.setText(self.tableWidget_2.item(0, 3).text())
            self.lineEdit_10.setText(self.tableWidget_2.item(0, 4).text())
            self.lineEdit_12.setText(self.tableWidget_2.item(0, 5).text())
        elif row == 1:
            self.lineEdit_6.setText(self.tableWidget_2.item(1, 0).text())
            self.lineEdit_7.setText(self.tableWidget_2.item(1, 1).text())
            self.lineEdit_8.setText(self.tableWidget_2.item(1, 2).text())
            self.lineEdit_9.setText(self.tableWidget_2.item(1, 3).text())
            self.lineEdit_10.setText(self.tableWidget_2.item(1, 4).text())
            self.lineEdit_12.setText(self.tableWidget_2.item(1, 5).text())
        elif row == 2:
            self.lineEdit_6.setText(self.tableWidget_2.item(2, 0).text())
            self.lineEdit_7.setText(self.tableWidget_2.item(2, 1).text())
            self.lineEdit_8.setText(self.tableWidget_2.item(2, 2).text())
            self.lineEdit_9.setText(self.tableWidget_2.item(2, 3).text())
            self.lineEdit_10.setText(self.tableWidget_2.item(2, 4).text())
            self.lineEdit_12.setText(self.tableWidget_2.item(2, 5).text())

    def Rent_book(self):
        if self.lineEdit_5.text() == '대출 안됨' and self.lineEdit_10.text() == '대출 가능' and self.lineEdit_12.text() == '없음':
            self.tableWidget.item(row_1, 4).setText('대출 됨')
            self.tableWidget_2.item(row_2, 4).setText('대출 불가능')
            self.tableWidget_2.item(row_2, 5).setText(self.lineEdit_2.text())
            self.lineEdit_5.setText('대출 됨')
            self.lineEdit_10.setText('대출 불가능')
            self.lineEdit_12.setText(self.lineEdit_2.text())

    def Return_book(self):
        if self.lineEdit_12.text() != '없음':
            i = 0
            while i < 3:
                if self.tableWidget_2.item(row_2, 5).text() == self.tableWidget.item(i, 1).text():
                    self.tableWidget.item(i, 4).setText('대출 안됨')
                    self.tableWidget_2.item(row_2, 4).setText('대출 가능')
                    self.tableWidget_2.item(row_2, 5).setText('없음')
                    self.lineEdit_5.setText('대출 안됨')
                    self.lineEdit_10.setText('대출 가능')
                    self.lineEdit_12.setText('없음')
                    break
                i += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()