# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 378)
        Form.setStyleSheet("border-bottom-right-radius: 50px;\n"
"border-top-left-radius: 50px;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(000000), stop:1 rgb(35, 255, 222));\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(330, 10, 31, 24))
        self.exit.setStyleSheet("\n"
"#exit{\n"
"\n"
" background-color:transparent;\n"
"\n"
"\n"
"}\n"
"#exit:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"#exit:pressed {\n"
"    border: 4px solid #98c1fe;\n"
"    border-radius:10px\n"
"}\n"
"")
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setObjectName("exit")
        self.mini = QtWidgets.QPushButton(self.frame)
        self.mini.setGeometry(QtCore.QRect(310, 10, 21, 24))
        self.mini.setStyleSheet("\n"
"#mini{\n"
"\n"
" background-color:transparent;\n"
"\n"
"\n"
"}\n"
"#mini:hover {\n"
"    background-color: rgb(190, 190, 0);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"#mini:pressed {\n"
"    border: 4px solid #98c1fe;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"")
        self.mini.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/Maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mini.setIcon(icon1)
        self.mini.setObjectName("mini")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 8, 21, 24))
        self.pushButton_3.setStyleSheet("background-color:none;\n"
"")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/Minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.conversionComboBox = QtWidgets.QComboBox(self.frame)
        self.conversionComboBox.setGeometry(QtCore.QRect(50, 100, 301, 21))
        self.conversionComboBox.setStyleSheet("background-color:none;")
        self.conversionComboBox.setObjectName("conversionComboBox")
        self.conversionComboBox.addItem("")
        self.conversionComboBox.addItem("")
        self.conversionComboBox.addItem("")
        self.conversionComboBox.addItem("")
        self.conversionComboBox.addItem("")
        self.filePathLabel = QtWidgets.QLabel(self.frame)
        self.filePathLabel.setGeometry(QtCore.QRect(120, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        font.setItalic(False)
        self.filePathLabel.setFont(font)
        self.filePathLabel.setStyleSheet("#filePathLabel{\n"
"  font: 500 12pt \"Roboto Medium\";\n"
"  background-color:none;\n"
"  border-bottom-right-radius: 50px;\n"
"}\n"
"\n"
"\n"
"#filePathLabel::hover{\n"
"\n"
"   color:rgb(255, 255, 255)\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.filePathLabel.setObjectName("filePathLabel")
        self.statusLabel = QtWidgets.QLabel(self.frame)
        self.statusLabel.setGeometry(QtCore.QRect(120, 210, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("#statusLabel{\n"
"  background-color:none;\n"
"  border-bottom-right-radius: 50px;\n"
"}\n"
"\n"
"\n"
"#statusLabel::hover{\n"
"\n"
"   color:rgb(171, 39, 39)\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.statusLabel.setObjectName("statusLabel")
        self.convertButton = QtWidgets.QPushButton(self.frame)
        self.convertButton.setGeometry(QtCore.QRect(190, 280, 161, 28))
        self.convertButton.setStyleSheet("\n"
"#convertButton{\n"
"   background-color:rgb(123, 125, 255);\n"
"   border-radius:10px;\n"
"   color: white;\n"
"}\n"
"\n"
"\n"
"#convertButon::clicked\n"
"{\n"
"  \n"
" background-color : red;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#convertButton:hover {\n"
"    background-color: #0055ff;\n"
"}\n"
"\n"
"#convertButton:pressed {\n"
"    border: 4px solid #98c1fe;\n"
"}\n"
"")
        self.convertButton.setObjectName("convertButton")
        self.selectFileButton = QtWidgets.QPushButton(self.frame)
        self.selectFileButton.setGeometry(QtCore.QRect(10, 280, 171, 28))
        self.selectFileButton.setStyleSheet("\n"
"#selectFileButton{\n"
"   background-color:rgb(255, 167, 255);\n"
"   border-radius:10px;\n"
"   color: white;\n"
"}\n"
"\n"
"#selectFileButton::clicked\n"
"{\n"
"  \n"
" background-color : red;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#selectFileButton:hover {\n"
"    background-color: rgb(255, 90, 49);\n"
"}\n"
"\n"
"#selectFileButton:pressed {\n"
"    border: 4px solid #98c1fe;\n"
"}")
        self.selectFileButton.setObjectName("selectFileButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(24)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"\n"
"#label{\n"
"  font:;\n"
"    font: 900 24pt \"Segoe UI Black\";\n"
"  background-color:none;\n"
"  color:#fff;\n"
"  border-bottom-right-radius: 50px;\n"
"}\n"
"\n"
"#label::hover{\n"
"\n"
"   color:rgb(0, 0, 0)\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.conversionComboBox.setItemText(0, _translate("Form", "PDF to Word"))
        self.conversionComboBox.setItemText(1, _translate("Form", "Excel to Word"))
        self.conversionComboBox.setItemText(2, _translate("Form", "Word to PDF"))
        self.conversionComboBox.setItemText(3, _translate("Form", "Image to PDF"))
        self.conversionComboBox.setItemText(4, _translate("Form", "Image Text Extract"))
        self.filePathLabel.setText(_translate("Form", "No file selected"))
        self.statusLabel.setText(_translate("Form", "status"))
        self.convertButton.setText(_translate("Form", "Convert"))
        self.selectFileButton.setText(_translate("Form", "Select File"))
        self.label.setText(_translate("Form", "Converter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
