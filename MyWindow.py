import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('SlopeForse.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Поверхность скольжения')

        self.pushButton_calculate.clicked.connect(self.calculation)
        self.pushButton_calculate.clicked.connect(self.calculation)

        self.pushButton_calculate.clicked.connect(self.calculation)
        self.pushButton_show_result.clicked.connect(self.showResult)
        self.pushButton_save_result.clicked.connect(self.saveFile)
        # self.openFile()

    def calculation(self):
        pass

    def showResult(self):
        pass

    def saveFile(self, text):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить файл')
        file = open(name, 'w')
        file.write(text)
        file.close()

    def setProgress(self, minValue, maxValue, value):
        self.progressBar.setValue(value)
        self.progressBar.setMaximum(maxValue)
        self.progressBar.setMinimum(minValue)

    def openFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), "txt (*.txt)")
        file = open(name, 'r')
        with file:
            text = file.read()
            print(text)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    # from PyQt5 import QtWidgets, QtGui
    # from qtLabel import Ui_MainWindow
    # import sys
    #
    #
    # class mywindow(QtWidgets.QMainWindow):
    #
    #     def __init__(self):
    #         super(mywindow, self).__init__()
    #         self.ui = Ui_MainWindow()
    #         self.ui.setupUi(self)
    #
    #         self.ui.label.setText("qwewqe")
    #         # self.ui.pushButton.clicked.connect(self.btnClicked)
    #
    #     def calculation(self):
    #         pass
    #
    #     def example(self):
    #         pass
    #
    #
    # app = QtWidgets.QApplication([])
    # application = mywindow()
    # application.show()
    #
    # sys.exit(app.exec())