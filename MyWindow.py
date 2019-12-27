from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('SlopeForse.ui', self)


    def example(self):
        pass
    def calculation(self):
        pass



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

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