import sys
import os
from PyQt5 import QtWidgets, QtGui
from Frontend.app import Ui_MainWindow
from Frontend.windown1 import Ui_MainWindow as Ui_MainWindow_win_1
from Frontend.windown2 import Ui_MainWindow as Ui_MainWindow_win_2
from Parser import parser
from Excel import book
from cloud import google_drive_operations as drive
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem


url_android = 'https://www.antutu.com/en/ranking/rank1.htm'
url_ios = 'https://www.antutu.com/en/ranking/ios1.htm'
url_ai = 'https://www.antutu.com/en/ranking/ai1.htm'


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_BtnAlfandega_2.clicked.connect(lambda: self.create_book('Android', url_android))
        self.ui.pushButton_BtnAlfandega_7.clicked.connect(lambda: self.create_book('IOS', url_ios))
        self.ui.pushButton_BtnAlfandega_10.clicked.connect(lambda: self.create_book('AI', url_ai))
        self.ui.pushButton_Android.clicked.connect(lambda: self.set_page(1))
        self.ui.pushButton_IOS.clicked.connect(lambda: self.set_page(2))
        self.ui.pushButton_AI.clicked.connect(lambda: self.set_page(3))
        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.open_win_1())
        self.ui.pushButton_BtnAlfandega_8.clicked.connect(lambda: self.open_win_1())
        self.ui.pushButton_BtnAlfandega_11.clicked.connect(lambda: self.open_win_1())

        self.ui.pushButton_BtnAlfandega.clicked.connect(lambda: self.table('Android', url_android))
        self.ui.pushButton_BtnAlfandega_9.clicked.connect(lambda: self.table('IOS', url_ios))
        self.ui.pushButton_BtnAlfandega_12.clicked.connect(lambda: self.table('AI', url_ai))

    def create_book(self, platform, url):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Сохранить файл",
                                                             ".",
                                                             "Xlsx Files (*.xlsx)")
        if filename == '':
            return
        data = parser.get_data(parser.parse_text(url), platform)
        book.main(data, filename)
        QtWidgets.QMessageBox.information(self, "Information", "Успешно!")

    def set_page(self, index):
        self.button_set_down(index)
        self.ui.stackedWidget.setCurrentIndex(index)

    def button_set_down(self, index):
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setItalic(False)
        self.ui.pushButton_Android.setFont(font)
        self.ui.pushButton_IOS.setFont(font)
        self.ui.pushButton_AI.setFont(font)
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        if index == 1:
            self.ui.pushButton_Android.setFont(font)
        elif index == 2:
            self.ui.pushButton_IOS.setFont(font)
        else:
            self.ui.pushButton_AI.setFont(font)

    def open_win_1(self):
        try:
            g_drive = drive.Adapter(drive.GDrive())
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Невозможно пройти аутентификацию!")
            return
        self.win_1 = Win1(g_drive)
        self.win_1.show()

    def table(self, platform, url):
        self.test1 = Table(platform, url)
        self.test1.show()


class Win1(QtWidgets.QMainWindow):
    def __init__(self, g_drive):
        self.g_drive = g_drive
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_win_1()
        self.ui.setupUi(self)
        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.open_win_2())

    def open_win_2(self):
        url = self.ui.lineEdit.text()
        try:
            folder_id = self.parse_url(url)
            self.g_drive.connect_to_folder(folder_id)
            self.win_2 = Win2(self.g_drive)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите ссылку на папку!")
            return
        self.win_2.show()
        self.close()

    def parse_url(self, url):
        splitted_url = url.split('/')
        return splitted_url[len(splitted_url) - 1]


class Win2(QtWidgets.QMainWindow):
    def __init__(self, g_drive):
        self.g_drive = g_drive
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_win_2()
        self.ui.setupUi(self)
        file_list = g_drive.list_files_in_drive()
        text = ''
        for index, file_drive in enumerate(file_list, 1):
            text += '{}. {}\n'.format(index, file_drive["title"])
        self.ui.textEdit.setText(text)
        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.download_file(file_list))
        self.ui.pushButton_BtnAlfandega_4.clicked.connect(lambda: self.upload_file())
        self.ui.pushButton_BtnAlfandega_5.clicked.connect(lambda: self.open_win_1())

    def download_file(self, file_list):
        num = self.ui.lineEdit.text()
        if num == '':
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите номер документа!")
            return
        path_to_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if path_to_folder == '':
            return
        try:
            local_file_path = os.path.join(path_to_folder, file_list[int(num) - 1]['title'])
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный номер документа!")
            return
        try:
            self.g_drive.download_file_from_drive(file_list[int(num) - 1]['id'], local_file_path)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Невозможно скачать файл!")
            return
        QtWidgets.QMessageBox.information(self, "Information", "Успешно!")

    def upload_file(self):
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self,
                                                             "Выберите файл",
                                                             ".",
                                                             "Xlsx Files (*.xlsx)")
        if filename == '':
            return
        try:
            self.g_drive.upload_file_to_drive(filename)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Невозможно загрузить файл!")
            return
        QtWidgets.QMessageBox.information(self, "Information", "Успешно!")

    def open_win_1(self):
        self.win_1 = Win1(self.g_drive)
        self.win_1.show()
        self.close()


class Table(QMainWindow):
    def __init__(self, platform, url):
        super().__init__()
        data = parser.get_data(parser.parse_text(url), platform)
        self.setWindowTitle(platform)
        self.setGeometry(100, 100, 1000, 400)
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)
        self.table.setColumnCount(len(data[1]))
        self.table.setColumnWidth(1, 400)
        if platform == 'AI':
            self.table.setColumnWidth(2, 200)
            self.table.setColumnWidth(3, 200)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setRowCount(len(data[1:]))
        for row in range(1, len(data)):
            print(row)
            for i in range(len(data[1])):
                self.table.setItem(row - 1, i, QTableWidgetItem(data[row][i]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
