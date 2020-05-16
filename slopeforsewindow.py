# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slopeforse.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Argument_search import Argument_search

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 607)
        MainWindow.setMinimumSize(QtCore.QSize(617, 607))
        MainWindow.setMaximumSize(QtCore.QSize(617, 607))
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 581, 121))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_H = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_H.setGeometry(QtCore.QRect(30, 90, 71, 22))
        self.lineEdit_H.setObjectName("lineEdit_H")
        self.label_file_surface = QtWidgets.QLabel(self.groupBox_2)
        self.label_file_surface.setEnabled(False)
        self.label_file_surface.setGeometry(QtCore.QRect(340, 30, 211, 21))
        self.label_file_surface.setObjectName("label_file_surface")
        self.label_alpha = QtWidgets.QLabel(self.groupBox_2)
        self.label_alpha.setGeometry(QtCore.QRect(110, 60, 151, 16))
        self.label_alpha.setObjectName("label_alpha")
        self.label_H = QtWidgets.QLabel(self.groupBox_2)
        self.label_H.setGeometry(QtCore.QRect(110, 90, 151, 16))
        self.label_H.setObjectName("label_H")
        self.radioButton_auto_geometry = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_auto_geometry.setEnabled(True)
        self.radioButton_auto_geometry.setGeometry(QtCore.QRect(340, 10, 241, 20))
        self.radioButton_auto_geometry.setTabletTracking(False)
        self.radioButton_auto_geometry.setObjectName("radioButton_auto_geometry")
        self.radioButton_user_geometry = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_user_geometry.setEnabled(True)
        self.radioButton_user_geometry.setGeometry(QtCore.QRect(30, 10, 271, 20))
        self.radioButton_user_geometry.setMouseTracking(True)
        self.radioButton_user_geometry.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_user_geometry.setAutoFillBackground(False)
        self.radioButton_user_geometry.setChecked(True)
        self.radioButton_user_geometry.setObjectName("radioButton_user_geometry")
        self.lineEdit_alpha = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_alpha.setGeometry(QtCore.QRect(30, 60, 71, 22))
        self.lineEdit_alpha.setObjectName("lineEdit_alpha")
        self.lineEdit_file_surface = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_file_surface.setEnabled(False)
        self.lineEdit_file_surface.setGeometry(QtCore.QRect(340, 60, 191, 22))
        self.lineEdit_file_surface.setDragEnabled(False)
        self.lineEdit_file_surface.setReadOnly(False)
        self.lineEdit_file_surface.setObjectName("lineEdit_file_surface")
        self.label_gemetr = QtWidgets.QLabel(self.groupBox_2)
        self.label_gemetr.setGeometry(QtCore.QRect(30, 40, 201, 16))
        self.label_gemetr.setObjectName("label_gemetr")
        self.pushButton_file_surface = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_file_surface.setEnabled(False)
        self.pushButton_file_surface.setGeometry(QtCore.QRect(488, 90, 41, 25))
        self.pushButton_file_surface.setObjectName("pushButton_file_surface")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 581, 181))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_auto_physic = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_auto_physic.setGeometry(QtCore.QRect(340, 10, 241, 20))
        self.radioButton_auto_physic.setObjectName("radioButton_auto_physic")
        self.label_phi = QtWidgets.QLabel(self.groupBox)
        self.label_phi.setGeometry(QtCore.QRect(110, 60, 191, 16))
        self.label_phi.setObjectName("label_phi")
        self.lineEdit_gamma = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_gamma.setGeometry(QtCore.QRect(30, 90, 71, 22))
        self.lineEdit_gamma.setObjectName("lineEdit_gamma")
        self.label_dx = QtWidgets.QLabel(self.groupBox)
        self.label_dx.setGeometry(QtCore.QRect(110, 120, 151, 16))
        self.label_dx.setObjectName("label_dx")
        self.lineEdit_dx = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dx.setGeometry(QtCore.QRect(30, 120, 71, 22))
        self.lineEdit_dx.setObjectName("lineEdit_dx")
        self.label_physic = QtWidgets.QLabel(self.groupBox)
        self.label_physic.setGeometry(QtCore.QRect(30, 40, 251, 16))
        self.label_physic.setObjectName("label_physic")
        self.label_gamma = QtWidgets.QLabel(self.groupBox)
        self.label_gamma.setGeometry(QtCore.QRect(110, 90, 151, 16))
        self.label_gamma.setObjectName("label_gamma")
        self.lineEdit_parametr_file_physic = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_parametr_file_physic.setEnabled(False)
        self.lineEdit_parametr_file_physic.setGeometry(QtCore.QRect(340, 70, 191, 22))
        self.lineEdit_parametr_file_physic.setObjectName("lineEdit_parametr_file_physic")
        self.radioButton_user_physic = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_user_physic.setGeometry(QtCore.QRect(30, 10, 261, 20))
        self.radioButton_user_physic.setChecked(True)
        self.radioButton_user_physic.setObjectName("radioButton_user_physic")
        self.label_c = QtWidgets.QLabel(self.groupBox)
        self.label_c.setGeometry(QtCore.QRect(110, 150, 151, 16))
        self.label_c.setObjectName("label_c")
        self.label_physic_auto = QtWidgets.QLabel(self.groupBox)
        self.label_physic_auto.setEnabled(False)
        self.label_physic_auto.setGeometry(QtCore.QRect(340, 40, 281, 21))
        self.label_physic_auto.setObjectName("label_physic_auto")
        self.lineEdit_phi = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_phi.setGeometry(QtCore.QRect(30, 60, 71, 22))
        self.lineEdit_phi.setObjectName("lineEdit_phi")
        self.lineEdit_C = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_C.setGeometry(QtCore.QRect(30, 150, 71, 22))
        self.lineEdit_C.setObjectName("lineEdit_C")
        self.pushButton_file_physic = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_file_physic.setEnabled(False)
        self.pushButton_file_physic.setGeometry(QtCore.QRect(488, 100, 41, 25))
        self.pushButton_file_physic.setObjectName("pushButton_file_physic")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 450, 441, 131))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(30, 10, 391, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_scale_result = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_scale_result.setGeometry(QtCore.QRect(290, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_scale_result.setFont(font)
        self.lineEdit_scale_result.setTabletTracking(False)
        self.lineEdit_scale_result.setAcceptDrops(False)
        self.lineEdit_scale_result.setToolTip("")
        self.lineEdit_scale_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_scale_result.setAutoFillBackground(True)
        self.lineEdit_scale_result.setText("")
        self.lineEdit_scale_result.setFrame(True)
        self.lineEdit_scale_result.setDragEnabled(True)
        self.lineEdit_scale_result.setReadOnly(True)
        self.lineEdit_scale_result.setObjectName("lineEdit_scale_result")
        self.lineEdit_physic_result = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_physic_result.setGeometry(QtCore.QRect(290, 100, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_physic_result.setFont(font)
        self.lineEdit_physic_result.setTabletTracking(False)
        self.lineEdit_physic_result.setAcceptDrops(False)
        self.lineEdit_physic_result.setToolTip("")
        self.lineEdit_physic_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_physic_result.setAutoFillBackground(True)
        self.lineEdit_physic_result.setText("")
        self.lineEdit_physic_result.setFrame(True)
        self.lineEdit_physic_result.setDragEnabled(True)
        self.lineEdit_physic_result.setReadOnly(True)
        self.lineEdit_physic_result.setObjectName("lineEdit_physic_result")
        self.lineEdit_geometr_result = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_geometr_result.setGeometry(QtCore.QRect(290, 70, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_geometr_result.setFont(font)
        self.lineEdit_geometr_result.setTabletTracking(False)
        self.lineEdit_geometr_result.setAcceptDrops(False)
        self.lineEdit_geometr_result.setToolTip("")
        self.lineEdit_geometr_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_geometr_result.setAutoFillBackground(True)
        self.lineEdit_geometr_result.setText("")
        self.lineEdit_geometr_result.setFrame(True)
        self.lineEdit_geometr_result.setDragEnabled(True)
        self.lineEdit_geometr_result.setReadOnly(True)
        self.lineEdit_geometr_result.setObjectName("lineEdit_geometr_result")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(30, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 70, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(470, 450, 131, 131))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_show_result = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_show_result.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.pushButton_show_result.setObjectName("pushButton_show_result")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_calculate.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.pushButton_save_result = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_save_result.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.pushButton_save_result.setObjectName("pushButton_save_result")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 360, 581, 71))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_K_accuracy = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_K_accuracy.setGeometry(QtCore.QRect(340, 40, 71, 22))
        self.lineEdit_K_accuracy.setObjectName("lineEdit_K_accuracy")
        self.lineEdit_K = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_K.setGeometry(QtCore.QRect(30, 40, 71, 22))
        self.lineEdit_K.setObjectName("lineEdit_K")
        self.radioButton_K = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_K.setGeometry(QtCore.QRect(340, 10, 161, 17))
        self.radioButton_K.setCheckable(True)
        self.radioButton_K.setChecked(False)
        self.radioButton_K.setAutoRepeat(False)
        self.radioButton_K.setObjectName("radioButton_K")
        self.radioButton_K_accuracy = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_K_accuracy.setGeometry(QtCore.QRect(30, 10, 161, 17))
        self.radioButton_K_accuracy.setChecked(True)
        self.radioButton_K_accuracy.setObjectName("radioButton_K_accuracy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_input = QtWidgets.QAction(MainWindow)
        self.action_input.setObjectName("action_input")
        self.action_result = QtWidgets.QAction(MainWindow)
        self.action_result.setObjectName("action_result")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поверхность скольжения"))
        self.label_file_surface.setText(_translate("MainWindow", "Файл поверхности откоса:"))
        self.label_alpha.setText(_translate("MainWindow", "Угол откоса"))
        self.label_H.setText(_translate("MainWindow", "Высота откоса"))
        self.radioButton_auto_geometry.setText(_translate("MainWindow", "Автоматический ввод данных"))
        self.radioButton_user_geometry.setText(_translate("MainWindow", "Пользовательский ввод данных"))
        self.label_gemetr.setText(_translate("MainWindow", "Геометрические параметры"))
        self.pushButton_file_surface.setText(_translate("MainWindow", "Файл"))
        self.radioButton_auto_physic.setText(_translate("MainWindow", "Автоматический ввод данных"))
        self.label_phi.setText(_translate("MainWindow", "Угол внутреннего трения"))
        self.label_dx.setText(_translate("MainWindow", "Приращение длины"))
        self.label_physic.setText(_translate("MainWindow", "Физико-механические параметры"))
        self.label_gamma.setText(_translate("MainWindow", "Объемный вес"))
        self.radioButton_user_physic.setText(_translate("MainWindow", "Пользовательский ввод данных"))
        self.label_c.setText(_translate("MainWindow", "Сцепление"))
        self.label_physic_auto.setText(_translate("MainWindow", "Файл физико-механических свойств:"))
        self.pushButton_file_physic.setText(_translate("MainWindow", "Файл"))
        self.label_13.setText(_translate("MainWindow", "Физическая невязка: "))
        self.label.setText(_translate("MainWindow", "Масштабный коэффициент:"))
        self.label_12.setText(_translate("MainWindow", "Геометрическая невязка: "))
        self.pushButton_show_result.setText(_translate("MainWindow", "Отобр. график"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Расcчитать"))
        self.pushButton_save_result.setText(_translate("MainWindow", "Сохранить"))
        self.radioButton_K.setText(_translate("MainWindow", "Масштабный коэффициент"))
        self.radioButton_K_accuracy.setText(_translate("MainWindow", "Точность поиска К"))
        self.action_input.setText(_translate("MainWindow", "Ввод двнных"))
        self.action_result.setText(_translate("MainWindow", "Результаты расчета"))
        self.initUI()

    def initUI(self):
        # self.setWindowTitle('Поверхность скольжения')
        self.slope = None

        self.bool_surface = False
        self.bool_physic = False
        self.bool_K = False

        self.pushButton_calculate.clicked.connect(self.calculation)
        self.pushButton_show_result.clicked.connect(self.showResult)
        self.pushButton_save_result.clicked.connect(self.saveFile)

        self.radioButton_auto_geometry.clicked.connect(self.autoGeometryRadio)
        self.radioButton_user_geometry.clicked.connect(self.userGeometryRadio)

        self.radioButton_auto_physic.clicked.connect(self.autoPhysicsRadio)
        self.radioButton_user_physic.clicked.connect(self.userPhysicsRadio)

        self.pushButton_file_physic.clicked.connect(self.physicOpenFile)
        self.pushButton_file_surface.clicked.connect(self.surfaceOpenFile)
        # self.scale_factor.stateChanged.connect(self.onStateScaleFactor)

        self.radioButton_K.clicked.connect(self.KRadio)
        self.radioButton_K_accuracy.clicked.connect(self.KAccuracyRadio)

        # Test Value:
        self.lineEdit_H.setText(str(100))
        self.lineEdit_alpha.setText(str(45))

        self.lineEdit_phi.setText(str(35))
        self.lineEdit_gamma.setText(str(2.5))
        self.lineEdit_dx.setText(str(0.1))
        self.lineEdit_C.setText(str(5.240734270891313))

        self.lineEdit_K.setText(str(100))

    def userGeometryRadio(self):
        print("userGeometryRadio")
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

    def KRadio(self):
        self.bool_K = True

    def KAccuracyRadio(self):
        self.bool_K = False

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
        print("calculation")
        H = self.lineEdit_H.text()
        alpha = self.lineEdit_alpha.text()

        if (self.bool_surface):
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

        self.slope = Argument_search('manual', [float(alpha), float(H), float(phi), float(gamma), float(dx), 'red'],
                                     self)

        if (self.bool_K == False):
            self.slope.search_best_K(float(C), float(self.lineEdit_K.text()))
        else:
            self.slope.draw_slope(float(C), float(self.lineEdit_K_accuracy.text()))

    def writeResult(self, scale, geometr, physic):
        self.lineEdit_geometr_result.setText('{:.3f}'.format(geometr))
        self.lineEdit_physic_result.setText('{:.3f}'.format(physic))
        self.lineEdit_scale_result.setText('{:.3f}'.format(scale))

    def showResult(self):
        if (self.slope == None):
            return
        self.slope.draw_in_page()

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
        if (state != 0):
            self.lineEdit_scale_factor.setEnabled(True)
            self.lineEdit_scale_factor.setText('')
            # self.scale_factor.setEnabled(True)
        else:
            self.lineEdit_scale_factor.setText('off')
            self.lineEdit_scale_factor.setEnabled(False)

            # self.scale_factor.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
