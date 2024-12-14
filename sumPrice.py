# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumPrice.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtWidgets import QMessageBox


class Ui_sumPrice(object):
    def setupUi(self, sumPrice):
        sumPrice.setObjectName("sumPrice")
        sumPrice.resize(449, 300)
        self.label_S = QtWidgets.QLabel(sumPrice)
        self.label_S.setGeometry(QtCore.QRect(125, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_S.setFont(font)
        self.label_S.setObjectName("label_S")
        self.lineEdit_S = QtWidgets.QLineEdit(sumPrice)
        self.lineEdit_S.setGeometry(QtCore.QRect(20, 90, 391, 31))
        self.lineEdit_S.setObjectName("lineEdit_S")
        self.find_button_S = QtWidgets.QPushButton(sumPrice)
        self.find_button_S.setGeometry(QtCore.QRect(200, 250, 93, 28))
        self.find_button_S.setObjectName("find_button_S")
        self.cencel_button_S = QtWidgets.QPushButton(sumPrice)
        self.cencel_button_S.setGeometry(QtCore.QRect(320, 250, 93, 28))
        self.cencel_button_S.setObjectName("cencel_button_S")

        self.retranslateUi(sumPrice)
        QtCore.QMetaObject.connectSlotsByName(sumPrice)
        self.cencel_button_S.clicked.connect(lambda: self.closePanel(sumPrice))
        self.find_button_S.clicked.connect(self.sumShipment)


    def closePanel(self,sumPrice):
        sumPrice.hide()

    def sumShipment(self):
        ID = self.lineEdit_S.text().strip()
        try:
            if not os.path.exists("data.txt"):
                raise FileNotFoundError("Файл data.txt отсутствует.")
            total=0
            with open("data.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(";")

                    if len(data) == 5:
                        item_ID = data[0].strip()
                        try:
                            price = int(data[4])
                            kol=int(data[3])
                        except ValueError:
                            print(f"Ошибка преобразования количества: {data[4]}")
                            continue

                        if item_ID.lower() == ID.lower():
                            total = price * kol

            message = QMessageBox()
            if total == 0:
                message.setWindowTitle("Пусто")
                message.setText("Товары не найдены")
                message.setIcon(QMessageBox.Warning)
            else:
                message.setWindowTitle("Суммарное количество")
                message.setText(f"Общее количество товаров из {ID}: {total}")
                message.setIcon(QMessageBox.Information)

            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()

        except FileNotFoundError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Файл не найден")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

        except Exception as e:
            error = QMessageBox()
            error.setWindowTitle("Упс")
            error.setText(f"Ошибка: {str(e)}")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()


    def retranslateUi(self, sumPrice):
        _translate = QtCore.QCoreApplication.translate
        sumPrice.setWindowTitle(_translate("sumPrice", "Суммарная стоимость товаров по шифру"))
        self.label_S.setText(_translate("sumPrice", "Введите шифр"))
        self.find_button_S.setText(_translate("sumPrice", "Найти"))
        self.cencel_button_S.setText(_translate("sumPrice", "Отмена"))