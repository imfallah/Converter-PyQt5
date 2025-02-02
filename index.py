# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splash(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 342)
        
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        MainWindow.setMinimumSize(QtCore.QSize(523, 342))
        MainWindow.setMaximumSize(QtCore.QSize(523, 342))
        MainWindow.setStyleSheet("QProgressBar {\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 12px;\n"
"\n"
"    margin: 0.5px;\n"
"    background-color: red;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(142, 68, 173);\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(000000), stop:1 rgb(35, 255, 222));\n"
" ;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_all = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_all.setFont(font)
        self.frame_all.setStyleSheet("border-bottom-right-radius: 50px;\n"
"border-top-left-radius: 50px;")
        self.frame_all.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_all.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_all.setObjectName("frame_all")
        self.prog = QtWidgets.QProgressBar(self.frame_all)
        self.prog.setGeometry(QtCore.QRect(100, 160, 331, 31))
        self.prog.setProperty("value", 24)
        self.prog.setObjectName("prog")
        self.label = QtWidgets.QLabel(self.frame_all)
        self.label.setGeometry(QtCore.QRect(70, 60, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("    background-color: transparent;\n"
"color:#fff")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_tz = QtWidgets.QLabel(self.frame_all)
        self.label_tz.setGeometry(QtCore.QRect(170, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(16)
        self.label_tz.setFont(font)
        self.label_tz.setStyleSheet("    background-color: transparent;")
        self.label_tz.setTextFormat(QtCore.Qt.RichText)
        self.label_tz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tz.setObjectName("label_tz")
        self.gridLayout.addWidget(self.frame_all, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Converter App"))
        self.label_tz.setText(_translate("MainWindow", "<html><head/><body><p>Loading App ...</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Splash()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
