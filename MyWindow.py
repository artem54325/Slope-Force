import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('SlopeForse.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Поверхность скольжения')
        self.scale_factor.setChecked(True)

        self.bool_surface = False
        self.bool_physic = False

        self.pushButton_calculate.clicked.connect(self.calculation)
        self.pushButton_show_result.clicked.connect(self.showResult)
        self.pushButton_save_result.clicked.connect(self.saveFile)

        self.radioButton_auto_geometry.clicked.connect(self.autoGeometryRadio)
        self.radioButton_user_geometry.clicked.connect(self.userGeometryRadio)

        self.radioButton_auto_physic.clicked.connect(self.autoPhysicsRadio)
        self.radioButton_user_physic.clicked.connect(self.userPhysicsRadio)

        self.pushButton_file_physic.clicked.connect(self.physicOpenFile)
        self.pushButton_file_surface.clicked.connect(self.surfaceOpenFile)
        self.scale_factor.stateChanged.connect(self.onStateScaleFactor)

        # Test Value:
        self.lineEdit_H.setText(str(100))
        self.lineEdit_alpha.setText(str(45))

        self.lineEdit_phi.setText(str(35))
        self.lineEdit_gamma.setText(str(2.5))
        self.lineEdit_dx.setText(str(0.1))
        self.lineEdit_C.setText(str(5.240734270891313))

        self.lineEdit_scale_factor.setText(str(45))


    def userGeometryRadio(self):
        self.bool_surface = False

        self.label_alpha.setEnabled(True)
        self.label_H.setEnabled(True)
        self.label_file_surface.setEnabled(True)
        self.label_gemetr.setEnabled(True)

        self.label_file_surface.setEnabled(False)
        self.lineEdit_file_surface.setEnabled(False)
        self.pushButton_file_surface.setEnabled(False)

    def autoGeometryRadio(self):
        self.bool_surface = True

        self.label_alpha.setEnabled(False)
        self.label_H.setEnabled(False)
        self.label_file_surface.setEnabled(False)
        self.label_gemetr.setEnabled(False)
        self.lineEdit_H.setEnabled(False)
        self.lineEdit_alpha.setEnabled(False)
        self.label_gemetr.setEnabled(False)

        self.label_file_surface.setEnabled(True)
        self.lineEdit_file_surface.setEnabled(True)
        self.pushButton_file_surface.setEnabled(True)

    def userPhysicsRadio(self):
        self.bool_physic = False

        self.lineEdit_phi.setEnabled(True)
        self.label_phi.setEnabled(True)
        self.lineEdit_gamma.setEnabled(True)
        self.label_gamma.setEnabled(True)
        self.label_dx.setEnabled(True)
        self.lineEdit_dx.setEnabled(True)
        self.label_physic.setEnabled(True)
        self.lineEdit_C.setEnabled(True)
        self.label_c.setEnabled(True)

        self.pushButton_file_physic.setEnabled(False)
        self.lineEdit_parametr_file_physic.setEnabled(False)
        self.label_physic_auto.setEnabled(False)

    def autoPhysicsRadio(self):
        self.bool_physic = True

        self.lineEdit_phi.setEnabled(False)
        self.label_phi.setEnabled(False)
        self.lineEdit_gamma.setEnabled(False)
        self.label_gamma.setEnabled(False)
        self.label_dx.setEnabled(False)
        self.lineEdit_dx.setEnabled(False)
        self.label_physic.setEnabled(False)
        self.lineEdit_C.setEnabled(False)
        self.label_c.setEnabled(False)

        self.pushButton_file_physic.setEnabled(True)
        self.lineEdit_parametr_file_physic.setEnabled(True)
        self.label_physic_auto.setEnabled(True)

    def calculation(self):
        h = self.lineEdit_H.text()
        alpha = self.lineEdit_alpha.text()

        if(self.bool_surface):
            pass
            # self.lineEdit_parametr_file_physic.setText(str(name[0]))
            # str(name[0])
            # print('name = ' + name[0])
            # file = open(name, 'r')
            # with file:
            #     text = file.read()
            #     print(text)

        phi = self.lineEdit_phi.text()
        gamma = self.lineEdit_gamma.text()
        dx = self.lineEdit_dx.text()
        C = self.lineEdit_C.text()

        if (self.bool_physic):
            pass

        scale = self.lineEdit_scale_factor.text()

        if (self.bool_physic):
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

    def surfaceOpenFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), "txt (*.txt)")
        self.lineEdit_file_surface.setText(str(name[0]))

    def physicOpenFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), "txt (*.txt)")
        self.lineEdit_parametr_file_physic.setText(str(name[0]))
        # str(name[0])
        # print('name = ' + name[0])
        # file = open(name, 'r')
        # with file:
        #     text = file.read()
        #     print(text)

    def onStateScaleFactor(self, state):
        if(state != 0):
            self.lineEdit_scale_factor.setEnabled(True)
            self.lineEdit_scale_factor.setText('')
            # self.scale_factor.setEnabled(True)
        else:
            self.lineEdit_scale_factor.setText('off')
            self.lineEdit_scale_factor.setEnabled(False)

            # self.scale_factor.setEnabled(False)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()