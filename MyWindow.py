import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Argument_search import Argument_search
from Search_Constant_Test import Search_Constant_Test

from Argument_search import Argument_search
from slopeforsewindow import Ui_MainWindow


class MyWindow():
    def __init__(self, ui):
        # super(MyWindow,self).__init__()
        self.ui = ui
        self.initUI()

    def initUI(self):
        # self.ui.setWindowTitle('Поверхность скольжения')
        self.slope = None

        self.bool_surface = False
        self.bool_physic = False
        self.bool_K = False

        self.ui.pushButton_calculate.clicked.connect(self.calculation)
        self.ui.pushButton_show_result.clicked.connect(self.showResult)
        self.ui.pushButton_save_result.clicked.connect(self.saveFile)

        self.ui.radioButton_auto_geometry.clicked.connect(self.autoGeometryRadio)
        self.ui.radioButton_user_geometry.clicked.connect(self.userGeometryRadio)

        self.ui.radioButton_auto_physic.clicked.connect(self.autoPhysicsRadio)
        self.ui.radioButton_user_physic.clicked.connect(self.userPhysicsRadio)

        self.ui.pushButton_file_physic.clicked.connect(self.physicOpenFile)
        self.ui.pushButton_file_surface.clicked.connect(self.surfaceOpenFile)
        # self.scale_factor.stateChanged.connect(self.onStateScaleFactor)

        self.ui.radioButton_K.clicked.connect(self.KRadio)
        self.ui.radioButton_K_accuracy.clicked.connect(self.KAccuracyRadio)

        # Test Value:
        self.ui.lineEdit_H.setText(str(100))
        self.ui.lineEdit_alpha.setText(str(45))

        self.ui.lineEdit_phi.setText(str(35))
        self.ui.lineEdit_gamma.setText(str(2.5))
        self.ui.lineEdit_dx.setText(str(0.1))
        self.ui.lineEdit_C.setText(str(5.240734270891313))

        self.ui.lineEdit_K.setText(str(100))


    def userGeometryRadio(self):
        print("userGeometryRadio")
        self.bool_surface = False

        self.ui.label_alpha.setEnabled(True)
        self.ui.label_H.setEnabled(True)
        self.ui.label_file_surface.setEnabled(True)
        self.ui.label_gemetr.setEnabled(True)

        self.ui.label_file_surface.setEnabled(False)
        self.ui.lineEdit_file_surface.setEnabled(False)
        self.ui.pushButton_file_surface.setEnabled(False)

    def autoGeometryRadio(self):
        self.bool_surface = True

        self.ui.label_alpha.setEnabled(False)
        self.ui.label_H.setEnabled(False)
        self.ui.label_file_surface.setEnabled(False)
        self.ui.label_gemetr.setEnabled(False)
        self.ui.lineEdit_H.setEnabled(False)
        self.ui.lineEdit_alpha.setEnabled(False)
        self.ui.label_gemetr.setEnabled(False)

        self.ui.label_file_surface.setEnabled(True)
        self.ui.lineEdit_file_surface.setEnabled(True)
        self.ui.pushButton_file_surface.setEnabled(True)

    def userPhysicsRadio(self):
        self.bool_physic = False

        self.ui.lineEdit_phi.setEnabled(True)
        self.ui.label_phi.setEnabled(True)
        self.ui.lineEdit_gamma.setEnabled(True)
        self.ui.label_gamma.setEnabled(True)
        self.ui.label_dx.setEnabled(True)
        self.ui.lineEdit_dx.setEnabled(True)
        self.ui.label_physic.setEnabled(True)
        self.ui.lineEdit_C.setEnabled(True)
        self.ui.label_c.setEnabled(True)

        self.ui.pushButton_file_physic.setEnabled(False)
        self.ui.lineEdit_parametr_file_physic.setEnabled(False)
        self.ui.label_physic_auto.setEnabled(False)

    def KRadio(self):
        self.bool_K = True

    def KAccuracyRadio(self):
        self.bool_K = False

    def autoPhysicsRadio(self):
        self.bool_physic = True

        self.ui.lineEdit_phi.setEnabled(False)
        self.ui.label_phi.setEnabled(False)
        self.ui.lineEdit_gamma.setEnabled(False)
        self.ui.label_gamma.setEnabled(False)
        self.ui.label_dx.setEnabled(False)
        self.ui.lineEdit_dx.setEnabled(False)
        self.ui.label_physic.setEnabled(False)
        self.ui.lineEdit_C.setEnabled(False)
        self.ui.label_c.setEnabled(False)

        self.ui.pushButton_file_physic.setEnabled(True)
        self.ui.lineEdit_parametr_file_physic.setEnabled(True)
        self.ui.label_physic_auto.setEnabled(True)

    def calculation(self):
        print("calculation")
        H = self.ui.lineEdit_H.text()
        alpha = self.ui.lineEdit_alpha.text()

        if(self.bool_surface):
            pass
            # self.lineEdit_parametr_file_physic.setText(str(name[0]))
            # str(name[0])
            # print('name = ' + name[0])
            # file = open(name, 'r')
            # with file:
            #     text = file.read()
            #     print(text)

        phi = self.ui.lineEdit_phi.text()
        gamma = self.ui.lineEdit_gamma.text()
        dx = self.ui.lineEdit_dx.text()
        C = self.ui.lineEdit_C.text()

        if (self.bool_physic):
            pass

        self.slope = Argument_search('manual', [float(alpha), float(H), float(phi), float(gamma), float(dx), 'red'], self)

        if(self.bool_K==False):
            self.slope.search_best_K(float(C), float(self.ui.lineEdit_K.text()))
        else:
            self.slope.draw_slope(float(C), float(self.ui.lineEdit_K_accuracy.text()))

    def writeResult(self, scale, geometr, physic):
        self.ui.lineEdit_geometr_result.setText('{:.3f}'.format(geometr))
        self.ui.lineEdit_physic_result.setText('{:.3f}'.format(physic))
        self.ui.lineEdit_scale_result.setText('{:.3f}'.format(scale))

    def showResult(self):
        if(self.slope == None):
            return
        self.slope.draw_in_page()

    def saveFile(self, text):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить файл')
        file = open(name, 'w')
        file.write(text)
        file.close()

    def setProgress(self, minValue, maxValue, value):
        self.ui.progressBar.setValue(value)
        self.ui.progressBar.setMaximum(maxValue)
        self.ui.progressBar.setMinimum(minValue)

    def surfaceOpenFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), "txt (*.txt)")
        self.ui.lineEdit_file_surface.setText(str(name[0]))

    def physicOpenFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), "txt (*.txt)")
        self.ui.lineEdit_parametr_file_physic.setText(str(name[0]))
        # str(name[0])
        # print('name = ' + name[0])
        # file = open(name, 'r')
        # with file:
        #     text = file.read()
        #     print(text)

    def onStateScaleFactor(self, state):
        if(state != 0):
            self.ui.lineEdit_scale_factor.setEnabled(True)
            self.ui.lineEdit_scale_factor.setText('')
            # self.scale_factor.setEnabled(True)
        else:
            self.ui.lineEdit_scale_factor.setText('off')
            self.ui.lineEdit_scale_factor.setEnabled(False)

            # self.scale_factor.setEnabled(False)




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MyWindow(ui)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()