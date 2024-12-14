from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from sumPrice import Ui_sumPrice
from sumV import Ui_Summar_V_Country
from info import Ui_info


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1280, 720)
        self.current_row = -1
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(0, 329, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table.sizePolicy().hasHeightForWidth())
        self.Table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Table.setFont(font)
        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(5)
        self.Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, item)
        self.Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Table.horizontalHeader().setDefaultSectionSize(256)
        self.Table.verticalHeader().setCascadingSectionResizes(True)
        self.Table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table.setMinimumSize(600, 400)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.Table)
        self.scrollArea.setGeometry(QtCore.QRect(0, 329, 1280, 400))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 30, 211, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.change_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_button.setObjectName("change_button")
        self.verticalLayout.addWidget(self.change_button)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout.addWidget(self.delete_button)
        self.load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_button.setObjectName("load_button")
        self.verticalLayout.addWidget(self.load_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(950, 30, 299, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Скаченное/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getInfo_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.getInfo_button.setIcon(icon)
        self.getInfo_button.setObjectName("getInfo_button")
        self.verticalLayout_2.addWidget(self.getInfo_button)
        self.summar_price_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.summar_price_button.setObjectName("summar_price_button")
        self.verticalLayout_2.addWidget(self.summar_price_button)
        self.summar_V_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.summar_V_button.setObjectName("summar_V_button")
        self.verticalLayout_2.addWidget(self.summar_V_button)
        self.min_price_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.min_price_button.setObjectName("min_price_button")
        self.verticalLayout_2.addWidget(self.min_price_button)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(150, 30, 511, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ID_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ID_input.setObjectName("ID_input")
        self.verticalLayout_4.addWidget(self.ID_input)
        self.name_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.name_input.setObjectName("name_input")
        self.verticalLayout_4.addWidget(self.name_input)
        self.country_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.country_input.setObjectName("country_input")
        self.verticalLayout_4.addWidget(self.country_input)
        self.kol_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.kol_input.setObjectName("kol_input")
        self.verticalLayout_4.addWidget(self.kol_input)
        self.price_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.price_input.setObjectName("price_input")
        self.verticalLayout_4.addWidget(self.price_input)
        self.country_label = QtWidgets.QLabel(self.centralwidget)
        self.country_label.setGeometry(QtCore.QRect(20, 160, 158, 16))
        self.country_label.setObjectName("country_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 110, 91, 21))
        self.name_label.setObjectName("name_label")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(20, 260, 158, 21))
        self.price_label.setObjectName("price_label")
        self.kol_label = QtWidgets.QLabel(self.centralwidget)
        self.kol_label.setGeometry(QtCore.QRect(20, 210, 158, 21))
        self.kol_label.setObjectName("kol_label")
        self.ID_label = QtWidgets.QLabel(self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(20, 50, 121, 21))
        self.ID_label.setObjectName("ID_label")
        MainMenu.setCentralWidget(self.centralwidget)
        self.Table.setSortingEnabled(True)
        self.Table.setHorizontalHeaderLabels(["Шифр", "Наименование товара", "Страна-импортёр","Размер партии", "Стоимость 1 ед"])
        self.sort_order = {}
        self.load_from_file()


        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

        self.add_button.clicked.connect(self.add_to_table)
        self.delete_button.clicked.connect(self.delete_cell)
        self.load_button.clicked.connect(self.load_row)
        self.change_button.clicked.connect(self.change_row)
        self.min_price_button.clicked.connect(self.find_min_price)
        self.summar_price_button.clicked.connect(self.summar_price)
        self.summar_V_button.clicked.connect(self.summar_V)
        self.Table.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.getInfo_button.clicked.connect(self.about_program)

    def save_to_file(self):
        with open("data.txt", "w", encoding="utf-8") as file:
            row_count = self.Table.rowCount()
            for row in range(row_count):
                data = [
                    self.Table.item(row, col).text() if self.Table.item(row, col) else ""
                    for col in range(self.Table.columnCount())
                ]
                file.write(";".join(data) + "\n")

    def load_from_file(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                self.Table.setRowCount(0)
                for line in file:
                    data = line.strip().split(";")
                    row_position = self.Table.rowCount()
                    self.Table.insertRow(row_position)
                    for col, value in enumerate(data):
                        self.Table.setItem(row_position, col, QTableWidgetItem(value))
        except FileNotFoundError:
            pass

    def add_to_table(self):
        try:
            # Получение текста из QLineEdit
            textID = self.ID_input.text()
            textName = self.name_input.text()
            textCountry = self.country_input.text()
            textKol = int(self.kol_input.text())
            textPrice = int(self.price_input.text())
            # Добавление новой строки
            row_position = self.Table.rowCount()
            self.Table.insertRow(row_position)
            # Вставка данных
            self.Table.setItem(row_position, 0, QTableWidgetItem(textID))
            self.Table.setItem(row_position, 1, QTableWidgetItem(textName))
            self.Table.setItem(row_position, 2, QTableWidgetItem(textCountry))
            self.Table.setItem(row_position, 3, QTableWidgetItem(str(textKol)))
            self.Table.setItem(row_position, 4, QTableWidgetItem(str(textPrice)))
            # Очистка полей ввода
            self.ID_input.clear()
            self.name_input.clear()
            self.country_input.clear()
            self.kol_input.clear()
            self.price_input.clear()
        except ValueError:
            QMessageBox.warning(self.centralwidget, "Приехали", "Сначала загрузите строку для изменения.")
            return
        self.save_to_file()

    def delete_cell(self):
        selected_items = self.Table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self.centralwidget, "Приехали", "Нет выделенных ячеек.")
            return
        row = selected_items[0].row()
        self.Table.removeRow(row)
        QMessageBox.information(self.centralwidget, "Успех", "Данные удалены.")
        self.save_to_file()

    def load_row(self):
        load_items = self.Table.selectedItems()
        if not load_items or len(set(item.row() for item in load_items)) > 1:
            QMessageBox.warning(self.centralwidget, "Приехали", "Выберете данные для загрузки.")
            return

        self.current_row = load_items[0].row()
        self.ID_input.setText(self.Table.item(self.current_row, 0).text())
        self.name_input.setText(self.Table.item(self.current_row, 1).text())
        self.country_input.setText(self.Table.item(self.current_row, 2).text())
        self.kol_input.setText(self.Table.item(self.current_row, 3).text())
        self.price_input.setText(self.Table.item(self.current_row, 4).text())

    def change_row(self):
        if self.current_row == -1:
            QMessageBox.warning(self.centralwidget, "Ошибка", "Сначала загрузите строку для изменения.")
            return

        try:
            textID = self.ID_input.text()
            textName = self.name_input.text()
            textCountry = self.country_input.text()
            textKol = int(self.kol_input.text())
            textPrice = int(self.price_input.text())

            self.Table.setItem(self.current_row, 0, QTableWidgetItem(textID))
            self.Table.setItem(self.current_row, 1, QTableWidgetItem(textName))
            self.Table.setItem(self.current_row, 2, QTableWidgetItem(textCountry))
            self.Table.setItem(self.current_row, 3, QTableWidgetItem(str(textKol)))
            self.Table.setItem(self.current_row, 4, QTableWidgetItem(str(textPrice)))
            QMessageBox.information(self.centralwidget, "Успех", "Данные успешно обновлены.")
            self.current_row = -1
            self.ID_input.clear()
            self.name_input.clear()
            self.country_input.clear()
            self.kol_input.clear()
            self.price_input.clear()
        except ValueError:
            QMessageBox.warning(self.centralwidget, "Ошибка", "Неправильный ввод данных.")
        self.save_to_file()

    def find_min_price(self):
        row_count = self.Table.rowCount()
        if row_count == 0:
            QMessageBox.warning(self.centralwidget, "Ошибка", "Таблица пуста.")
            return
        min_price = float('inf')
        min_row = -1

        for row in range(row_count):
            item_price = self.Table.item(row, 4)
            if item_price is not None:
                try:
                    price = int(item_price.text())
                    if price < min_price:
                        min_price = price
                        min_row = row
                except ValueError:
                    continue
        if min_row == -1:
            QMessageBox.warning(self.centralwidget, "Ошибка", "Не удалось найти минимальную цену.")
        else:
            item_id = self.Table.item(min_row, 0).text()
            item_name = self.Table.item(min_row, 1).text()
            item_country = self.Table.item(min_row, 2).text()
            item_kol = self.Table.item(min_row, 3).text()
            QMessageBox.information(
                self.centralwidget,
                "Товар с минимальной ценой:",
                f"Шифр: {item_id}\n"
                f"Наименование: {item_name}\n"
                f"Страна-импортёр: {item_country}\n"
                f"Стоимость 1 ед: {min_price}\n"
                f"количество: {item_kol}"

            )

    def sort_table(self, column_index):
        """ Сортировка таблицы по столбцу с чередованием порядка """
        # Определение текущего порядка сортировки
        current_order = self.sort_order.get(column_index, QtCore.Qt.AscendingOrder)
        # Определение нового порядка
        new_order = QtCore.Qt.DescendingOrder if current_order == QtCore.Qt.AscendingOrder else QtCore.Qt.AscendingOrder
        # Сортировка
        self.Table.sortItems(column_index, new_order)
        # Обновление состояния сортировки
        self.sort_order[column_index] = new_order

    def summar_price(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_sumPrice()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def summar_V(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Summar_V_Country()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def about_program(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_info()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Система учёта экспортных товаров"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainMenu", "Шифр"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainMenu", "Наименование товара"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainMenu", "Страна-импортёр"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainMenu", "Размер партии"))
        item = self.Table.horizontalHeaderItem(4)
        item.setText(_translate("MainMenu", "Стоимость 1 ед"))
        self.getInfo_button.setText(_translate("MainMenu", "О программе"))
        self.add_button.setText(_translate("MainMenu", "Добавить "))
        self.change_button.setText(_translate("MainMenu", "Изменить"))
        self.delete_button.setText(_translate("MainMenu", "Удалить"))
        self.load_button.setText(_translate("MainMenu", "Загрузить"))
        self.summar_price_button.setText(_translate("MainMenu", "Суммарная стоимость товаров по шифру"))
        self.summar_V_button.setText(_translate("MainMenu", "Сумар объём товаров по стране"))
        self.min_price_button.setText(_translate("MainMenu", "Минимальная стоимость товара"))
        self.country_label.setText(_translate("MainMenu", "Страна-импортёр:"))
        self.name_label.setText(_translate("MainMenu", "Имя товара:"))
        self.price_label.setText(_translate("MainMenu", "Стоимость 1 ед:"))
        self.kol_label.setText(_translate("MainMenu", "Размер партии:"))
        self.ID_label.setText(_translate("MainMenu", "Шифр товара:"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()