import unittest
from PyQt5.QtWidgets import QApplication, QMainWindow
from prog import Ui_MainMenu
from sumPrice import Ui_sumPrice
from sumV import Ui_Summar_V_Country

class TestMainMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.main_window = QMainWindow()
        self.mainmenu = Ui_MainMenu()
        self.mainmenu.setupUi(self.main_window)
        self.mainmenu.Table.setRowCount(0)  # Очистка таблицы перед каждым тестом

    def test_add_to_table(self):
        valid_data = [
            ("001", "Товар1", "Страна1", "10", "100"),
            ("002", "Товар2", "Страна2", "20", "200"),
            ("003", "Товар3", "Страна3", "30", "300"),
        ]

        invalid_data = [
            ("004", "Товар4", "Страна4", "abc", "400"),  # Неверный размер партии
            ("005", "Товар5", "Страна5", "50", "xyz"),  # Неверная стоимость
            ("006", "Товар6", "Страна6", "", "600"),    # Пустой размер партии
        ]

        for data in valid_data:
            self.mainmenu.ID_input.setText(data[0])
            self.mainmenu.name_input.setText(data[1])
            self.mainmenu.country_input.setText(data[2])
            self.mainmenu.kol_input.setText(data[3])
            self.mainmenu.price_input.setText(data[4])
            self.mainmenu.add_to_table()

        self.assertEqual(self.mainmenu.Table.rowCount(), 3)

        for data in invalid_data:
            self.mainmenu.ID_input.setText(data[0])
            self.mainmenu.name_input.setText(data[1])
            self.mainmenu.country_input.setText(data[2])
            self.mainmenu.kol_input.setText(data[3])
            self.mainmenu.price_input.setText(data[4])
            self.mainmenu.add_to_table()

        self.assertEqual(self.mainmenu.Table.rowCount(), 3)  # Проверяем, что неверные строки не добавлены

    def test_change_row(self):
        self.test_add_to_table()  # Предзаполнить таблицу
        self.mainmenu.Table.selectRow(0)
        self.mainmenu.load_row()
        self.mainmenu.price_input.setText("500")
        self.mainmenu.change_row()
        self.assertEqual(self.mainmenu.Table.item(0, 4).text(), "500")

    def test_delete_cell(self):
        self.test_add_to_table()  # Предзаполнить таблицу
        self.mainmenu.Table.selectRow(0)
        self.mainmenu.delete_cell()
        self.assertEqual(self.mainmenu.Table.rowCount(), 2)

    def test_find_min_price(self):
        self.test_add_to_table()  # Предзаполнить таблицу
        self.mainmenu.min_price_button.click()
        # Предполагается, что товар с минимальной ценой будет найден корректно

    def test_sum_shipment(self):
        self.test_add_to_table()  # Предзаполнить таблицу
        sum_window = QMainWindow()
        sum_price = Ui_sumPrice()
        sum_price.setupUi(sum_window)
        sum_price.lineEdit_S.setText("001")
        sum_price.sumShipment()  # Запуск функции расчета суммарной стоимости

    def test_find_summar_v(self):
        self.test_add_to_table()  # Предзаполнить таблицу
        v_window = QMainWindow()
        sum_v = Ui_Summar_V_Country()
        sum_v.setupUi(v_window)
        sum_v.lineEdit_V.setText("Страна1")
        sum_v.findSummarV()  # Запуск функции расчета суммарного объема

if __name__ == '__main__':
    unittest.main()
